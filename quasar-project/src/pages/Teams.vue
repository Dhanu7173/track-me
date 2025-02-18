<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex justify-between items-center">
      <h2 class="text-2xl font-bold">Teams</h2>
      <q-btn color="primary" icon="group_add" label="Create Team" @click="openCreateTeam(false)" />
    </div>

    <!-- Teams Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="team in teams"
        :key="team.id"
        class="bg-white rounded-lg shadow-sm p-6"
      >
        <div class="flex justify-between items-start mb-4">
          <div>
            <h3 class="text-lg font-semibold">{{ team.name }}</h3>
            <p class="text-gray-500">{{ team.description }}</p>
          </div>
          <q-btn-dropdown flat dense round>
            <q-list>
              <q-item clickable v-close-popup @click="openCreateTeam(true, team)">
                <q-item-section>Edit</q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="deleteTeam(team.id)">
                <q-item-section class="text-negative">Delete</q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
        </div>

        <!-- Team Members -->
        <div class="flex items-center gap-2 mb-4">
          <q-avatar v-for="member in team.members.slice(0, 3)" :key="member.id" size="32px">
            <img :src="member.avatar" />
          </q-avatar>
          <q-chip v-if="team.members.length > 3" size="sm" class="bg-gray-100">
            +{{ team.members.length - 3 }}
          </q-chip>
        </div>

        <div class="flex justify-between text-sm text-gray-500">
          <span>{{ team.projects }} Projects</span>
          <span>{{ team.tasks }} Tasks</span>
        </div>
      </div>
    </div>

    <!-- Create/Edit Team Dialog -->
    <q-dialog v-model="teamDialog">
      <q-card class="w-full max-w-lg bg-white rounded-lg shadow-lg p-6">
        <q-card-section class="flex justify-between items-center border-b pb-3">
          <h3 class="text-xl font-semibold text-gray-800">
            {{ editMode ? 'Edit Team' : 'Create Team' }}
          </h3>
          <q-btn flat dense icon="close" class="text-gray-500" @click="teamDialog = false" />
        </q-card-section>

        <q-card-section class="space-y-4">
          <q-input v-model="newTeam.name" label="Team Name" outlined dense class="w-full" />
          <q-input v-model="newTeam.description" label="Description" outlined dense class="w-full" />
          <q-input v-model="newTeam.projects" type="number" label="Projects" outlined dense class="w-full" />
          <q-input v-model="newTeam.tasks" type="number" label="Tasks" outlined dense class="w-full" />

          <!-- Team Members -->
          <div class="border-t pt-4">
            <h4 class="text-lg font-semibold">Team Members</h4>
            <div v-for="(member, index) in newTeam.members" :key="index" class="flex gap-2 items-center">
              <q-avatar size="32px">
                <img :src="member.avatar" alt="Team Member" />
              </q-avatar>
              <q-input v-model="member.name" label="Member Name" outlined dense class="flex-grow mt-1" />
              <q-btn icon="delete" flat color="red" @click="removeTeamMember(index)" />
            </div>
            <q-btn label="Add Team Member" class="mt-2" outline color="primary" @click="addTeamMember" />
          </div>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" @click="teamDialog = false" />
          <q-btn color="primary" :label="editMode ? 'Update Team' : 'Create Team'" @click="saveTeam" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { useQuasar } from 'quasar'

export default defineComponent({
  name: 'Teams',
  setup() {
    const $q = useQuasar()
    const teamDialog = ref(false)
    const editMode = ref(false)
    const teams = ref([])

    const newTeam = ref({
      id: 0,
      name: '',
      description: '',
      projects: 0,
      tasks: 0,
      members: [],
    })

    // Load teams from localStorage
    const loadTeams = () => {
      const savedTeams = localStorage.getItem('teams')
      if (savedTeams) {
        teams.value = JSON.parse(savedTeams)
      }
    }

    // Save teams to localStorage whenever teams change
    watch(teams, (newTeams) => {
      localStorage.setItem('teams', JSON.stringify(newTeams))
    }, { deep: true })

    // Open Dialog for New or Edit
    const openCreateTeam = (isEdit: boolean, team = null) => {
      editMode.value = isEdit
      if (isEdit && team) {
        newTeam.value = { ...team }
      } else {
        newTeam.value = {
          id: Date.now(),
          name: '',
          description: '',
          projects: 0,
          tasks: 0,
          members: [],
        }
      }
      teamDialog.value = true
    }

    // Save or Update Team
    const saveTeam = () => {
      if (!newTeam.value.name.trim()) return
      if (editMode.value) {
        const index = teams.value.findIndex(t => t.id === newTeam.value.id)
        if (index !== -1) {
          teams.value[index] = { ...newTeam.value }
        }
      } else {
        teams.value.push({ ...newTeam.value, id: Date.now() })
      }
      teamDialog.value = false
    }

    // Delete Team
    const deleteTeam = (id: number) => {
      $q.dialog({
        title: 'Confirm',
        message: 'Are you sure you want to delete this team?',
        cancel: true,
        persistent: true
      }).onOk(() => {
        teams.value = teams.value.filter(t => t.id !== id)
        $q.notify({ message: 'Team deleted successfully', color: 'positive' })
      })
    }

    // Generate random user avatar
    const getRandomAvatar = () => {
      return `https://randomuser.me/api/portraits/men/${Math.floor(Math.random() * 99) + 1}.jpg`
    }

    // Add and remove team members
    const addTeamMember = () => {
      newTeam.value.members.push({ name: '', avatar: getRandomAvatar() })
    }

    const removeTeamMember = (index: number) => {
      newTeam.value.members.splice(index, 1)
    }

    // Load teams on mount
    loadTeams()

    return {
      teams,
      teamDialog,
      editMode,
      newTeam,
      openCreateTeam,
      saveTeam,
      deleteTeam,
      addTeamMember,
      removeTeamMember,
    }
  },
})
</script>
