# OJITOCORP: instalar la web actual en cPanel

Actualizado el 15 de octubre de 2026. El usuario confirmó que `ojitocorp.com.pe` utiliza `/public_html` y que la nueva web sustituirá al WordPress informativo. La carpeta de destino ya está definida. No se ha accedido ni modificado el servidor.

## Paquetes entregados

| Archivo local | Uso |
|---|---|
| `OJITOCORP-CPANEL-PUBLIC_HTML.zip` | Instalación principal en `/public_html`: incluye `index.html`, `css/`, `js/`, `assets/` y `.htaccess` directamente en la raíz |
| `OJITOCORP-CPANEL.zip` | La misma web sin `.htaccess`, útil para una prueba en una carpeta independiente |
| `OJITOCORP-CPANEL-PUBLIC_HTML.sha256.txt` | Hash del paquete principal y commit de origen |

El paquete principal incluye el logo sin acento y el correo `atencionalcliente@ojitocorp.com.pe` en Conversa. No contiene WordPress, credenciales, bases de datos, instrucciones internas ni configuración de Sites. La guía se entrega aparte; no forma parte de la web pública. La nueva web es estática y no necesita la base de datos antigua. Su formulario prepara la conversación para que el visitante la envíe por WhatsApp o correo.

## Antes de cambiar la web

