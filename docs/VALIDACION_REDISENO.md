# Validación del rediseño por ambientes

Versión local 2.0.7. Fecha: 12 de octubre de 2026, Perú. Vista: http://127.0.0.1:4180/. Se conserva el Site original; no se publicó este rediseño.

| ID | Estado | Evidencia real |
|---|---|---|
| V01 | Aprobado | Inicio inspeccionado en escritorio y 390 px; logo centrado, explicación concreta y CTA visible. Capturas en `qa/ambientes/`. |
| V02 | Aprobado | Se recorrieron las cinco áreas y se guardaron sus capturas. Paletas, imágenes, contenido y catálogos propios; la portada de las cinco categorías comparte la composición de Alimentos, mientras Inicio recupera su composición propia en 2.0.7. |
| V03 | Ajustado por solicitud del usuario | En 2.0.7 se corrige el alcance: Inicio vuelve a una composición propia; la portada basada en Alimentos se aplica solo a las cinco áreas. Los catálogos conservan distribuciones propias. Capturas `ui-*.jpg`. |
| V04 | Aprobado | Ola observada al entrar en Tecnología y Alimentos; atributo `right` al avanzar, `left` al regresar a Negocios. Overlay oculto al terminar. Contacto y footer fuera de la escena. |
| V05 | Aprobado | Cinco selecciones rápidas desde el header; resultado final Formación, hash correcto y un único overlay oculto. No se encadenan escenas intermedias. |
| V06 | Aprobado | 32 fichas recorridas individualmente; contenido específico, imagen y CTA. 31 en catálogo principal y conectividad en bloque de evaluación. `qa/ambientes/fichas.json`. |
| V07 | Aprobado | Botón y Escape cierran; foco retorna al elemento disparador. Fondo habilitado al terminar el evento de cierre. |
| V08 | Aprobado | Borrador de nombre, correo, teléfono y mensaje conservado al consultar Café; formulario selecciona `alimentos` + `ali-cafe`. Cambio de área limpia el elemento y explica el cambio. |
| V09 | Aprobado | URL de WhatsApp inspeccionada y texto decodificado por la comprobación Node: área y Café correctos; ampersand, tildes y saltos codificados. No se envió el mensaje. |
| V10 | Aprobado | Los seis hashes se abrieron y recargaron individualmente. Hash desconocido muestra Inicio útil. |
| V11 | Aprobado | Atrás desde contacto vuelve a Alimentos; Adelante restaura contacto conservando el área. No agrega historial al restaurar. |
| V12 | Aprobado | Probados servicios, soluciones, productos, equipamiento, consultoría, desarrollo, nosotros, visión y posibilidades. Mapeo descrito más abajo. |
| V13 | Aprobado | Inicio y cinco áreas recorridos en 320, 390, 768, 1280 y 1440 px. Sin desbordamiento horizontal; logo dentro del header. Revisión visual móvil y escritorio. Evidencia DOM en `qa/ambientes/tamanos.json`. |
| V14 | Aprobado | Enter abre área y ficha; menú móvil se cierra y enfoca la introducción. Tab y Shift+Tab circulan entre cierre y consulta del modal; Escape devuelve foco. Se corrigió un escape de foco observado en el navegador. |
| V15 | No ejecutado | No se pudo emular la preferencia real del dispositivo en la API de este navegador. Pausa manual comprobada: ola oculta, cambio instantáneo y `animation-name: none` en texto e imagen. CSS/JS incluyen el mismo bloqueo para `prefers-reduced-motion` y cambios de preferencia. |
| V16 | No ejecutado | Prueba parcial aprobada: se retiraron temporalmente ambas resoluciones de laptop, se recargó Tecnología y cargó el fallback `repair-800.webp` con alt de área. Archivos restaurados. La red lenta no pudo emularse; no se presenta como probada. El controlador no espera imágenes para desbloquear navegación. |
| V17 | Aprobado | 20 fotografías reales verificadas en páginas gratuitas y descargadas desde enlaces publicados. Cada área usa tres distintas y cada familia tiene un visual pertinente. Dos WebP por foto; registro en ASSETS_UTILIZADOS.md. |
| V18 | Aprobado | Revisión de las 32 descripciones y el registro editorial: sin precios, stock, resultados o formatos inventados. Conectividad explícitamente en evaluación; conceptos ambiguos fuera de la oferta principal. |

