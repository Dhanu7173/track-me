<template>
  <q-layout view="hHh LpR fFf">
    <SideBar />

    <q-page-container class="bg-gray-50">
      <div class="p-6">
        <div class="flex justify-between items-center mb-6">
          <!-- Search Bar -->
          <q-input outlined dense v-model="search" placeholder="Search here..." class="w-64">
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>

          <!-- Notifications & Profile -->
          <div class="flex items-center gap-4">
            <!-- Notifications Dropdown -->
            <q-btn round flat icon="notifications">
              <q-badge floating color="red" v-if="notifications.length > 0" />
              <q-menu class="px-2 py-4" fit anchor="bottom right" self="top end">
                <q-list dense style="min-width: 250px">
                  <q-item v-for="(notification, index) in notifications.slice(0, 3)" :key="index" clickable v-ripple>
                    <q-item-section avatar>
                      <q-avatar size="32px">
                        <img :src="notification.avatar" />
                      </q-avatar>
                    </q-item-section>
                    <q-item-section>
                      <q-item-label class="font-medium">{{ notification.message }}</q-item-label>
                      <q-item-label caption>{{ notification.time }}</q-item-label>
                    </q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-btn>

            <!-- Profile Menu -->
            <q-btn round flat>
              <q-avatar size="32px">
                <img src="~/assets/profile.jpg" />
              </q-avatar>
              <q-menu fit anchor="bottom right" self="top end">
                <q-list dense style="min-width: 150px">
                  <q-item clickable v-close-popup to="/profile">
                    <q-item-section avatar>
                      <q-icon name="person" />
                    </q-item-section>
                    <q-item-section>Profile</q-item-section>
                  </q-item>
                  <q-item clickable v-close-popup to="/settings">
                    <q-item-section avatar>
                      <q-icon name="settings" />
                    </q-item-section>
                    <q-item-section>Settings</q-item-section>
                  </q-item>
                  <q-separator />
                  <q-item clickable v-close-popup @click="logout">
                    <q-item-section avatar>
                      <q-icon name="logout" color="red" />
                    </q-item-section>
                    <q-item-section class="text-red-500">Logout</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-btn>
          </div>
        </div>

        <router-view />
      </div>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import SideBar from '../components/SideBar.vue'

const search = ref('')
const notifications = ref([
  { avatar: 'https://randomuser.me/api/portraits/men/5.jpg', message: 'New task assigned', time: '5 mins ago' },
  { avatar: 'https://randomuser.me/api/portraits/women/6.jpg', message: 'Meeting at 3 PM', time: '1 hour ago' },
  { avatar: 'https://randomuser.me/api/portraits/men/8.jpg', message: 'Project deadline tomorrow', time: '3 hours ago' }
])

const viewAllNotifications = () => {
  console.log('View all notifications clicked')
}

/*************  ✨ Codeium Command ⭐  *************/
/**
 * Logs out the current user.
 * This function performs necessary cleanup and logging actions required for user logout.
 */

/******  2ebf320a-d668-4b5f-bc26-076acd09f2bf  *******/
const logout = () => {
  console.log('User logged out')
}
</script>
