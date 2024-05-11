import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

// function isAuthenticated(_to, _from, next) {
//   if (localStorage.getItem(AUTH_TOKEN_KEY)) {
//     next();
//   } else {
//     next('/');
//   }
// }

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
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
    {
      path: '/test',
      component: () => import('@/views/TestView.vue'),
    },
  ],
});

export default router;