## Ajuste de espacios — versión 2.0.1

Se compactaron las reglas existentes de padding, márgenes y gaps, sin añadir una hoja de overrides. Las introducciones crecen según su contenido en lugar de reservar altura de pantalla. Digital integra la ilustración en su columna visual y sustituye las tarjetas que ocupaban dos filas por una tarjeta horizontal destacada. Alimentos presenta los tres elementos de cada grupo en filas completas. Los textos secundarios y 13 tarjetas de Negocios, Digital y Formación ahora explican cómo orientar la consulta; se añadió una guía breve junto al formulario.

Se recorrieron Inicio y las cinco áreas en 320, 390, 768, 1280, 1440 y 2560 px: 36 estados sin desbordamiento horizontal y con el logo dentro del header. Las cantidades del catálogo permanecen 9/5/5/9/3. Evidencia: `qa/ambientes/espacios-tamanos.json`; capturas de catálogo, contacto y móvil con prefijo `espacios-`. Se inspeccionaron visualmente las nuevas filas de Digital y Alimentos, Formación en móvil y escritorio y la ficha de Café. La ficha abre sin desbordamiento y su CTA selecciona `alimentos` + `ali-cafe` en el formulario.

Tras selecciones rápidas Digital → Tecnología → Formación, prevalece Formación, la ola queda oculta y la animación de entrada permanece activa (`copy-arrive`). Sin errores de consola en la pestaña de comprobación. El servidor de revisión sigue en el puerto 4180. Este ajuste no modifica la publicación ni la identidad del Site. Los límites de las pruebas de movimiento reducido y red lenta indicados en V15 y V16 siguen vigentes.

## Orden de Tecnología y Negocios — versión 2.0.2

Tecnología tiene una columna de texto más amplia y un titular proporcionado, accesos a Equipos y Soporte TI, cuatro tarjetas con acciones alineadas y cinco servicios distribuidos en filas de tres y dos en escritorio. En tablet y móvil los servicios usan una lista vertical. La fotografía secundaria técnica se integra en el bloque explicativo.

Negocios usa una portada editorial con fotografía y nota alineadas, accesos a dos grupos y un índice de tres asesorías de gestión empresarial. Las dos propuestas de educación financiera y digital tienen su propio bloque. Los cinco IDs, contenido, fotografías de ficha y selección en contacto se conservan.

Comprobaciones reales:

- Tecnología y Negocios en 320, 390, 768, 1280, 1440 y 2560 px: 12 estados sin desbordamientos ni titulares, tarjetas o accesos fuera del viewport. Grupos 4+5 y 3+2. Evidencia en `qa/ambientes/orden-tamanos.json`.
- Accesos directos por clic y Enter: desplazan al grupo y enfocan su encabezado. En móvil se comprobó el acceso a Gestión de tu empresa con teclado.
- En 1440 px las cuatro acciones de Equipos tienen la misma posición vertical; también se alinean las acciones de cada fila de Servicios TI. Filas con alturas 185/161 px.
- Se abrieron las cinco fichas de Negocios, cada una con título, imagen y contenido; Escape cierra y devuelve el foco. Sin desbordamiento de los diálogos.
- Consulta de Constitución selecciona `negocios` + `neg-constitucion`; consulta de Laptops selecciona `tecnologia` + `tec-laptops` en el formulario.
- Transiciones entre las áreas terminan con la ola oculta; sin errores de consola en la pestaña de comprobación.

Capturas con prefijo `orden-` en `qa/ambientes/`. Este ajuste sigue siendo local; los límites de emulación de V15/V16 no cambian.

## Fotos, simetría y separadores — versión 2.0.3

