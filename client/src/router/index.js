import { createRouter, createWebHashHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
import Landing from '@/components/Landing.vue'
import CreateAccount from '@/components/CreateAccount.vue'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingView,
    children: [
      {
        path: 'landing',
        component: Landing
      },
      {
        path: 'create-account',
        component: CreateAccount
      }
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
