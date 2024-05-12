/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js}', 'node_modules/preline/dist/*.js'],
  theme: {
    extend: {
      fontFamily: {
        ubuntu: ['Ubuntu', 'Helvetica', 'Arial', 'sans-serif'],
      },
      colors: {
        backdrop: '#f2f2f2',
        green: '#444F2D',
      },
    },
  },
  plugins: [require('preline/plugin')],
};
