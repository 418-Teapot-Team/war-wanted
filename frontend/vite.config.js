import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import VueDevTools from 'vite-plugin-vue-devtools';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    VueDevTools(),
    vue({
      script: {
        // Experimental feature!
        defineModel: true,
      },
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  chainWebpack: (config) => {
    config.module.rule('images').set('parser', {
      dataUrlCondition: {
        maxSize: 1024 * 1024, // 1024KiB
      },
    });
  },
});