Las cinco tarjetas de Negocios vuelven a mostrar fotografías y usan la misma composición de imagen y texto, tanto en Gestión como en Educación. Los cinco servicios TI ahora son filas del mismo ancho y proporción, manteniendo el orden del catálogo. Las portadas de ambas áreas usan columnas iguales. Se retiró el aviso final del catálogo solicitado por el usuario.

Todos los subtemas del catálogo tienen un único borde superior de 2 px con color más visible. Cada grupo aplica el mismo padding superior e inferior: 32 px en escritorio y 24 px en móvil. El encabezado del catálogo y los bloques explicativos siguen ese mismo ritmo; se eliminaron márgenes y bordes duplicados de la implementación anterior.

Comprobaciones reales:

- Inicio y cinco ambientes en 320, 390, 768, 1280, 1440 y 2560 px: 36 estados sin desbordamientos ni elementos principales fuera del viewport. Todos los grupos tienen padding superior igual al inferior y borde de 2 px. El texto retirado no aparece en ninguno de los estados.
- Negocios conserva cinco fotografías de tarjeta en los seis anchos. En 1440 px las cinco tarjetas miden 1280 × 282 px y sus imágenes 419 × 232 px.
- Tecnología: en 1440 px las cinco filas TI miden 1280 × 148 px, con imágenes de 106 px de alto.
- Las imágenes de las tarjetas abren su ficha. Consultar Hardware selecciona `tecnologia` + `tec-hardware`; consultar Constitución selecciona `negocios` + `neg-constitucion`. Transición de área completa con ola oculta; sin errores de consola.
- Revisión visual de ambos catálogos en escritorio y de Negocios en móvil. Capturas `simetria-tecnologia.jpg`, `simetria-negocios.jpg` y `simetria-movil.jpg`; mediciones en `qa/ambientes/simetria-tamanos.json`.

Las fotos y los datos comerciales existentes se conservan. Este ajuste sigue siendo local. Los límites de emulación de V15 y V16 siguen vigentes.

## Fichas y acción de exploración — versión 2.0.4

Las fichas comparten los colores del ambiente del elemento seleccionado. El cierre tiene icono SVG centrado y una barra sticky con espacio propio; se retiraron los márgenes negativos. El botón visible de consulta usa el mismo texto corto y dimensiones comunes. Las tarjetas conservan sus fotos y títulos y una sola acción «Explorar ↗», con nombre accesible específico por elemento. Conectividad incluye una fotografía de router y mantiene su estado de línea en evaluación. El pie de fotografía y la nota genérica final solicitados se retiraron de las fichas.

Comprobaciones reales:

- 32 fichas abiertas y cerradas individualmente en 1440 px: paleta correcta, cierre dentro del panel, icono centrado en ambos ejes, CTA de 280 × 48 px, sin desbordamiento ni los textos retirados. Evidencia: `qa/ambientes/fichas-ajustadas.json`.
- Una ficha de cada categoría en 320, 390, 768, 1280, 1440 y 2560 px: 30 estados válidos, cierre centrado y dentro del panel, CTA de 48 px de alto y ancho adaptable, sin desbordamiento horizontal. Evidencia: `qa/ambientes/fichas-responsive.json`.
- El primer recorrido responsive se interrumpió durante la navegación; se reinició con recarga de la pestaña de prueba en cada categoría y tandas cortas. Los 30 estados guardados corresponden al recorrido completo posterior.
- Tab pasa de cierre a consulta y vuelve a cierre; Escape cierra. En móvil, al enfocar consulta el diálogo se desplaza 143 px y la barra de cierre permanece visible.
- Consultar Marketing selecciona `digital` + `dig-marketing` en el formulario. La ficha de conectividad carga `network-800.webp` y mantiene la nota específica sobre implementación/cobertura.
- Una única acción de detalle por cada uno de los 32 IDs, verificada también en `npm run build`. Sin errores de consola en la pestaña de comprobación.

