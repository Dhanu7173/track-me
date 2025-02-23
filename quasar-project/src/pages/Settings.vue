<template>
  <div class="tw-space-y-6">
    <h2 class="tw-text-2xl tw-font-bold">Settings</h2>

    <div class="tw-bg-white tw-rounded-lg tw-shadow-sm">
      <div class="tw-p-6 tw-border-b">
        <h3 class="tw-text-lg tw-font-semibold tw-mb-4">Profile Settings</h3>
        
        <div class="tw-flex tw-items-center tw-gap-6">
          <q-avatar size="100px">
            <img :src="profile.avatar" />
            <q-btn
              round
              color="primary"
              icon="edit"
              size="sm"
              class="tw-absolute tw-bottom-0 tw-right-0"
              @click="uploadAvatar"
            />
          </q-avatar>

          <div class="tw-flex-1 tw-grid tw-grid-cols-2 tw-gap-4">
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

      <div class="tw-p-6 tw-border-b">
        <h3 class="tw-text-lg tw-font-semibold tw-mb-4">Notifications</h3>
        
        <div class="tw-space-y-4">
          <div
            v-for="(setting, index) in notificationSettings"
            :key="index"
            class="tw-flex tw-items-center tw-justify-between"
          >
            <div>
              <div class="tw-font-medium">{{ setting.title }}</div>
              <div class="tw-text-sm tw-text-gray-500">
                {{ setting.description }}
              </div>
            </div>
            <q-toggle v-model="setting.enabled" color="primary" />
          </div>
        </div>
      </div>

      <div class="tw-p-6 tw-border-b">
        <h3 class="tw-text-lg tw-font-semibold tw-mb-4">Theme</h3>
        
        <div class="tw-flex tw-items-center tw-gap-4">
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

      <div class="tw-p-6 tw-flex tw-justify-end tw-gap-4">
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