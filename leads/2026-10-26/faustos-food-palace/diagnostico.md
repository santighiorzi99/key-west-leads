# Fausto's Food Palace

- Rubro: Tienda de alimentos / mercado histórico (gourmet, pescadería, carnicería, delicatessen)
- URL original: https://www.faustos.com/
- Rango de precio / tipo de público: institución local desde 1926, dos locales (Fleming St. y White St.), alto tráfico de residentes y turistas con delivery propio
- Proveedor actual del sitio: crédito en el pie de página a "Blue-Turtle" (blue-turtle.com, agencia aún activa) · Última actualización: assets con timestamps de 2010/2013/2014/2019 (sin cambios recientes visibles)

## Por qué es candidato
- [verificado] `curl` al HTML real muestra **cero coincidencias de `viewport`** — el sitio no tiene meta tag responsive y las imágenes del home están fijadas a `width="998px"`, es decir, no se adapta a celular.
- [verificado] El sitio carga `prototype.js` y `scriptaculous.js` (librerías JS reemplazadas por jQuery hace más de una década) y usa el snippet clásico de Google Analytics `_gaq.push(...)` con `ga.js` — la versión de Analytics que Google discontinuó hace años, por lo que ese tracking ya ni siquiera funciona.
- [verificado] Las hojas de estilo se cargan con parámros de cache-busting tipo `core.v.1566414880` y `fader.v.1289226392`, que son timestamps Unix: el más antiguo corresponde a **noviembre de 2010** y el más reciente a **agosto de 2019** — sin evidencia de cambios posteriores.
- [inferido/con salvedad] El pie de página acredita el diseño a "Blue-Turtle" (blue-turtle.com), agencia de Key West que sigue en línea hoy — no se pudo confirmar si la relación de mantenimiento sigue activa o si es un crédito histórico que quedó de la construcción original del sitio (2010-2014). Se marca explícitamente para que el usuario decida si ya hay proveedor pago o no.

## Primera impresión de oportunidad
Institución centenaria con mucho volumen (dos locales, delivery) que puede pagar perfectamente un rediseño, pero su sitio está técnicamente congelado desde hace 10+ años (sin responsive, analytics roto, librerías muertas). Única duda real es el crédito de agencia en el pie — vale la pena confirmarlo antes de avanzar, ya que si la relación sigue activa correspondería descartarlo.