Capturas: `ficha-tecnologia.jpg`, `ficha-digital.jpg`, `ficha-movil.jpg` y `conectividad-imagen.jpg`. La nueva foto se registra junto a las demás en ASSETS_UTILIZADOS.md (21 fuentes). La identidad de hosting y los datos de contacto se conservan.

## Distribución del contenido de las fichas — versión 2.0.5

La imagen y la descripción ocupan la primera fila. La fotografía se ajusta a su altura, sin quedar aislada encima de una columna vacía. Alcance y público usan dos columnas debajo a todo el ancho; las siete fichas con variantes incorporan un bloque adicional con opciones en dos columnas. El pie de consulta y las notas específicas también aprovechan el ancho del diálogo. En móvil, las filas se convierten en una sola columna. Se mantienen el contenido, las paletas, el cierre y la conexión con contacto.

Comprobaciones reales:

- Las 32 fichas abiertas y cerradas en 1440 × 1000 px: imagen y descripción con igual altura, bloques inferiores del ancho del contenido y separación de 24 px después de la fila superior. Sin desbordamiento horizontal. Evidencia: `qa/ambientes/fichas-distribucion.json`.
- Una ficha de cada categoría en 320, 390, 768, 1280, 1440 y 2560 px: 30 estados sin desbordamiento; contenido apilado en móvil y CTA de 48 px de alto. Se eligieron fichas con títulos largos, variantes y notas adicionales. Evidencia: `qa/ambientes/fichas-distribucion-responsive.json`.
- En 390 × 844 px, Tab enfoca consulta y desplaza el diálogo 493 px manteniendo visibles el botón y la barra de cierre. Tab y Shift+Tab recorren ambos controles; Escape cierra y devuelve el foco a Explorar. Consultar Activos digitales y blockchain selecciona `negocios` + `neg-blockchain` y enfoca nombre. Evidencia: `qa/ambientes/fichas-distribucion-interaccion.json`.
- Revisión visual de Desarrollo personal, Vinos con opciones y una ficha móvil. Capturas: `ficha-distribucion-formacion.jpg`, `ficha-distribucion-opciones.jpg`, `ficha-distribucion-movil.jpg`. Sin errores de consola en la pestaña de comprobación.
- `npm run build` comprueba los módulos y recursos del proyecto. El auditor estático de Frontend Design Premium en modo strict terminó sin hallazgos (`distribucion-audit.json`); su configuración por defecto excluye `dist/`, por lo que la evidencia de la fuente editable se apoya en la comprobación del proyecto y el recorrido real del navegador. No se añadieron contratos de administración a esta web de marca.

## Portadas y enlaces comunes — versión 2.0.6

Por solicitud expresa del usuario, Inicio y las cinco categorías comparten la composición de Alimentos: fotografía hasta el borde derecho, texto editorial a la izquierda, degradado y frase sobre la imagen. Las paletas, los protagonistas fotográficos, el contenido y los catálogos se conservan por área. Esta decisión sustituye la diferenciación de portadas del paquete original. En móvil se apilan texto y fotografía. Se retiraron los accesos adicionales de Tecnología y Negocios y sus reglas/manejador, así como el aviso «Línea en evaluación. Implementación y cobertura por confirmar.» del bloque de Tecnología.

«Explorar» tiene una etiqueta separada de su flecha SVG: 18 px, 8 px de distancia y alineación al centro. El hover aplica una línea de 1 px solo al texto, a 4 px de distancia. Las acciones de portada, contacto y footer comparten el mismo tratamiento. Se sustituyeron las reglas existentes, sin añadir hojas de overrides ni dependencias.

Comprobaciones reales:

