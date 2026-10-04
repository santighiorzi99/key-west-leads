# /cazador-de-leads

Busca **sin intervención** negocios locales de Key West (cualquier rubro) cuyo sitio web tenga señales claras de necesitar arreglo, diagnostica los 5 mejores candidatos de la semana en base a su HTML/contenido público, y deja todo commiteado en este repo para revisión.

Esta skill **solo descubre y diagnostica** — no arma demo, no despliega, no escribe propuesta ni email. Para eso, una vez que el usuario elige un candidato de la lista, se usa la skill hermana `cazador-de-webs` (repo `stinkin-crawfish-kw`) pasándole el nombre + URL de ese negocio puntual (esa skill sí saca capturas reales con Playwright, corriendo localmente en la máquina del usuario).

Pensada para correr **una vez por semana vía cron** (routine en claude.ai/code/routines), en un sandbox en la nube sin estado entre corridas — cada corrida parte de un checkout limpio de este repo. También se puede correr a mano si el usuario pide "buscá negocios para prospectar" o similar.

**Nota técnica:** esta skill diagnostica sin capturas de pantalla. Se probó correr Playwright/Chromium dentro del sandbox en la nube y el navegador headless no logra completar el handshake HTTPS a través del proxy de salida del sandbox (`net::ERR_CONNECTION_RESET`, confirmado no resoluble incluso configurando el proxy explícitamente y confiando su CA) — es una limitación del entorno, no del sitio target.

**Importante:** `WebFetch` NO devuelve el HTML crudo — devuelve un resumen procesado por otro modelo. Por eso no sirve para afirmar cosas del código (meta viewport, tablas, doctype, imágenes) y en las primeras corridas generó muchos falsos positivos. Las señales técnicas se verifican con `curl` sobre el HTML real (Paso 3); `WebFetch` se usa solo para leer el contenido/texto.

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

## Paso 3 — Prefiltro y diagnóstico

### 3a. Señales técnicas con `curl` (HTML real)

