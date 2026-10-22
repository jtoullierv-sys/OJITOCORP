# Revisión del ZIP de cPanel — OJITOCORP

Revisión del 15 de octubre de 2026. Archivo recibido: `well-known.zip` (170.747.615 bytes). SHA-256: `ce94e14e4cbb796deadecf5ac481c7a3b668bc441e15b49ceda4d6d1ad5f0a13`.

**Conclusión**

El archivo sirve para analizar la migración. Su nombre no describe todo el contenido: incluye los archivos de dos estructuras WordPress, además de `.well-known`. **El usuario confirmó en cPanel → Dominios que `ojitocorp.com.pe` utiliza `/public_html`.** Se ha seleccionado la configuración de la raíz para sustituir el WordPress informativo por la web actual. La confirmación procede del usuario, no del ZIP. La función de la instalación `wp/` sigue sin confirmarse y se conserva.

**Hallazgos comprobados**

| Elemento | Resultado |
|---|---|
| Integridad del ZIP | CRC correcto en las 23.006 entradas; sin nombres duplicados ni enlaces simbólicos detectados |
| Tamaño descomprimido | 372.981.226 bytes |
| WordPress en la raíz del ZIP | Presentes `index.php`, `wp-admin`, `wp-includes`, `wp-content` y `wp-config.php` |
| WordPress en `wp/` | Segunda estructura con sus propios archivos de entrada, configuración y `.htaccess` |
| Entrada de la raíz | `index.php` carga `wp-blog-header.php` de esa misma raíz |
| Entrada de `wp/` | `wp/index.php` carga el WordPress de `wp/` |
| Caché | Ambas configuraciones incluyen bloques de LiteSpeed para WordPress |
| Reescritura de la raíz | Las rutas virtuales se envían a `/index.php` |
| Reescritura de `wp/` | Las rutas virtuales se envían a `/wp/index.php` |
| PHP en el archivo raíz | Bloque generado por cPanel que declara el handler `ea-php81`; no confirma la versión efectiva del servidor |
| WooCommerce | Archivos del plugin en ambas estructuras; no acredita que esté activo ni que existan pedidos. El usuario confirmó que la web se utiliza como informativa |
| Base de datos | No se encontró un volcado de datos de WordPress. Los `.sql` presentes son estructuras internas del plugin LiteSpeed |
| `.well-known` | Carpeta con el subdirectorio `acme-challenge`; no es el sitio completo |

Se revisó la estructura y se leyeron los archivos de entrada y reglas del servidor. No se ejecutó PHP ni se inspeccionaron pedidos o registros personales. No se copiaron archivos `wp-config.php` al proyecto ni se publicaron sus valores.

**Ruta de sustitución confirmada**

| Carpeta asignada en cPanel | Actuación |
|---|---|
| `/public_html` | Destino confirmado para la nueva web. Respaldar y retirar únicamente el WordPress de esa raíz |
| `/public_html/wp` | Segunda estructura. Conservar sus archivos y configuración hasta conocer su uso |

Las dos estructuras no demuestran que existan dos webs activas: la asignación de la carpeta secundaria y el estado de su base de datos se desconocen. No se debe seleccionar todo el directorio y eliminarlo.

**Configuraciones preparadas**

Se guardaron dos candidatos como texto, fuera de los archivos públicos de la web:

- `exports/cpanel-revision/htaccess-raiz-candidato.txt`: deriva del `.htaccess` raíz. Retira los bloques de WordPress y LiteSpeed, conserva exactamente el bloque PHP generado por cPanel y configura `index.html` como índice.
- `exports/cpanel-revision/htaccess-wp-candidato.txt`: deriva del `.htaccess` de `wp/`, sin inventar un bloque PHP que ese archivo no tenía.
- `exports/cpanel-revision/verificacion.json`: trazabilidad y hashes de las configuraciones originales; no contiene credenciales.

Tras confirmar `/public_html`, se creó **`exports/cpanel-revision/htaccess-public_html.txt`** a partir de la configuración raíz. Conserva byte por byte su handler PHP y selecciona `index.html` primero, con `index.php` como alternativa para los subdirectorios conservados. Esta alternativa evita restringir sus índices a HTML como hacía el candidato inicial. La configuración seleccionada se incluye como `.htaccess` en **`OJITOCORP-CPANEL-PUBLIC_HTML.zip`**.

La configuración no se ha instalado ni validado contra el servidor. Antes de extraer el paquete principal, hay que respaldar el `.htaccess` actual y comprobar que no contiene cambios posteriores a la copia revisada. La selección del índice se apoya en [DirectoryIndex de Apache](https://httpd.apache.org/docs/2.4/mod/mod_dir.html); los permisos de sobrescritura y la compatibilidad efectiva del hosting deben comprobarse al probarlo.

No se agregaron redirecciones de HTTPS o `www` sin conocer dónde se administran actualmente. `OJITOCORP-CPANEL.zip` se conserva sin `.htaccess` para la prueba independiente; el paquete específico de `PUBLIC_HTML` lleva la configuración de raíz seleccionada. Los candidatos previos se mantienen solo como registro del análisis.

**Procedimiento para la raíz confirmada**

1. Guardar este ZIP en almacenamiento privado y obtener también el respaldo de la base de datos desde cPanel. Los archivos de WordPress no contienen los registros de páginas, ajustes, usuarios o posibles datos de plugins que se guardan en la base. [Respaldo de cPanel](https://docs.cpanel.net/cpanel/files/backup-wizard/)
2. Utilizar `/public_html`, confirmado por el usuario. Conservar `wp/` mientras se identifica su uso; no bloquea la instalación de la portada principal.
3. Probar `OJITOCORP-CPANEL.zip` en la carpeta de prueba descrita en `GUIA_CPANEL.md`.
4. Durante el cambio, trasladar únicamente la instalación antigua identificada a un respaldo privado fuera del directorio web. Conservar `.well-known`, `cgi-bin`, otras aplicaciones y carpetas de dominios ajenos al cambio.
5. Extraer `OJITOCORP-CPANEL-PUBLIC_HTML.zip` directamente en `/public_html`, después de respaldar y revisar el `.htaccess` actual. Comprobar dominio, HTTPS, imágenes, categorías, fichas, contacto y las carpetas conservadas.
6. Si falla, apartar los archivos nuevos añadidos, restaurar la instalación y su configuración en las rutas originales y revisar las cachés con el proveedor. La base anterior se conserva durante la transición para facilitar la recuperación.

El sitio en Sites sigue siendo la versión de trabajo publicada. No se ha accedido ni modificado el servidor cPanel. La ruta se confirmó mediante la respuesta del usuario; el ZIP no certifica el DNS, el certificado ni el estado actual del servidor.

**Protección del respaldo**

El ZIP recibido contiene archivos de configuración de WordPress y no debe subirse como descarga pública junto a la nueva web. Conserva el respaldo y cualquier copia de base de datos de forma privada. El paquete para el dominio principal es `OJITOCORP-CPANEL-PUBLIC_HTML.zip`: solo lleva los archivos estáticos de nuestra web y el `.htaccess` preparado, sin credenciales ni respaldo WordPress.
