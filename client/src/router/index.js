import { createRouter, createWebHashHistory } from 'vue-router'
import store from '@/store/index.js';
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
    props: true,
    beforeEnter: (to, from, next) => {
      if(store.state.logged_in_user == null) {
          next(false);
      } else {
          next();
      }
  }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
