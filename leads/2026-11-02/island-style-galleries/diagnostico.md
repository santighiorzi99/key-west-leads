# Island Style Galleries

- Rubro: Galería de arte / artesanías (tienda de regalos)
- URL: https://www.islandstylegalleries.com/
- Rango de precio / tipo de público: tienda de arte y artesanía americana en 512 Duval St, descrita en directorios como "one of the top 100 retailers of American crafts"
- Proveedor actual del sitio: ninguno visible (WordPress autoalojado, tema antiguo sin mantenimiento aparente) · Última actualización: no determinable

## Por qué es candidato
- [verificado] No hay ninguna meta `viewport` en el HTML (`grep -c viewport` = 0): el sitio no está preparado para mobile pese a correr en WordPress.
- [verificado] Una de las hojas de estilo del tema está rota: `<link rel="stylesheet" href=".../wp-content/themes/complexity-2/layout/css/style/.css">` — la URL queda con el nombre de archivo vacío (termina en `style/.css`), y un `curl -I` a esa misma URL confirma `HTTP/2 404`.
- [verificado] El `<title>` de la portada queda literalmente como `Island Style Galleries | ` (con un placeholder de plantilla sin completar después de la barra "|"), visible en el código fuente.
- [verificado] El tema usado (`complexity-2`) es una plantilla de WordPress antigua; no aparece ningún `<meta name="generator">` de WordPress moderno ni señales de actualización reciente.
- [inferido] Dado que el CSS de "color variation" no carga, es probable que partes del diseño visual (colores del tema) no se vean como fueron pensadas originalmente.

## Primera impresión de oportunidad
Negocio real y de cierto prestigio (top 100 retailers de artesanía americana, en pleno Duval St), pero con un sitio WordPress visiblemente abandonado: sin versión mobile y con un recurso roto que cualquier visitante puede notar en el inspector. Buen caso para un rediseño responsive.
