# Interacción: ola lateral y navegación por ambientes

## Objetivo

El visitante selecciona un área y percibe un cambio completo del contexto visual. La ola es un barrido lateral con un borde curvo amplio; no tiene que representar una ola de mar. Debe cubrir el cambio de contenido y revelar la nueva escena de manera continua.

## Estados y dirección

Orden estable: `inicio`, `tecnologia`, `negocios`, `digital`, `alimentos`, `formacion`.

| Selección | Dirección visual |
|---|---|
| Índice destino mayor que el actual | La ola entra desde la derecha y avanza hacia la izquierda. |
| Índice destino menor que el actual | La ola entra desde la izquierda y avanza hacia la derecha. |
| Misma categoría | Conserva el ambiente; si el visitante está abajo, regresa a su introducción. No repite la ola. |
| Carga directa por URL | Muestra directamente el destino. No obliga a pasar por Inicio. |
| Atrás/Adelante | Restaura el destino del historial; puede usar la dirección correspondiente, excepto con movimiento reducido. |

Categorías no adyacentes usan la misma duración y muestran solo el destino elegido. No se reproducen escenas intermedias.

## Secuencia recomendada

Duración total orientativa en desktop: 550–650 ms. En móvil: 350–450 ms. Estos tiempos se superponen con pequeñas entradas de contenido; no se suman hasta producir una espera larga.

1. **Preparación:** identifica el destino; cierra cualquier detalle abierto; prepara los datos y las imágenes de entrada. Si la categoría se elige desde una zona inferior, coloca la introducción de la escena bajo el header antes del cambio.
2. **Cobertura, aproximadamente 0–180 ms:** entra una superficie opaca del ambiente de destino con un borde curvo. El contenido saliente puede desplazarse unos pocos píxeles para acompañarla.
3. **Cambio, aproximadamente 180–300 ms:** bajo la cobertura intercambia la escena y sus tokens visuales. Ajusta altura y fondo del contenedor sin mostrar un flash de una página vacía.
4. **Revelado, aproximadamente 300–600 ms:** la ola continúa y sale por el lado opuesto. La nueva imagen y el texto llegan coordinadamente a su posición final.
5. **Estabilización:** elimina el overlay, limpia estilos temporales y deja la escena en estado navegable.

La transición puede realizarse con transformaciones de CSS y una silueta curva de CSS/SVG, o con la librería de animación ya presente. Evita dependencias o motores gráficos para conseguir este barrido.

## Zona que cambia

El contenedor de escena comprende portada/introducción, catálogo y bloques propios de la categoría. El formulario y el footer permanecen en el flujo común del documento y no se transforman con la ola.

La ola se recorta dentro de la escena y cubre de borde a borde la zona visible. No debe bloquear el header ni capturar clics. Usa una capa decorativa no enfocada y sin eventos de puntero. En una escena larga, resuelve la transición desde su inicio; no animes la altura de miles de píxeles del documento.

Mantén la escena anterior visible hasta que exista contenido de destino. El cambio de altura puede ocurrir bajo la cobertura; comprueba que no aparezca el footer en mitad de una transición iniciada en la portada.

## Clics rápidos: prevalece el último destino

Mantén un único controlador con, al menos, estado activo, destino solicitado, fase y un identificador de transición. No deben coexistir varias animaciones independientes intentando escribir el ambiente activo.

- Si se solicita un destino nuevo durante el movimiento, cancela o termina de forma controlada la transición anterior y dirige la experiencia al último destino.
- Al cancelar, limpia overlays, transforms, clases, temporizadores y estados de interacción.
- Un callback de una transición antigua no puede restaurar su escena ni actualizar la URL después de otra selección.
- Comprueba el identificador antes de aplicar resultados asíncronos, incluyendo imágenes.
- No pongas en cola todos los clics. Después de una ráfaga, el destino final debe aparecer en un tiempo razonable, aproximadamente menos de 900 ms desde la última selección cuando sus recursos ya están disponibles.
- No desactives toda la navegación durante varios segundos.

Ejemplo de intención, independiente del framework:

```text
solicitarAmbiente(destino):
  validar destino y registrar última intención
  invalidar callbacks anteriores
  cerrar detalle si está abierto
  resolver recursos disponibles y fallback
  ejecutar cobertura -> cambio -> revelado
  confirmar estado solo si sigue siendo la última intención
  limpiar efectos temporales
```

No es obligatorio usar esta forma literal; sí resolver la condición de carrera.

## URL e historial

URLs canónicas: `#inicio`, `#tecnologia`, `#negocios`, `#digital`, `#alimentos` y `#formacion`. `#contacto` lleva al cierre común conservando la categoría seleccionada.

