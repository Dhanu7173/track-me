<template>
  <div class="tw-space-y-6">
    <h2 class="tw-text-2xl tw-font-bold">Activity</h2>

    <div class="tw-bg-white tw-rounded-lg tw-shadow-sm tw-p-6">
      <div class="tw-flex tw-gap-4 tw-mb-6">
        <q-btn
          v-for="filter in filters"
          :key="filter"
          :label="filter"
          :color="activeFilter === filter ? 'primary' : 'grey-3'"
          :text-color="activeFilter === filter ? 'blue' : 'black'"
          @click="activeFilter = filter"
          flat
          tw-rounded
        />
      </div>

      <q-timeline color="primary">
        <q-timeline-entry
          v-for="activity in filteredActivities"
          :key="activity.id"
          :title="activity.title"
          :subtitle="activity.time"
          :icon="activity.icon"
        >
          <div class="tw-text-gray-600">{{ activity.description }}</div>
          
          <div v-if="activity.project" class="tw-mt-2">
            <q-chip
              size="sm"
              class="tw-bg-blue-50 tw-text-blue-600"
            >
              {{ activity.project }}
            </q-chip>
          </div>
        </q-timeline-entry>
      </q-timeline>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue'

export default defineComponent({
  name: 'Activity',
  
  setup() {
    const activeFilter = ref('All')
    const filters = ['All', 'Tasks', 'Projects', 'Comments']

    const activities = ref([
      {
        id: 1,
        type: 'task',
        title: 'Task Completed',
        description: 'Completed the dashboard layout design',
        project: 'Dashboard Design',
        time: '2 hours ago',
        icon: 'check_circle'
      },
      {
        id: 2,
        type: 'comment',
        title: 'New Comment',
        description: 'Left a comment on UI design task',
        project: 'App UI UX Design',
        time: '4 hours ago',
        icon: 'chat'
      },
      // Add more activities...
    ])

    const filteredActivities = computed(() => {
      if (activeFilter.value === 'All') return activities.value
      return activities.value.filter(
        activity => activity.type.toLowerCase() === activeFilter.value.toLowerCase()
      )
    })

    return {
      activeFilter,
      filters,
      filteredActivities
    }
  }
})
</script>