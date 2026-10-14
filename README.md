# Ojitocorp — carpeta principal

El trabajo actual es el rediseño por cinco ambientes (versión 2.0.7), publicado en https://ojitocorp-conecta.wavy-robin-3389.chatgpt.site/. La publicación vigente es la versión 8 de Sites, del 13 de octubre de 2026, con `atencionalcliente@ojitocorp.com.pe` en Conversa y el logo sin marca sobre la primera O. Inicio recupera su composición propia y la portada basada en Alimentos queda limitada a las cinco categorías. Los catálogos tienen distribuciones y acciones más claras; el contacto destaca en verde, con formulario claro y acceso Hablemos permanente en el header. La revisión incluye móvil, tablet y 2K, teclado y la consulta desde las 32 fichas. Consulta `docs/DISENO_UI_UX.md`, `docs/VALIDACION_REDISENO.md` y `docs/PUBLICACION.md`. Las versiones 4 y 5 descritas abajo son el historial previo.

Desde el 10 de octubre de 2026, el proyecto se trabaja en `C:\Users\USER\OJITOCORP`. La carpeta `C:\OJITOCORP` se conserva como respaldo de la versión anterior.

La web y su historial Git están en `sites/ojitocorp`. Se conserva el Site `appgprj_6ac7f30f47888191b0e77378f8d16d43` y el alojamiento existente:

https://ojitocorp-conecta.wavy-robin-3389.chatgpt.site

La versión 4 se publicó correctamente el 10 de octubre de 2026 desde esta carpeta. El paquete de despliegue correspondiente es `ojitocorp-deploy-v4.tar.gz`; el código sincronizado corresponde al commit `acf6ba7b94a83c37c24c8b0548656a00a7b6dbeb`.

La versión 5 incorpora la corrección del logo responsive y ajustes moderados para pantallas 2K. Su paquete es `ojitocorp-deploy-v5.tar.gz` y corresponde al commit `2a41397d7df83ca9835b73cb7f1494adf9905ef8`. Las capturas de revisión están en `qa/`.

Para trabajar desde esta carpeta:

```powershell
cd C:\Users\USER\OJITOCORP
npm run dev
```

`npm run check` verifica el proyecto y `npm run build` prepara la misma entrega estática. No se necesita instalar dependencias. El servidor local muestra su dirección al iniciar.

Los archivos editables están en `sites/ojitocorp/dist/`. La configuración de alojamiento está en `sites/ojitocorp/.openai/hosting.json`; su identidad corresponde al Site existente y se conserva en las próximas actualizaciones.

Los ZIP, TAR y capturas copiados de la carpeta anterior son entregas históricas. La fuente vigente es `sites/ojitocorp/`, con su guía de arquitectura y documentación propias.

La versión 6 publicó el rediseño, con código sincronizado en el commit `d0986f590d35ab62602c701addd8d442d55ee9c5` y paquete `ojitocorp-deploy-v6.tar.gz`. La versión 7 actualiza el logo: commit `abe9ba74f4a54b37e8c4cffdd138a89cbc09c8af` y paquete `ojitocorp-deploy-v7.tar.gz`. Se mantiene el dominio original y su audiencia pública.

La versión 8 actualiza el correo de Conversa: commit `c5a31fe456361d4f3864f33343be747946d0b826` y paquete `ojitocorp-deploy-v8.tar.gz`.
