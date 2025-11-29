<template>
  <div class="bg-gray-100">
    <div class="min-h-screen flex flex-col justify-center">
      <div class="flex-grow py-12 px-6 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
          <img
            class="mx-auto h-12 w-auto"
            src="@/assets/images/brand/logo-ssc.png"
            alt="Workflow"
          />
          <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Registra tu cuenta Mi Perfil
          </h2>
          <p class="mt-2 text-center text-sm text-gray-600">
            O
            {{ " " }}
            <a
              @click.prevent="router.push({ name: 'login' })"
              class="
                font-medium
                text-maincolor-600
                hover:text-blue-600
                cursor-pointer
              "
            >
              Inicia sesion si ya tienes una cuenta
            </a>
          </p>
        </div>

        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
          <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
            <form class="space-y-6" @submit.prevent="submit">
              <div>
                <label-form text="Corporación" class="text-left" />

                <div class="mt-1">
                  <select-input
                    v-model="form.corporacion_id"
                    :options="corporaciones"
                    width="max-w-3xl"
                    required
                  />
                  <span
                    v-show="errors.corporacion.length > 0"
                    class="mt-2 text-xs text-red-600"
                  >
                    <p
                      v-for="(error, i) in errors.corporacion"
                      :key="i"
                      class="tw-mb-0"
                    >
                      {{ error }}
                    </p>
                  </span>
                </div>
              </div>
              <div v-if="esPolicia">
                <label-form text="Numero de empleado" class="text-left" />

                <div class="mt-1">
                  <text-input
                    width="max-w-3xl"
                    :required="true"
                    v-model="form.numero_empleado"
                  />
                  <span
                    v-show="errors.numero_empleado.length > 0"
                    class="mt-2 text-xs text-red-600"
                  >
                    <p
                      v-for="(error, i) in errors.numero_empleado"
                      :key="i"
                      class="tw-mb-0"
                    >
                      {{ error }}
                    </p>
                  </span>
                </div>
              </div>
              <div v-if="esPolicia">
                <label-form text="CUIP" class="text-left" />

                <div class="mt-1">
                  <text-input
                    width="max-w-3xl"
                    :required="true"
                    v-model="form.cuip"
                  />
                  <span
                    v-show="errors.cuip.length > 0"
                    class="mt-2 text-xs text-red-600"
                  >
                    <p
                      v-for="(error, i) in errors.cuip"
                      :key="i"
                      class="tw-mb-0"
                    >
                      {{ error }}
                    </p>
                  </span>
                </div>
              </div>
              <div>
                <label-form text="Correo electrónico" class="text-left" />

                <div class="mt-1">
                  <text-input
                    width="max-w-3xl"
                    :required="true"
                    v-model="form.username"
                    type="email"
                  />
                  <span
                    v-show="errors.username.length > 0"
                    class="mt-2 text-xs text-red-600"
                  >
                    <p
                      v-for="(error, i) in errors.username"
                      :key="i"
                      class="tw-mb-0"
                    >
                      {{ error }}
                    </p>
                  </span>
                </div>
              </div>
              <div>
                <label-form text="Contraseña" class="text-left" />

                <div class="mt-1">
                  <text-input
                    width="max-w-3xl"
                    :required="true"
                    type="password"
                    v-model="form.password"
                  />
                  <span
                    v-show="errors.password.length > 0"
                    class="mt-2 text-xs text-red-600"
                  >
                    <p
                      v-for="(error, i) in errors.password"
                      :key="i"
                      class="tw-mb-0"
                    >
                      {{ error }}
                    </p>
                  </span>
                </div>
              </div>

              <div>
                <button
                  type="submit"
                  class="
                    w-full
                    flex
                    justify-center
                    py-2
                    px-4
                    border border-transparent
                    rounded-md
                    shadow-sm
                    text-sm
                    font-medium
                    text-white
                    bg-maincolor-600
                    hover:bg-maincolor-700
                    focus:outline-none
                    focus:ring-2
                    focus:ring-offset-2
                    focus:ring-maincolor-500
                  "
                >
                  Enviar
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <full-footer />
    </div>
    <modal-tailwind
      :open="open"
      @close="closeModal"
      title="Gracias"
      text="Se ha registrado tu cuenta con exito"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, watch, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import LabelForm from "@/components/forms/LabelForm.vue";
import TextInput from "@/components/forms/TextInput.vue";
import ModalTailwind from "@/components/common/ModalTailwind.vue";
import SelectInput from "../../../components/forms/SelectInput.vue";
import UsersService from "@/services/UsersService";
import FullFooter from "@/components/layouts/full/components/FullFooter.vue";

export default defineComponent({
  components: {
    LabelForm,
    TextInput,
    SelectInput,
    ModalTailwind,
    FullFooter,
  },
  setup() {
    const router = useRouter();

    const open = ref(false);

    const form = ref({
      username: null,
      password: null,
      cuip: null,
      corporacion_id: null,
      numero_empleado: null,
    });

    const errors = ref({
      username: [],
      password: [],
      cuip: [],
      corporacion: [],
      numero_empleado: [],
    });

    const defaultErrors = {
      username: [],
      password: [],
      cuip: [],
      corporacion: [],
      numero_empleado: [],
    };

    const defaultForm = {
      username: null,
      password: null,
      cuip: null,
      corporacion_id: null,
      numero_empleado: null,
    };

    const corporaciones = reactive([
      {
        id: 1,
        descripcion: "SSC Policía Preventiva",
      },
      {
        id: 2,
        descripcion: "SSC Policía Auxiliar",
      },
      {
        id: 3,
        descripcion: "SSC Policía Bancaria e Industrial",
      },
      {
        id: 5,
        descripcion: "Fiscalía General de Justicia de la CDMX",
      },
      {
        id: 6,
        descripcion: "Heroico Cuerpo de Bomberos de la CDMX",
      },
    ]);

    const corpPolicia = [1, 2, 3, 5];

    const esPolicia = computed(() =>
      corpPolicia.includes(form.value.corporacion_id)
    );

    function success() {
      open.value = true;
    }

    function resetForm() {
      Object.assign(form.value, defaultForm);
    }

    function submit() {
      const vm = this;
      Object.assign(errors.value, defaultErrors);
      UsersService.register(vm.form)
        .then(() => {
          success();
          resetForm();
        })
        .catch((error) => {
          const { response } = error;
          if (response.status === 400) {
            Object.assign(errors.value, response.data.data);
          }
        })
        .finally(() => {
          //
        });
    }

    function closeModal() {
      open.value = false;
      router.push({ name: "login" });
    }

    return {
      form,
      corporaciones,
      esPolicia,
      open,
      submit,
      errors,
      closeModal,
      router,
    };
  },
});
</script>
