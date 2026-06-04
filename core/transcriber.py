"""
Transcripción de audio a texto usando OpenAI Whisper (local, sin coste).
"""

import numpy as np
import whisper
from dataclasses import dataclass
from utils.logger import obtener_logger

logger = obtener_logger(__name__)


@dataclass
class ResultadoTranscripcion:
    texto: str
    idioma_detectado: str


class Transcriptor:
    def __init__(self, modelo: str = "base"):
        """
        Carga el modelo Whisper en memoria.
        La primera vez descarga el modelo automáticamente (~74 MB para 'base').

        Args:
            modelo: Tamaño del modelo. Opciones: tiny, base, small, medium, large.
        """
        logger.info(f"Cargando modelo Whisper '{modelo}'...")
        self.modelo = whisper.load_model(modelo, device="cpu")
        logger.info(f"Modelo '{modelo}' listo.")

        # Pre-calentar el modelo con silencio para evitar latencia en la primera llamada real
        self._precalentar()

    def transcribir(self, audio_float32: np.ndarray) -> ResultadoTranscripcion:
        """
        Transcribe un array de audio a texto.

        Args:
            audio_float32: Audio normalizado float32 a 16000 Hz mono.

        Returns:
            ResultadoTranscripcion con el texto y el idioma detectado.
        """
        # Ignorar audio demasiado corto o en silencio
        if len(audio_float32) < 3200:  # Menos de 0.2 segundos
            return ResultadoTranscripcion("", "unknown")

        if np.abs(audio_float32).mean() < 0.001:
            logger.debug("Silencio detectado, omitiendo transcripción.")
            return ResultadoTranscripcion("", "unknown")

        resultado = self.modelo.transcribe(
            audio_float32,
            fp16=False,      # Siempre False en CPU
            language=None,   # None = detección automática del idioma
            task="transcribe",
        )

        texto = resultado.get("text", "").strip()
        idioma = resultado.get("language", "unknown")

        if texto:
            logger.debug(f"Transcripción [{idioma}]: {texto}")

        return ResultadoTranscripcion(texto=texto, idioma_detectado=idioma)

    def _precalentar(self):
        """Transcribe silencio para inicializar el modelo y evitar latencia inicial."""
        logger.debug("Pre-calentando modelo Whisper...")
        silencio = np.zeros(16000, dtype=np.float32)
        self.modelo.transcribe(silencio, fp16=False)
        logger.debug("Modelo precalentado.")
