# Candidatos semana del 2026-08-23

| Negocio | Rubro | URL | Problema principal | Carpeta |
|---|---|---|---|---|
| Coconut Palms of Key West | Tours de snorkel/pesca | https://www.coconutpalmsofkeywest.com/snorkeling.html | Enlaces sin HTTPS en página de reservas, sin viewport, diseño con logo fechado 2019 | [link](./coconut-palms-of-key-west/diagnostico.md) |
| Sunshine Scooters | Alquiler de bicis/scooters | https://www.sunshinescootersinc.com/Bicycles | CMS legado sin viewport, error de copy-paste ("Gas Club Car" en página de bicis) | [link](./sunshine-scooters/diagnostico.md) |
| Art On Duval (Procaccini Galleries) | Galería de arte | https://www.artonduval.com/ | Contenido mínimo, múltiples imágenes rotas/placeholder, sin viewport | [link](./art-on-duval/diagnostico.md) |
| BikeMan Bike Rental Key West | Alquiler de bicis/scooters | https://www.bikemanbikerentalkeywest.com/ | Sin viewport, frontend desactualizado, cache-busting de 2023 sin tocar desde entonces | [link](./bikeman-bike-rental/diagnostico.md) |
| Florida Keys Electric Bikes | Alquiler de bicis/scooters | https://floridakeyselectricbikes.com/ | Sin viewport, logo con ruta de imagen potencialmente rota, sin framework CSS moderno | [link](./florida-keys-electric-bikes/diagnostico.md) |

## Notas de la corrida
- Rubros cubiertos esta semana: alquiler de bicis/scooters, tours de buceo/snorkel/pesca, galerías de arte (primera corrida del pipeline, sin rubros previos en tracker.md).
- Pool inicial: ~20 negocios. Dos dominios (WeCycle, Easy Day Charters) dieron 403 persistente (bot-blocking) y se descartaron como ruido de infraestructura, no como señal de mal sitio.
