# Implementación y validación

## Alcance mínimo completo

Implementa la portada de Inicio, los cinco ambientes, la ola lateral, la navegación, el catálogo informativo, las fichas de detalle y el contacto común. Integra imágenes reales seleccionadas de fuentes verificables y contenido específico.

La implementación se considera completa cuando la experiencia puede recorrerse, consultar un elemento y llegar al formulario conservando su selección. Un render estático, una captura o un componente aislado no completa el encargo.

La versión es una landing de presentación. Checkout, pagos, login, inventario, CRM, base de datos, panel administrativo, WebGL y escenas 3D quedan fuera. No añadas estos componentes para justificar la variedad de categorías.

## Inspección inicial

1. Lee las instrucciones y el estado de Git. Conserva cambios ajenos.
2. Identifica el stack, las dependencias, los comandos existentes, los assets y el flujo de contacto.
3. Localiza el contenido y los datos confirmados de la empresa.
4. Comprueba si existen restricciones de hosting, rutas o pipeline.
5. Traza un plan breve de implementación con los archivos que realmente deban cambiar.

La revisión previa de esta conversación observó una landing con HTML, módulos JavaScript, `js/app.js`, `js/config.js` y varias hojas CSS. Es una referencia del sitio revisado, no una orden de imponer esos nombres si el repositorio de trabajo cambió.

Si sigue siendo un proyecto buildless, HTML/CSS/JavaScript pueden resolver este encargo. Si ya utiliza React u otro stack, reutilízalo. No migres de stack solo para ejecutar la ola.

## Organización técnica sugerida

Separar responsabilidades, adaptando nombres a la arquitectura real:

- Config comercial: categorías, grupos, elementos y datos de contacto.
- Assets: rutas, encuadres, alt y metadatos de las imágenes seleccionadas.
- Presentaciones por ambiente: cinco composiciones específicas.
- Controlador de navegación: estado activo, URL e historial.
- Controlador de transición: cobertura, cambio, revelado y cancelación.
- Componentes comunes: header, botones, detalle y contacto.
- Estilos comunes y estilos acotados por ambiente.

Ejemplo para un proyecto de módulos simples:

```text
js/
  config.js
  scenes.js
  navigation.js
  transition.js
  detail.js
  contact.js
css/
  base.css
  scenes.css
  motion.css
assets/
  images/
docs/
  ASSETS_UTILIZADOS.md
```

Es una propuesta de responsabilidades, no un requisito de crear todos esos archivos. Si la estructura existente ya resuelve una responsabilidad, reutilízala.

## Secuencia de ejecución

### 1. Contenido y assets

Mapea la oferta a cinco ambientes y prepara las fichas de datos. Selecciona imágenes pertinentes por categoría y registra sus fuentes. Los conceptos ambiguos o futuros no se convierten en oferta disponible.

### 2. Navegación funcional

Implementa selección de escenas, estado activo, deep links, alias antiguos, historial y contacto. Primero debe funcionar sin depender de la animación.

### 3. Diseño de los ambientes

Completa las cinco composiciones y su adaptación móvil. El contenido comercial y las imágenes deben estar integrados antes de considerarlas terminadas.

### 4. Ola y movimiento secundario

Añade una implementación única del barrido, con dirección, cancelación y movimiento reducido. Después incorpora efectos sutiles propios de cada ambiente.

### 5. Detalles y consulta

Completa la ficha reutilizable, el foco y la selección del elemento en el formulario. Conserva borradores de datos personales y mensaje.

### 6. Comprobación y corrección

Ejecuta las comprobaciones del proyecto y la matriz siguiente. Corrige defectos encontrados antes de ampliar el diseño con efectos opcionales.

## Matriz de aceptación

Codex debe registrar para cada fila «aprobado», «falló» o «no ejecutado», con evidencia breve. No marque como aprobado un resultado solo porque el código parece contemplarlo.