- Seis portadas en 320, 390, 768, 1280, 1440 y 2560 px: 36 estados sin desbordamiento horizontal, fotografía hasta el borde, frase dentro de la foto y separada del pie. Móvil apila texto y fotografía. No aparecen los accesos o el aviso retirados. Evidencia: `qa/ambientes/portadas-enlaces-responsive.json`.
- Los 32 botones de catálogo, en cada ancho, conservan una flecha centrada y un gap de 8 px. El estado hover se comprobó en Negocios: subrayado en la etiqueta; botón y SVG sin subrayado. Captura `explorar-alineado.jpg`.
- Las 32 fichas se abrieron haciendo clic en el SVG de su botón. Escape cierra y devuelve el foco al mismo ID. Evidencia: `qa/ambientes/explorar-svg-fichas.json`.
- «Ver la oferta» desplaza al catálogo (y = 90 px). El CTA de portada, pulsado sobre el SVG, prepara `tecnologia` + `general` en contacto. Evidencia: `qa/ambientes/portadas-enlaces-interaccion.json`.
- La revisión de proporciones se realizó con la pausa manual activada. Se restauró el movimiento y se seleccionó Digital → Tecnología → Negocios rápidamente: prevalece Negocios, la ola termina oculta y las entradas `copy-arrive`/`photo-arrive` permanecen activas. Sin errores de consola en la pestaña de comprobación.
- Capturas `portada-inicio.jpg`, `portada-tecnologia.jpg`, `portada-negocios.jpg`, `portada-digital.jpg`, `portada-alimentos.jpg`, `portada-formacion.jpg` y `portadas-movil.jpg`. Se inspeccionaron visualmente las portadas y el botón con hover. `npm run build` verifica la entrega actual.

Las fotos, los contactos y la identidad de alojamiento se conservan. El estado específico de conectividad en las fichas no se convierte en una disponibilidad comercial confirmada.

## Inicio, áreas y contacto — versión 2.0.7

Se corrigió el alcance de la referencia de Alimentos: Inicio recupera un titular propio, fotografía de arco y dos recortes subordinados; la portada con degradado se mantiene exclusivamente en las cinco categorías. Se aplicaron los métodos de diseño web y UI móvil solicitados. Las decisiones vigentes están en `docs/DISENO_UI_UX.md`.

Tecnología tiene cuatro equipos comparables y filas TI con título/descripción juntos. Negocios presenta tres asesorías y dos propuestas educativas. Digital destaca Marketing y ordena los otros servicios por parejas. Formación muestra tres propuestas comparables. Alimentos conserva su escala y refina marcos, textos y acciones. Los bloques explicativos agrupan las fotos con el texto. Las tarjetas conservan todas sus fotografías, IDs y acción específica; el recorte de celulares destaca el teléfono existente mediante CSS.

Contacto usa verde de marca y formulario claro, con canales visibles y Hablemos en el header. En una columna la guía queda debajo del formulario. El acceso general enfoca el título; una consulta de ficha muestra el formulario y enfoca nombre. La selección de área se prepara solo si está vacía, salvo una consulta explícita de ficha/portada. Escape en el menú devuelve foco a su botón. La barra de scroll mantiene su espacio al abrir diálogos.

Comprobaciones reales:

