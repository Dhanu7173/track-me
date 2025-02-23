/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        sidebar: "#dc2f02",
        primary: "#6a040f",
      },
    },
  },
  plugins: [],
  prefix: "tw-",
};