| ID | Comprobación | Resultado esperado |
|---|---|---|
| V01 | Abrir Inicio en desktop y móvil | Logo, explicación concreta, imagen protagonista y acceso a las áreas; sin texto cortado. |
| V02 | Entrar en las cinco categorías | Cada una muestra título, composición, paleta, imágenes y catálogo propios. |
| V03 | Comparar Tecnología y Alimentos | Distribución, fotografías y presentación del catálogo son materialmente diferentes. |
| V04 | Avanzar y retroceder entre categorías | Ola desde derecha al avanzar y desde izquierda al retroceder; no hay flash blanco ni footer que salte a la portada. |
| V05 | Seleccionar cinco categorías rápidamente | Solo un controlador/overlay; termina en la última selección y no vuelve a un destino antiguo. |
| V06 | Abrir cada elemento del catálogo principal | Imagen pertinente, texto propio, explicación y consulta; IDs sin duplicación ni contenido vacío. |
| V07 | Cerrar un detalle con botón y Escape | Cierre correcto, fondo habilitado y foco devuelto al disparador. |
| V08 | Consultar un elemento tras escribir un borrador | Formulario conserva los datos escritos y prepara la categoría y el elemento correctos. |
| V09 | Comprobar el mensaje y URL de WhatsApp | Mensaje codificado con datos y selección correctos; la comprobación no envía una consulta real. |
| V10 | Abrir cada hash directamente y recargar | Destino correcto sin paso forzado por Inicio; hash desconocido con fallback útil. |
| V11 | Recorrer Atrás/Adelante y contacto | Restaura categoría y estado coherentes sin crear un bucle de historial. |
| V12 | Abrir `#servicios`, `#productos` y otros alias | Enlaces anteriores resuelven según el mapa documentado. |
| V13 | Revisar 320, 390, 768, 1280 y 1440 px | Sin scroll horizontal involuntario, superposición de textos ni CTA fuera de alcance. |
| V14 | Recorrer con teclado | Navegación, detalles y formulario operables; foco visible y paneles ocultos fuera de tabulación. |
| V15 | Activar movimiento reducido | Funcionalidad completa con cambio instantáneo/opacidad breve; sin ola, zoom, parallax ni loops. |
| V16 | Simular una imagen fallida y red lenta | Fallback pertinente; contenido usable; ninguna espera indefinida ni overlay bloqueado. |
| V17 | Revisar imágenes y registro | Al menos tres imágenes distintas por ambiente, cobertura de familias y fuentes reales registradas. |
| V18 | Revisar redacción y oferta | Sin claims inventados, productos futuros como disponibles, notas internas públicas ni repetición mecánica de descripciones. |

## Calidad técnica y alcance de pruebas

- Ejecuta los comandos de comprobación/build realmente definidos en el proyecto; no inventes scripts.
- Comprueba consola y enlaces rotos cuando haya vista de navegador disponible.
- Si hay tests existentes, ejecuta los relevantes para los cambios.
- Una prueba pequeña para dirección, aliases, estado o cancelación puede ser útil. No añadas una suite extensa que repita literalmente el código ni tests de cada decisión cosmética.
- La comprobación visual debe usar los mecanismos admitidos por el entorno. Si no están disponibles, ejecuta las verificaciones posibles y explica cuáles quedaron pendientes.
- Verifica carga y dimensiones de imágenes; evita cargar el catálogo entero en su resolución máxima al inicio.
- Contraste orientativo: al menos 4.5:1 para texto normal y 3:1 para texto grande; comprueba los pares reales usados.
- Los botones táctiles deben ser cómodos, aproximadamente de 44 px de área cuando corresponda, sin encimar controles.
- No prometas puntuaciones de rendimiento ni resultados de accesibilidad sin medición.

## Qué debe entregar Codex

1. Implementación integrada en el proyecto existente.
2. Acceso a la vista local o vista de trabajo disponible y sus instrucciones de apertura.
3. Resumen de cómo cambian los cinco ambientes y qué se reorganizó.
4. Matriz de aceptación con estados reales y comprobaciones realizadas.
5. `docs/ASSETS_UTILIZADOS.md` con fuentes de las imágenes efectivamente usadas.
6. Limitaciones pendientes de contenido o del entorno, si existen.

La entrega de este encargo no publica la web en producción. Si el usuario lo pide después, conserva la identidad del sitio y su audiencia y utiliza el flujo de publicación de su entorno.

## Referencias de intención

- Cuberto: https://cuberto.com/ — navegación, continuidad entre páginas/áreas y presentación comercial.
- Lusion: https://lusion.co/ — protagonismo visual y composición de experiencias.
- Midwam: https://midwam.com/en — motivo visual común y presentación por narrativa.
- Chartogne-Taillet: https://chartogne-taillet.com/ — producto y ambiente cálido. Documentación del diseño: https://immersive-g.com/projects/chartogne-taillet-1

Las referencias son inspiración; no implican reproducir sus efectos exactos ni su complejidad técnica. Cuberto es la referencia prioritaria indicada por el usuario.
