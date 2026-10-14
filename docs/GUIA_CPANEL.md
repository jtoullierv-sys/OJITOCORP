# OJITOCORP: subir la web a cPanel y preparar una futura tienda

Preparada el 13 de octubre de 2026 para la entrega vigente de OJITOCORP, con el logo sin acento y el correo de atención al cliente en Conversa. El usuario confirmó que el WordPress actual es informativo, no contiene una tienda y será reemplazado por completo. El resultado final es esta web estática como sitio corporativo principal; WordPress queda retirado y respaldado fuera de la carpeta pública.

El ZIP de instalación es `OJITOCORP-CPANEL.zip`, en la raíz del workspace. La guía se entrega por separado y no debe subirse como parte de la web. El paquete incluye `index.html`, `css/`, `js/` y `assets/` directamente en su raíz. No incluye `.htaccess`, Git, instrucciones internas ni configuración de Sites. Su integridad y las referencias HTML se comprueban al generarlo; el hash está en `OJITOCORP-CPANEL.sha256.txt`.

**Lo que muestra tu captura**

Hay archivos de WordPress: `wp-admin`, `wp-content`, `wp-includes`, `wp-config.php` e `index.php`. La imagen no muestra la ruta completa de esa carpeta ni el contenido de `.htaccess`. Debemos confirmar la carpeta del dominio en cPanel, no deducirla solo de la captura.

No borres esos archivos para probar la nueva portada. Conserva también `.well-known`, `cgi-bin`, `wp` y las reglas existentes de `.htaccess`. La función de la carpeta `wp` no se puede determinar por su nombre. La base de datos de WordPress se gestiona aparte de los archivos.

**Primero: respaldo y prueba sin reemplazar WordPress**

