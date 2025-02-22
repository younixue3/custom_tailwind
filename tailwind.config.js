/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../../custom_TA/**/*.{html,js,xml}"], // Make sure to include your custom addons' paths here as well
  theme: {
    extend: {},
  },
  plugins: [],
  prefix: "tw-",
  blocklist: ["container", "collapse"], // Add classes to blocklist to avoid generating them
};
