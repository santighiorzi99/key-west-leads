# Papa Scooters
- Rubro: Alquiler de bicis/scooters/golf carts
- URL: http://www.papascooters.com
- Rango de precio / tipo de público: alquiler turístico de scooters de 1-2 plazas y golf carts, público de visitantes de corta estadía
- Proveedor actual del sitio: ninguno — el dominio histórico está parkeado en GoDaddy · Última actualización: no aplica (dominio en reventa)

## Por qué es candidato
- [verificado] `curl` a `http://www.papascooters.com` devuelve HTTP 200 pero el HTML entero es un stub de 114 bytes: `<!DOCTYPE html><html><head><script>window.onload=function(){window.location.href="/lander"}</script></head></html>` — sin contenido, sin meta viewport, solo un redirect por JavaScript.
- [verificado] Siguiendo manualmente a `/lander`, el servidor responde HTTP 403 "Access Denied" apuntando a `forsale.godaddy.com/forsale/www.papascooters.com?...traffic_type=TDFS_BINNS` — el dominio está listado para la venta en el mercado de dominios de GoDaddy, no sirve ningún sitio del negocio.
- [verificado] Directorios turísticos externos (Visit Florida Keys, MapQuest) listan el negocio como activo — "family and veteran-owned", con reseñas recientes en Yelp/Birdeye y domicilio en 5585 2nd Ave #2, Key West — es decir, el negocio sigue operando pero su dominio propio ya no apunta a nada utilizable.
- [inferido] Cualquier cliente que busque "papascooters.com" directamente (en vez de pasar por un directorio) llega a una página de reventa de dominio ajena a la marca, perdiendo la reserva.

## Primera impresión de oportunidad
Caso muy claro y fácil de mostrar: el dominio de la empresa se cayó y quedó listado para la venta en GoDaddy mientras el negocio sigue operando y recibiendo reseñas. Es un alquiler turístico con tráfico recurrente (delivery gratis en toda la isla), así que probablemente puede pagar un sitio nuevo — el pitch es directo: "tu propio dominio ahora muestra un cartel de 'se vende'".
