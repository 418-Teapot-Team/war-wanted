/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      fontFamily: {
        ubuntu: ['Ubuntu', 'Helvetica', 'Arial', 'sans-serif'],
      },
      colors: {
        backdrop: '#f1faee',
        primary: '#457b9d',
        'primary-dark': '#1d3557',
        'primary-light': '#a8dadc',
        error: '#e63946',
      },
    },
  },
  plugins: [],
};
