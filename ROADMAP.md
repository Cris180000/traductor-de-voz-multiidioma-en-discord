# 🗺️ ROADMAP — Voice Translator Discord
**by Romero Web Solutions**
Actualizado: Junio 2026 | Basado en análisis competitivo vs HaloVoice, Seagull, Univox

---

## 🎯 Posicionamiento elegido

> **"Sé tú mismo en cualquier idioma."**
> La única app que combina tu voz clonada + traducción saliente + entender a los demás,
> nativa en Discord. Sin robots. Sin voces genéricas. Tú.

### Ventaja diferencial real vs competidores
| Competidor | Lo que hace bien | Lo que le falta | Nuestra ventaja |
|---|---|---|---|
| HaloVoice | Traducción en Discord nativa, <200ms | Sin clonación de voz | Tu voz, no una genérica |
| Seagull | Subtítulos elegantes de los demás | Voice playback = "próximamente" | Ya lo tienes tú |
| Univox | Clona tu voz + traduce | No es nativo en Discord | Nativo en Discord |
| TraducteurAI | Bot viral en servidores | Voz genérica del bot | Suenas como tú |

---

## ⚠️ Riesgo crítico a tener en cuenta

Discord adquirió una startup de traducción. Ventana de oportunidad estimada: **12-18 meses**
antes de que lancen solución nativa. El objetivo es tener base de usuarios y tracción antes de eso.

---

## FASE 0 — Validación real (ahora mismo)
**Duración: 2-4 semanas | Coste: $0**

Objetivo: confirmar que el producto funciona antes de invertir en SaaS.

- [x] MVP funcional en local (tu voz → otro idioma con ElevenLabs)
- [ ] Instalar y probar con tu propia voz clonada
- [ ] Dárselo a tu amiga (freelancer marketing) → feedback real
- [ ] Grabar 1 clip de demo funcionando (30-60 segundos)
- [ ] Recoger testimonio en vídeo si funciona bien

**Métrica de éxito:** el producto funciona y tu amiga lo usaría de verdad.

---

## FASE 1 — MVP completo con diferenciador clave
**Duración: 1-2 meses | Coste: ~$22/mes ElevenLabs**

Objetivo: ser la única app con las 3 funcionalidades juntas.

### Técnico
- [ ] Micrófono virtual (VB-Cable) → tu voz traducida sale como si fuera tu micrófono en Discord
- [ ] Captura audio de Discord (voz de otros) → subtítulos en pantalla en tiempo real
- [ ] UI básica: overlay de subtítulos + panel on/off + selector de idioma destino
- [ ] Soporte 30 idiomas principales (EN, ES, FR, DE, JA, KO, ZH, PT, AR, RU, IT, NL)
- [ ] Migrar STT de Whisper local a **ElevenLabs Scribe v2** (~150ms latencia) o **Deepgram Nova-3**
- [ ] Migrar TTS a **ElevenLabs Flash v2.5** (75ms latencia) para reducir latencia total a ~350ms
- [ ] Ejecutable .exe con PyInstaller (sin necesidad de instalar Python)

### Distribución
- [ ] Landing page simple con lista de espera (sin pagar aún)
- [ ] Grabar 3-5 clips TikTok de demostración (formato: "hablo japonés con mi voz")
- [ ] Identificar 10 servidores Discord grandes con comunidades multinacionales
- [ ] Contactar admins de esos servidores con acceso gratuito

**Métrica de éxito:** 500-1.000 usuarios en lista de espera antes de lanzar.

---

## FASE 2 — Lanzamiento freemium + primeros ingresos
**Duración: 1-2 meses | Coste: según usuarios**

Objetivo: primeros euros reales.

### Producto
- [ ] Sistema de cuentas con Supabase Auth
- [ ] Registro de uso mensual por usuario (caracteres/minutos)
- [ ] Clonación de voz desde la propia app (sin ir a ElevenLabs manualmente)
- [ ] Dashboard web del usuario (plan, uso, gestionar voz clonada)
- [ ] Modo "Invisible": los demás no saben que usas IA

### Monetización
**Pricing ajustado al mercado (referencia: HaloVoice $9,90 / Seagull $6,99):**

| Plan | Precio | Límite | Voz clonada | Idiomas |
|---|---|---|---|---|
| Free | 0€ | 60 min/día | ❌ Voz genérica | 15 |
| Pro | 9,99€/mes | Ilimitado | ✅ Tu voz | 100+ |
| Pro Anual | 69,99€/año | Ilimitado | ✅ Tu voz | 100+ |
| Discord Server | 29,99€/mes | Todo Pro + bot servidor entero | ✅ | 100+ |

