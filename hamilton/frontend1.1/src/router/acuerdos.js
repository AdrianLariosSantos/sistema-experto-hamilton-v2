export const acuerdosRoutes = [
  {
    path: '/acuerdos/notificaciones',
    name: 'acuerdoNotificaciones',
    component: () =>
      import('@/views/acuerdos/notificaciones/IndexAcuerdoNotificaciones.vue'),
    meta: {
      requiresAuth: true,
      layout: 'horizontal',
      pageTitle: 'Acuerdo 00/2022 ',
      breadcrumb: [
        {
          text: 'Acuerdos',
          to: '',
          active: false,
        },
        {
          text: 'Acuerdo 00/2022 ',
          to: '',
          active: true,
        },
      ],
    }
  }
];
