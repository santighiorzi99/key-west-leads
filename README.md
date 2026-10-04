# key-west-leads

Pipeline de prospección de negocios locales de Key West con sitios web que necesitan un rediseño. Corre automáticamente cada lunes vía un routine programado (cron) en claude.ai/code/routines, usando la skill `.claude/skills/cazador-de-leads`.

Cada corrida:
1. Busca ~15-20 negocios de Key West en 2-3 rubros distintos.
2. Verifica cada sitio con `curl` (HTML real: caído, sin viewport, placeholders sin renderizar, copyright viejo, etc.) y lee su contenido con `WebFetch`. No saca capturas: el sandbox en la nube no puede correr Chromium.
3. Elige los 5 mejores combinando gravedad verificada del problema y valor del negocio.
4. Escribe un diagnóstico corto por candidato y actualiza `tracker.md`.

Resultados en `leads/<fecha>/`. El estado de cada lead (candidato / en proceso / ganado / perdido) se actualiza a mano en `tracker.md`.

Para avanzar con un candidato (demo + propuesta + email de outreach), se usa la skill `cazador-de-webs` del repo [stinkin-crawfish-kw](https://github.com/santighiorzi99/stinkin-crawfish-kw), pasándole nombre + URL del negocio elegido.

Esta skill nunca contacta a los negocios — solo mira sus sitios públicos y diagnostica. El outreach lo decide y manda el usuario, siempre a mano.