1. En **cPanel → Copias de seguridad / Asistente de copias de seguridad**, genera y descarga un respaldo. Conserva también copias parciales de los archivos y de la base de datos del WordPress principal para facilitar la recuperación. `well-known.zip` sirve como copia de archivos, pero no contiene un volcado de datos de WordPress. Guarda los respaldos en tu equipo y fuera de cualquier carpeta pública. La restauración automática de una copia completa requiere al proveedor o WHM. [Documentación de copias de cPanel](https://docs.cpanel.net/cpanel/files/backup-wizard/)

2. Abre **Administrador de archivos → public_html**. En Configuración, activa **Mostrar archivos ocultos**. Descarga el `.htaccess` actual antes de sustituirlo. El archivo raíz revisado tenía bloques de WordPress, LiteSpeed y el handler PHP generado por cPanel; su SHA-256 es `a71ecd4753ac25321ffbe49601f699162be957e04358a8d198ad3d506e468d6f`. Si ha cambiado desde la copia enviada, revisa las diferencias antes de extraer el paquete principal: las reglas nuevas del hosting deben conservarse o adaptarse. No apliques la configuración antigua sobre cambios sin revisar.

3. Crea una carpeta privada de respaldo **fuera de `public_html` y de las raíces de otros dominios**, por ejemplo `respaldo-ojitocorp-2026-10-15` en el directorio principal de tu cuenta. Descarga también su contenido al equipo. Anota los nombres y ubicaciones de los archivos que traslades para poder restaurarlos.

## Prueba previa recomendada

Puedes probar la web antes del cambio con un subdominio como `preview.ojitocorp.com.pe`, con carpeta propia y sin compartir la raíz principal. Es una propuesta; no se ha creado. Si el DNS se administra fuera de cPanel, configura el registro allí y comprueba el certificado HTTPS. [Crear un dominio o subdominio](https://docs.cpanel.net/cpanel/domains/domains/create-a-new-domain/), [estado SSL/TLS](https://docs.cpanel.net/cpanel/security/ssl-tls-status/).

En esa carpeta de prueba, extrae **`OJITOCORP-CPANEL.zip`**, que no lleva configuración del servidor. Abre primero `/index.html` y después la raíz del subdominio. Revisa categorías, fichas y contacto. Si se heredan redirecciones de WordPress o el índice no funciona, revisa esa carpeta con el proveedor; no cambies el `.htaccess` principal para arreglar la prueba.

## Sustituir el WordPress de public_html

4. Con el respaldo descargado, traslada **solo la instalación WordPress de la raíz** a la carpeta privada. En la copia revisada se identificaron:

   - `wp-admin/`, `wp-content/` y `wp-includes/` de `public_html`.
   - `index.php`, los archivos `wp-*.php` de esa raíz —incluido `wp-config.php`— y `xmlrpc.php`.
   - `license.txt` y `readme.html` de esa instalación.
   - El `.htaccess` original y su copia `.htaccess.bk`, si todavía coincide con el inventario revisado. El paquete nuevo colocará su propio `.htaccess`.

   **Conserva en su sitio `.well-known/`, `cgi-bin/`, `wp/` y las carpetas de otros dominios o aplicaciones.** `wp/` contiene otra estructura WordPress y su función aún no está confirmada; no hace falta retirarla para sustituir la portada principal. No utilices «Seleccionar todo» para mover o eliminar el directorio. Si ya existen `index.html`, `css/`, `js/` o `assets/`, identifica su uso y respáldalos antes de reemplazarlos. No mezcles las carpetas nuevas con archivos antiguos sin inventariar.

5. Sube **`OJITOCORP-CPANEL-PUBLIC_HTML.zip`** a `public_html`, selecciónalo y pulsa **Extraer** en esa misma ubicación. No crees una carpeta llamada `dist` ni extraigas dentro de `wp/`. [Administrador de archivos de cPanel](https://docs.cpanel.net/cpanel/files/file-manager/)

   La raíz debe quedar así, además de las carpetas conservadas:

   ```text
   public_html/
   ├── .htaccess
   ├── index.html
   ├── css/
   ├── js/
   └── assets/
   ```

   Comprueba que `.htaccess` aparece al mostrar archivos ocultos. Evita permisos `777`; conserva los permisos normales que asigne el hosting al extraer.

6. Abre **`https://ojitocorp.com.pe/index.html`** y luego **`https://ojitocorp.com.pe/`**. Comprueba también la dirección con `www`. Si aparece la versión anterior, prueba una recarga completa y revisa las cachés del hosting o CDN. Si hay un error 500 tras aplicar `.htaccess`, restaura la copia anterior y pide al proveedor revisar las directivas permitidas; si sus reglas remiten al WordPress retirado, restaura también esa instalación o solicita la adaptación del índice estático.

7. Completa esta comprobación en escritorio y móvil:

   - Inicio y las cinco categorías cambian correctamente; las imágenes, las fuentes y el logo cargan.
   - Los enlaces con `#tecnologia`, `#negocios`, `#digital`, `#alimentos` y `#formacion` funcionan al abrirlos directamente y al recargar.
   - Explorar abre cada ficha, el cierre funciona y Consultar selecciona el producto o servicio en el formulario.
   - El correo de Conversa es `atencionalcliente@ojitocorp.com.pe` y el teléfono coincide con el actual.
   - El formulario valida y prepara la consulta; no envíes mensajes de prueba reales a la empresa.
   - HTTPS funciona, no se producen bucles y las carpetas de otros sitios conservadas siguen respondiendo.

8. Tras verificar, retira el ZIP subido de la carpeta pública y conserva tu copia local. Mantén el respaldo de WordPress y su base de datos privados durante la transición. Revisa con el proveedor las tareas programadas y cachés que pertenecían al WordPress retirado. La eliminación definitiva de su base de datos puede hacerse después, cuando se confirme que no la usa ninguna otra instalación y exista un respaldo recuperable.

Si el dominio ya apunta a este hosting, la sustitución se realiza en su carpeta actual: no requiere cambiar DNS ni los registros de correo. El enlace temporal de Sites se conserva como versión de trabajo.

## Qué contiene el .htaccess preparado

La configuración elegida deriva del `.htaccess` **raíz** enviado. Retira sus bloques de WordPress y LiteSpeed y conserva byte por byte el bloque PHP generado por cPanel. No añade redirecciones de HTTPS o `www`: el archivo recibido no tenía reglas propias de ese tipo y el hosting puede administrarlas aparte.

La selección del índice es:

```apache
DirectoryIndex disabled
DirectoryIndex index.html index.php
```

Da prioridad a la portada estática y conserva `index.php` como alternativa para los subdirectorios existentes que lo utilicen. Se añadió esa alternativa respecto al candidato inicial para evitar limitar los índices de la carpeta `wp/` que se conserva. El soporte efectivo de estas directivas todavía debe comprobarse en tu hosting. [Referencia de DirectoryIndex de Apache](https://httpd.apache.org/docs/2.4/mod/mod_dir.html)

El archivo seleccionado también está disponible como `exports/cpanel-revision/htaccess-public_html.txt`. Los dos candidatos anteriores se conservan como registro del análisis; no se deben aplicar ambos ni usar el de `wp/` para la raíz principal.

## Cómo volver al sitio anterior

Si el cambio falla, aparta los archivos nuevos identificados en el inventario (`index.html`, `css/`, `js/`, `assets/` y el nuevo `.htaccess`), y devuelve los archivos de WordPress y el `.htaccess` original desde el respaldo a sus ubicaciones exactas. Restaura también cualquier archivo previo que el paquete sustituyera. No muevas las carpetas conservadas ajenas al cambio. La base antigua se mantiene durante la transición; si se modificó, utiliza además su copia. Revisa la caché con el proveedor y comprueba nuevamente el dominio.

## Futura tienda

| Dirección | Aplicación prevista | Datos |
|---|---|---|
| `ojitocorp.com.pe` | Esta web corporativa | Archivos estáticos; contacto hacia WhatsApp/correo |
| `tienda.ojitocorp.com.pe` | Tienda con una carpeta independiente | Su propia base de datos y archivos de medios |

El subdominio no crea automáticamente una base de datos. Cuando se implemente la tienda, se puede instalar, por ejemplo, WordPress + WooCommerce con base y usuario propios, configurando productos, pagos, existencias, envíos y correos. Antes de elegirlo, comprueba los recursos y requisitos vigentes del hosting. [Requisitos de WooCommerce](https://woocommerce.com/document/server-requirements/), [asistente de bases de datos de cPanel](https://docs.cpanel.net/cpanel/databases/database-wizard/).

La web actual conserva el enlace de tienda a `/shop/`. Como no hay una tienda activa confirmada, compruébalo en la revisión de contenido. Cuando exista la tienda futura, actualiza `company.shop` en `sites/ojitocorp/dist/js/config.js` y genera otro paquete. Esta entrega no crea ecommerce ni base de datos.

## Estado de entrega

| Comprobación | Estado |
|---|---|
| Directorio principal `/public_html` | Confirmado por el usuario en cPanel |
| Contenido e integridad de `well-known.zip` | Revisados; informe en `REVISION_CPANEL_ZIP.md` |
| Respaldo de datos WordPress en el ZIP recibido | No encontrado; obtenerlo en cPanel |
| Configuración de raíz seleccionada | Preparada; handler PHP original conservado |
| Paquete estático e integridad ZIP | Verificados localmente al exportar |
| Uso de `wp/` por otro dominio | Pendiente; carpeta conservada |
| Instalación, HTTPS y funcionamiento en cPanel | Pendientes; sin acceso al servidor |

Para regenerar el paquete desde el workspace: `python scripts/package-cpanel.py --public-html`. El informe y `exports/cpanel-revision/verificacion.json` registran la procedencia de la configuración. No es necesario compartir contraseñas ni archivos `wp-config.php` por el chat.
