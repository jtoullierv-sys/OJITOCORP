# OJITOCORP: manual para encargar el rediseño a Codex

## Qué se quiere construir

Una landing corporativa cálida, visual y diversa, organizada en cinco ambientes. Al seleccionar una categoría, una ola lateral cubre el área de exploración y revela un diseño diferente: cambian la paleta, la composición, las imágenes, los textos y las animaciones secundarias. Cada producto o servicio se puede explorar con su propia información e imagen. El formulario y el footer son el cierre común.

Sitio de partida: https://ojitocorp-conecta.wavy-robin-3389.chatgpt.site/

Referencia de intención: https://cuberto.com/. Se toma la continuidad entre navegación, transición y presentación de contenido. Los diseños, imágenes, textos y código de esa referencia no se copian.

Este paquete contiene instrucciones para tu Codex. No contiene una modificación de la landing ni imágenes descargadas: la selección e incorporación de imágenes forma parte del encargo de implementación.

## Cómo entregarlo

1. Descomprime el ZIP.
2. Abre en Codex el repositorio o proyecto original de OJITOCORP. La URL publicada sirve como referencia, pero Codex necesita acceso al código para cambiarlo.
3. Copia `MACROPROMPT.md` y la carpeta `docs/` a la raíz de ese proyecto.
4. Incorpora `AGENTS.md` a la raíz. Si ya existe uno, conserva sus instrucciones y agrega el bloque de OJITOCORP; no lo reemplaces automáticamente.
5. Envía a Codex el contenido completo de `MACROPROMPT.md`. También puedes pedirle: «Lee MACROPROMPT.md, AGENTS.md y todos los documentos de docs indicados en el manual. Ejecuta el rediseño completo siguiendo esas especificaciones».
6. Comprueba su entrega con la matriz de aceptación de `docs/05_IMPLEMENTACION_VALIDACION.md`.

Si estás usando otro chat de Codex, adjunta el ZIP, identifica el proyecto que debe editar y envía el macroprompt. Si ese entorno no tiene acceso al repositorio, primero debe recibirlo o conectarlo; los archivos de instrucciones no sustituyen el código fuente.

## Para qué sirve cada archivo

| Archivo | Función |
|---|---|
| `MACROPROMPT.md` | Encargo completo listo para enviar a Codex. |
| `AGENTS.md` | Reglas persistentes para que el agente conserve la dirección durante el trabajo. |
| `docs/01_DISENO_AMBIENTES.md` | Identidad común y composición específica de los cinco ambientes. |
| `docs/02_CONTENIDO_CATALOGO.md` | Organización de la oferta, textos iniciales y campos de las fichas de detalle. |
| `docs/03_TRANSICIONES_NAVEGACION.md` | Ola, direcciones, clics rápidos, URL, scroll, móvil y detalle de productos. |
| `docs/04_IMAGENES_RECURSOS.md` | Criterios y búsquedas de imágenes referenciales, optimización y registro de fuentes. |
| `docs/05_IMPLEMENTACION_VALIDACION.md` | Secuencia de trabajo, alcance técnico y comprobaciones de entrega. |

## Orden de lectura para Codex

`AGENTS.md`, `MACROPROMPT.md`, diseño, catálogo, transiciones, imágenes y validación. Codex debe completar esa lectura antes de escoger la arquitectura o empezar a añadir efectos.

## Cómo debería sentirse el resultado

- La primera pantalla explica OJITOCORP y presenta una composición visual protagonista.
- La navegación permite entrar directamente a Tecnología, Negocios, Digital, Alimentos y bebidas, o Formación.
- El cambio de categoría se percibe como entrar en otra área de la empresa.
- Cada área tiene un diseño reconocible incluso sin leer su título.
- Se pueden ver imágenes, entender la oferta y abrir detalles concretos.
- El visitante puede llegar al contacto en cualquier momento y consultar por el elemento elegido.
- El movimiento es breve y sutil fuera de la transición principal.

## Libertad creativa autorizada

Codex puede buscar e incorporar imágenes de internet con condiciones de uso adecuadas; escoger encuadres, colores, tratamientos y pequeños efectos; reorganizar bloques; y mejorar la redacción comercial. Puede resolver esas decisiones sin solicitar aprobación para cada detalle.

Los nombres de productos, las capacidades de la empresa, los datos de contacto, los precios, el stock, las certificaciones y los resultados deben proceder de información confirmada. La libertad visual no autoriza inventar información comercial.

## Alcance controlado

El encargo incluye presentación, navegación por ambientes, catálogo informativo, detalle y contacto. Carrito, pagos, cuentas, base de datos, panel de administración, simulaciones 3D y experiencias WebGL quedan fuera de esta versión. Se reutiliza el proyecto y su stack.

La salida por defecto de este macroprompt es una implementación local revisable o la vista de trabajo ya disponible. Si quieres publicación en producción, añádelo expresamente al encargo de tu Codex. Esto evita que preparar y probar el rediseño modifique por sí solo la web pública.

## Qué revisar en la entrega

La pregunta principal es: «¿Cambian realmente la composición y el contenido al seleccionar otra categoría?». Un cambio de color sobre las mismas tarjetas no cumple el encargo. Comprueba también las imágenes, las fichas de detalle, los clics rápidos, el móvil, el botón Atrás y la consulta por WhatsApp.

Fecha de preparación: 12 de octubre de 2026, UTC / 11 de octubre de 2026, Perú.
