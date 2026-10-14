# Diseño UI/UX vigente

Versión 2.0.7, 12 de octubre de 2026. Se aplicaron los métodos de las skills `website-ui-design` y `mobile-app-ui` solicitadas por el usuario: componentes compartidos, jerarquía, adaptación por tamaños, lectura y controles táctiles. La identidad existente y el contenido empresarial gobiernan el diseño.

## Alcance de las portadas

Inicio tiene una composición propia con fotografía de arco, recortes de equipos/café y titular con remate de menor escala. La composición de Alimentos se usa exclusivamente en las cinco categorías: texto editorial, fotografía hasta el borde y degradado. Los cinco ambientes mantienen su paleta y sus protagonistas fotográficos. No se reintroducen accesos adicionales de grupo en Tecnología o Negocios.

## Composición de las áreas

| Área | Catálogo en escritorio | Adaptación |
|---|---|---|
| Tecnología | Cuatro equipos; cinco filas TI con título/descripción juntos y acción a la derecha; conectividad conserva su ficha secundaria. | Dos equipos en tablet y uno en móvil. Servicios con miniatura lateral; en 320 px la foto ocupa la fila superior para evitar títulos estrechos. |
| Negocios | Tres asesorías de Gestión y dos propuestas de Educación, con imágenes y acciones alineadas. | Filas uniformes en tablet y tarjetas de una columna en móvil. |
| Digital | Marketing destacado y parejas de servicios en los dos grupos existentes. | Una columna en móvil, conservando el orden. |
| Formación | Tres propuestas comparables en una fila. | Filas en tablet y tarjetas de una columna en móvil. |
| Alimentos y bebidas | Tres productos por grupo, manteniendo la primera imagen de mayor escala. Marcos suaves y acciones al pie. | Primer producto ancho en tablet y una columna en móvil. |

Los bloques explicativos agrupan las dos fotografías secundarias junto a una columna de texto. En tablet y móvil una foto protagonista acompaña al texto. Se conserva la colección de 21 fotografías y su registro; la tarjeta de celulares encuadra el teléfono de la fotografía existente mediante CSS.

## Contacto y acciones

Contacto usa la superficie verde de marca, texto claro y un formulario crema. Los canales de comunicación se distinguen mediante marcos e iconos. «Hablemos» permanece accesible junto al logo y al menú móvil. La guía está a la izquierda del formulario en escritorio y debajo en una columna.

El acceso a contacto enfoca su título. Si el formulario no tiene un área seleccionada, se prepara el área activa; una selección previa se conserva. Consultar desde una ficha selecciona el elemento solicitado, desplaza al formulario y enfoca nombre. Los demás campos y el borrador se conservan. El formulario prepara enlaces de WhatsApp/correo para revisión y no envía automáticamente.

«Explorar» conserva etiqueta e icono SVG separados 8 px. Solo se subraya el texto. Las tarjetas tienen una zona de acción de al menos 48 px; los inputs mantienen texto de 16 px. El cierre y el acceso de header conservan 44 px. El menú devuelve el foco a su botón al cerrar con Escape. Las fichas mantienen el ciclo de foco y cierre nativo.

## Fuentes de verdad

Las rutas siguientes parten de `sites/ojitocorp/`.

- `dist/js/catalog.js`: oferta, temas, IDs, alcance y textos.
- `dist/js/scenes.js`: Inicio, portadas, bloques y catálogos.
- `dist/js/details.js`: ficha compartida.
- `dist/js/app.js`: navegación, foco, menú y coordinación con contacto.
- `dist/js/contact.js`: formulario, borrador, validación y preparación de enlaces.
- `dist/css/base.css`: marca, header, contacto, formulario y diálogos.
- `dist/css/scenes.css`: paletas y layouts por tamaño.
- `dist/css/motion.css`: ola, entradas, pausa y movimiento reducido; la pausa conserva los encuadres estáticos.

El contenedor máximo sigue en 1280 px y pasa a 1400 px en pantallas grandes. Los grupos conservan separadores de 2 px y espacio igual arriba/abajo (32 px o 24 px en móvil). `scrollbar-gutter: stable` reserva el ancho de la barra al abrir una ficha. La evidencia actual está en `VALIDACION_REDISENO.md` y `qa/ambientes/ui-*.json`.
