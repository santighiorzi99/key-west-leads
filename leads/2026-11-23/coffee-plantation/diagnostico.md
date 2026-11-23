# Coffee Plantation
- Rubro: Cafetería
- URL: https://coffeeplantationkeywest.com/
- Rango de precio / tipo de público: cafetería tradicional de Key West ("Original Key West Coffeehouse"), público mixto turista/local, ticket bajo-medio.
- Proveedor actual del sitio: ninguno visible (corre en WordPress, sin créditos de agencia ni plataforma gestionada) · Última actualización: no determinable (la home no carga)

## Por qué es candidato
- [verificado] La home devuelve HTTP 500 en dos intentos separados (`curl -sL -o /dev/null -w "%{http_code}"` → `500` ambas veces), y el cuerpo de la respuesta es la pantalla de error fatal de WordPress: "There has been a critical error on this website." (ver `wp-die-message` en el HTML).
- [verificado] El tamaño de la respuesta es de solo 2.679 bytes — no es la página real, es exclusivamente la pantalla de error de WordPress, con `<title>WordPress › Error</title>`.
- [inferido] En el mismo domicilio (713 Caroline St) aparece hoy "Funky Rooster Coffee House & Wine Bar" en directorios turísticos, lo que sugiere que el negocio pudo haber cambiado de nombre/operador y el sitio viejo quedó abandonado sin que nadie lo mantenga.

## Primera impresión de oportunidad
Caso muy claro y fácil de mostrar: cualquier visitante que entre hoy ve un error técnico de WordPress en vez del negocio. Si todavía operan bajo ese nombre (o bajo el nuevo), es una venta rápida porque el problema es 100% visible e innegable.
