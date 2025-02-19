<template>
  <q-layout view="hHh LpR fFf">
    <SideBar />

    <q-page-container class="bg-gray-50">
      <div class="p-6">
        <div class="flex justify-between items-center mb-6">
          <!-- Search Bar -->
          <q-input
            outlined
            dense
            rounded
            v-model="search"
            placeholder="Search here..."
            class="w-64 rounded-full shadow-sm"
          >
            <template v-slot:append>
              <Icon icon="mdi:magnify" class="text-gray-500" />
            </template>
          </q-input>

          <!-- Notifications & Profile -->
          <div class="flex items-center gap-4">
            <!-- Notifications Dropdown -->
            <q-btn round flat>
              <Icon icon="mdi:bell-outline" class="text-xl" />
              <q-badge floating color="red" v-if="notifications.length > 0" />
              <q-menu class="px-2 py-4 rounded-lg shadow-lg" fit anchor="bottom right" self="top end">
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
              <q-avatar size="36px" class="shadow-md">
                <img src="~/assets/profile.jpg" />
              </q-avatar>
              <q-menu class="rounded-lg shadow-lg" fit anchor="bottom right" self="top end">
                <q-list dense style="min-width: 150px">
                  <q-item clickable v-close-popup to="/profile">
                    <q-item-section avatar>
                      <Icon icon="mdi:account-outline" class="text-lg" />
                    </q-item-section>
                    <q-item-section>Profile</q-item-section>
                  </q-item>
                  <q-item clickable v-close-popup to="/settings">
                    <q-item-section avatar>
                      <Icon icon="mdi:cog-outline" class="text-lg" />
                    </q-item-section>
                    <q-item-section>Settings</q-item-section>
                  </q-item>
                  <q-separator />
                  <q-item clickable v-close-popup @click="logout">
                    <q-item-section avatar>
                      <Icon icon="mdi:logout-variant" class="text-lg text-red-500" />
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
import { Icon } from '@iconify/vue' // Import Iconify

const search = ref('')
const notifications = ref([
  { avatar: 'https://randomuser.me/api/portraits/men/5.jpg', message: 'New task assigned', time: '5 mins ago' },
  { avatar: 'https://randomuser.me/api/portraits/women/6.jpg', message: 'Meeting at 3 PM', time: '1 hour ago' },
  { avatar: 'https://randomuser.me/api/portraits/men/8.jpg', message: 'Project deadline tomorrow', time: '3 hours ago' }
])

const logout = () => {
  console.log('User logged out')
}
</script>

<style scoped>
/* Modern Styling for Dropdowns */
.q-menu {
  border-radius: 8px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
