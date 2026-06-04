"""
Utilidad para listar los dispositivos de audio disponibles en el sistema.
Ejecutar directamente: python utils/audio_devices.py
"""

import pyaudio


def listar_dispositivos():
    """Imprime todos los dispositivos de audio disponibles con sus índices."""
    p = pyaudio.PyAudio()
    total = p.get_device_count()
    print(f"\nDispositivos de audio ({total} encontrados):\n")
    print(f"{'IDX':<5} {'TIPO':<12} {'NOMBRE'}")
    print("-" * 60)

    for i in range(total):
        info = p.get_device_info_by_index(i)
        tipos = []
        if info["maxInputChannels"] > 0:
            tipos.append("ENTRADA")
        if info["maxOutputChannels"] > 0:
            tipos.append("SALIDA")
        tipo_str = " / ".join(tipos) if tipos else "desconocido"
        print(f"[{i}]   {tipo_str:<12} {info['name']}")

    print("\n💡 Para VB-Cable busca 'CABLE Output' como ENTRADA")
    print("💡 Copia el índice en config.py → MIC_DEVICE_INDEX o DISCORD_DEVICE_INDEX\n")
    p.terminate()


if __name__ == "__main__":
    listar_dispositivos()
