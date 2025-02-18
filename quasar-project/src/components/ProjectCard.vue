<template>
  <div
    class="bg-white rounded-2xl p-6 shadow-md cursor-pointer hover:shadow-lg transition-shadow relative border border-gray-200"
  >
    <!-- Three-dot menu for Edit/Delete -->
    <q-btn flat dense round class="absolute right-2">
      <!-- <template v-slot:label> -->
        <Icon icon="mage:dots" width="24" height="24" class="text-gray-500" />
      <!-- </template> -->
     <q-menu>
       <q-list>
        <q-item clickable v-close-popup @click="$emit('edit', project)">
          <q-item-section avatar>
            <Icon icon="mdi:pencil-outline" class="text-lg text-gray-500" />
          </q-item-section>
          <q-item-section>Edit</q-item-section>
        </q-item>
        <q-item clickable v-close-popup @click="$emit('delete', project.id)">
          <q-item-section avatar>
            <Icon icon="mdi:trash-can-outline" class="text-lg text-red-500" />
          </q-item-section>
          <q-item-section class="text-red-500">Delete</q-item-section>
        </q-item>
      </q-list>
     </q-menu>
    </q-btn>

    <!-- Project Details -->
    <div @click="openProjectDialog">
      <div class="flex justify-between items-start">
        <div>
          <span class="text-sm text-gray-500">{{ project.type }}</span>
          <h3 class="text-lg font-semibold mt-2">{{ project.title }}</h3>
          <p class="text-gray-500 text-sm mt-1">{{ project.description }}</p>
        </div>
        <q-chip :color="getStatusColor(project.status)" text-color="white" size="sm" class="capitalize">
          {{ project.status }}
        </q-chip>
      </div>

      <!-- Progress Bar -->
      <div class="mt-4">
        <div class="flex justify-between text-sm text-gray-500 mb-2">
          <span>Progress</span>
          <span>{{ project.progress }}% Complete</span>
        </div>
        <q-linear-progress :value="project.progress / 100" color="primary" class="rounded-full transition-all" />
      </div>

      <!-- Dates & Team -->
      <div class="flex justify-between mt-4 text-sm">
        <div>
          <div class="text-gray-500">Start Date</div>
          <div class="font-medium">{{ formatDate(project.startDate) }}</div>
        </div>
        <div>
          <div class="text-gray-500">End Date</div>
          <div class="font-medium">{{ formatDate(project.endDate) }}</div>
        </div>
      </div>

      <!-- Team Avatars -->
      <div class="flex justify-between items-center mt-4">
        <div class="flex -space-x-2">
          <q-avatar v-for="member in project.team.slice(0, 3)" :key="member.id" size="26px" class="border border-white shadow-sm">
            <img :src="member.avatar" />
          </q-avatar>
          <div
            v-if="project.team.length > 3"
            class="flex items-center justify-center w-7 h-7 rounded-full bg-gray-200 text-xs font-medium border border-white shadow-sm"
          >
            +{{ project.team.length - 3 }}
          </div>
        </div>
        <span class="text-sm text-gray-500">Due {{ formatDate(project.dueDate) }}</span>
      </div>
    </div>

    <!-- Project Details Dialog -->
    <q-dialog v-model="projectDialog" persistent>
      <q-card class="w-full max-w-md bg-white rounded-lg shadow-lg p-6">
        <q-card-section class="flex justify-between items-center border-b pb-3">
          <h3 class="text-xl font-semibold text-gray-800">{{ project.title }}</h3>
          <q-btn flat dense icon="close" class="text-gray-500" @click="projectDialog = false" />
        </q-card-section>

        <q-card-section class="space-y-4">
          <div>
            <h4 class="text-gray-600 font-medium">Description</h4>
            <p class="text-gray-500">{{ project.description }}</p>
          </div>

          <div>
            <h4 class="text-gray-600 font-medium">Status</h4>
            <q-chip :color="getStatusColor(project.status)" text-color="white">
              {{ project.status }}
            </q-chip>
          </div>

          <div>
            <h4 class="text-gray-600 font-medium">Progress</h4>
            <q-linear-progress :value="project.progress / 100" color="primary" />
            <p class="text-gray-500 text-sm mt-1">{{ project.progress }}% Complete</p>
          </div>

          <div>
            <h4 class="text-gray-600 font-medium">Due Date</h4>
            <p class="text-gray-500">{{ formatDate(project.dueDate) }}</p>
          </div>

          <div>
            <h4 class="text-gray-600 font-medium">Team</h4>
            <div class="flex flex-wrap gap-2 mt-2">
              <q-chip v-for="member in project.team" :key="member.id" size="md">
                <q-avatar><img :src="member.avatar" /></q-avatar>
                {{ member.name }}
              </q-chip>
            </div>
          </div>

          <div>
            <h4 class="text-gray-600 font-medium">Tasks</h4>
            <q-list bordered separator>
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
