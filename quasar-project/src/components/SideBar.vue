<template>
  <q-drawer
    v-model="leftDrawerOpen"
    show-if-above
    :width="260"
    class="tw-bg-sidebar tw-text-white tw-rounded-r-lg tw-shadow-lg"
  >
    <div class="tw-p-4">
      <!-- Logo Section -->
      <div class="tw-flex tw-items-center tw-gap-3 tw-mb-8">
        <img src="~/assets/logo1.png" alt="Tasker" class="tw-h-12 tw-rounded-md tw-shadow-sm" />
        <!-- <span class="tw-text-xl tw-font-bold tw-tracking-wide tw-text-white">Track Me</span> -->
      </div>

      <!-- Menu List -->
      <q-list>
        <q-item
          v-for="item in menuItems"
          :key="item.label"
          :to="item.route"
          clickable
          v-ripple
          class="menu-item tw-mt-2"
          :class="{ 'tw-bg-primary tw-text-white tw-rounded-lg tw-shadow-md': isActive(item.route) }"
        >
          <q-item-section avatar>
            <Icon :icon="item.icon" class="tw-text-lg tw-text-white" />
          </q-item-section>
          <q-item-section class="tw-text-white">
            {{ item.label }}
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </q-drawer>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { Icon } from '@iconify/vue' // Import Iconify

const leftDrawerOpen = ref(true)
const route = useRoute()

const menuItems = [
  { label: 'Dashboard', icon: 'material-symbols:dashboard-outline', route: '/' },
  { label: 'Projects', icon: 'carbon:folder', route: '/projects' },
  { label: 'My Tasks', icon: 'mdi:clipboard-list-outline', route: '/tasks' },
  { label: 'Activity', icon: 'mdi:chart-line', route: '/activity' },
  { label: 'Teams', icon: 'mdi:account-group-outline', route: '/teams' },
  { label: 'Messages', icon: 'mdi:message-outline', route: '/messages' },
  { label: 'Settings', icon: 'mdi:cog-outline', route: '/settings' },
]

// Function to check if the menu item is active
const isActive = (path: string) => {
  return computed(() => route.path.startsWith(path)).value
}
</script>

<style scoped lang="scss">
/* Sidebar Background */
.bg-sidebar {
  background: linear-gradient(135deg, #1e293b 0%, #111827 100%);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}

/* Menu Item Hover & Active Effects */
.menu-item {
  transition: all 0.3s tw-ease-in-out;
  padding: 10px 15px;
  border-radius: 8px;
}

.menu-item:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateX(4px);
}

/* Gradient Text for Branding */
.text-gradient {
  background: linear-gradient(45deg, #38bdf8, #9333ea);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
