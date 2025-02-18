<template>
  <div class="space-y-6">
    <h2 class="text-2xl font-bold">Settings</h2>

    <div class="bg-white rounded-lg shadow-sm">
      <div class="p-6 border-b">
        <h3 class="text-lg font-semibold mb-4">Profile Settings</h3>
        
        <div class="flex items-center gap-6">
          <q-avatar size="100px">
            <img :src="profile.avatar" />
            <q-btn
              round
              color="primary"
              icon="edit"
              size="sm"
              class="absolute bottom-0 right-0"
              @click="uploadAvatar"
            />
          </q-avatar>

          <div class="flex-1 grid grid-cols-2 gap-4">
            <q-input
              v-model="profile.firstName"
              label="First Name"
              outlined
              dense
            />
            <q-input
              v-model="profile.lastName"
              label="Last Name"
              outlined
              dense
            />
            <q-input
              v-model="profile.email"
              label="Email"
              outlined
              dense
              type="email"
            />
            <q-input
              v-model="profile.phone"
              label="Phone"
              outlined
              dense
            />
          </div>
        </div>
      </div>

      <div class="p-6 border-b">
        <h3 class="text-lg font-semibold mb-4">Notifications</h3>
        
        <div class="space-y-4">
          <div
            v-for="(setting, index) in notificationSettings"
            :key="index"
            class="flex items-center justify-between"
          >
            <div>
              <div class="font-medium">{{ setting.title }}</div>
              <div class="text-sm text-gray-500">
                {{ setting.description }}
              </div>
            </div>
            <q-toggle v-model="setting.enabled" color="primary" />
          </div>
        </div>
      </div>

      <div class="p-6 border-b">
        <h3 class="text-lg font-semibold mb-4">Theme</h3>
        
        <div class="flex items-center gap-4">
          <q-btn
            v-for="theme in themes"
            :key="theme.name"
            :label="theme.name"
            :color="selectedTheme === theme.name ? 'primary' : 'grey-3'"
            :text-color="selectedTheme === theme.name ? 'white' : 'black'"
            @click="selectedTheme = theme.name"
            padding="sm lg"
          />
        </div>
      </div>

      <div class="p-6 flex justify-end gap-4">
        <q-btn flat label="Cancel" color="grey" />
        <q-btn
          color="primary"
          label="Save Changes"
          @click="saveSettings"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useQuasar } from 'quasar'

export default defineComponent({
  name: 'Settings',
  
  setup() {
    const $q = useQuasar()
    
    const profile = ref({
      avatar: 'https://randomuser.me/api/portraits/men/1.jpg',
      firstName: 'John',
      lastName: 'Doe',
      email: 'john.doe@example.com',
      phone: '+1 234 567 890'
    })

    const notificationSettings = ref([
      {
        title: 'Email Notifications',
        description: 'Receive email notifications for important updates',
        enabled: true
      },
      {
        title: 'Push Notifications',
        description: 'Receive push notifications on your device',
        enabled: true
      },
      {
        title: 'Task Reminders',
        description: 'Get reminded about upcoming and overdue tasks',
        enabled: true
      }
    ])

    const themes = [
      { name: 'Light' },
      { name: 'Dark' },
      { name: 'System' }
    ]

    const selectedTheme = ref('Light')

    const uploadAvatar = () => {
      // Implement avatar upload
    }

    const saveSettings = () => {
      $q.notify({
        message: 'Settings saved successfully',
        color: 'positive'
      })
    }

    return {
      profile,
      notificationSettings,
      themes,
      selectedTheme,
      uploadAvatar,
      saveSettings
    }
  }
})
</script>