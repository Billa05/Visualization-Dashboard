/** @type {import('tailwindcss').Config} */
export const content = [
  "./src/**/*.{js,jsx,ts,tsx}",
];
export const theme = {
  extend: {
    gridAutoRows: {
      '2fr': 'minmax(300px, auto)',
    }
  },
};
export const plugins = [];