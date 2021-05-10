import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Board from '../views/Board.vue'
import AddBoard from '../views/Board.vue'
import store from '../store'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/users/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/users/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/boards',
    name: 'AddBoard',
    component: AddBoard,
    beforeEnter(to, from, next) {
      if (store.state.isAuthenticated) {
        next()
      } else {
        next('/');
      }
    }
  },
  {
    path: '/boards/:id',
    name: 'Board',
    component: Board,
    beforeEnter(to, from, next) {
      if (store.state.isAuthenticated) {
        next()
      } else {
        next('/');
      }
    }
  },
]

const router = createRouter({
  linkActiveClass: 'is-active',
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

