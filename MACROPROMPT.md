# Macroprompt: rediseño de OJITOCORP por ambientes

Actúa como diseñador de interfaces, desarrollador frontend y responsable de la experiencia de usuario. Trabaja sobre el proyecto existente de OJITOCORP y lleva el rediseño hasta una implementación funcional y comprobable.

## Contexto y objetivo

La landing actual es https://ojitocorp-conecta.wavy-robin-3389.chatgpt.site/. La empresa reúne tecnología, asesoría, servicios digitales, alimentos y bebidas, y formación. Quiero que esa diversidad se perciba mediante ambientes visuales propios.

Quiero una entrada imponente y una navegación superior por categorías. Cuando selecciono una categoría, una ola lateral entra desde la derecha o la izquierda y da paso a una nueva composición. Cambian el fondo, los colores, las imágenes, la distribución del contenido, las descripciones y las animaciones secundarias. Quiero una web cálida, diversa, entretenida y cuidada, con abundante contenido visual pertinente.

Toma https://cuberto.com/ como referencia de intención para las transiciones y el cambio de contexto al navegar. El diseño de OJITOCORP debe ser original y tener un alcance razonable.

## Lee primero los archivos

Lee `AGENTS.md` y estos documentos completos:

1. `docs/01_DISENO_AMBIENTES.md`
2. `docs/02_CONTENIDO_CATALOGO.md`
3. `docs/03_TRANSICIONES_NAVEGACION.md`
4. `docs/04_IMAGENES_RECURSOS.md`
5. `docs/05_IMPLEMENTACION_VALIDACION.md`

Inspecciona después el código, los assets, los comandos y las instrucciones del repositorio. Reutiliza el stack, la identidad y las integraciones existentes. Si el código no está accesible, identifica esa dependencia concreta; la URL pública no permite reconstruir con certeza todo el proyecto.

## Experiencia obligatoria

- Primera pantalla con una composición protagonista, una explicación concreta de la empresa y acceso a sus áreas.
- Navegación con Inicio, Tecnología, Negocios, Digital, Alimentos y bebidas, Formación y Contacto. El logo puede funcionar como Inicio.
- Un ambiente activo a la vez. Cada categoría debe cambiar materialmente la composición, además de sus colores y textos.
- Transición de ola lateral breve y coordinada. Al avanzar en el orden de categorías entra desde la derecha; al retroceder, desde la izquierda.
- Desplazamiento vertical normal dentro de cada ambiente y hacia el contacto.
- Varias imágenes pertinentes por ambiente: una principal y al menos dos secundarias distintas, con mayor cobertura cuando lo requiera el catálogo.
- Catálogo con nombres, imágenes, descripciones concretas y acceso a una ficha para cada familia de productos o servicios.
- Una ficha reutilizable con contenido específico: qué es, qué contempla, para quién resulta útil, variantes conocidas cuando existan y botón de consulta.
- Formulario y footer comunes. Consultar desde una ficha conserva la categoría y el elemento elegidos al llegar al formulario.
- Enlaces directos por categoría, navegación Atrás/Adelante y adaptación móvil.
- Interacción usable con teclado y con movimiento reducido.

## Dirección visual

Construye cinco composiciones propias: Tecnología con equipos y estructura precisa; Negocios con tratamiento editorial; Digital con muestras visuales y ritmo; Alimentos y bebidas con fotografía cálida y productos; Formación con personas y situaciones de aprendizaje.

Usa la marca para conectar las áreas mediante el logo, la tipografía principal, la navegación y una familia de botones. Las categorías pueden cambiar superficies, acentos, encuadres, alineaciones y recursos de composición.

Puedes usar fotografías referenciales de internet. Selecciónalas por pertinencia y calidad; verifica sus condiciones de uso, guárdalas de forma estable y registra su fuente. No hay un banco fotográfico propio disponible y no debes detener el trabajo por ello. No compres recursos ni requieras servicios de pago para esta versión.

Da a las imágenes espacio real en el diseño. Aplica movimiento sutil cuando aporte: pequeños desplazamientos, una entrada coordinada o un cambio de encuadre. Evita animar continuamente todo el contenido.

## Redacción y precisión

Reescribe las frases abstractas y repetitivas para que el visitante entienda qué puede consultar. Usa nombres concretos como soporte TI, laptops, desarrollo web, pedidos mayoristas, contabilidad, café o liderazgo.

Parte de la ficha empresarial resumida en el catálogo. Revisa el contenido actual y conserva únicamente lo respaldado. Los productos se ofrecen como familias consultables: no inventes SKU, precios, cantidades, plazos, marcas, stock ni fotografías de supuestos productos propios. Los conceptos ambiguos se mantienen como información pendiente interna o consulta secundaria; no los transformes en un servicio específico sin respaldo.

## Alcance y trabajo

Implementa en el proyecto existente. No añadas carrito, pagos, login, base de datos, panel de administración, WebGL ni un framework nuevo para resolver esta landing. Usa la herramienta de animación ya disponible o CSS/JavaScript cuando sean suficientes.

Resuelve autónomamente las decisiones visuales y técnicas rutinarias. Ejecuta el trabajo; un plan, un wireframe o una explicación no completan este encargo. Mantén el funcionamiento de contacto y los datos confirmados. Conserva los cambios ajenos ya presentes en el repositorio.

La salida solicitada es una versión local revisable o la vista de trabajo del proyecto. Este encargo no solicita publicación en producción. Si recibes una instrucción posterior explícita de publicar, utiliza el flujo del entorno y conserva la identidad y audiencia del sitio.

## Comprobación y entrega

Verifica los cinco ambientes, las imágenes, la transición en ambos sentidos, las selecciones rápidas, los detalles, el contacto, los enlaces directos, Atrás/Adelante y los anchos de 320, 390, 768, 1280 y 1440 px.

Usa la matriz de `docs/05_IMPLEMENTACION_VALIDACION.md`. Añade pruebas automatizadas solo para lógica que lo justifique; comprueba las decisiones visuales mediante una vista real cuando el entorno lo permita. Si una comprobación no se puede ejecutar, indica ese límite y no la marques como aprobada.

Entrega la implementación, un resumen breve de cambios, los comandos o comprobaciones realizados, el acceso a la vista revisable y el registro de las imágenes usadas. La experiencia debe quedar completa y lista para evaluar.
