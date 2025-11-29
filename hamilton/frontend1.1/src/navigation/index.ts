// import carreraPolicial from './carrera-policial/index'

export const navigationMenu = [
  {
    title: 'Inicio',
    route: 'main',
    resource: 'index',
    action: 'view'
  },
  {
    title: 'Programas',
    route: 'convocatorias',
    resource: 'index',
    action: 'view',
    hasChildren: true,
    children: [
      {
        title: 'Actualizacion de domicilio',
        route: 'acuerdoNotificaciones',
        resource: 'index',
        icon: 'IdentificationIcon',
        iconForeground: 'text-orange-700',
        iconBackground: 'bg-orange-50',
        description:
          'De cumplimiento al acuerdo 00/2022, proporciona un domicilio para oir y recibir notificaciones.',
        action: 'view',
        featured: true,
      },
      {
        title: 'Poli Olimpiadas',
        route: 'convPoliOlimpiadas',
        resource: 'index',
        icon: 'StarIcon',
        iconForeground: 'text-blue-700',
        iconBackground: 'bg-blue-50',
        description:
        'Registrate tu participacion en las Poli Olimipiadas.',
        action: 'view',
        featured: false,
      },
      {
        title: 'Registro de Hechos Relevantes',
        route: 'landing',
        resource: 'index',
        icon: 'BookmarkIcon',
        iconForeground: 'text-green-700',
        iconBackground: 'bg-green-50',
        description:
          'Da a conocer acciones o hechos relavantes que crees deban ser reconocidas.',
        action: 'view',
        featured: false,
      },
      
    ]
  }
  //   ...carreraPolicial,
];