Para cada uno del pool, bajá la home con `curl` y sacá las señales del HTML crudo:

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
curl -sL -m 20 -A "$UA" -o home.html -w "%{http_code} %{url_effective}\n" "$URL"
grep -ci 'name="\?viewport' home.html          # 0 = de verdad no es responsive
grep -oi '<meta name="generator"[^>]*' home.html  # plataforma (WordPress, Wix, Square...)
grep -oi 'copyright[^<]\{0,40\}\|©[^<]\{0,40\}' home.html | head -3
grep -c '{{[a-z_]*}}\|\[[a-z_-]*feed[^]]*\]' home.html   # placeholders/shortcodes sin renderizar
grep -ci 'plus.google\|spacer.gif\|<font\|<table' home.html
# ¿ya tienen agencia/diseñador? (créditos en el footer y servicios administrados)
sed 's/<[^>]*>/ /g' home.html | tr -s ' \n\t' ' ' | grep -oiE '(design|designed|developed|marketing|managed|built|created)[^.|]{0,40} by [^.|<]{0,40}'
grep -oiE 'hibu|thryv|yodle|web\.com|scorpion|bentobox|popmenu|[a-z0-9-]+(media|digital|marketing|agency|creative)\.(com|net)' home.html | sort -u
grep -oiE 'article:modified_time" content="[^"]*"|"dateModified":"[^"]*"' home.html | head -1   # última actualización
```

Si `curl` falla, repetí una vez más tarde y verificá DNS (`getent hosts <dominio>` o `dig +short`) para distinguir caído de bloqueado.

### 3b. Contenido con `WebFetch`

Usá `WebFetch` solo para leer qué dice la página (cuánto texto real tiene, si están dirección/horarios/precios/reserva, errores de contenido como textos copiados de otra sección o datos contradictorios). No le pidas que juzgue el código.

### 3c. Cómo interpretar las señales

**Señales fuertes (verificadas):**
- El dominio no resuelve (DNS), timeout o 5xx (500/502/503/522) en **dos intentos separados** → sitio caído. Es la mejor señal posible, no es ruido.
- Sin sitio propio (solo Facebook/Instagram/directorios).
- Placeholders o shortcodes visibles para el visitante (`{{...}}`, `[instagram-feed]`), contenido duplicado, datos contradictorios (dos direcciones, textos de otra página).
- Copyright con un año viejo (ej. "© 2018"), botones de redes muertas (Google+), links a `localhost` o `href="#"` en la navegación principal.
- `curl` confirma que no hay meta viewport, o que es HTTP sin redirección a HTTPS.

**NO son señales (falsos positivos comunes):**
- Imágenes como `data:image/gif;base64,R0lGOD...` o SVG vacíos con `data-src`/`loading="lazy"`: es carga diferida, en el navegador se ven bien.
- Textos "Loading..." o poco texto en sitios que cargan contenido con JavaScript (Wix, Squarespace, Square Online, ArtCloud, widgets de reserva). Solo cuentan si `WebFetch` tampoco encuentra el contenido.
- Copyright con el año actual: está bien, no es un error.
- Copyrights viejos que vienen de licencias de fuentes o librerías en el CSS/JS ("Copyright 2011 The Montserrat Project Authors", "Copyright 2010, 2012 Adobe"): no son del sitio. Solo cuenta el copyright del footer con el nombre del negocio.
- Un dominio "caído" o "estacionado" que adivinaste vos: usá siempre la URL que figura en el directorio (Cámara de Comercio, visitfloridakeys.com) o en Google, y limpiale espacios al final antes de chequearla.
- 403/406 o páginas de challenge de Cloudflare: es bot-blocking, ruido de infraestructura. Descartá el candidato y pasá al siguiente.
- Que `WebFetch` "no detecte" meta viewport: no lo puede ver, usá `curl`.

### 3d. Elegir los 5

Quedate con los **5 mejores candidatos** combinando:
1. **Gravedad verificada** del problema (caído / sin sitio > error visible > sitio viejo).
2. **Valor del negocio**: priorizá los que pueden pagar un rediseño (hoteles, restaurantes con mucho tráfico, tours con reserva online, servicios que consiguen clientes por la web) por sobre negocios muy chicos o cash-only.
3. **Ya tienen proveedor**: si el footer acredita a una agencia o diseñador ("Site Design by Overseas Media Group", "Design by ...") o el sitio corre en un servicio administrado con abono mensual (Hibu, Thryv, Scorpion, BentoBox, Popmenu...), **descartalo**: ya le pagan a alguien y el sitio tiene mantenimiento. La única excepción es un sitio caído pese al crédito: ahí mencioná el proveedor en el diagnóstico. Lo mismo si `dateModified` o el contenido muestran que se actualizó en los últimos ~12 meses: no es un sitio abandonado.
4. **Quién decide**: descartá sucursales de cadenas o propiedades manejadas por un grupo (ej. una inn que redirige al sitio de su empresa madre), porque el dueño local no decide el sitio.

Si hay empate, priorizá diversidad de rubro (no 5 restaurantes).

## Paso 4 — Diagnóstico corto por candidato

Para cada uno, escribí `${REPO_ROOT}/leads/<fecha>/<slug>/diagnostico.md`:

```markdown
# <Nombre del negocio>
- Rubro: <rubro>
- URL: <url>
- Rango de precio / tipo de público (si es identificable): ...
- Proveedor actual del sitio: <agencia/plataforma acreditada, o "ninguno visible"> · Última actualización: <fecha si se encontró>


## Por qué es candidato
- [verificado] <problema concreto 1, con la evidencia: código HTTP, línea de HTML, texto exacto>
- [verificado] <problema concreto 2>
- [inferido] <problema concreto 3 (opcional), si no lo pudiste confirmar con curl>

## Primera impresión de oportunidad
<1-2 líneas: qué tan urgente/vendible es este caso y si el negocio parece poder pagar>
```

Marcá cada bullet como `[verificado]` (lo confirmaste en el HTML real con `curl` o en el contenido con `WebFetch`) o `[inferido]`. Ningún candidato puede quedar elegido solo con bullets `[inferido]`. No inventes problemas ni uses los falsos positivos del Paso 3c — 3 a 5 bullets concretos alcanza, no hace falta el checklist completo de `cazador-de-webs` acá (eso se hace en detalle cuando el usuario elige avanzar con `/cazador-de-webs`, que sí saca capturas reales).

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

- Un `curl` (más un reintento si falla) y un `WebFetch` por candidato — no scraping agresivo, no loops en paralelo contra el mismo dominio.
- Esta skill **nunca contacta al negocio** de ninguna forma (ni email, ni formulario, ni redes) — solo mira su sitio público. El outreach lo hace el usuario a mano, después, vía `cazador-de-webs`.
- No repitas negocios que ya estén en `tracker.md`.
