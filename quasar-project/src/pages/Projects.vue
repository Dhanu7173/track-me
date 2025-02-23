<template>
  <div class="tw-space-y-6">
    <!-- Page Header -->
    <div class="tw-flex tw-justify-between tw-items-center">
      <h2 class="tw-text-2xl tw-font-bold">Projects</h2>
      <q-btn color="primary" icon="add" label="New Project" @click="openNewProjectDialog(false)" />
    </div>

    <!-- Projects Grid -->
    <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-2 lg:tw-grid-cols-3 tw-gap-6">
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
      <q-card class="tw-w-full tw-max-w-xl tw-bg-white tw-rounded-2xl tw-shadow-lg tw-p-6">
        <q-card-section class="tw-flex tw-justify-between tw-items-center tw-border-b tw-pb-3">
          <h3 class="tw-text-xl tw-font-semibold tw-text-gray-800">
            {{ editMode ? 'Edit Project' : 'New Project' }}
          </h3>
          <q-btn flat dense icon="close" class="tw-text-gray-500" @click="projectDialog = false" />
        </q-card-section>

        <q-card-section class="tw-space-y-4">
          <q-input v-model="newProject.title" label="Project Title" outlined dense class="tw-w-full" />
          <q-input v-model="newProject.description" label="Description" outlined dense class="tw-w-full" />
          <q-select v-model="newProject.type" :options="['Ongoing Project', 'Completed Project']" label="Type" outlined dense class="tw-w-full" />
          <q-input v-model="newProject.progress" type="number" label="Progress (%)" outlined dense class="tw-w-full" />
          <q-select v-model="newProject.status" :options="['In Progress', 'Completed', 'On Hold', 'Pending']" label="Status" outlined dense class="tw-w-full" />
          <q-input v-model="newProject.startDate" type="date" label="Start Date" outlined dense class="tw-w-full" />
          <q-input v-model="newProject.endDate" type="date" label="End Date" outlined dense class="tw-w-full" />
          <q-input v-model="newProject.dueDate" type="date" label="Due Date" outlined dense class="tw-w-full" />

          <!-- Team Members -->
          <div class="tw-border-t tw-pt-4">
            <h4 class="tw-text-lg tw-font-semibold">Team Members</h4>
            <div v-for="(member, index) in newProject.team" :key="index" class="tw-flex tw-gap-2 tw-items-center">
              <q-avatar size="32px">
                <img :src="member.avatar" alt="Team Member" />
              </q-avatar>
              <q-input v-model="member.name" label="Member Name" outlined dense class="tw-flex-grow tw-mt-1" />
              <q-btn icon="delete" flat color="red" @click="removeTeamMember(index)" />
            </div>
            <q-btn label="Add Team Member" class="tw-mt-2" outline color="primary" @click="addTeamMember" />
          </div>

          <!-- Tasks -->
          <div class="tw-border-t tw-pt-4">
            <h4 class="tw-text-lg tw-font-semibold">Tasks</h4>
            <div v-for="(task, index) in newProject.tasks" :key="index" class="tw-flex tw-gap-2 tw-items-center">
              <q-input v-model="task.name" label="Task Name" outlined dense class="tw-flex-grow tw-mt-1" />
              <q-select v-model="task.status" :options="['Pending', 'In Progress', 'Completed']" label="Status" outlined dense class="tw-w-40" />
              <q-btn icon="delete" flat color="red" @click="removeTask(index)" />
            </div>
            <q-btn label="Add Task" class="tw-mt-2" outline color="primary" @click="addTask" />
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
      deleteProject,
      addTeamMember,
      removeTeamMember,
      addTask,
      removeTask,
    }
  },
  methods: {
    async saveProject() {
      if (!this.newProject.title.trim()) return;

      const projectData = {
        title: this.newProject.title,
        description: this.newProject.description,
        type: this.newProject.type,
        progress: this.newProject.progress,
        status: this.newProject.status,
        startDate: this.newProject.startDate,
        endDate: this.newProject.endDate,
        dueDate: this.newProject.dueDate,
        team: this.newProject.team,  // Send team members as an array
        tasks: this.newProject.tasks // Send tasks as an array
      };

      try {
        const response = await this.$api.post("/users/projects", projectData);
        
        this.$q.notify({
          type: "positive",
          message: "Project added successfully!",
        });

        // Update UI with new project
        this.projects.push({ ...projectData, id: response.data.project_id });

        this.projectDialog = false;
      } catch (error) {
        this.$q.notify({
          type: "negative",
          message: error.response?.data?.error || "Failed to add project",
        });
      }
    },
  },
})
</script>
