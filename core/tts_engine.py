"""
Motor de Text-to-Speech con ElevenLabs (clonación de voz).
Usa la voz clonada del usuario para reproducir las traducciones.

Para configurar:
1. Crear cuenta en elevenlabs.io
2. Voices → Add Voice → Instant Voice Cloning → subir 1-3 min de tu voz
3. Copiar el Voice ID generado
4. Añadir al .env: ELEVENLABS_API_KEY y ELEVENLABS_VOICE_ID
"""

import io
import os
import threading
import requests
import pygame
from utils.logger import obtener_logger

logger = obtener_logger(__name__)

# URL base de la API de ElevenLabs
ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1"


class MotorTTS:
    def __init__(self, api_key: str = "", voice_id: str = ""):
        """
        Args:
            api_key: API key de ElevenLabs. Si vacío, lee de variable de entorno.
            voice_id: ID de la voz clonada. Si vacío, lee de variable de entorno.
        """
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY", "")
        self.voice_id = voice_id or os.getenv("ELEVENLABS_VOICE_ID", "")
        self._lock = threading.Lock()

        if not self.api_key:
            logger.warning("ELEVENLABS_API_KEY no configurada. TTS desactivado.")
        if not self.voice_id:
            logger.warning("ELEVENLABS_VOICE_ID no configurado. TTS desactivado.")

        pygame.mixer.init()
        logger.info("Motor TTS (ElevenLabs) inicializado.")

    def hablar(self, texto: str, idioma: str = "es"):
        """
        Convierte texto a voz usando la voz clonada del usuario.
        Bloquea hasta que termina la reproducción.

        Args:
            texto: Texto a convertir en voz.
            idioma: No afecta a ElevenLabs (detecta el idioma automáticamente).
        """
        if not texto or not texto.strip():
            return

        if not self.api_key or not self.voice_id:
            logger.error("Configura ELEVENLABS_API_KEY y ELEVENLABS_VOICE_ID en el .env")
            return

        with self._lock:
            try:
                audio_bytes = self._generar_audio(texto)
                if audio_bytes:
                    self._reproducir(audio_bytes)
            except Exception as e:
                logger.error(f"Error en TTS ElevenLabs: {e}")

    def hablar_async(self, texto: str, idioma: str = "es"):
        """Versión no bloqueante de hablar()."""
        hilo = threading.Thread(
            target=self.hablar,
            args=(texto, idioma),
            daemon=True
        )
        hilo.start()

    def _generar_audio(self, texto: str) -> bytes | None:
        """Llama a la API de ElevenLabs y retorna los bytes de audio."""
        url = f"{ELEVENLABS_API_URL}/text-to-speech/{self.voice_id}"

        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json",
        }

        payload = {
            "text": texto,
            "model_id": "eleven_multilingual_v2",  # Soporta español, inglés, francés y más
            "voice_settings": {
                "stability": 0.5,        # 0.0-1.0 — más alto = más consistente
                "similarity_boost": 0.75, # 0.0-1.0 — más alto = más parecido a tu voz
                "style": 0.0,
                "use_speaker_boost": True,
            },
        }

        response = requests.post(url, json=payload, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.content
        elif response.status_code == 401:
            logger.error("API key de ElevenLabs inválida.")
        elif response.status_code == 422:
            logger.error("Voice ID inválido o voz no encontrada.")
        else:
            logger.error(f"Error ElevenLabs [{response.status_code}]: {response.text}")

        return None

    def _reproducir(self, audio_bytes: bytes):
        """Reproduce bytes de audio MP3 con pygame."""
        buffer = io.BytesIO(audio_bytes)
        pygame.mixer.music.load(buffer)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(50)

    def verificar_credenciales(self) -> bool:
        """
        Verifica que la API key y el Voice ID son válidos.
        Útil para mostrar error al usuario antes de empezar.
        """
        if not self.api_key or not self.voice_id:
            return False
        try:
            url = f"{ELEVENLABS_API_URL}/voices/{self.voice_id}"
            headers = {"xi-api-key": self.api_key}
            r = requests.get(url, headers=headers, timeout=5)
            return r.status_code == 200
        except Exception:
            return False
