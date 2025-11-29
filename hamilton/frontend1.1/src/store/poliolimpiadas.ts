import { defineStore } from 'pinia';

export const usePoliOlimpiadasStore = defineStore('poliolimpiadas', {
  state: () => {
    return {
      reload: 0
    };
  },
  persist: {
    key: 'perfil-poliolimpiadas-store'
  }
});
