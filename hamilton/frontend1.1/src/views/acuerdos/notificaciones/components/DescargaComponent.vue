<template>
  <div>
    <div class="space-y-8 divide-y divide-gray-200">
      <div>
        <div>
          <h3 class="text-md leading-6 font-medium text-gray-900">
            Descarga tu Comprobante
          </h3>
          <p class="mt-1 text-sm text-gray-500">
            Recuerda que este comprobante es requisito para tramites internos,
            con antiguedad no mayor a 1 año.
          </p>
        </div>

        <div class="mt-5">
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            <ul
              role="list"
              class="border border-gray-200 rounded-md divide-y divide-gray-200"
            >
              <li
                class="pl-3 pr-4 py-3 flex items-center justify-between text-sm"
              >
                <div class="w-0 flex-1 flex items-center">
                  <hero-icon
                    icon="PaperClipIcon"
                    class="flex-shrink-0 h-5 w-5 text-gray-400"
                  ></hero-icon>
                  <span class="ml-2 flex-1 w-0 truncate">
                    {{ data.cuip }}
                  </span>
                </div>
                <div class="ml-4 flex-shrink-0 flex space-x-4">
                  <button
                    @click="downloadComprobante"
                    type="button"
                    class="
                      bg-white
                      rounded-md
                      font-medium
                      text-maincolor-500
                      hover:text-maincolor-400
                      focus:outline-none
                      focus:ring-2
                      focus:ring-offset-2
                      focus:ring-maincolor-400
                      inline-flex
                    "
                  >
                    <svg
                      v-if="isLoading"
                      role="status"
                      class="
                        w-5
                        h-5
                        mr-3
                        text-gray-200
                        animate-spin
                        fill-maincolor-600
                      "
                      viewBox="0 0 100 101"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                        fill="currentColor"
                      />
                      <path
                        d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                        fill="currentFill"
                      />
                    </svg>
                    <span v-if="isLoading">Descargando ...</span>
                    <span v-else>Descargar</span>
                  </button>
                </div>
              </li>
            </ul>
          </dd>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import labelForm from "@/components/forms/LabelForm.vue";
import textInput from "@/components/forms/TextInput.vue";
import SelectInput from "@/components/forms/SelectInput.vue";
import IButton from "@/components/common/IButton.vue";
import "element-plus/es/components/upload/style/css";
import { ElUpload, ElIcon } from "element-plus";
import { UploadFilled } from "@element-plus/icons-vue";
import HeroIcon from "@/components/common/HeroIcon.vue";
import ModalTailwind from "@/components/common/ModalTailwind.vue";
import ExportService from "@/services/misc/ExportService";

export default defineComponent({
  components: {
    labelForm,
    textInput,
    SelectInput,
    IButton,
    ElUpload,
    ElIcon,
    UploadFilled,
    HeroIcon,
    ModalTailwind,
  },
  props: {
    data: {
      type: Object,
      default: () => {},
    },
  },
  setup(props) {
    const open = ref(false);
    const fileRequired = ref(false);
    const isLoading = ref(false);
    const modalType = ref("success");
    const modalTitle = ref("¡Muchas Gracias!");
    const modalText = ref("Tus datos fueron registrados con éxito.");
    const fileHelperText = ref(
      "El documento de comprobante de domicilio el obligatorio"
    );

    function onSuccess(evt) {
      console.log("onSuccess");
      console.log(evt);
    }

    function success() {
      modalType.value = "success";
      modalTitle.value = "¡Muchas Gracias!";
      modalText.value = "Tus datos fueron registrados con éxito.";
      open.value = true;
    }

    function errorMsg() {
      modalType.value = "error";
      modalTitle.value = "Ha ocurrido un error";
      modalText.value = "Revisa los datos ingresados y Vuelve a intentarlo";
      open.value = true;
    }

    function getFilename(response) {
      const disposition = response.headers["content-disposition"];
      let filename = "COMEDOR.pdf";
      if (disposition) {
        const regexExpr =
          /filename[^;\n]*=(UTF-\d['"]*)?((['"]).*?[.]$\2|[^;\n]*)?/gi;
        const matches = regexExpr.exec(disposition);
        if (matches !== null && matches[2]) {
          // eslint-disable-next-line prefer-destructuring
          filename = matches[2];
        }
      }
      return filename;
    }

    function downloadComprobante() {
      isLoading.value = true;
      ExportService.exportComprobanteAcuerdo0022()
        .then((response) => {
          const filename = getFilename(response);
          const blob = new Blob([response.data], {
            type: response.headers["content-type"],
          });
          const link = document.createElement("a");
          link.href = window.URL.createObjectURL(blob);
          link.download = filename;
          link.click();
        })
        .finally(() => {
          isLoading.value = false;
        });
    }

    return {
      open,
      fileRequired,
      onSuccess,
      fileHelperText,
      modalType,
      modalTitle,
      modalText,
      downloadComprobante,
      isLoading,
    };
  },
});
</script>

<style>
.el-upload-list__item-file-name {
  color: rgb(24, 74, 124);
}
</style>