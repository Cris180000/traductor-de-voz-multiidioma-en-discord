# 🚀 Hoja de ruta SaaS — Voice Translator

Este documento describe cómo evolucionar la app de escritorio a un producto SaaS monetizable.

---

## Modelo de negocio propuesto

| Plan       | Precio      | Límite          | Voz clonada | Idiomas |
|------------|-------------|-----------------|-------------|---------|
| Free       | 0€/mes      | 10.000 chars    | ❌ Voz genérica | 3 |
| Pro        | 9€/mes      | 100.000 chars   | ✅ Tu voz    | Ilimitados |
| Team       | 29€/mes     | 500.000 chars   | ✅ Múltiples voces | Ilimitados |

**Margen:** ElevenLabs Pro cuesta ~$22/mes con 100k chars. Con 5 usuarios Pro ya cubre costes.

---

## Stack SaaS

- **Auth + DB:** Supabase (usuarios, planes, uso mensual)
- **Pagos:** Stripe (suscripciones recurrentes)
- **Backend API:** FastAPI o Node.js (gestión de licencias)
- **Desktop app:** Electron o PyInstaller (distribución)
- **Web dashboard:** React + Supabase (gestión de cuenta)

---

## Flujo de usuario SaaS

1. Usuario se registra en la web
2. Elige plan y paga con Stripe
3. Descarga la app de escritorio
4. Inicia sesión → la app obtiene su API key de ElevenLabs y Voice ID desde Supabase
5. Clona su voz desde la app o desde la web
6. Usa el traductor — el uso se registra en Supabase

---

## Tabla Supabase necesaria (futuro)

```sql
-- Usuarios y planes
CREATE TABLE usuarios (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  plan TEXT DEFAULT 'free',         -- 'free' | 'pro' | 'team'
  elevenlabs_api_key TEXT,          -- key propia del usuario (plan pro+)
  elevenlabs_voice_id TEXT,         -- voz clonada del usuario
  caracteres_usados INT DEFAULT 0,  -- uso mensual
  caracteres_limite INT DEFAULT 10000,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## Pasos para llegar al SaaS (después del MVP)

1. ✅ MVP funcional con voz clonada (ahora mismo)
2. ⬜ Dar gratis a amiga → obtener testimonio
3. ⬜ Web landing page con lista de espera
4. ⬜ Integrar Supabase Auth
5. ⬜ Integrar Stripe pagos
6. ⬜ Dashboard web de usuario
7. ⬜ Empaquetar app como .exe con PyInstaller
8. ⬜ Beta privada con 5-10 usuarios
9. ⬜ Lanzamiento público
