import { createWebHistory, createRouter } from 'vue-router';
import { useAuthenticationStore } from '@/store/authentication';
import { convRoutes } from './convocatorias';
import { acuerdosRoutes } from './acuerdos';
import { userRoutes } from './user';

const routes = [
  {
    path: '/',
    name: 'landing',
    component: () => import('@/views/landing/IndexLanding.vue'),
    meta: {
      requiresAuth: false,
      layout: 'full'
    }
  },
  // {
  //   path: '/registro',
  //   name: 'registro',
  //   component: () => import('@/views/auth/registro/IndexRegistro.vue'),
  //   meta: {
  //     requiresAuth: false,
  //     layout: 'full'
  //   }
  // },
  // {
  //   path: '/login',
  //   name: 'login',
  //   component: () => import('@/views/auth/login/IndexLogin.vue'),
  //   meta: {
  //     requiresAuth: false,
  //     layout: 'full'
  //   }
  // },
  // {
  //   path: '/main',
  //   name: 'main',
  //   component: () => import('@/views/dashboard/IndexDashboard.vue'),
  //   meta: {
  //     requiresAuth: true,
  //     layout: 'horizontal',
  //     pageTitle: 'Mi Perfil'
  //     // breadcrumb: [
  //     //   {
  //     //     text: 'Mi Perfil',
  //     //     active: true,
  //     //   },
  //     // ],
  //   }
  // },
  {
    path: '/maintenance',
    name: 'maintenance',
    component: () => import('@/views/static/UnderMaintenance.vue'),
    meta: {
      requiresAuth: false,
      layout: 'full',
      pageTitle: 'Mi Perfil'
      // breadcrumb: [
      //   {
      //     text: 'Mi Perfil',
      //     active: true,
      //   },
      // ],
    }
  },
  {
    path: '/:catchAll(.*)',
    redirect: 'maintenance'
  },
  // ...convRoutes,
  // ...acuerdosRoutes,
  // ...userRoutes
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  // const authenticationStore = useAuthenticationStore();  

  // if (to.meta.requiresAuth && !authenticationStore.isAuthenticated) {    
  //   return next({ name: 'login' });
  // }
  
  // if (authenticationStore.isAuthenticated && to.name === 'login') {
  //   return next({ name: 'main' });
  // }

  return next();
});

export default router;
