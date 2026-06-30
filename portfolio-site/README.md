# Vinula Kasthuriarachchi Portfolio

Static cybersecurity portfolio built with Astro.

## Overview

This site presents cybersecurity experience, resume details, contact information, and selected project case studies covering infrastructure security, governance, identity and access management, network segmentation, and cyber risk.

## Requirements

- Node.js 22.12 or later
- npm

## Local Development

```sh
npm install
npm run dev
```

The development server starts at:

```text
http://localhost:4321
```

## Production Build

```sh
npm run build
```

Astro writes the static output to:

```text
dist/
```

## Preview Production Build

```sh
npm run preview
```

## Deployment Notes

This project can be deployed to static hosting providers such as Netlify, Vercel, Cloudflare Pages, or GitHub Pages.

Recommended build settings:

- Build command: `npm run build`
- Publish directory: `dist`
- Node version: `22.12.0` or later

## Repository Hygiene

The `.gitignore` excludes generated build output, Astro cache files, dependencies, logs, environment files, and local IDE/system files.

Do not commit:

- `node_modules/`
- `dist/`
- `.astro/`
- `.env`
- `.env.production`
