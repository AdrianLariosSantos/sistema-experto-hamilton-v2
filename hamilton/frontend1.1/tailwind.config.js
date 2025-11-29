/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')
const colors = require('tailwindcss/colors')

module.exports = {
  content: [
    "./src/**/*.vue",
    "./src/**/*.ts",
    "./src/**/*.tsx",
    "./src/**/*.js",
    "./src/**/*.jsx",
    "./src/**/*.html",
    "./public/index.html"
  ],
  theme: {
    extend: {
      animation: {
        'animate-bounce-once': 'bounce 1s',
      },
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        'maincolor': {
          DEFAULT: '#184A7C',
          50: '#d1dbe5',
          100: '#7492b0',
          200: '#5d80a3',
          300: '#466e96',
          400: '#2f5c89',
          500: '#184a7c',
          600: '#164370',
          700: '#133b63',
          800: '#113457',
          900: '#0e2c4a',
        },
        'verdebienestar': {
          DEFAULT: '#235b4e',
          100: '#7b9d95',
          200: '#658c83',
          300: '#4f7c71',
          400: '#396b60',
          500: '#235b4e',
          600: '#205246',
          700: '#1c493e',
          800: '#194037',
          900: '#15372f',
        },
        'doradobienestar': {
          DEFAULT: '#ddc9a3',
          100: '#ebdfc8',
          200: '#e7d9bf',
          300: '#e4d4b5',
          400: '#e0ceac',
          500: '#ddc9a3',
          600: '#c7b593',
          700: '#b1a182',
          800: '#9b8d72',
          900: '#857962',
        },
        sky: colors.sky,
        teal: colors.teal,
        rose: colors.rose,
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
