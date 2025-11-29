<template>
  <div class="bg-gray-100">
    <div class="h-screen flex flex-col justify-center py-12 px-6 sm:px-6 lg:px-8 max-w-2xl mx-auto">
      <div class="flex items-center sm:mx-auto sm:w-full sm:max-w-md justify-center">
        <img
          class=" h-12 w-auto"
          src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
          alt="Workflow"
        />
        <span class="text-center ml-5 text-3xl font-extrabold text-gray-900">
          Mi Perfil
        </span>
      </div>
      <div class=" text-center">
        <p class="mt-2 text-5xl md:text-6xl font-extrabold text-gray-700">
          Ésta opción aun no se encuentra disponible
        </p>
        <p class="mt-5">Regresa de vez en cuando para verificar la disponibilidad.</p>
        <p class="mt-10 text-blue-500 hover:underline font-semibold"><a href="/main" class="">Regresar al inicio</a></p>
      </div>

    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useRouter, RouterLink } from "vue-router";
import LabelForm from "@/components/forms/LabelForm.vue";
import TextInput from "@/components/forms/TextInput.vue";
import AlertCard from "@/components/common/AlertCard.vue";
import { XCircleIcon } from "@heroicons/vue/solid";

export default defineComponent({
  components: {
    LabelForm,
    TextInput,
    RouterLink,
    AlertCard,
    XCircleIcon,
  },
  setup() {
    const router = useRouter();

    return {
      open,
      router,
    };
  },
});
</script>
