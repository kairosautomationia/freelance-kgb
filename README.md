# KGB Security Services & Solutions

Landing page institucional de KGB Security Services & Solutions, construida con Astro y preparada para despliegue estático.

## Desarrollo local

```bash
npm install
npm run dev
```

## Producción

```bash
npm run build
```

El resultado se genera en `dist/`.

## Cloudflare Pages

Configuración para conectar este repositorio:

- Rama de producción: `main`
- Comando de build: `npm run build`
- Directorio de salida: `dist`
- Directorio raíz: `/`

Cloudflare Pages puede construir el sitio directamente desde este repositorio. No requiere Railway ni un servidor persistente.
