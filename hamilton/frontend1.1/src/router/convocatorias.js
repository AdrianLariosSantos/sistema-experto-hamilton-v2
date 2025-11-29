export const convRoutes = [
  {
    path: '/convocatorias/poli-olimpiadas',
    name: 'convPoliOlimpiadas',
    component: () =>
      import('@/views/convocatorias/poli-olimpiadas/IndexPoliOlimpiadas.vue'),
    meta: {
      requiresAuth: true,
      layout: 'horizontal',
      pageTitle: 'Poli Olimpiadas 2022',
      breadcrumb: [
        {
          text: 'Convocatorias',
          to: '',
          active: false,
        },
        {
          text: 'Poli Olimpiadas',
          to: '',
          active: true,
        },
      ],
    }
  }
];
