<template>
  <div class="tw-space-y-6">
    <!-- Welcome Banner -->
    <WelcomeBanner />

    <!-- Project Grid -->
    <div class="tw-grid tw-grid-cols-1 md:tw-grid-cols-2 lg:tw-grid-cols-3 tw-gap-6">
      <ProjectCard v-for="project in projects" :key="project.id" :project="project" />
    </div>

    <!-- Overall Projects Stats -->
    <div class="tw-bg-white tw-rounded-lg tw-p-6 tw-shadow-2xl">
      <div class="tw-flex tw-justify-between tw-items-center tw-mb-4">
        <h3 class="tw-text-lg tw-font-semibold">Overall Projects Stats</h3>
        <q-select
          v-model="timeRange"
          :options="['Last 7 Days', 'Last 30 Days', 'Last 3 Months']"
          dense
          outlined
          class="tw-w-40"
        />
      </div>
      <StatsChart />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import WelcomeBanner from '../components/WelcomeBanner.vue'
import ProjectCard from '../components/ProjectCard.vue'
import StatsChart from '../components/StatsChart.vue'

const timeRange = ref('Last 7 Days')

const projects = ref([
  {
    id: 1,
    title: 'Website Redesign',
    type: 'Ongoing Project',
    description: 'Redesign the company website with a modern and user-friendly interface.',
    progress: 75,
    status: 'In Progress',
    startDate: '2024-01-10',
    endDate: '2024-03-20',
    dueDate: '2024-03-20',
    team: [
      { id: 1, name: 'John Doe', avatar: 'https://randomuser.me/api/portraits/men/1.jpg' },
      { id: 2, name: 'Jane Smith', avatar: 'https://randomuser.me/api/portraits/women/1.jpg' },
      { id: 3, name: 'Alice Johnson', avatar: 'https://randomuser.me/api/portraits/women/2.jpg' },
    ],
    tasks: [
      { id: 1, name: 'Wireframe Design', status: 'Completed' },
      { id: 2, name: 'UI/UX Prototyping', status: 'In Progress' },
      { id: 3, name: 'Backend API Development', status: 'Pending' },
    ],
  },
  {
    id: 2,
    title: 'Mobile App Development',
    type: 'Ongoing Project',
    description: 'Develop a cross-platform mobile application for Android and iOS.',
    progress: 40,
    status: 'In Progress',
    startDate: '2024-02-05',
    endDate: '2024-06-15',
    dueDate: '2024-06-15',
    team: [
      { id: 4, name: 'Emily Brown', avatar: 'https://randomuser.me/api/portraits/women/3.jpg' },
      { id: 5, name: 'David Lee', avatar: 'https://randomuser.me/api/portraits/men/4.jpg' },
    ],
    tasks: [
      { id: 4, name: 'UI Design', status: 'Completed' },
      { id: 5, name: 'Frontend Development', status: 'In Progress' },
      { id: 6, name: 'API Integration', status: 'Pending' },
    ],
  },
  {
    id: 3,
    title: 'E-commerce Platform',
    type: 'New Project',
    description: 'Build a scalable e-commerce platform with payment integration.',
    progress: 20,
    status: 'Pending',
    startDate: '2024-03-01',
    endDate: '2024-09-30',
    dueDate: '2024-09-30',
    team: [
      { id: 6, name: 'Sophia Wilson', avatar: 'https://randomuser.me/api/portraits/women/4.jpg' },
      { id: 7, name: 'Michael Scott', avatar: 'https://randomuser.me/api/portraits/men/5.jpg' },
      { id: 8, name: 'Ryan Howard', avatar: 'https://randomuser.me/api/portraits/men/6.jpg' },
    ],
    tasks: [
      { id: 7, name: 'Database Architecture', status: 'In Progress' },
      { id: 8, name: 'Payment Gateway Setup', status: 'Pending' },
      { id: 9, name: 'Admin Panel Development', status: 'Pending' },
    ],
  },
  {
    id: 4,
    title: 'AI Chatbot Integration',
    type: 'Ongoing Project',
    description: 'Implement an AI-powered chatbot for customer service automation.',
    progress: 60,
    status: 'In Progress',
    startDate: '2024-01-20',
    endDate: '2024-04-15',
    dueDate: '2024-04-15',
    team: [
      { id: 9, name: 'Olivia Taylor', avatar: 'https://randomuser.me/api/portraits/women/5.jpg' },
      { id: 10, name: 'Ethan Carter', avatar: 'https://randomuser.me/api/portraits/men/7.jpg' },
    ],
    tasks: [
      { id: 10, name: 'Chatbot Training', status: 'Completed' },
      { id: 11, name: 'NLP Model Fine-tuning', status: 'In Progress' },
      { id: 12, name: 'User Testing & Deployment', status: 'Pending' },
    ],
  },
  {
    id: 5,
    title: 'Cloud Migration',
    type: 'Completed Project',
    description: 'Migrate all company data and applications to a secure cloud environment.',
    progress: 100,
    status: 'Completed',
    startDate: '2023-11-01',
    endDate: '2024-02-15',
    dueDate: '2024-02-15',
    team: [
      { id: 11, name: 'Lucas Martin', avatar: 'https://randomuser.me/api/portraits/men/8.jpg' },
      { id: 12, name: 'Isabella Harris', avatar: 'https://randomuser.me/api/portraits/women/6.jpg' },
    ],
    tasks: [
      { id: 13, name: 'Cloud Infrastructure Setup', status: 'Completed' },
      { id: 14, name: 'Data Migration', status: 'Completed' },
      { id: 15, name: 'Security Audits', status: 'Completed' },
    ],
  },
    {
        id: 6,
        title: 'Social Media Marketing',
        type: 'Ongoing Project',
        description: 'Create and manage social media campaigns for brand promotion.',
        progress: 80,
        status: 'In Progress',
        startDate: '2024-02-10',
        endDate: '2024-04-30',
        dueDate: '2024-04-30',
        team: [
        { id: 13, name: 'Ava Davis', avatar: 'https://randomuser.me/api/portraits/women/7.jpg' },
        { id: 14, name: 'James Wilson', avatar: 'https://randomuser.me/api/portraits/men/9.jpg' },
        ],
        tasks: [
        { id: 16, name: 'Campaign Planning', status: 'Completed' },
        { id: 17, name: 'Content Creation', status: 'In Progress' },
        { id: 18, name: 'Performance Analysis', status: 'Pending' },
        ],
    },
])
</script>
