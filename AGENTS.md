# Instrucciones de proyecto: OJITOCORP

Este bloque gobierna el rediseño de la landing por ambientes. Al incorporarlo a un repositorio con instrucciones previas, combina ambos documentos y conserva las reglas existentes. Las instrucciones directas del usuario tienen prioridad.

## Lectura obligatoria

Antes de implementar, lee `MACROPROMPT.md` y los documentos `docs/01_DISENO_AMBIENTES.md`, `docs/02_CONTENIDO_CATALOGO.md`, `docs/03_TRANSICIONES_NAVEGACION.md`, `docs/04_IMAGENES_RECURSOS.md` y `docs/05_IMPLEMENTACION_VALIDACION.md`.

Los documentos tienen funciones complementarias: diseño, oferta, interacción, imágenes y aceptación. Resuelve contradicciones concretas con el objetivo del macroprompt y documenta las decisiones que afecten al resultado.

## Reglas del resultado

1. Cinco ambientes: Tecnología, Negocios, Digital, Alimentos y bebidas y Formación.
2. Cada ambiente tiene composición, imágenes, contenido y tratamiento visual propios.
3. El cambio se realiza con una ola lateral breve, en la dirección del desplazamiento entre categorías.
4. La navegación, el logo, el formulario y el footer conectan la experiencia.
5. Los detalles de productos y servicios deben ser específicos y accesibles.
6. Las fotografías referenciales de internet están autorizadas. Registra fuentes y condiciones de uso.
7. Los nombres, datos de contacto, oferta y disponibilidad se sustentan en información confirmada. No inventes hechos comerciales.
8. Se mantiene el scroll vertical normal, el historial y el funcionamiento en móvil.
9. Se respetan teclado, foco, contraste y `prefers-reduced-motion`.
10. La selección final del visitante siempre debe prevalecer, incluso con clics rápidos.

## Reglas de implementación

- Inspecciona el stack y reutiliza la arquitectura adecuada antes de añadir dependencias.
- Mantén los datos comerciales separados del marcado y de la lógica de transición.
- Evita repetir cinco páginas completas si pueden compartir piezas: header, botones, ficha de detalle y contacto.
- La reutilización de componentes no debe uniformar las cinco composiciones.
- Usa una sola implementación de transición y un solo controlador del estado activo.
- Aísla los estilos de cada ambiente y conserva los estilos comunes de marca.
- No agregues capas sucesivas de overrides para ocultar problemas de CSS; consolida las reglas que modifiques.
- No agregues ecommerce transaccional, autenticación, backend, base de datos, 3D ni un nuevo framework por iniciativa propia.
- No cambies los datos de contacto ni envíes formularios de prueba a la empresa.
- Conserva el proyecto, su identidad de hosting y los cambios ajenos.
- Prepara una vista local revisable. Publicación en producción solo si el encargo del usuario la incluye expresamente.

## Cómo trabajar

Haz una inspección breve, define la estructura y ejecuta una implementación completa. Resuelve encuadres, colores, composición, redacción y animaciones rutinarias con criterio propio. No pidas aprobación por cada recurso o decisión reversible. Mantén actualizaciones breves sobre avances y hallazgos.

Lee las instrucciones de tu entorno antes de ejecutar herramientas de vista previa o publicación. Usa sus mecanismos admitidos; si no hay acceso a una comprobación visual, registra la limitación.

## Antes de entregar

Completa la matriz de aceptación y reporta el estado real de cada comprobación. Entrega el código, la vista disponible, el resumen de cambios y el registro de assets. No presentes una maqueta parcial ni un plan como una implementación terminada.
