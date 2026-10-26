# Candidatos semana del 2026-10-26

Rubros de esta semana (rotando hacia los menos cubiertos recientemente): restaurantes, tours de snorkel/dive, tiendas de souvenirs. Pool investigado: ~35 negocios de Key West en estos 3 rubros.

| Negocio | Rubro | URL | Problema principal | Carpeta |
|---|---|---|---|---|
| Croissants De France | Cafetería / panadería francesa | https://www.croissantsdefrance.com/ | Dominio caído en un parking de Sedo ("website for sale"), negocio sigue activo (2 locales) pero perdió su URL | [link](./croissants-de-france/diagnostico.md) |
| Honest Eco | Tours de snorkel / dolphin watch | https://www.honesteco.com/ | Dominio redirige a un listado de reventa en GoDaddy marketplace; negocio activo y bien reseñado pero sin sitio propio funcional | [link](./honest-eco-tours/diagnostico.md) |
| Key West Shell Warehouse | Tienda de souvenirs | (sin sitio propio — el directorio oficial enlaza a Facebook) | Sin sitio propio: el campo "website" del directorio de turismo apunta a una página de Facebook | [link](./key-west-shell-warehouse/diagnostico.md) |
| Fausto's Food Palace | Tienda de alimentos / mercado histórico | https://www.faustos.com/ | Sin meta viewport (no responsive), librerías JS de ~2010-2014 (Prototype.js/Scriptaculous), Google Analytics clásico roto. *Pie de página acredita agencia (Blue-Turtle) — a confirmar si sigue activa.* | [link](./faustos-food-palace/diagnostico.md) |
| BO's Fish Wagon | Restaurante (seafood shack) | https://www.bosfishwagon.com/ | Sin meta viewport (no responsive), jQuery 1.3.2 (2009) + lightbox discontinuado, contenido mixto http/https, texto de debug suelto en el HTML. *Pie de página acredita agencia (wodumedia.com, renombrada a wodu.com) — a confirmar si sigue activa.* | [link](./bos-fish-wagon/diagnostico.md) |

Nota: los dos últimos candidatos tienen un crédito de agencia visible en el footer. Según la metodología normalmente eso descarta el candidato, pero se incluyeron con salvedad explícita porque la evidencia técnica de abandono es muy fuerte (código sin tocar hace 10+ años) y no quedó claro si esas agencias (una renombrada, otra sin rastro de actividad reciente en el sitio del cliente) siguen cobrando mantenimiento. Queda a criterio del usuario decidir el estado en el tracker.
