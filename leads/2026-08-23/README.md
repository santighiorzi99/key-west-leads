# Candidatos semana del 2026-08-23

| Negocio | Rubro | URL | Problema principal | Carpeta |
|---|---|---|---|---|
| Coconut Palms of Key West | Tours de snorkel/pesca | https://www.coconutpalmsofkeywest.com/snorkeling.html | Enlaces sin HTTPS en página de reservas, sin viewport, diseño con logo fechado 2019 | [link](./coconut-palms-of-key-west/diagnostico.md) |
| Sunshine Scooters | Alquiler de bicis/scooters | https://www.sunshinescootersinc.com/Bicycles | CMS legado sin viewport, error de copy-paste ("Gas Club Car" en página de bicis) | [link](./sunshine-scooters/diagnostico.md) |
| Art On Duval (Procaccini Galleries) | Galería de arte | https://www.artonduval.com/ | Contenido mínimo, múltiples imágenes rotas/placeholder, sin viewport | [link](./art-on-duval/diagnostico.md) |
| BikeMan Bike Rental Key West | Alquiler de bicis/scooters | https://www.bikemanbikerentalkeywest.com/ | Sin viewport, frontend desactualizado, cache-busting de 2023 sin tocar desde entonces | [link](./bikeman-bike-rental/diagnostico.md) |
| Florida Keys Electric Bikes | Alquiler de bicis/scooters | https://floridakeyselectricbikes.com/ | Sin viewport, logo con ruta de imagen potencialmente rota, sin framework CSS moderno | [link](./florida-keys-electric-bikes/diagnostico.md) |
| Suite Dreams Inn by the Beach | Hotel boutique / guesthouse | https://suitedreamskeywest.com/ | 26+ imágenes rotas (placeholders base64), footer "©2010-" sin cerrar, insignias TripAdvisor de 2016 | [link](./suite-dreams-inn/diagnostico.md) |
| The Paradise Inn | Hotel boutique / guesthouse | https://theparadiseinn.com/ | Texto de bienvenida duplicado, sin viewport, shortcode `[instagram-feed]` sin renderizar en footer | [link](./paradise-inn/diagnostico.md) |
| Kino Sandals | Tienda de souvenirs / calzado artesanal | https://kinosandals.com/ | Sin viewport, HTML genérico con marcado semántico mínimo, layout no responsive | [link](./kino-sandals/diagnostico.md) |
| Flow Spa Key West | Salón de belleza / spa | https://flowspakeywest.com/ | Layout con jerarquía visual inconsistente, CTAs redundantes, reserva externa desconectada del diseño | [link](./flow-spa/diagnostico.md) |
| Tucker's Provisions | Tienda de souvenirs / general store | https://www.tuckersprovisions.com/ | Múltiples imágenes de producto rotas (placeholders GIF con alt text visible) en la vidriera principal | [link](./tuckers-provisions/diagnostico.md) |

## Notas de la corrida
- Corrida 1 (mañana): rubros cubiertos — alquiler de bicis/scooters, tours de buceo/snorkel/pesca, galerías de arte (primera corrida del pipeline, sin rubros previos en tracker.md). Pool inicial ~20 negocios; dos dominios (WeCycle, Easy Day Charters) dieron 403 persistente (bot-blocking) y se descartaron como ruido de infraestructura, no como señal de mal sitio.
- Corrida 2 (tarde): rubros cubiertos — tiendas de souvenirs, salones de belleza/spa, hoteles boutique/guesthouses (rotando a rubros no cubiertos en la corrida anterior). Pool ~13 negocios; Besame Mucho dio 403 persistente y se descartó como ruido de infraestructura.
