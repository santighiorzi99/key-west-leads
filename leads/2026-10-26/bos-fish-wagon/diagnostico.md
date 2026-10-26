# BO's Fish Wagon

- Rubro: Restaurante (seafood shack, sandwiches de pescado/conch)
- URL original: https://www.bosfishwagon.com/ (el dominio `.net` del mismo nombre está detrás de un challenge de Cloudflare — se descartó ese y se usó el `.com`, que sí carga)
- Rango de precio / tipo de público: shack histórico, cash-only, muy conocido (cubierto por Travel+Leisure, Infatuation, etc.)
- Proveedor actual del sitio: crédito de imagen en el pie a "wodumedia.com" (la agencia se renombró hace tiempo a "Wodu" / wodu.com; el enlace viejo sigue ahí) · Última actualización: sin fecha detectable, tecnología de ~2009-2011

## Por qué es candidato
- [verificado] `curl` al HTML real muestra **cero coincidencias de `viewport`** — no tiene meta tag responsive, confirmado directamente en el HTML.
- [verificado] El sitio carga `jquery-1.3.2.js` (versión de jQuery de 2009) y el plugin de galería `highslide.js` (lightbox discontinuado hace más de una década), varios recursos cargados por `http://` en vez de `https://` (contenido mixto) dentro de una página servida por HTTPS.
- [verificado] Hay un literal `test` suelto como texto visible en medio del HTML del footer (resto de una edición/depuración que nunca se limpió), justo al lado del logo-crédito de la agencia.
- [inferido/con salvedad] El crédito de imagen enlaza a `http://www.wodumedia.com`, que hoy redirige a `https://www.wodu.com` (la agencia se renombró). No se pudo confirmar si la relación de mantenimiento con ese estudio sigue activa o si es un logo-crédito que quedó de una versión del sitio de hace más de 10 años sin tocar desde entonces. Se marca con salvedad para que el usuario lo confirme antes de avanzar.

## Primera impresión de oportunidad
Marca muy reconocida (sale en notas nacionales de "mejores sandwiches de pescado") con un sitio técnicamente abandonado (jQuery de 2009, sin responsive, HTML con restos de debug). El único freno es el logo-crédito de agencia en el pie — si esa relación ya no está activa (lo más probable dado el estado del código), es un candidato excelente.
