<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex justify-between items-center">
      <h2 class="text-2xl font-bold">Projects</h2>
      <q-btn color="primary" icon="add" label="New Project" @click="openNewProjectDialog(false)" />
    </div>

    <!-- Projects Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <ProjectCard 
        v-for="project in projects" 
        :key="project.id" 
        :project="project"
        @edit="openNewProjectDialog(true, project)"
        @delete="deleteProject(project.id)"
      />
    </div>

    <!-- New/Edit Project Dialog -->
    <q-dialog v-model="projectDialog">
      <q-card class="w-full max-w-xl bg-white rounded-lg shadow-lg p-6">
        <q-card-section class="flex justify-between items-center border-b pb-3">
          <h3 class="text-xl font-semibold text-gray-800">
            {{ editMode ? 'Edit Project' : 'New Project' }}
          </h3>
          <q-btn flat dense icon="close" class="text-gray-500" @click="projectDialog = false" />
        </q-card-section>

        <q-card-section class="space-y-4">
          <q-input v-model="newProject.title" label="Project Title" outlined dense class="w-full" />
          <q-input v-model="newProject.description" label="Description" outlined dense class="w-full" />
          <q-select v-model="newProject.type" :options="['Ongoing Project', 'Completed Project']" label="Type" outlined dense class="w-full" />
          <q-input v-model="newProject.progress" type="number" label="Progress (%)" outlined dense class="w-full" />
          <q-select v-model="newProject.status" :options="['In Progress', 'Completed', 'On Hold', 'Pending']" label="Status" outlined dense class="w-full" />
          <q-input v-model="newProject.startDate" type="date" label="Start Date" outlined dense class="w-full" />
          <q-input v-model="newProject.endDate" type="date" label="End Date" outlined dense class="w-full" />
          <q-input v-model="newProject.dueDate" type="date" label="Due Date" outlined dense class="w-full" />

          <!-- Team Members -->
          <div class="border-t pt-4">
            <h4 class="text-lg font-semibold">Team Members</h4>
            <div v-for="(member, index) in newProject.team" :key="index" class="flex gap-2 items-center">
              <q-avatar size="32px">
                <img :src="member.avatar" alt="Team Member" />
              </q-avatar>
              <q-input v-model="member.name" label="Member Name" outlined dense class="flex-grow mt-1" />
              <q-btn icon="delete" flat color="red" @click="removeTeamMember(index)" />
            </div>
            <q-btn label="Add Team Member" class="mt-2" outline color="primary" @click="addTeamMember" />
          </div>

          <!-- Tasks -->
          <div class="border-t pt-4">
            <h4 class="text-lg font-semibold">Tasks</h4>
            <div v-for="(task, index) in newProject.tasks" :key="index" class="flex gap-2 items-center">
              <q-input v-model="task.name" label="Task Name" outlined dense class="flex-grow mt-1" />
              <q-select v-model="task.status" :options="['Pending', 'In Progress', 'Completed']" label="Status" outlined dense class="w-40" />
              <q-btn icon="delete" flat color="red" @click="removeTask(index)" />
            </div>
            <q-btn label="Add Task" class="mt-2" outline color="primary" @click="addTask" />
          </div>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" @click="projectDialog = false" />
          <q-btn color="primary" :label="editMode ? 'Update Project' : 'Add Project'" @click="saveProject" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import ProjectCard from '../components/ProjectCard.vue'

export default defineComponent({
  name: 'Projects',
  components: {
    ProjectCard,
  },
  setup() {
    const projectDialog = ref(false)
    const editMode = ref(false)
    const projects = ref([])

    const newProject = ref({
      id: 0,
      title: '',
      description: '',
      type: 'Ongoing Project',
      progress: 0,
      status: 'In Progress',
      startDate: '',
      endDate: '',
      dueDate: '',
      team: [],
      tasks: [],
    })

    // Load projects from localStorage
    const loadProjects = () => {
      const savedProjects = localStorage.getItem('projects')
      if (savedProjects) {
        projects.value = JSON.parse(savedProjects)
      }
    }

    // Save projects to localStorage whenever projects change
    watch(projects, (newProjects) => {
      localStorage.setItem('projects', JSON.stringify(newProjects))
    }, { deep: true })

    // Open Dialog for New or Edit
    const openNewProjectDialog = (isEdit: boolean, project = null) => {
      editMode.value = isEdit
      if (isEdit && project) {
        newProject.value = { ...project }
      } else {
        newProject.value = {
          id: Date.now(),
          title: '',
          description: '',
          type: 'Ongoing Project',
          progress: 0,
          status: 'In Progress',
          startDate: '',
          endDate: '',
          dueDate: '',
          team: [],
          tasks: [],
        }
      }
      projectDialog.value = true
    }

    // Save or Update Project
    const saveProject = () => {
      if (!newProject.value.title.trim()) return
      if (editMode.value) {
        const index = projects.value.findIndex(p => p.id === newProject.value.id)
        if (index !== -1) {
          projects.value[index] = { ...newProject.value }
        }
      } else {
        projects.value.push({ ...newProject.value, id: Date.now() })
      }
      projectDialog.value = false
    }

    // Delete Project
    const deleteProject = (id: number) => {
      projects.value = projects.value.filter(p => p.id !== id)
    }

    // Add and remove team members
    const addTeamMember = () => {
      newProject.value.team.push({ name: '', avatar: `https://randomuser.me/api/portraits/men/${Math.floor(Math.random() * 99) + 1}.jpg` })
    }

    const removeTeamMember = (index: number) => {
      newProject.value.team.splice(index, 1)
    }

    // Add and remove tasks
    const addTask = () => {
      newProject.value.tasks.push({ name: '', status: 'Pending' })
    }

    const removeTask = (index: number) => {
      newProject.value.tasks.splice(index, 1)
    }

    // Load projects on mount
    loadProjects()

    return {
      projects,
      projectDialog,
      editMode,
      newProject,
      openNewProjectDialog,
      saveProject,
      deleteProject,
      addTeamMember,
      removeTeamMember,
      addTask,
      removeTask,
    }
  },
})
</script>
