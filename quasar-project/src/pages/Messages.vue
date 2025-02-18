<template>
  <div class="flex h-[calc(100vh-120px)]">
    <!-- Contacts Sidebar -->
    <div class="w-80 bg-white border-r">
      <div class="p-4">
        <q-input
          v-model="search"
          outlined
          dense
          placeholder="Search messages"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </div>

      <q-list separator>
        <q-item
          v-for="contact in filteredContacts"
          :key="contact.id"
          clickable
          :active="selectedContact?.id === contact.id"
          @click="selectContact(contact)"
          v-ripple
        >
          <q-item-section avatar>
            <q-avatar>
              <img :src="contact.avatar" />
            </q-avatar>
          </q-item-section>

          <q-item-section>
            <q-item-label>{{ contact.name }}</q-item-label>
            <q-item-label caption>
              {{ contact.lastMessage }}
            </q-item-label>
          </q-item-section>

          <q-item-section side>
            <div class="text-grey-6 text-caption">
              {{ contact.time }}
            </div>
            <q-badge
              v-if="contact.unread"
              color="primary"
              floating
            >
              {{ contact.unread }}
            </q-badge>
          </q-item-section>
        </q-item>
      </q-list>
    </div>

    <!-- Chat Area -->
    <div class="flex-1 flex flex-col bg-gray-50">
      <template v-if="selectedContact">
        <div class="bg-white p-4 border-b flex items-center gap-4">
          <q-avatar size="40px">
            <img :src="selectedContact.avatar" />
          </q-avatar>
          <div>
            <div class="font-medium">{{ selectedContact.name }}</div>
            <div class="text-sm text-gray-500">
              {{ selectedContact.status }}
            </div>
          </div>
        </div>

        <div class="flex-1 p-4 overflow-y-auto">
          <div
            v-for="message in messages"
            :key="message.id"
            :class="[
              'max-w-[70%] mb-4 p-3 rounded-lg',
              message.sent
                ? 'ml-auto bg-primary text-white'
                : 'bg-white'
            ]"
          >
            {{ message.content }}
            <div
              :class="[
                'text-xs mt-1',
                message.sent
                  ? 'text-blue-100'
                  : 'text-gray-500'
              ]"
            >
              {{ message.time }}
            </div>
          </div>
        </div>

        <div class="p-4 bg-white border-t">
          <div class="flex gap-2">
            <q-input
              v-model="newMessage"
              outlined
              dense
              placeholder="Type a message..."
              class="flex-1"
              @keyup.enter="sendMessage"
            />
            <q-btn
              color="primary"
              icon="send"
              round
              @click="sendMessage"
            />
          </div>
        </div>
      </template>

      <div
        v-else
        class="flex-1 flex items-center justify-center text-gray-500"
      >
        Select a conversation to start messaging
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue'

export default defineComponent({
  name: 'Messages',
  
  setup() {
    const search = ref('')
    const newMessage = ref('')
    const selectedContact = ref(null)

    const contacts = ref([
      {
        id: 1,
        name: 'John Doe',
        avatar: 'https://randomuser.me/api/portraits/men/1.jpg',
        lastMessage: "Hey, how's it going?",
        time: '5m ago',
        unread: 2,
        status: 'Online'
      },
      // Add more contacts...
    ])

    const messages = ref([
      {
        id: 1,
        content: 'Hi there!',
        time: '10:00 AM',
        sent: false
      },
      {
        id: 2,
        content: 'Hello! How are you?',
        time: '10:02 AM',
        sent: true
      },
      // Add more messages...
    ])

    const filteredContacts = computed(() => {
      return contacts.value.filter(contact =>
        contact.name.toLowerCase().includes(search.value.toLowerCase())
      )
    })

    const selectContact = (contact: any) => {
      selectedContact.value = contact
    }

    const sendMessage = () => {
      if (!newMessage.value.trim()) return

      messages.value.push({
        id: Date.now(),
        content: newMessage.value,
        time: new Date().toLocaleTimeString([], { 
          hour: '2-digit', 
          minute: '2-digit'
        }),
        sent: true
      })

      newMessage.value = ''
    }

    return {
      search,
      newMessage,
      selectedContact,
      contacts,
      messages,
      filteredContacts,
      selectContact,
      sendMessage
    }
  }
})
</script>