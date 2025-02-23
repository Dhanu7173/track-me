<template>
  <div class="tw-space-y-6">
    <!-- Header -->
    <div class="tw-flex tw-justify-between tw-items-center">
      <h2 class="tw-text-2xl tw-font-bold">My Tasks</h2>
      <div class="tw-flex tw-gap-4">
        <q-select
          v-model="filterStatus"
          :options="statusOptions"
          label="Status"
          outlined
          dense
          class="tw-w-40"
        />
        <q-btn color="primary" icon="add" label="New Task" @click="openNewTaskDialog" />
      </div>
    </div>

    <!-- Task Table -->
    <div class="tw-bg-white tw-border tw-border-gray-200 ">
      <q-table
        :rows="filteredTasks"
        :columns="columns"
        row-key="id"
        flat
        :pagination="{ rowsPerPage: 10 }"
        class="tw-w-full tw-rounded-2xl"
      >
        <!-- Status Column -->
        <template v-slot:body-cell-status="props">
          <q-td :props="props">
            <q-chip :color="getStatusColor(props.value)" text-color="white" size="sm">
              {{ props.value }}
            </q-chip>
          </q-td>
        </template>

        <!-- Priority Column -->
        <template v-slot:body-cell-priority="props">
          <q-td :props="props">
            <q-chip :color="getPriorityColor(props.value)" text-color="white" size="sm">
              {{ props.value }}
            </q-chip>
          </q-td>
        </template>

        <!-- Actions Column -->
        <template v-slot:body-cell-actions="props">
          <q-td :props="props">
            <div class="tw-flex tw-gap-2">
              <q-btn flat round size="sm" color="primary" icon="edit" @click="editTask(props.row)" />
              <q-btn flat round size="sm" color="negative" icon="delete" @click="deleteTask(props.row.id)" />
            </div>
          </q-td>
        </template>
      </q-table>
    </div>

    <!-- Add/Edit Task Dialog -->
    <q-dialog v-model="taskDialog">
    <q-card class="tw-w-full tw-max-w-md tw-bg-white tw-rounded-lg tw-shadow-lg tw-p-6">
        <!-- Dialog Header -->
        <q-card-section class="tw-flex tw-justify-between tw-items-center tw-border-b tw-pb-3">
        <h3 class="tw-text-xl tw-font-semibold tw-text-gray-800">
            {{ editMode ? "Edit Task" : "New Task" }}
        </h3>
        <q-btn flat dense icon="close" class="tw-text-gray-500" @click="taskDialog = false" />
        </q-card-section>

        <!-- Form Fields -->
        <q-card-section class="tw-space-y-4">
        <q-input v-model="taskForm.title" label="Task Title" outlined dense class="tw-w-full" />
        <q-input v-model="taskForm.project" label="Project" outlined dense class="tw-w-full" />
        
        <div class="tw-grid tw-grid-cols-2 tw-gap-4">
            <q-select v-model="taskForm.status" :options="statusOptions" label="Status" outlined dense class="tw-w-full" />
            <q-select v-model="taskForm.priority" :options="priorityOptions" label="Priority" outlined dense class="tw-w-full" />
        </div>
        
        <q-input v-model="taskForm.dueDate" label="Due Date" outlined dense type="date" class="tw-w-full" />
        </q-card-section>

        <!-- Actions -->
        <q-card-actions align="right" class="tw-border-t tw-pt-3">
        <q-btn flat label="Cancel" class="tw-text-gray-600" @click="taskDialog = false" />
        <q-btn color="primary" class="tw-px-4 tw-py-2 tw-rounded-md tw-shadow-md" :label="editMode ? 'Update' : 'Add'" @click="saveTask" />
        </q-card-actions>
    </q-card>
    </q-dialog>

  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, watch } from 'vue'

export default defineComponent({
  name: 'MyTasks',
  
  setup() {
    // Local Storage Key
    const STORAGE_KEY = 'tasks'
    const columns = [
      { name: 'title', label: 'Task', field: 'title', sortable: true },
      { name: 'project', label: 'Project', field: 'project', sortable: true },
      { name: 'status', label: 'Status', field: 'status', sortable: true },
      { name: 'priority', label: 'Priority', field: 'priority', sortable: true },
      { name: 'dueDate', label: 'Due Date', field: 'dueDate', sortable: true },
      { name: 'actions', label: 'Actions', field: 'actions' },
    ]
    // Reactive Data
    const filterStatus = ref('All')
    const statusOptions = ['All', 'In Progress', 'Completed', 'On Hold']
    const priorityOptions = ['High', 'Medium', 'Low']
    const taskDialog = ref(false)
    const editMode = ref(false)
    const taskForm = ref({
      id: 0,
      title: '',
      project: '',
      status: 'In Progress',
      priority: 'Medium',
      dueDate: '',
    })

    // Load tasks from localStorage
    const tasks = ref(JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'))

    // Watch for changes and update localStorage
    watch(tasks, (newTasks) => {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(newTasks))
    }, { deep: true })

    // Filter tasks based on status
    const filteredTasks = computed(() => {
      return filterStatus.value === 'All'
        ? tasks.value
        : tasks.value.filter(task => task.status === filterStatus.value)
    })

    // Get chip colors
    const getStatusColor = (status: string) => {
      return { 'In Progress': 'blue', 'Completed': 'green', 'On Hold': 'orange' }[status] || 'grey'
    }

    const getPriorityColor = (priority: string) => {
      return { 'High': 'negative', 'Medium': 'warning', 'Low': 'positive' }[priority] || 'grey'
    }

    // Open task form dialog for new task
    const openNewTaskDialog = () => {
      editMode.value = false
      taskForm.value = { id: Date.now(), title: '', project: '', status: 'In Progress', priority: 'Medium', dueDate: '' }
      taskDialog.value = true
    }

    // Open dialog for editing an existing task
    const editTask = (task: any) => {
      editMode.value = true
      taskForm.value = { ...task }
      taskDialog.value = true
    }

    // Save or update task
    const saveTask = () => {
      if (editMode.value) {
        const index = tasks.value.findIndex(t => t.id === taskForm.value.id)
        if (index !== -1) {
          tasks.value[index] = { ...taskForm.value }
        }
      } else {
        tasks.value.push({ ...taskForm.value })
      }
      taskDialog.value = false
    }

    // Delete task
    const deleteTask = (taskId: number) => {
      tasks.value = tasks.value.filter(task => task.id !== taskId)
    }

    return {
      filterStatus,
      statusOptions,
      priorityOptions,
      taskDialog,
      editMode,
      taskForm,
      tasks,
      filteredTasks,
      columns,
      getStatusColor,
      getPriorityColor,
      openNewTaskDialog,
      editTask,
      saveTask,
      deleteTask,
    }
  },
})
</script>