> ⚠️ Calcula bien los costes de ElevenLabs antes de lanzar el free tier.
> ElevenLabs Flash v2.5 = ~$0,04 por 1.000 caracteres.
> 60 min/día × 150 chars/min × 1.000 usuarios free = controla el gasto.

- [ ] Integrar Stripe suscripciones recurrentes
- [ ] Gate de features por plan en la app

### Distribución
- [ ] Lanzar en Product Hunt
- [ ] Publicar en r/discordapp, r/gaming, r/languagelearning
- [ ] Contactar 3-5 streamers pequeños con audiencia internacional (pago en Pro gratuito)
- [ ] Activar los clips TikTok preparados en Fase 1

**Métrica de éxito realista:** 50-100 usuarios de pago → $500-1.000 MRR.
*(No 10.000 usuarios en 30 días como sugiere el informe — eso es sin audiencia previa)*

---

## FASE 3 — Tracción y efecto de red
**Duración: 2-4 meses**

Objetivo: que el producto se distribuya solo.

### Producto
- [ ] Bot de Discord opcional para servidores enteros
- [ ] Modo Grupo: hasta 8 personas, cada una oye en su idioma
- [ ] App móvil iOS + Android (WhatsApp, FaceTime, llamadas)
- [ ] Perfiles multilingüe: guarda tu voz para 5 idiomas
- [ ] Historial y transcripciones guardadas
- [ ] Detección automática del idioma del interlocutor

### Distribución
- [ ] Programa de referidos (mes gratis por cada usuario que traes)
- [ ] Identificar 50 servidores Discord grandes → plan Community gratuito 3 meses
- [ ] Cuando un servidor de 50.000 miembros adopta el bot → viral dentro del ecosistema
- [ ] Colaboraciones con streamers internacionales medianos

**Métrica de éxito realista:** 1.000-3.000 usuarios de pago → $10K-30K MRR.

---

## FASE 4 — Escala y moat competitivo
**Duración: 6-12 meses desde lanzamiento**

Objetivo: construir barreras de entrada antes de que Discord lance lo suyo.

### Producto
- [ ] API pública para developers (integra nuestra tecnología)
- [ ] SDK para administradores de Discord
- [ ] Plan Teams para clanes, guilds y comunidades gaming
- [ ] Integración OBS/stream (plan Creator)
- [ ] Reducir latencia a <200ms con modelos locales (Whisper.cpp + TTS local)
- [ ] Considerar modelo de voz propio para reducir dependencia de ElevenLabs

### Defensa ante riesgo ElevenLabs
> Si ElevenLabs sube precios agresivamente, tener alternativas listas:
> Resemble AI, Play.ai, o modelo TTS propio fine-tuneado.

**Métrica de éxito:** 10.000+ usuarios activos, $50K+ MRR, 500+ servidores Discord activos.

---

## 💰 Proyección financiera realista

| Fase | Tiempo | Usuarios pago | MRR estimado |
|---|---|---|---|
| Fase 0-1 | Mes 1-3 | 0 (validación) | $0 |
| Fase 2 | Mes 3-5 | 50-150 | $500-1.500 |
| Fase 3 | Mes 5-9 | 500-1.500 | $5K-15K |
| Fase 4 | Mes 9-18 | 3.000-10.000 | $30K-100K |

> El informe de Perplexity propone $15K MRR en 6 meses.
> Esto es alcanzable SOLO con un clip viral de verdad o inversión en ads.
> Sin eso, los números de arriba son más honestos para un proyecto bootstrapped.

---

## 🔑 Los 3 momentos virales a fabricar primero

Antes de cualquier paid marketing, fabricar estos clips orgánicos:

1. **"Hablo japonés con mi voz"** — alguien que no sabe japonés hablándolo perfectamente
2. **"Mi clan finalmente se entiende"** — equipo de 5 países coordinando en un juego
3. **"Le hablé a mi novia en su idioma"** — pareja con idiomas distintos

Estos clips son el marketing. El producto se demuestra solo en 15 segundos.

---

## 📌 Próximo paso inmediato

**Terminar Fase 0:** instalar la app, clonar tu voz en ElevenLabs, dársela a tu amiga.
Si ella lo usa de verdad → construir. Si no → ajustar antes de invertir más tiempo.
