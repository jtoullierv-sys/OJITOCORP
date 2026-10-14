# Imágenes referenciales y recursos visuales

## Autorización y objetivo

El usuario autoriza buscar e incorporar imágenes referenciales de internet porque no dispone de fotografías propias. Codex debe seleccionarlas e integrarlas durante la implementación, sin pedir un banco de imágenes como requisito previo.

El objetivo es una web cálida y visualmente potente. Las imágenes deben mostrar productos, tareas o personas relacionados con la oferta, tener un encuadre útil y formar una serie coherente por ambiente.

## Fuentes preferentes

- Pexels: https://www.pexels.com/ y https://www.pexels.com/license/
- Colección gratuita de Unsplash: https://unsplash.com/ y https://unsplash.com/license
- Otros repositorios cuando la página concreta del asset permita comprobar las condiciones de uso, por ejemplo Wikimedia Commons.

Las licencias generales de Pexels y de la colección gratuita de Unsplash permiten diversos usos de sus recursos, con restricciones. Comprueba la página y las condiciones aplicables a cada imagen. No presupongas que un recurso de Unsplash+ o de otro proveedor comparte la licencia gratuita.

Si se usa una API, sus condiciones pueden definir cómo servir y atribuir imágenes; respétalas. Para descargas manuales permitidas, guarda archivos optimizados en el proyecto y evita enlaces temporales o dependencias de una imagen remota aleatoria.

No extraigas imágenes comerciales de Cuberto, Lusion u otra web de referencia para incorporarlas al sitio. Las referencias sirven para estudiar composición e interacción.

## Brief de búsqueda por ambiente

Las consultas son puntos de partida, no URLs de assets seleccionados. Codex debe abrir los resultados, escoger fotografías y registrar las fuentes reales.

| Ambiente | Imagen protagonista | Imágenes secundarias | Consultas sugeridas |
|---|---|---|---|
| Inicio | Trabajo humano con tecnología, o producto y espacio de trabajo | Equipo / producto como recorte subordinado | `creative workspace natural light`, `small business workspace` |
| Tecnología | Laptop o estación de trabajo con luz y detalle | Reparación de hardware; smartphone/periféricos | `laptop workspace dark`, `computer repair technician`, `smartphone keyboard desk` |
| Negocios | Mesa de trabajo con documentos y personas | Análisis de documentos; conversación de asesoría | `business planning natural light`, `accounting documents desk`, `small business consultation` |
| Digital | Producción de contenido o trabajo creativo | Cámara/edición; herramientas digitales | `content creation workspace`, `creative team design`, `video editing desk` |
| Alimentos y bebidas | Café o bodegón amplio de productos | Cacao/especias; fruta/snacks; vino/pisco referencial | `coffee beans warm light`, `cacao beans`, `turmeric still life`, `avocado banana`, `plantain chips`, `wine bottle neutral label` |
| Formación | Persona hablando o grupo en aprendizaje | Práctica de presentación; acompañamiento individual | `public speaking workshop`, `adult learning natural light`, `presentation practice` |

## Cantidad y cobertura

- Cada ambiente tiene al menos tres imágenes distintas: una protagonista y dos secundarias.
- Añade las imágenes necesarias para cubrir las familias del catálogo. No uses la misma foto de café para cacao, chifles y frutas.
- Una fotografía puede reutilizarse en la entrada de una familia y su ficha de detalle, evitando duplicaciones gratuitas de descarga.
- Las variantes de una misma familia no necesitan fichas y fotografías inventadas como si fueran SKUs confirmados.
- Usa como presupuesto inicial aproximado 18–26 fotografías optimizadas; es una guía de alcance, no una cifra obligatoria ni un límite que justifique contenido sin imagen.
- La portada puede reutilizar encuadres existentes para contener el peso total.

## Criterios de selección

1. Relación reconocible con el producto o actividad descritos.
2. Espacio y encuadre adecuados para el texto o la composición prevista.
3. Consistencia de temperatura de luz y tratamiento dentro de cada ambiente.
4. Buena resolución sin descargar originales enormes innecesariamente.
5. Fotos naturales, con pocas marcas visibles y sin imágenes de ejecutivos genéricos en todas las áreas.
6. Personas y contextos que no se presenten como empleados, clientes o instalaciones reales de OJITOCORP.
7. Productos sin etiquetas que aparenten una marca o inventario no confirmado.
8. Ninguna marca de agua ni recursos con licencia no comprobada.

Una foto de vino puede ilustrar la familia de vinos. No representa automáticamente una etiqueta vendida por la empresa. Una foto de taller ilustra soporte técnico; no acredita un taller propio.

## Tratamiento visual y movimiento

Aplica recortes deliberados y `object-position` por imagen, no un centro fijo para toda la serie. Usa un tratamiento suave de temperatura y contraste por ambiente. Conserva el color reconocible de los alimentos.

Las imágenes protagonistas pueden tener un cambio de encuadre pequeño al entrar. Los secundarios pueden entrar con 60–90 ms de separación. Hover de zoom como máximo aproximado de 1.03. Parallax solo si funciona bien, es discreto y se desactiva con movimiento reducido. Ningún producto esencial depende de hover para verse.

Un video es opcional y no forma parte del alcance mínimo. No añadas autoplay con sonido ni varios videos como fondos simultáneos.

## Rendimiento

- Genera WebP o AVIF cuando el pipeline existente lo permita; usa fallback adecuado.
- Prepara tamaños acordes a desktop y móvil con `srcset`/`sizes` cuando corresponda.
- Define ancho, alto o proporción para reservar el espacio.
- Prioriza la imagen principal visible; carga progresivamente secundarios y categorías no seleccionadas.
- No cargues todos los originales grandes de las cinco áreas al inicio.
- Objetivos orientativos: protagonista de 1600–2000 px y 150–350 KB, secundarios de 800–1200 px y 60–180 KB. Evalúa la calidad real; estas cifras no sustituyen una comprobación.
- Si una descarga está bloqueada, intenta otra fuente válida. Evita inventar URLs y deja un registro explícito de cualquier limitación de assets.

## Registro que debe completar Codex

Crea `docs/ASSETS_UTILIZADOS.md` en el proyecto de implementación. Incluye una fila por cada imagen seleccionada:

| Archivo local | Ambiente / elemento | Autor | Página de origen | Licencia aplicable | Fecha de revisión | Tratamiento | Alt / carácter referencial |
|---|---|---|---|---|---|---|---|

Este archivo se completa con recursos reales durante el desarrollo. No contiene fuentes ficticias ni atribuciones a fotógrafos no comprobados. Si una licencia exige atribución pública, inclúyela también en la interfaz o página de créditos correspondiente.

## Fuentes consultadas

- Licencia Pexels: https://www.pexels.com/license/
- Licencia de la colección gratuita de Unsplash: https://unsplash.com/license

Consultadas el 12 de octubre de 2026, UTC. Verifica las condiciones vigentes al seleccionar cada recurso.
