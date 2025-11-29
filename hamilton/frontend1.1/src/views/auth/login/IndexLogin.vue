<template>
  <div class="bg-gray-100">
    <div class="min-h-screen flex flex-col justify-center">
      <div class="flex-grow py-12 px-6 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md ">
          <img
            class="mx-auto h-14 w-auto"
            src="@/assets/images/brand/logo-ssc.png"
            alt="Workflow"
          />
          <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Entra a tu cuenta Mi Perfil
          </h2>
          <p class="mt-2 text-center text-sm text-gray-600">
            O
            <a
              @click.prevent="router.push({ name: 'registro' })"
              class="
                font-medium
                text-maincolor-600
                hover:text-blue-600
                cursor-pointer
              "
            >
              Registra una cuenta nueva
            </a>
          </p>
        </div>

        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
          <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
            <form class="space-y-6" @submit.prevent="submit">
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

              <alert-card v-show="errors.non_field_errors.length > 0">
                <div class="flex">
                  <div class="flex-shrink-0">
                    <XCircleIcon
                      class="h-5 w-5 text-red-400"
                      aria-hidden="true"
                    />
                  </div>
                  <div class="ml-3">
                    <h3 class="text-sm font-medium text-red-800">Alerta</h3>
                    <div class="mt-2 text-sm text-red-700">
                      <ul role="list" class="list-disc pl-5 space-y-1">
                        <li
                          class="text-xs"
                          v-for="(error, i) in errors.non_field_errors"
                          :key="i"
                        >
                          {{ error }}
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </alert-card>

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
                  Entrar
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <full-footer />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, watch, computed } from "vue";
import { useRouter, useRoute, RouterLink } from "vue-router";
import LabelForm from "@/components/forms/LabelForm.vue";
import TextInput from "@/components/forms/TextInput.vue";
import AlertCard from "@/components/common/AlertCard.vue";
import UsersService from "@/services/UsersService";
import { useAuthenticationStore } from "@/store/authentication";
import { useUserStore } from "@/store/user";
import { XCircleIcon } from "@heroicons/vue/solid";
import FullFooter from "@/components/layouts/full/components/FullFooter.vue";

export default defineComponent({
  components: {
    LabelForm,
    TextInput,
    RouterLink,
    AlertCard,
    XCircleIcon,
    FullFooter,
  },
  setup() {
    const router = useRouter();
    const isLoading = ref(false);
    const authStore = useAuthenticationStore();
    const userStore = useUserStore();

    const form = ref({
      username: null,
      password: null,
    });

    const errors = ref({
      username: [],
      password: [],
      non_field_errors: [],
    });

    const defaultErrors = {
      username: [],
      password: [],
      non_field_errors: [],
    };

    const defaultForm = {
      username: null,
      password: null,
    };

    function submit() {
      const vm = this;
      isLoading.value = true;
      errors.value = { ...defaultErrors };
      UsersService.login(vm.form)
        .then((response) => {
          setAuthenticationData(response.data);
          router.push({ name: "main" });
        })
        .catch((error) => {
          console.log(error);

          const { response } = error;

          if (response.status === 400) {
            Object.assign(errors.value, response.data);
          }
        })
        .finally(() => {
          isLoading.value = false;
        });
    }

    function setAuthenticationData(data) {
      console.log("set data");

      authStore.isAuthenticated = true;
      authStore.authentication = data.token;
      userStore.data = data.user;
      userStore.userLogged = true;
      userStore.permissions = data.permissions;
    }

    return {
      form,
      open,
      submit,
      errors,
      router,
      userStore,
      authStore,
    };
  },
});
</script>
