# My Framework Docs (Nuxt 3 + Tailwind CSS)

This project is a documentation-style site built with **Nuxt 3** and **Tailwind CSS**.  
Some directories such as `pages`, `layouts`, and `components` are placed inside the `app/` folder — this is fully supported in Nuxt 3 and helps keep your project organized.

---

## 🧩 Project structure

```
my-framework-docs/
│
├── app/
│   ├── pages/          # Application pages (e.g. index.vue, about.vue, etc.)
│   ├── layouts/        # Layouts wrapping pages (default.vue, etc.)
│   ├── components/     # Reusable Vue components
│   └── app.vue         # Root component
│
├── assets/
│   └── css/            # Custom styles (tailwind.css, prism.css)
│
├── public/             # Static assets
├── tailwind.config.js  # Tailwind configuration
├── nuxt.config.ts      # Nuxt configuration (includes @nuxtjs/tailwindcss module)
└── package.json
```

---

## ⚙️ Setup

Install project dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

---

## 🚀 Development server

Start the local dev server at `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

---

## 🏗️ Production

Build the project for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Preview the production build locally:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

---

## 📘 Notes

- Tailwind CSS is automatically loaded via the `@nuxtjs/tailwindcss` module.  
- Page, layout, and component files must be placed inside the `app/` directory (not the root).  
- If you see Tailwind warnings like  
  _“No utility classes were detected in your source files”_,  
  check your `tailwind.config.js` to ensure it includes this path:

```js
content: [
  "./app/**/*.{vue,js,ts}",
  "./components/**/*.{js,vue,ts}",
  "./layouts/**/*.vue",
  "./pages/**/*.vue",
  "./plugins/**/*.{js,ts}",
  "./app.vue",
  "./error.vue",
],
```

---

Check out the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction)  
and [Tailwind CSS docs](https://tailwindcss.com/docs) for more.
