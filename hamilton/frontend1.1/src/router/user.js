export const userRoutes = [
    {
      path: '/usuario/perfil',
      name: 'usuarioPerfil',
      component: () =>
        import('@/views/user/perfil/IndexPerfil.vue'),
      meta: {
        requiresAuth: true,
        layout: 'horizontal',
        pageTitle: 'Detalles de tu Perfil',

      }
    }
  ];
  