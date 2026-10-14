# Publicación en el dominio existente

Dominio principal que se conserva: https://ojitocorp-conecta.wavy-robin-3389.chatgpt.site/

Identidad de Sites: `appgprj_6ac7f30f47888191b0e77378f8d16d43`, declarada en `sites/ojitocorp/.openai/hosting.json`. Entrega estática: `dist`. Las actualizaciones deben usar este mismo Site y conservar su audiencia; no crear otro dominio.

## Publicación vigente: correo de Conversa — versión 8

Publicada el 13 de octubre de 2026 a las 19:14, hora de Lima. El servicio devolvió `succeeded` y el mismo dominio, conservando la audiencia pública.

- Commit: `c5a31fe456361d4f3864f33343be747946d0b826`.
- Versión guardada: `appgprj_6ac7f30f47888191b0e77378f8d16d43~appgver_17a3e2a9ecb48191985bc7c25560ea3b`.
- Despliegue: `appgdep_6acec959d5848191b8ef27e224a98571`.
- Paquete: `ojitocorp-deploy-v8.tar.gz`; SHA-256 `c341e89567c81fec20f443fdbfab7f4ed6f9042a90adde1e02b75ec0d221ab84`.

Conversa utiliza el correo de atención al cliente confirmado por el usuario: `atencionalcliente@ojitocorp.com.pe`. El valor está centralizado en `company.customerServiceEmail`; el enlace del footer muestra esa dirección y usa `mailto:atencionalcliente@ojitocorp.com.pe`. La modificación se limita al correo de Conversa solicitado.

`npm run build` pasó. Se verificaron el texto y el destino del enlace en la web pública, sin desbordamiento horizontal ni errores de consola observados. Evidencia: `qa/ambientes/correo-conversa-verificacion.json` y `correo-conversa-publicado.png`. No se envió correo ni se abrió el cliente de correo.

## Logo sin acento — versión 7

Publicada el 13 de octubre de 2026 a las 19:05, hora de Lima. El servicio devolvió `succeeded` y el mismo dominio, conservando su audiencia pública.

- Commit: `abe9ba74f4a54b37e8c4cffdd138a89cbc09c8af`.
- Versión guardada: `appgprj_6ac7f30f47888191b0e77378f8d16d43~appgver_1bc773e8d4588191bfba51d66c3e5742`.
- Despliegue: `appgdep_6acec730ed4481919da2f4dfaedc4d2c`.
- Paquete: `ojitocorp-deploy-v7.tar.gz`; SHA-256 `2a23831c63176585197e278e27e15a3422de95e3288b5fb2f79a7a3d4ba58109`.

El logo activo es `dist/assets/logo-sin-acento.svg`. Su máscara SVG excluye la marca aislada sobre la primera O, conservando la forma del resto de las letras y la transparencia. Header y footer usan el nuevo nombre de archivo para evitar reutilizar la versión anterior desde caché. Los originales quedan como referencia.

`npm run build` pasó. En la web pública ambos logos cargan, con 5100 px de ancho intrínseco y las mismas dimensiones de presentación (94.52 × 48 px en la vista revisada), sin desbordamiento horizontal. Se inspeccionaron visualmente header y footer y se dejó la página en Inicio. Capturas `qa/ambientes/logo-sin-acento-header.png` y `logo-sin-acento-footer.png`. El navegador bloqueó el acceso automatizado a la vista local; la comprobación visual se realizó sobre el dominio HTTPS publicado. No se repitió la matriz completa del rediseño para este cambio de asset.

## Publicación confirmada — 13 de octubre de 2026

La conexión se recuperó y el rediseño 2.0.7 está publicado como versión 6 de Sites. El despliegue devolvió `succeeded` y la URL principal exacta, con la audiencia pública existente.

- Commit sincronizado: `d0986f590d35ab62602c701addd8d442d55ee9c5`.
- Versión guardada: `appgprj_6ac7f30f47888191b0e77378f8d16d43~appgver_34616ef2f1ac819186861671e68ebef2`.
- Despliegue: `appgdep_6acec1f5275c8191ad644f6a55b60db6`.
- Paquete: `ojitocorp-deploy-v6.tar.gz`; SHA-256 `d5ee47d0fbb93d17ecfd9534eab5535c0347a024bd32ecc8ce4e140e285ac83c`.
- Confirmación del servicio: 18:43 del 13 de octubre, hora de Lima.

La página pública muestra Inicio con `home-intro`, las cinco categorías y el contacto «Conversemos. Tu consulta empieza aquí.». Se abrió Tecnología y la ficha Computadoras PC; Consultar selecciona `tecnologia` + `tec-pc`, cierra el diálogo y enfoca Nombre. No se enviaron consultas. Sin desbordamiento horizontal en la vista comprobada. Evidencia: `qa/ambientes/publicado-v6-inicio.png`.

El helper oficial abrió la fuente, sincronizó el commit y generó el paquete de la misma fuente. En Windows se añadió temporalmente Git Bash al PATH del proceso y `TAR_OPTIONS=--force-local` para interpretar correctamente la ruta de la unidad C. Las credenciales temporales se pasaron por stdin y no se guardaron en archivos.

## Historial de los intentos anteriores

El usuario autorizó publicar la versión local 2.0.7 en esta dirección. `npm run build` pasa: cinco ambientes + Inicio, 32 fichas, 21 fotografías, recursos y sintaxis comprobados.

La publicación quedó pendiente por un fallo de conexión del conector Sites con su servicio. Tres consultas `get_site` y la solicitud de credencial de escritura devolvieron un error de transporte. No se obtuvo credencial, no se sincronizó código ni se guardó o desplegó una versión nueva. No se cambió la identidad ni el acceso del sitio.

La página pública se recargó en el navegador: todavía muestra la navegación anterior («Nosotros», «Soluciones», «Nuestra visión», «En acción», «Contacto») y el contacto «Tu idea merece un siguiente paso.»; no muestra el rediseño 2.0.7.

Para completar, recuperar la conexión de Sites, consultar este mismo identificador y su audiencia, abrir/sincronizar la fuente mediante `site-workflow.mjs`, empaquetar el estado sincronizado y publicar la versión guardada. Confirmar que la URL devuelta coincide con el dominio principal y comprobar el rediseño publicado. La autorización del usuario para este despliegue ya existe.

### Reintento autorizado

El usuario reiteró que se debe publicar el proyecto actualizado en el dominio entregado. Se repitieron la consulta del Site y la solicitud de credencial: ambas fallaron antes de ejecutar la operación, con el mismo error de transporte. La consulta de dependencias de Plugin Management también devolvió ese error; esto apunta al canal compartido de conexión de Codex, no a la configuración del proyecto. Una comprobación HTTPS anónima fuera de la red restringida sí llegó a `chatgpt.com` (respuesta 403 con desafío de Cloudflare); no demuestra que el canal autenticado de Sites funcione. No se usaron credenciales ni se intentó eludir la autenticación.

En ese reintento la publicación continuó pendiente. La conexión se recuperó en el intento posterior, registrado arriba como publicación confirmada.