1. En cPanel, abre el asistente de copias de seguridad. Genera una copia completa y descárgala al terminar. Guarda el respaldo fuera de las carpetas públicas. Para una recuperación sencilla, descarga también las copias parciales del directorio principal y de la base de datos de WordPress. La restauración automática de una copia completa requiere al proveedor o WHM. [Copias de seguridad de cPanel](https://docs.cpanel.net/cpanel/files/backup-wizard/)

2. Ve a Dominios y localiza `ojitocorp.com.pe`. Anota su carpeta raíz real. Conserva una copia descargada de su `.htaccess` y de cualquier `index.html` existente antes de modificarlos.

3. Crea un subdominio de prueba, por ejemplo `preview.ojitocorp.com.pe`, desde Dominios → Crear un nuevo dominio (o Subdominios en paneles antiguos). Desmarca compartir la carpeta del dominio principal y utiliza una carpeta independiente, como `public_html/ojitocorp-preview`, si el panel la permite. Este nombre es una propuesta, no un subdominio ya creado. [Crear dominios y subdominios](https://docs.cpanel.net/cpanel/domains/domains/create-a-new-domain/)

4. Comprueba dónde se administra el DNS. Si es externo al hosting, añade allí el registro de `preview` con la IP indicada por tu proveedor. Si ya se administra en este cPanel, comprueba el registro en su editor de zona. No hace falta cambiar los registros de correo para esta prueba.

5. Comprueba en el estado SSL/TLS que el subdominio tenga un certificado válido. Si AutoSSL no lo genera, pide al proveedor que revise DNS y emisión. Accede por HTTPS cuando el certificado esté activo. [Estado de certificados](https://docs.cpanel.net/cpanel/security/ssl-tls-status/)

6. Abre el Administrador de archivos en la carpeta asignada al subdominio. Sube `OJITOCORP-CPANEL.zip` y extráelo allí. Al terminar deben aparecer directamente `index.html`, `css`, `js` y `assets`; no una carpeta superior llamada `dist`. [Administrador de archivos](https://docs.cpanel.net/cpanel/files/file-manager/)

7. Abre `https://preview.ojitocorp.com.pe/index.html`. Revisa Inicio, las cinco categorías, imágenes, Explorar, cierre de las fichas y Consultar. Revisa también el móvil, el logo y el nuevo correo de Conversa. Puedes comprobar la selección del formulario sin enviar mensajes reales. Luego prueba la URL del subdominio sin `index.html`.

8. Si aparece WordPress, una redirección al dominio principal o un error 500, revisa con el proveedor las reglas aplicadas a esa carpeta y su índice predeterminado. No reemplaces todo el `.htaccess` del dominio principal para corregir el subdominio.

**Después: reemplazar el sitio informativo antiguo**

9. Una vez aprobada la prueba y descargado el respaldo, vuelve a la carpeta real de `ojitocorp.com.pe`. Revisa si hay otras aplicaciones o carpetas de subdominios. Identifica los archivos de la instalación antigua: `wp-admin`, `wp-content`, `wp-includes`, sus archivos `wp-*.php`, `index.php` y `xmlrpc.php`. Confirma la función de `wp` y de los demás archivos antes de incluirlos. Durante el cambio, traslada la instalación identificada a una carpeta privada de respaldo fuera de `public_html`, dentro de tu cuenta; no la dejes accesible desde una URL. Conserva `.well-known`, `cgi-bin`, la carpeta de prueba y las carpetas de otros dominios. `.htaccess` se trata por separado en el paso 11.

10. Extrae `OJITOCORP-CPANEL.zip` en la raíz del dominio. Si ya existían `index.html`, `css`, `js` o `assets`, deben estar identificados y respaldados antes de sustituirlos. Comprueba `https://ojitocorp.com.pe/index.html` y luego `https://ojitocorp.com.pe/`. La instalación nueva entrega `index.html` y las carpetas estáticas; no requiere la base de datos del WordPress anterior.

11. Revisa el `.htaccess` existente con su copia de respaldo a mano. Retira las reglas que envían las solicitudes al WordPress eliminado, así como las reglas de caché específicas de esa instalación que puedan interceptar la portada. Conserva y adapta los ajustes de HTTPS, hostname y las directivas del hosting que aún correspondan. En Apache que permita estas directivas, una configuración candidata para el índice estático es:

```apache
DirectoryIndex disabled
DirectoryIndex index.html
```

Estas líneas no son un `.htaccess` completo ni reemplazan su revisión. La primera reinicia una lista anterior y la segunda selecciona `index.html`. La configuración definitiva depende del servidor y de las reglas actuales. Si aparece un error 500, restaura la copia de `.htaccess` y pide al proveedor revisar las directivas permitidas. [Directiva DirectoryIndex de Apache](https://httpd.apache.org/docs/2.4/mod/mod_dir.html)

12. Comprueba la nueva web con y sin `www`, HTTPS, todas las categorías, fichas, fotografías y contactos. Revisa las URLs de páginas antiguas y acuerda redirecciones a destinos pertinentes cuando se necesiten. WordPress ya no será el sitio activo. Si hay tareas programadas o cachés asociadas al antiguo WordPress, revísalas con el proveedor para completar su retirada.

13. Para revertir, aparta los archivos nuevos que hayas añadido, restaura la instalación antigua en sus rutas originales y repón su `.htaccess` y cualquier archivo anterior sustituido. La base de datos antigua se conserva durante la transición; si se modificó, utiliza también su respaldo. Otras reglas o cachés pueden necesitar restauración adicional. Conserva el inventario de archivos trasladados para poder deshacer el cambio.

14. Tras verificar el sitio, retira el ZIP de la carpeta pública y conserva su copia local. Guarda el respaldo antiguo en almacenamiento privado. La base de datos anterior queda sin uso por esta web estática; su eliminación se decide después de confirmar la sustitución y disponer de un respaldo recuperable.

Si el dominio ya apunta a este hosting, subir la nueva portada allí no requiere cambiar sus servidores DNS. La prueba y la activación en tu cPanel todavía no se han ejecutado: se ha preparado el paquete y esta guía.

**Futura tienda en un subdominio**

La estructura propuesta es:

| Dirección propuesta | Aplicación | Datos |
|---|---|---|
| `ojitocorp.com.pe` | Portada corporativa actual | Archivos estáticos; formulario hacia WhatsApp/correo |
| `tienda.ojitocorp.com.pe` | Tienda, por ejemplo WordPress + WooCommerce | Base MySQL/MariaDB de la tienda y archivos de medios |

El subdominio identifica dónde se sirve la tienda. No crea una base de datos ni convierte el catálogo actual en ecommerce automáticamente.

1. Crear `tienda.ojitocorp.com.pe` con una carpeta propia, sin compartir la raíz corporativa. Configurar su DNS y certificado.
2. Verificar con el proveedor que el plan permite otra aplicación, base de datos, usuarios y recursos suficientes. WooCommerce es una opción para hosting con PHP y MySQL/MariaDB; comprobar sus requisitos vigentes antes de instalarlo. [Requisitos de WooCommerce](https://woocommerce.com/document/server-requirements/)
3. Instalar WordPress y WooCommerce en esa carpeta. Si el instalador crea la base y el usuario, verificar qué creó. Para una instalación manual, usar el asistente de bases de datos de cPanel: crear una base propia, un usuario y asignarlo con los permisos necesarios para la aplicación. [Asistente de bases de datos](https://docs.cpanel.net/cpanel/databases/database-wizard/)
4. Configurar productos reales, existencias, pagos, envíos, correo transaccional y las páginas legales de la tienda. El catálogo informativo actual no confirma esos datos ni los implementa.
5. Cuando la tienda funcione, cambiar `company.shop` en `js/config.js` desde la dirección actual `/shop/` al subdominio. Ese enlace aún no se ha cambiado porque la tienda futura no existe.

La aplicación guarda y consulta productos, clientes y pedidos en el servidor MySQL/MariaDB. cPanel administra esa base, sus usuarios y copias; el visitante no se conecta directamente a ella. Conviene una base y un usuario propios para la tienda.

**Para concretar la sustitución**

Falta confirmar la carpeta raíz de `ojitocorp.com.pe`, el inventario de la instalación antigua y el contenido de su `.htaccess`. Esas comprobaciones permiten concretar qué se traslada al respaldo y qué reglas se conservan. Para revisar las reglas basta ese archivo, con cualquier dato sensible oculto. No se necesita compartir `wp-config.php`, contraseñas de cPanel ni credenciales de base de datos por el chat.
