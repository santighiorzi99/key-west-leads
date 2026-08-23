# /cazador-de-leads

Busca **sin intervención** negocios locales de Key West (cualquier rubro) cuyo sitio web tenga señales claras de necesitar arreglo, diagnostica los 5 mejores candidatos de la semana en base a su HTML/contenido público, y deja todo commiteado en este repo para revisión.

Esta skill **solo descubre y diagnostica** — no arma demo, no despliega, no escribe propuesta ni email. Para eso, una vez que el usuario elige un candidato de la lista, se usa la skill hermana `cazador-de-webs` (repo `stinkin-crawfish-kw`) pasándole el nombre + URL de ese negocio puntual (esa skill sí saca capturas reales con Playwright, corriendo localmente en la máquina del usuario).

Pensada para correr **una vez por semana vía cron** (routine en claude.ai/code/routines), en un sandbox en la nube sin estado entre corridas — cada corrida parte de un checkout limpio de este repo. También se puede correr a mano si el usuario pide "buscá negocios para prospectar" o similar.

**Nota técnica:** esta skill diagnostica solo con `WebFetch` (HTML/contenido), sin capturas de pantalla. Se probó correr Playwright/Chromium dentro del sandbox en la nube y el navegador headless no logra completar el handshake HTTPS a través del proxy de salida del sandbox (`net::ERR_CONNECTION_RESET`, confirmado no resoluble incluso configurando el proxy explícitamente y confiando su CA) — es una limitación del entorno, no del sitio target. `WebFetch` sí funciona bien y da señales suficientes para diagnosticar.

## Resolver `SKILL_DIR`

`SKILL_DIR` es el directorio que contiene este `SKILL.md`.

```bash
REPO_ROOT="<raíz del repo, dos niveles arriba de .claude/skills/cazador-de-leads>"
```

## Paso 1 — Ver qué ya se prospectó

Leé `${REPO_ROOT}/tracker.md`. Extraé la lista de negocios (nombre + URL) que ya aparecen ahí de semanas anteriores — **no los vuelvas a elegir** esta semana, aunque su sitio siga siendo malo (ya están en el pipeline, el usuario decide qué hacer con ellos).

## Paso 2 — Descubrir candidatos (pool amplio)

Rubros a rotar semana a semana para cubrir todo Key West, no repetir siempre lo mismo (mirá qué rubros ya se cubrieron en `tracker.md` y priorizá los que falten):

restaurantes, bares, cafeterías, tiendas de souvenirs, alquiler de bicis/scooters, tours de buceo/snorkel/pesca, salones de belleza/spa, tiendas de ropa, galerías de arte, hoteles boutique/guesthouses, servicios (limpieza, mudanzas, etc).

Elegí 2-3 rubros para esta semana. Usá `WebSearch` con queries tipo `"<rubro> key west florida"`, `"best <rubro> key west site:yelp.com"`, o directorios locales (Key West Chamber of Commerce, TripAdvisor, Yelp) para armar un pool de **~15-20 negocios** con nombre + URL de su sitio propio (no cuenta si solo tienen página de Facebook/Instagram sin sitio — anotalo igual, es una señal fuerte de "necesita sitio").

## Paso 3 — Prefiltro y diagnóstico vía WebFetch

Para cada uno del pool, usá `WebFetch` sobre la home (pedile explícitamente que evalúe: si carga o tira error/timeout, si redirige a Facebook/Instagram en vez de tener sitio propio, si es HTTP sin HTTPS, cuánto texto/contenido real tiene, si el HTML se ve viejo — tablas de layout, `<font>`, sin meta viewport — o genérico/desactualizado, y cualquier señal roja concreta como imágenes rotas, links a `localhost`, doctypes antiguos, viewport no responsive, etc).

Quedate con los **5 candidatos con peores señales**. Si hay empate, priorizá diversidad de rubro (no 5 restaurantes). Si algún dominio da error de red persistente (bot-blocking tipo Cloudflare, 403 reiterado) descartalo y reemplazalo por el siguiente candidato del pool — no lo cuentes como señal de mal sitio, es ruido de infraestructura.

## Paso 4 — Diagnóstico corto por candidato

Para cada uno, escribí `${REPO_ROOT}/leads/<fecha>/<slug>/diagnostico.md`:

```markdown
# <Nombre del negocio>
- Rubro: <rubro>
- URL: <url>
- Rango de precio / tipo de público (si es identificable): ...

## Por qué es candidato
- <problema concreto 1, con base en lo que viste en las capturas/HTML>
- <problema concreto 2>
- <problema concreto 3 (opcional)>

## Primera impresión de oportunidad
<1-2 líneas: qué tan urgente/vendible es este caso>
```

No inventes problemas que no viste en el HTML/contenido — 3 a 5 bullets concretos alcanza, no hace falta el checklist completo de `cazador-de-webs` acá (eso se hace en detalle cuando el usuario elige avanzar con `/cazador-de-webs`, que sí saca capturas reales).

## Paso 5 — Reporte semanal + tracker

Creá `${REPO_ROOT}/leads/<fecha>/README.md`:

```markdown
# Candidatos semana del <fecha>

| Negocio | Rubro | URL | Problema principal | Carpeta |
|---|---|---|---|---|
| ... | ... | ... | ... | [link](./<slug>/diagnostico.md) |
```

Agregá una fila por candidato a `${REPO_ROOT}/tracker.md` (creá el archivo con encabezado si no existe):

```
| Negocio | Rubro | URL original | Fecha encontrado | Carpeta recon | Estado |
|---|---|---|---|---|---|
| <Negocio> | <rubro> | <url> | <fecha> | leads/<fecha>/<slug>/ | Candidato — pendiente de revisión |
```

El usuario actualiza manualmente el campo "Estado" a medida que decide (descartado / en proceso con cazador-de-webs / ganado / perdido).

## Paso 6 — Commit y push

```bash
cd "$REPO_ROOT"
git add leads tracker.md
git commit -m "leads: semana $(date +%Y-%m-%d)"
git push
```

## Al terminar, reportá

- Los 5 candidatos (nombre, rubro, 1 línea de por qué), no el diagnóstico completo repetido.
- Que están commiteados en el repo, en `leads/<fecha>/`.
- Que para avanzar con alguno, se corre `/cazador-de-webs <nombre> <url>` (en el repo `stinkin-crawfish-kw`, donde vive esa skill) para armar demo + propuesta + email.

## Seguridad / límites

- Un `WebFetch` por candidato — no scraping agresivo, no loops en paralelo contra el mismo dominio.
- Esta skill **nunca contacta al negocio** de ninguna forma (ni email, ni formulario, ni redes) — solo mira su sitio público. El outreach lo hace el usuario a mano, después, vía `cazador-de-webs`.
- No repitas negocios que ya estén en `tracker.md`.
