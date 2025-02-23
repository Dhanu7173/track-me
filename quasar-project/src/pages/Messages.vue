<template>
  <div class="tw-flex tw-h-[calc(100vh-120px)]">
    <!-- Contacts Sidebar -->
    <div class="tw-w-80 tw-bg-white tw-border-r">
      <div class="tw-p-4">
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
          class="text-grey-7 tw-rounded-xl tw-mx-4 tw-my-2"
        >
          <q-item-section avatar>
            <q-avatar>
              <img :src="contact.avatar" />
            </q-avatar>
          </q-item-section>

          <q-item-section class="text-grey-7">
            <q-item-label>{{ contact.name }}</q-item-label>
            <q-item-label caption class="text-grey-7">
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
    <div class="tw-flex-1 tw-flex tw-flex-col tw-bg-gray-50">
      <template v-if="selectedContact">
        <div class="tw-bg-white tw-p-4 tw-border-b tw-flex tw-items-center tw-gap-4">
          <q-avatar size="40px">
            <img :src="selectedContact.avatar" />
          </q-avatar>
          <div>
            <div class="tw-font-medium">{{ selectedContact.name }}</div>
            <div class="tw-text-sm tw-text-gray-500">
              {{ selectedContact.status }}
            </div>
          </div>
        </div>

        <div class="tw-flex-1 tw-p-4 tw-overflow-y-auto">
          <div
            v-for="message in messages"
            :key="message.id"
            :class="[
              'tw-max-w-[70%] tw-mb-4 tw-p-3 tw-rounded-lg',
              message.sent
                ? 'tw-ml-auto bg-primary tw-text-white'
                : 'tw-bg-white'
            ]"
          >
            {{ message.content }}
            <div
              :class="[
                'tw-text-xs tw-mt-1',
                message.sent
                  ? 'tw-text-blue-100'
                  : 'tw-text-gray-500'
              ]"
            >
              {{ message.time }}
            </div>
          </div>
        </div>

        <div class="tw-p-4 tw-bg-white tw-border-t">
          <div class="tw-flex tw-gap-2">
            <q-input
              v-model="newMessage"
              outlined
              dense
              placeholder="Type a message..."
              class="tw-flex-1"
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
        class="tw-flex-1 tw-flex tw-items-center tw-justify-center tw-text-gray-500"
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
      {
        id: 2,
        name: 'Pruthvi',
        avatar: 'https://randomuser.me/api/portraits/men/2.jpg',
        lastMessage: "Hey, ky kartoy?",
        time: '5m ago',
        unread: 2,
        status: 'Online'
      },
      {
        id: 3,
        name: 'ABCD',
        avatar: 'https://randomuser.me/api/portraits/men/3.jpg',
        lastMessage: "Hey, how's it going?",
        time: '5m ago',
        unread: 2,
        status: 'Online'
      },
      {
        id: 4,
        name: 'XYZW',
        avatar: 'https://randomuser.me/api/portraits/men/1.jpg',
        lastMessage: "Hey, how's it going?",
        time: '5m ago',
        unread: 2,
        status: 'Online'
      },
      {
        id: 5,
        name: 'Akash Melkeri',
        avatar: 'https://randomuser.me/api/portraits/men/5.jpg',
        lastMessage: "Hey, how's it going?",
        time: '5m ago',
        unread: 2,
        status: 'Online'
      }
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