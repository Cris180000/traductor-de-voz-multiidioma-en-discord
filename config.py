"""
Configuración global del traductor.
Modifica aquí los valores según tu sistema.

Para producción/SaaS: estos valores vendrán de base de datos por usuario.
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()  # Carga variables del archivo .env


@dataclass
class Config:
    # --- Audio ---
    SAMPLE_RATE: int = 16000
    CHUNK_SIZE: int = 1024
    CHUNK_SEGUNDOS: float = 4.0

    # --- Dispositivos de audio ---
    MIC_DEVICE_INDEX: int | None = None
    DISCORD_DEVICE_INDEX: int | None = None  # VB-Cable (Fase 2)

    # --- Whisper ---
    WHISPER_MODEL: str = "base"  # tiny, base, small, medium, large

    # --- Idiomas ---
    IDIOMA_DESTINO: str = "en"  # "es", "en", "fr", "de"...

    # --- ElevenLabs (TTS con voz clonada) ---
    # Se leen del .env — nunca hardcodear API keys en el código
    ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY", "")
    ELEVENLABS_VOICE_ID: str = os.getenv("ELEVENLABS_VOICE_ID", "")

    # --- SaaS (futuro) ---
    # En versión SaaS estos campos vendrán por usuario desde Supabase
    # PLAN: "free" | "pro"
    # free  → límite de caracteres mensuales, sin voz clonada propia
    # pro   → voz clonada, sin límite, multiidioma
    PLAN: str = "free"
    CARACTERES_MES_FREE: int = 10_000  # Límite plan gratuito ElevenLabs

    # --- Logging ---
    LOG_LEVEL: str = "INFO"
