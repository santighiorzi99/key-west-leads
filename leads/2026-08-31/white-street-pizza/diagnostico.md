# White Street Pizza
- Rubro: Restaurante (pizzería italiana)
- URL: https://www.whitestreetpizza.com/
- Rango de precio / tipo de público: casual, locales y turistas, gama media

## Por qué es candidato
- El HTML servido tiene `<title></title>` vacío — sin título de página, mal para SEO básico.
- El sitio es un shell de "Square Online" que depende 100% de JavaScript del lado del cliente: el HTML crudo (verificado con `curl`) solo trae un spinner de carga (`loading-view`), sin contenido real (sin texto de menú, dirección ni nada) hasta que el navegador ejecuta el bundle de JS.
- Como consecuencia, WebFetch no pudo extraer ningún contenido de la página — mismo problema que enfrentaría un crawler o alguien con JS lento/deshabilitado.

## Primera impresión de oportunidad
Caso interesante: negocio con buena reputación (reviews positivas, local desde 2024) pero con un sitio armado en un builder genérico que no expone contenido indexable — pérdida de SEO y de primera impresión real.