- Los enlaces del menú deben tener `href` reales, incluso cuando el controlador intercepte el clic.
- Un clic deliberado a otra categoría crea una entrada de historial. Elige una sola vía para actualizarla; no combines asignación de hash y `pushState` para el mismo clic.
- Atrás/Adelante no generan una nueva entrada al restaurar la escena.
- Registra en el estado de navegación la categoría cuando se accede a contacto o detalle.
- Un hash desconocido resuelve a Inicio sin dejar el sitio vacío.
- Para cargar con `#contacto`, usa la categoría del estado si existe; de lo contrario, Inicio. El formulario ofrece su selector normal.
- Mantén compatibilidad con enlaces antiguos: `#servicios` y `#soluciones` abren el índice de áreas de Inicio; `#productos` abre Alimentos y bebidas; `#equipamiento` abre Tecnología; `#consultoria` abre Negocios; `#desarrollo` abre Formación. Lee el marcado actual para mantener también los anchors comunes que sigan teniendo contenido.

Si la escena cambia dinámicamente, proporciona una alternativa de contenido o un índice útil cuando JavaScript no esté disponible. No conviertas el código desactivado en una página con solo decoraciones.

## Scroll y foco

- Conserva el scroll vertical nativo. No conviertas la rueda en un selector de categorías.
- Al elegir una categoría desde el header, lleva su introducción al inicio visible considerando el header fijo. Usa scroll instantáneo cuando sea necesario coordinarlo con la ola.
- Al volver con Atrás/Adelante, restaura la posición registrada cuando sea fiable. Si hay una limitación de layout, vuelve de forma consistente a la introducción y documenta esa decisión.
- Mantén el foco en el enlace del menú cuando el cambio surge de ese enlace. Anuncia una vez el nuevo ambiente con `aria-live="polite"`.
- Si el elemento enfocado desaparece por el cambio de escena, traslada el foco a un destino lógico visible.
- Los paneles inactivos o salientes no deben permanecer en el orden de tabulación; usa montaje condicional o `hidden`/`inert` correctamente.

## Detalle de productos y servicios

Usa un solo componente reutilizable. En desktop puede ser un panel/modal amplio con imagen y texto; en móvil una ficha en una columna con desplazamiento vertical. Cada instancia tiene contenido específico de su elemento.

Contenido: título, imagen, descripción, qué contempla, para quién, variantes respaldadas y botón «Consultar por [nombre]». Para una familia sin SKUs confirmados, explica las opciones conocidas y permite consultar; no inventes modelos.

- Botón de cierre visible y accesible.
- Escape cierra el detalle.
- Al abrir, foco inicial lógico; el fondo queda inactivo.
- El foco se mantiene dentro de un modal abierto y vuelve a su disparador al cerrar.
- El panel respeta su alto disponible, permite leer el final y no oculta el CTA.
- Cierra el detalle antes de cambiar de categoría.
- Si implementas URL de detalle, valida el ID, conserva la categoría y haz que Atrás cierre o restaure coherentemente. No es requisito añadir un router.

## Consulta y formulario

Conserva en estado la categoría y el ID del producto/servicio consultado. El botón de una ficha abre el formulario con ambos datos preparados y el detalle cerrado. No sobrescribas nombre, correo, teléfono ni el mensaje libre que el visitante ya haya escrito.

Si cambia la categoría seleccionada en el formulario, limpia el elemento incompatible y explica el cambio con una etiqueta breve. La validación debe señalar el campo que falta sin borrar otros valores.

El flujo existente continúa hacia WhatsApp y permite al usuario revisar y enviar su mensaje. Mantén ese funcionamiento mientras no se solicite otro canal. Codex puede comprobar la URL y el texto generado sin enviar una consulta real.

## Móvil

El menú compacto contiene las mismas áreas con nombres legibles. Al seleccionar, se cierra y se muestra el nuevo ambiente. La ola conserva su sentido y usa una versión más corta; el layout se apila.

No exijas gestos para descubrir categorías. El swipe horizontal es opcional y no necesario en esta versión. Las acciones deben funcionar con toque y sin hover.

## Movimiento reducido y fallos

Con `prefers-reduced-motion: reduce`, sustituye la ola y los desplazamientos por un cambio instantáneo o una opacidad breve de hasta 120 ms. Desactiva parallax, zoom y loops. Respeta cambios de esa preferencia durante la sesión.

Si una imagen no carga, usa un fallback de la misma categoría y mantén el texto y la navegación. No esperes indefinidamente para mostrar una escena. No dejes overlays si una animación falla o se interrumpe al ocultar la pestaña.

## Fuentes técnicas

- Movimiento reducido: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
- Modal y gestión de foco: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

Fuentes consultadas el 12 de octubre de 2026, UTC. Verifica su contenido si el entorno o la implementación elegida requiere detalles adicionales.
