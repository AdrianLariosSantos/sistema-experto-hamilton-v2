import { defineStore } from 'pinia';

export const useNotificationStore = defineStore('notifications', {
  state: () => {
    return {
      show: false,
      variant: 'success',
      title: 'Titulo',
      message: 'Mensaje',
    };
  },
  persist: {
    key: 'perfil-notifications-store'
  }
});
