# Key West Dive Center

- Rubro: Tours de buceo/snorkel
- URL: https://www.keywestdivecenter.com/
- Rango de precio / tipo de público: operador de buceo/snorkel de rango medio orientado a turistas (snapshots indexados describen "Key West's Top Dive Center Since 2003" y paquetes tipo "Rum and Reggae Sunset and Snorkel Cruise")
- Proveedor actual del sitio: ninguno visible · Última actualización: no determinable (el dominio ya no sirve el sitio)

## Por qué es candidato
- [verificado] El certificado TLS que entrega `www.keywestdivecenter.com` es para otro dominio completamente distinto (`CN=dino-detective.metalseed.io`); curl reporta `SSL: no alternative certificate subject name matches target host name`.
- [verificado] Tanto `http://` como `https://` (con `-k` para ignorar el error de certificado) devuelven el mismo HTML de 163 bytes: un `<meta http-equiv="refresh" CONTENT="0;URL=/cgi-sys/defaultwebpage.cgi">`, que es la página por defecto de una cuenta de hosting cPanel sin sitio configurado.
- [verificado] No hay ningún contenido real del negocio servido en el dominio — ni horarios, ni precios, ni forma de reservar — pese a que el negocio sigue apareciendo en resultados de búsqueda y directorios de buceo (PADI, Sport Diver).
- [inferido] El negocio probablemente dejó caer la configuración de hosting/DNS en algún momento reciente sin darse cuenta, ya que el dominio sigue registrado a su nombre pero no apunta a nada funcional.

## Primera impresión de oportunidad
Caso muy vendible: el negocio lleva "Since 2003" y aparece en guías de buceo serias (PADI, Sport Diver), pero quien busque su web hoy llega a una página de hosting vacía — están perdiendo reservas directas 100% del tiempo. Alta probabilidad de que puedan pagar un sitio nuevo dado el tamaño de la operación.
