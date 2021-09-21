import { createRouter, createWebHashHistory } from 'vue-router'
import Landing from '@/views/Landing.vue'
import Login from '@/components/Login.vue'
import CreateAccount from '@/components/CreateAccount.vue'
import Home from '@/views/UserHome.vue'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: Landing,
    children: [
      {
        path: '',
        component: Login
      },
      {
        path: 'create_account',
        component: CreateAccount
      }
    ]
  },
  {
    path: '/home/:username',
    name: 'Home',
    component: Home,
    props: true
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
