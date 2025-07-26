import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'UploadResume',
      component: () => import('@/components/UploadResume.vue')
    },
    {
      path: '/jobs',
      name: 'Jobs',
      component: () => import('@/components/JobDescriptionForm.vue')
    },
  ],
})

export default router
