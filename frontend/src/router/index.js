import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import { AUTH_TOKEN_KEY } from '@/utils/constants';

function isAuthenticated(_to, _from, next) {
  if (localStorage.getItem(AUTH_TOKEN_KEY)) {
    next();
  } else {
    next('/login');
  }
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: {
        layout: 'EmptyLayout',
      },
    },
    {
      path: '/',
      name: 'home',
      component: HomeView,
      beforeEnter: isAuthenticated,
    },
    {
      path: '/details/:id',
      name: 'details',
      component: () => import('@/views/DetailsView.vue'),
      beforeEnter: isAuthenticated,
    },
    {
      path: '/404',
      name: 'not_found',
      component: () => import('@/views/ErrorView.vue'),
      meta: {
        layout: 'EmptyLayout',
      },
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/404',
    },
  ],
});

export default router;