- Inicio y cinco áreas en 320, 390, 768, 1280, 1440 y 2560 px: 36 estados sin desbordamiento horizontal ni textos recortados. Inicio tiene `home-intro`; las cinco áreas tienen `scene-intro`. Header, logo, Hablemos y campos permanecen dentro de sus columnas. Inputs de al menos 48 px y 16 px de texto. Evidencia: `qa/ambientes/ui-ux-responsive.json`.
- La primera comprobación en 320 px detectó tres títulos TI más anchos que su columna. Los servicios se apilaron con foto arriba para ese tamaño y se repitió el recorrido completo. El botón de envío se compactó: una línea y 48.5 px de altura.
- En escritorio las acciones de cada fila de tarjetas quedan alineadas. Se inspeccionaron visualmente Inicio, los cinco catálogos y Contacto; capturas `ui-inicio.jpg`, `ui-catalogo-*.jpg` y `ui-contacto.jpg`, además de las versiones móviles.
- Las 32 fichas se abrieron desde el SVG y se consultaron: categoría/ID correctos, diálogo cerrado, nombre enfocado y visible. Desplazamiento horizontal del header al abrir = 0. Evidencia: `qa/ambientes/ui-fichas-formulario.json`. La primera tanda se interrumpió al alcanzar el tiempo máximo de la herramienta; el JSON guardado corresponde al recorrido completo posterior.
- Una ficha de cada categoría en 320 × 844 px confirma nombre visible y enfocado, selección correcta y ausencia de desbordamiento. Evidencia: `qa/ambientes/ui-fichas-movil.json`.
- En 390 px, el menú permite seleccionar Tecnología con Enter, se cierra y enfoca el titular. Hablemos enfoca `contact-title` y prepara Tecnología al estar vacía la selección. Escape en el menú vuelve a su botón. Tab/Shift+Tab circulan entre cierre y consulta del diálogo; Escape vuelve a Explorar.
- Se restauró el movimiento y se seleccionó Digital → Tecnología → Formación: prevalece Formación, la ola termina oculta y `copy-arrive` sigue activa. Evidencia: `qa/ambientes/ui-navegacion-final.json`. Sin errores de consola en la pestaña de comprobación.
- Un envío local con campos vacíos conserva oculto el resultado y enfoca Nombre inválido. Con datos de prueba válidos se generan enlaces de WhatsApp/correo y se enfoca el resultado. No se abrieron ni enviaron esos enlaces. Consultar Desarrollo personal después conserva el nombre y mensaje de prueba y selecciona `formacion` + `for-desarrollo`. Evidencia: `qa/ambientes/ui-ux-interaccion.json`.

Se conservaron contactos, fuentes, logo transparente, fotografías e identidad de hosting. La revisión de geometría usó la pausa manual, restaurada al finalizar. Los límites generales de emulación de dispositivo, red lenta y certificación de accesibilidad siguen vigentes.

## Comprobaciones técnicas

`node scripts/check.mjs` y `npm run build`: sintaxis de todos los módulos, 32 IDs únicos, descripciones de al menos 40 palabras, recursos y fuentes, cinco áreas + Inicio, rutas/aliases, dirección de ola y mensaje codificado. La vista responde HTTP 200. Sin errores de consola en la sesión final tras corregir el arranque del modal; los errores 404 de la prueba de imagen fueron intencionales y los recursos se restauraron.

Las pruebas no miden puntuaciones de rendimiento ni certifican accesibilidad completa. No se simuló una red lenta ni la preferencia real del sistema. El peso de las 40 versiones WebP y el registro de fuentes es aproximadamente 3.1 MB para toda la colección; no se descarga toda al inicio.

## Decisiones de navegación

Se conserva scroll vertical nativo. Atrás/Adelante retorna consistentemente a la introducción de la categoría o al contacto, en lugar de restaurar offsets antiguos de escenas con alturas diferentes. Se registra el scroll previo como contexto, pero no se utiliza para forzar una posición que pueda pertenecer a otro layout.

- `#servicios` y `#soluciones`: Inicio y su índice de áreas.
- `#productos`: Alimentos y bebidas.
- `#equipamiento`: Tecnología.
- `#consultoria`: Negocios.
- `#desarrollo`: Formación.
- `#nosotros`, `#vision`, `#posibilidades`: Inicio; las secciones abstractas anteriores se condensaron.
- `#contacto`: contacto conservando el área del historial; carga directa sin estado usa Inicio.
- `#catalogo`: catálogo del área actual; Inicio usa su índice.

## Revisar y ejecutar

Desde `C:\Users\USER\OJITOCORP`: `npm run dev` inicia normalmente http://localhost:4173. No necesita instalación de dependencias. Para usar la misma dirección de esta revisión: `$env:PORT = '4180'; npm run dev`.

La configuración `.openai/hosting.json` conserva la identidad existente. El usuario autorizó la publicación y la entrega 2.0.7 se desplegó el 13 de octubre de 2026 como versión 6 de Sites en el dominio principal. El servicio confirmó `succeeded`. La página pública muestra Inicio propio, las cinco categorías y el contacto actualizado; Tecnología y la consulta desde Computadoras PC funcionan. Registro completo en `docs/PUBLICACION.md` y captura `qa/ambientes/publicado-v6-inicio.png`.
