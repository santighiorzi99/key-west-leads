# Key West Moped
- Rubro: Alquiler de bicis/scooters (mopeds)
- URL: http://www.keywestmoped.com
- Rango de precio / tipo de público: alquiler turístico de mopeds single/double rider con entrega gratis a hoteles, negocio establecido desde 1998
- Proveedor actual del sitio: ninguno — el dominio histórico quedó convertido en una página de aparcamiento de dominio · Última actualización: no aplica (dominio en parking)

## Por qué es candidato
- [verificado] `curl` a `http://www.keywestmoped.com` devuelve HTTP 200 pero el HTML es un stub idéntico al de otros dominios caídos del mismo patrón: 114 bytes, solo `<script>window.onload=function(){window.location.href="/lander"}</script>`, sin meta viewport ni contenido.
- [verificado] Siguiendo manualmente a `/lander`, el servidor responde HTTP 200 pero carga una "parking lander" de registrador de dominios: `window.LANDER_SYSTEM="CP"`, scripts servidos desde `img1.wsimg.com/parking-lander/...` y `img1.wsimg.com/signals/js/clients/scc-c2/...` (infraestructura de aparcamiento de Website.com/GoDaddy) — no hay ningún contenido del negocio.
- [verificado] Directorios turísticos (Key West Tourist, Visit Florida Keys, Chamber of Commerce) describen el negocio como operativo desde 1998, con domicilio en 5700 4th Ave y teléfono (305) 296-2324, ofreciendo entrega gratuita de mopeds a hoteles.
- [inferido] El negocio sigue funcionando por teléfono/directorios de terceros, pero su propio dominio ya no muestra nada del negocio — pierde el control total de su presencia web directa.

## Primera impresión de oportunidad
Mismo patrón que Papa Scooters pero con un negocio aún más antiguo (28 años de trayectoria) y con mayor dependencia de reservas de turistas que buscan directo por nombre. Al ser un dominio que cayó en manos de un sistema de parking en lugar de una reventa pública, probablemente ni el dueño sabe que pasó — buen gancho para el primer contacto.
