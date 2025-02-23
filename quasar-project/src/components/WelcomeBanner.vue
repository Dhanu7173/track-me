<template>
  <div class="tw-relative tw-bg-white tw-rounded-2xl tw-px-8 tw-py-10 tw-shadow-lg tw-flex tw-flex-col md:tw-flex-row tw-items-center tw-justify-between">
    <!-- Left Content -->
    <div class="tw-space-y-4 tw-text-center md:tw-text-left">
      <h2 class="tw-text-2xl tw-font-bold tw-text-gray-800">Welcome To</h2>
      <h1 class="tw-text-4xl tw-font-extrabold tw-text-gray-800">Your Task Management Area</h1>
      <p class="tw-text-gray-500 tw-max-w-md">
        Lorem ipsum dolor sit amet consectetur. Egestas risus urna
        tortor praesent.
      </p>
      <q-btn
        color="sidebar"
        label="Learn More"
        class="tw-px-6 tw-py-2 tw-bg-sidebar tw-rounded-full tw-shadow-md tw-transition-transform tw-transform hover:tw-scale-105"
      />
    </div>

    <!-- Right Image -->
    <img
      src="~/assets/banner.png"
      alt="Welcome"
      class="tw-absolute tw-right-5 tw-bottom-5 tw-w-1/4 tw-object-contain tw-z-10"
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
