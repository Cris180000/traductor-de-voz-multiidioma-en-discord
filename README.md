# 🌐 Voice Translator Discord
**by Romero Web Solutions**

Traductor de voz en tiempo real para Discord con **tu propia voz clonada** por ElevenLabs.

Hablas en español → la IA traduce y responde con tu misma voz en el idioma que quieras.

---

## ¿Qué hace?

- 🎤 **Tu voz → otro idioma** con TU VOZ clonada (ElevenLabs)
- 👥 **Voz de otros → subtítulos en español** vía VB-Cable *(Fase 2)*
- 🌍 Soporta +30 idiomas automáticamente

---

## Instalación

### 1. Requisitos previos
- Python 3.11+
- Windows 10/11
- Cuenta en [elevenlabs.io](https://elevenlabs.io) (plan gratuito suficiente para empezar)

### 2. Clonar tu voz en ElevenLabs
1. Ve a **Voices → Add Voice → Instant Voice Cloning**
2. Sube 1-3 minutos de audio tuyo (más = mejor calidad)
3. Copia el **Voice ID** generado

### 3. Configurar credenciales
```bash
cp .env.example .env
# Edita .env y rellena ELEVENLABS_API_KEY y ELEVENLABS_VOICE_ID
```

### 4. Instalar PyTorch CPU
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### 5. Instalar pyaudio en Windows
```bash
pip install pipwin
pipwin install pyaudio
```

### 6. Instalar el resto
```bash
pip install -r requirements.txt
```

---

## Uso

### Ver dispositivos de audio
```bash
python utils/audio_devices.py
```

### Ejecutar
```bash
python main.py
```

---

## Configuración (`config.py`)

| Parámetro | Por defecto | Descripción |
|---|---|---|
| `WHISPER_MODEL` | `"base"` | Modelo Whisper. `tiny`=rápido, `small`=preciso |
| `IDIOMA_DESTINO` | `"en"` | Idioma al que traducir |
| `CHUNK_SEGUNDOS` | `4.0` | Segundos antes de transcribir |
| `MIC_DEVICE_INDEX` | `None` | Índice del micrófono |

---

## Estructura

```
voice-translator-discord/
├── main.py
├── config.py
├── .env.example        ← copia como .env y rellena
├── requirements.txt
├── core/
│   ├── audio_capture.py
│   ├── transcriber.py  ← Whisper (local, gratis)
│   ├── translator.py   ← deep_translator
│   └── tts_engine.py   ← ElevenLabs (voz clonada)
├── utils/
│   ├── audio_devices.py
│   └── logger.py
└── saas/
    └── README_SAAS.md  ← hoja de ruta para monetizar
```

---

## Hoja de ruta

- ✅ **Fase 1** — Tu voz → otro idioma con voz clonada
- ⬜ **Fase 2** — Subtítulos de voz de otros (VB-Cable)
- ⬜ **Fase 3** — UI con panel de control y overlay
- ⬜ **Fase 4** — Ejecutable .exe para Windows
- ⬜ **Fase SaaS** — Web + Supabase + Stripe → producto de pago
