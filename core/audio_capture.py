"""
Captura de audio del micrófono o de un dispositivo virtual (VB-Cable).
Usa pyaudio para capturar chunks de audio en un hilo separado.
"""

import threading
import numpy as np
import pyaudio
from queue import Queue, Empty
from utils.logger import obtener_logger

logger = obtener_logger(__name__)


class AudioCapture:
    def __init__(
        self,
        device_index: int | None = None,
        sample_rate: int = 16000,
        chunk_size: int = 1024,
    ):
        """
        Args:
            device_index: Índice del dispositivo de audio. None = por defecto.
            sample_rate: Frecuencia de muestreo en Hz (debe ser 16000 para Whisper).
            chunk_size: Número de muestras por chunk de lectura.
        """
        self.device_index = device_index
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size

        self._queue: Queue = Queue()
        self._running = False
        self._thread: threading.Thread | None = None
        self._pa = pyaudio.PyAudio()

    def iniciar(self):
        """Inicia la captura de audio en un hilo en segundo plano."""
        self._running = True
        self._thread = threading.Thread(target=self._capturar, daemon=True)
        self._thread.start()
        logger.info(f"Captura de audio iniciada (dispositivo: {self.device_index or 'default'})")

    def detener(self):
        """Para la captura de audio y libera recursos."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=2)
        self._pa.terminate()
        logger.info("Captura de audio detenida.")

    def acumular(self, segundos: float = 4.0) -> np.ndarray | None:
        """
        Bloquea hasta acumular N segundos de audio.
        Retorna array float32 normalizado listo para Whisper.

        Args:
            segundos: Cantidad de audio a acumular antes de retornar.

        Returns:
            Array numpy float32 normalizado, o None si no hay audio.
        """
        muestras_objetivo = int(segundos * self.sample_rate)
        buffer = []
        acumuladas = 0

        while acumuladas < muestras_objetivo:
            try:
                chunk = self._queue.get(timeout=5)
                buffer.append(chunk)
                acumuladas += len(chunk)
            except Empty:
                logger.warning("Timeout esperando audio — ¿micrófono activo?")
                return None

        audio_int16 = np.concatenate(buffer)
        return self._a_float32(audio_int16)

    def _capturar(self):
        """Bucle interno de captura. Corre en hilo separado."""
        try:
            stream = self._pa.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=self.sample_rate,
                input=True,
                input_device_index=self.device_index,
                frames_per_buffer=self.chunk_size,
            )
            logger.debug("Stream de audio abierto correctamente.")

            while self._running:
                try:
                    data = stream.read(self.chunk_size, exception_on_overflow=False)
                    chunk = np.frombuffer(data, dtype=np.int16)
                    self._queue.put(chunk)
                except Exception as e:
                    logger.error(f"Error leyendo audio: {e}")

            stream.stop_stream()
            stream.close()

        except Exception as e:
            logger.error(f"No se pudo abrir el dispositivo de audio [{self.device_index}]: {e}")
            logger.error("Ejecuta 'python utils/audio_devices.py' para ver los dispositivos disponibles.")
            self._running = False

    @staticmethod
    def _a_float32(audio_int16: np.ndarray) -> np.ndarray:
        """Convierte audio int16 a float32 normalizado entre -1.0 y 1.0."""
        return audio_int16.astype(np.float32) / 32768.0
