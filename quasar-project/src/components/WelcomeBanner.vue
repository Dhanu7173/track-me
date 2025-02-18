<template>
  <div class="relative bg-white rounded-2xl px-8 py-10 shadow-lg flex flex-col md:flex-row items-center justify-between">
    <!-- Left Content -->
    <div class="space-y-4 text-center md:text-left">
      <h2 class="text-2xl font-bold text-gray-800">Welcome To</h2>
      <h1 class="text-4xl font-extrabold text-gray-800">Your Task Management Area</h1>
      <p class="text-gray-500 max-w-md">
        Lorem ipsum dolor sit amet consectetur. Egestas risus urna
        tortor praesent.
      </p>
      <q-btn
        color="sidebar"
        label="Learn More"
        class="px-6 py-2 rounded-full shadow-md transition-transform transform hover:scale-105"
      />
    </div>

    <!-- Right Image -->
    <img
      src="~/assets/banner.png"
      alt="Welcome"
      class="absolute right-5 bottom-5 w-1/4 object-contain z-10"
    />
  </div>
</template>

<style scoped>
/* Gradient Text */
.text-gradient {
  background: linear-gradient(45deg, #38bdf8, #9333ea);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
