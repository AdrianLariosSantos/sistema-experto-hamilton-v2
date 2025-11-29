import { defineStore } from 'pinia';

export const useDataStore = defineStore('datos', {
  state: () => {
    return {
      reload: 0
    };
  },
  persist: {
    key: 'perfil-datos-store'
  }
});
