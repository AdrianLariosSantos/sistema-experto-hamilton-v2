<template>
  <div>
    <form @submit.prevent="validarToken">
      <div class="space-y-8 divide-y divide-gray-200">
        <div>
          <div>
            <h3 class="text-md leading-6 font-medium text-gray-900">
              Valida tú correo electrónico
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Te enviamos un correo con un código de 5 dígitos al correo que
              ingresaste para validar que existe, copia y pega aqui ese codigo
              para validar tu direccion de correo y puedas descargar tu
              comprobante.
            </p>
          </div>

          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <div class="sm:col-span-4">
              <label-form text="Token" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  v-model="token"
                  maxlength="5"
                />
              </div>
            </div>
            <div class="sm:col-span-4">
              <i-button class="mt-8" type="submit" variant="maincolor"
                >Validar correo</i-button
              >
            </div>
          </div>
        </div>
      </div>
    </form>
    <modal-tailwind
      :open="open"
      @close="onCloseModal"
      :type="modalType"
      :title="modalTitle"
      :text="modalText"
    />
  </div>
</template>
<script lang="ts">
import { defineComponent, ref } from "vue";
import IButton from "@/components/common/IButton.vue";
import DatosService from "@/services/datos/DatosService";
import ModalTailwind from "@/components/common/ModalTailwind.vue";
import {useDataStore} from '@/store/datos'

export default defineComponent({
  emits: ["saved"],
  components: {
    IButton,
    ModalTailwind,
  },
  setup(props, { emit }) {
    const token = ref(null);
    const open = ref(false);
    const modalType = ref("success");
    const modalTitle = ref("¡Muchas Gracias!");
    const modalText = ref("Se há validado tú correo con éxito.");
    const store = useDataStore()

    function validarToken() {
      DatosService.validarCorreoElectronico({ token: token.value })
        .then((response) => {
          console.log(response);

          success();
        })
        .catch((error) => {
          console.log(error);
        });
    }

    function success() {
      modalType.value = "success";
      modalTitle.value = "¡Muchas Gracias!";
      modalText.value = "Se há validado tú correo con éxito.";
      open.value = true;
    }

    function errorMsg() {
      modalType.value = "error";
      modalTitle.value = "Ha ocurrido un error";
      modalText.value = "Revisa los datos ingresados y Vuelve a intentarlo";
      open.value = true;
    }

    function onCloseModal() {
      open.value = false;
      emitReloadComponents();

      console.log("onCloseModal");
    }

    function emitReloadComponents() {
      store.reload++
    }

    return {
      token,
      open,
      modalType,
      modalTitle,
      modalText,
      success,
      errorMsg,
      validarToken,
      onCloseModal,
      store
    };
  },
});
</script>
