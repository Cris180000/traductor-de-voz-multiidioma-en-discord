"""
Voice Translator Discord - Punto de entrada principal
Autor: Cris Romero | Romero Web Solutions
"""

import sys
import threading
from config import Config
from core.audio_capture import AudioCapture
from core.transcriber import Transcriptor
from core.translator import Traductor
from core.tts_engine import MotorTTS
from utils.audio_devices import listar_dispositivos
from utils.logger import obtener_logger

logger = obtener_logger(__name__)


def verificar_configuracion(config: Config, tts: MotorTTS) -> bool:
    """Verifica que todo esté configurado antes de arrancar."""
    errores = []

    if not config.ELEVENLABS_API_KEY:
        errores.append("❌ ELEVENLABS_API_KEY no configurada en .env")
    if not config.ELEVENLABS_VOICE_ID:
        errores.append("❌ ELEVENLABS_VOICE_ID no configurado en .env")

    if errores:
        print("\n⚠️  Configuración incompleta:")
        for e in errores:
            print(f"   {e}")
        print("\n   Copia .env.example como .env y rellena los valores.")
        print("   Guía: elevenlabs.io → Profile → API Key\n")
        return False

    # Verificar credenciales con ElevenLabs
    print("   Verificando credenciales ElevenLabs...", end=" ")
    if tts.verificar_credenciales():
        print("✅")
    else:
        print("❌")
        print("   API key o Voice ID inválidos. Revisa el .env\n")
        return False

    return True


def main():
    config = Config()

    print("=" * 52)
    print("  🌐 Voice Translator Discord — v0.2")
    print("  by Romero Web Solutions")
    print("=" * 52)
    print(f"  Modelo Whisper  : {config.WHISPER_MODEL}")
    print(f"  Idioma destino  : {config.IDIOMA_DESTINO}")
    print(f"  Chunk segundos  : {config.CHUNK_SEGUNDOS}s")
    print(f"  Plan actual     : {config.PLAN.upper()}")
    print("=" * 52)

    # Inicializar TTS primero para verificar credenciales
    tts = MotorTTS(
        api_key=config.ELEVENLABS_API_KEY,
        voice_id=config.ELEVENLABS_VOICE_ID,
    )

    print("\n  Verificando configuración...")
    if not verificar_configuracion(config, tts):
        sys.exit(1)

    print("\n  Dispositivos de audio disponibles:\n")
    listar_dispositivos()

    print("\n  Cargando modelo Whisper (primera vez descarga ~74MB)...")
    transcriptor = Transcriptor(modelo=config.WHISPER_MODEL)
    traductor = Traductor()

    captura_mic = AudioCapture(
        device_index=config.MIC_DEVICE_INDEX,
        sample_rate=config.SAMPLE_RATE,
        chunk_size=config.CHUNK_SIZE,
    )

    print("\n✅ Todo listo. Escuchando tu micrófono...")
    print(f"   Habla en cualquier idioma → se traducirá a [{config.IDIOMA_DESTINO}]")
    print("   con TU VOZ clonada por ElevenLabs.")
    print("   Presiona Ctrl+C para salir.\n")
    print("-" * 52)

    captura_mic.iniciar()

    try:
        while True:
            audio = captura_mic.acumular(segundos=config.CHUNK_SEGUNDOS)
            if audio is None:
                continue

            resultado = transcriptor.transcribir(audio)
            if not resultado.texto:
                continue

            print(f"\n🎤 [{resultado.idioma_detectado.upper()}]: {resultado.texto}")

            # Si ya está en el idioma destino, reproducir directamente
            if resultado.idioma_detectado == config.IDIOMA_DESTINO:
                tts.hablar_async(resultado.texto)
                continue

            # Traducir y reproducir con voz clonada
            traduccion = traductor.traducir(
                texto=resultado.texto,
                idioma_destino=config.IDIOMA_DESTINO,
                idioma_origen=resultado.idioma_detectado,
            )

            print(f"🌐 [{config.IDIOMA_DESTINO.upper()}]: {traduccion}")
            tts.hablar_async(traduccion)

    except KeyboardInterrupt:
        print("\n\nDeteniendo traductor...")
    finally:
        captura_mic.detener()
        print("✅ Traductor detenido correctamente.")


if __name__ == "__main__":
    main()
