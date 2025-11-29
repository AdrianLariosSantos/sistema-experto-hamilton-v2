import { defineStore } from 'pinia';

export const useAuthenticationStore = defineStore('authentication', {
  state: () => {
    return {
      isAuthenticated: null,
      authentication: []
    };
  },
  persist: {
    key: 'perfil-authentication-store'
  }
});
