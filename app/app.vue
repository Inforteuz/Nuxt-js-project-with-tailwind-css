<template>
  <div class="flex h-screen bg-gray-100 text-gray-900">

    <!-- Sidebar -->
    <aside class="w-64 bg-gray-900 text-gray-100 flex flex-col">
      <div class="px-6 py-4 text-xl font-bold border-b border-gray-700">
        MyFramework Docs
      </div>
      <nav class="flex-1 px-4 py-2 space-y-2 overflow-y-auto">
        <a href="#" class="block px-3 py-2 rounded hover:bg-gray-800">🚀 Introduction</a>
        <a href="#" class="block px-3 py-2 rounded hover:bg-gray-800">⚙️ Installation</a>
        <a href="#" class="block px-3 py-2 rounded hover:bg-gray-800">📘 Controllers</a>
        <a href="#" class="block px-3 py-2 rounded hover:bg-gray-800">💾 Models</a>
        <a href="#" class="block px-3 py-2 rounded hover:bg-gray-800">🧩 Helpers</a>
        <a href="#" class="block px-3 py-2 rounded hover:bg-gray-800">📄 License</a>
      </nav>
      <div class="px-4 py-3 border-t border-gray-700 text-sm text-gray-400">
        v1.0.0 — Oyatillo
      </div>
    </aside>

    <!-- Main content -->
    <main class="flex-1 flex flex-col">
      <!-- Topbar -->
      <header class="bg-white border-b border-gray-200 px-6 py-3 flex justify-between items-center">
        <h1 class="text-xl font-semibold">Documentation</h1>
        <input
          type="text"
          placeholder="Search..."
          class="px-3 py-2 border rounded-lg w-64 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </header>

      <!-- Content -->
      <section class="p-8 overflow-y-auto">
        <h2 class="text-3xl font-bold mb-4">Welcome to MyFramework 🚀</h2>
        <p class="text-gray-700 mb-4">
          This is the official documentation site for your custom PHP framework.
          Built with <span class="font-semibold text-blue-600">Nuxt 3</span> and
          <span class="font-semibold text-teal-500">Tailwind CSS</span>.
        </p>

        <div class="bg-gray-50 border border-gray-200 rounded-lg p-4 shadow-sm">
          <h3 class="text-xl font-semibold mb-2">Example Code Block:</h3>
          <pre class="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto text-sm">
<code>public function index()
{
    echo "Hello from MyFramework Controller!";
}</code>
          </pre>
        </div>

        <p class="mt-6 text-gray-600">
          Use this layout as your base — we’ll add PrismJS syntax highlighting, routing,
          and sidebar auto-scroll in the next steps.
        </p>
      </section>
    </main>

  </div>
</template>
