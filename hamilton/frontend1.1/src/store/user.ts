import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => {
    return {
      data: '',
      userLogged: false,
      profile: '',
      assigned: 0,
      permissions: [],
    };
  },
  persist: {
    key: 'perfil-user-store'
  }
});
