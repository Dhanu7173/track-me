<template>
  <div class="tw-space-y-6">
    <!-- Page Header -->
    <div class="tw-flex tw-justify-between tw-items-center">
      <h2 class="tw-text-2xl tw-font-bold">Teams</h2>
      <q-btn color="primary" icon="group_add" label="Create Team" @click="openCreateTeam(false)" />
    </div>

    <!-- Teams Grid -->
    <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-2 lg:tw-grid-cols-3 tw-gap-6">
      <div
        v-for="team in teams"
        :key="team.id"
        class="tw-bg-white tw-rounded-lg tw-shadow-sm tw-p-6"
      >
        <div class="tw-flex tw-justify-between tw-items-start tw-mb-4">
          <div>
            <h3 class="tw-text-lg tw-font-semibold">{{ team.name }}</h3>
            <p class="tw-text-gray-500">{{ team.description }}</p>
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
        <div class="tw-flex tw-items-center tw-gap-2 tw-mb-4">
          <q-avatar v-for="member in team.members.slice(0, 3)" :key="member.id" size="32px">
            <img :src="member.avatar" />
          </q-avatar>
          <q-chip v-if="team.members.length > 3" size="sm" class="tw-bg-gray-100">
            +{{ team.members.length - 3 }}
          </q-chip>
        </div>

        <div class="tw-flex tw-justify-between tw-text-sm tw-text-gray-500">
          <span>{{ team.projects }} Projects</span>
          <span>{{ team.tasks }} Tasks</span>
        </div>
      </div>
    </div>

    <!-- Create/Edit Team Dialog -->
    <q-dialog v-model="teamDialog">
      <q-card class="tw-w-full tw-max-w-lg tw-bg-white tw-rounded-lg tw-shadow-lg tw-p-6">
        <q-card-section class="tw-flex tw-justify-between tw-items-center tw-border-b tw-pb-3">
          <h3 class="tw-text-xl tw-font-semibold tw-text-gray-800">
            {{ editMode ? 'Edit Team' : 'Create Team' }}
          </h3>
          <q-btn flat dense icon="close" class="tw-text-gray-500" @click="teamDialog = false" />
        </q-card-section>

        <q-card-section class="tw-space-y-4">
          <q-input v-model="newTeam.name" label="Team Name" outlined dense class="tw-w-full" />
          <q-input v-model="newTeam.description" label="Description" outlined dense class="tw-w-full" />
          <q-input v-model="newTeam.projects" type="number" label="Projects" outlined dense class="tw-w-full" />
          <q-input v-model="newTeam.tasks" type="number" label="Tasks" outlined dense class="tw-w-full" />

          <!-- Team Members -->
          <div class="tw-border-t tw-pt-4">
            <h4 class="tw-text-lg tw-font-semibold">Team Members</h4>
            <div v-for="(member, index) in newTeam.members" :key="index" class="tw-flex tw-gap-2 tw-items-center">
              <q-avatar size="32px">
                <img :src="member.avatar" alt="Team Member" />
              </q-avatar>
              <q-input v-model="member.name" label="Member Name" outlined dense class="tw-flex-grow tw-mt-1" />
              <q-btn icon="delete" flat color="red" @click="removeTeamMember(index)" />
            </div>
            <q-btn label="Add Team Member" class="tw-mt-2" outline color="primary" @click="addTeamMember" />
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
