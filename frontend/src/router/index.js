import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Board from '../views/Board.vue'


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
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  {
    path: '/boards/:id',
    name: 'Board',
    component: Board
  },
  // {
  //   path: '/boards',
  //   name: 'Board',
  //   component: Board
  // },
]

const router = createRouter({
  linkActiveClass: 'is-active',
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
