<template>
  <div
    class="tw-bg-white tw-rounded-2xl tw-p-6 tw-shadow-md tw-cursor-pointer hover:tw-shadow-lg tw-transition-shadow tw-relative tw-border tw-border-gray-200"
  >
    <!-- Three-dot menu for Edit/Delete -->
    <q-btn flat dense round class="tw-absolute tw-right-2">
      <!-- <template v-slot:label> -->
        <Icon icon="mage:dots" width="24" height="24" class="tw-text-gray-500" />
      <!-- </template> -->
     <q-menu>
       <q-list>
        <q-item clickable v-close-popup @click="$emit('edit', project)">
          <q-item-section avatar>
            <Icon icon="mdi:pencil-outline" class="tw-text-lg tw-text-gray-500" />
          </q-item-section>
          <q-item-section>Edit</q-item-section>
        </q-item>
        <q-item clickable v-close-popup @click="$emit('delete', project.id)">
          <q-item-section avatar>
            <Icon icon="mdi:trash-can-outline" class="tw-text-lg tw-text-red-500" />
          </q-item-section>
          <q-item-section class="tw-text-red-500">Delete</q-item-section>
        </q-item>
      </q-list>
     </q-menu>
    </q-btn>

    <!-- Project Details -->
    <div @click="openProjectDialog">
      <div class="tw-flex tw-justify-between tw-items-start">
        <div>
          <span class="tw-text-sm tw-text-gray-500">{{ project.type }}</span>
          <h3 class="tw-text-lg tw-font-semibold tw-mt-2">{{ project.title }}</h3>
          <p class="tw-text-gray-500 tw-text-sm tw-mt-1">{{ project.description }}</p>
        </div>
        <q-chip :color="getStatusColor(project.status)" text-color="white" size="sm" class="tw-capitalize">
          {{ project.status }}
        </q-chip>
      </div>

      <!-- Progress Bar -->
      <div class="tw-mt-4">
        <div class="tw-flex tw-justify-between tw-text-sm tw-text-gray-500 tw-mb-2">
          <span>Progress</span>
          <span>{{ project.progress }}% Complete</span>
        </div>
        <q-linear-progress :value="project.progress / 100" color="primary" class="tw-rounded-full tw-transition-all" />
      </div>

      <!-- Dates & Team -->
      <div class="tw-flex tw-justify-between tw-mt-4 tw-text-sm">
        <div>
          <div class="tw-text-gray-500">Start Date</div>
          <div class="tw-font-medium">{{ formatDate(project.startDate) }}</div>
        </div>
        <div>
          <div class="tw-text-gray-500">End Date</div>
          <div class="tw-font-medium">{{ formatDate(project.endDate) }}</div>
        </div>
      </div>

      <!-- Team Avatars -->
      <div class="tw-flex tw-justify-between tw-items-center tw-mt-4">
        <div class="tw-flex tw--space-x-2">
          <q-avatar v-for="member in project.team.slice(0, 3)" :key="member.id" size="26px" class="tw-border tw-border-white tw-shadow-sm">
            <img :src="member.avatar" />
          </q-avatar>
          <div
            v-if="project.team.length > 3"
            class="tw-flex tw-items-center tw-justify-center tw-w-7 tw-h-7 tw-rounded-full tw-bg-gray-200 tw-text-xs tw-font-medium tw-border tw-border-white tw-shadow-sm"
          >
            +{{ project.team.length - 3 }}
          </div>
        </div>
        <span class="tw-text-sm tw-text-gray-500">Due {{ formatDate(project.dueDate) }}</span>
      </div>
    </div>

    <!-- Project Details Dialog -->
    <q-dialog v-model="projectDialog" persistent>
      <q-card class="tw-w-full tw-max-w-md tw-bg-white tw-rounded-lg tw-shadow-lg tw-p-6">
        <q-card-section class="tw-flex tw-justify-between tw-items-center tw-border-b tw-pb-3">
          <h3 class="tw-text-xl tw-font-semibold tw-text-gray-800">{{ project.title }}</h3>
          <q-btn flat dense icon="close" class="tw-text-gray-500" @click="projectDialog = false" />
        </q-card-section>

        <q-card-section class="tw-space-y-4">
          <div>
            <h4 class="tw-text-gray-600 tw-font-medium">Description</h4>
            <p class="tw-text-gray-500">{{ project.description }}</p>
          </div>

          <div>
            <h4 class="tw-text-gray-600 tw-font-medium">Status</h4>
            <q-chip :color="getStatusColor(project.status)" text-color="white">
              {{ project.status }}
            </q-chip>
          </div>

          <div>
            <h4 class="tw-text-gray-600 tw-font-medium">Progress</h4>
            <q-linear-progress :value="project.progress / 100" color="primary" />
            <p class="tw-text-gray-500 tw-text-sm tw-mt-1">{{ project.progress }}% Complete</p>
          </div>

          <div>
            <h4 class="tw-text-gray-600 tw-font-medium">Due Date</h4>
            <p class="tw-text-gray-500">{{ formatDate(project.dueDate) }}</p>
          </div>

          <div>
            <h4 class="tw-text-gray-600 tw-font-medium">Team</h4>
            <div class="tw-flex tw-flex-wrap tw-gap-2 tw-mt-2">
              <q-chip v-for="member in project.team" :key="member.id" size="md">
                <q-avatar><img :src="member.avatar" /></q-avatar>
                {{ member.name }}
              </q-chip>
            </div>
          </div>

          <div>
            <h4 class="tw-text-gray-600 tw-font-medium">Tasks</h4>
            <q-list tw-bordered separator>
              <q-item v-for="task in project.tasks" :key="task.id">
                <q-item-section>
                  <q-item-label>{{ task.name }}</q-item-label>
                  <q-item-label caption>{{ task.status }}</q-item-label>
                </q-item-section>
                <q-item-section side>
                  <q-chip :color="getStatusColor(task.status)" text-color="white" size="sm">
                    {{ task.status }}
                  </q-chip>
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Close" color="primary" @click="projectDialog = false" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { date } from 'quasar'
import { Icon } from '@iconify/vue'

const props = defineProps<{
  project: {
    id: number
    title: string
    description: string
    type: string
    progress: number
    startDate: string
    endDate: string
    status: string
    dueDate: string
    team: { id: number; name: string; avatar: string }[]
    tasks: { id: number; name: string; status: string }[]
  }
}>()

const emit = defineEmits(['edit', 'delete'])

const projectDialog = ref(false)

const getStatusColor = (status: string) => {
  const colors = {
    'Completed': 'positive',
    'In Progress': 'primary',
    'On Hold': 'warning',
    'Pending': 'grey',
  }
  return colors[status] || 'grey'
}

const formatDate = (dateString: string) => {
  return date.formatDate(dateString, 'MMMM D, YYYY')
}

const openProjectDialog = () => {
  projectDialog.value = true
}
</script>
