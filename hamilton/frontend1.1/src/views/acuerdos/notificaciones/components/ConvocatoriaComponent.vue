<template>
  <div>
    <div id="texto-principal-conv" class="">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
      veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
      commodo consequat.
    </div>
    <div id="contenido-conv" class="text-center flex justify-center mt-5">
      <img src="https://via.placeholder.com/300" alt="" />
    </div>
    <div id="texto-principal-conv" class="mt-5">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
      veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
      commodo consequat.
    </div>
    <div class="mt-10 text-center">
      <i-button @click="goToRegistroTab">Iniciar registro</i-button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import IButton from "@/components/common/IButton.vue";
export default defineComponent({
  emits: ["changeToRegistro"],
  components: {
    IButton,
  },
  setup(props, { emit }) {
    function goToRegistroTab() {
      emit("changeToRegistro", { id: 2 });
    }
    return { goToRegistroTab };
  },
});
</script>
