<template>
  <div class="tw-w-full tw-h-full">
    <apexchart
      width="100%"
      type="bar"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import VueApexCharts from 'vue3-apexcharts'

export default defineComponent({
  components: {
    apexchart: VueApexCharts
  },
  setup() {
    const series = ref([
      {
        name: 'Projects',
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
      },
    ])

    const chartOptions = ref({
      chart: {
        type: 'line',
        toolbar: {
          show: false,
        },
      },
      stroke: {
        curve: 'smooth',
      },
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
      },
      colors: ['#0095ff'],
    })

    return {
      series,
      chartOptions
    }
  }
})
</script>

<style scoped>
/* Ensure parent container takes full height */

</style>
