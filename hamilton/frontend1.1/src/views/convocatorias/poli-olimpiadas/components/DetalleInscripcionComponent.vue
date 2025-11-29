<template>
  <div>
    <div class="pb-5 mb-10 border-b border-gray-200">
      <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
        <div class="sm:col-span-10">
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Folio: {{ data.folio_inscripcion }}
          </h3>
          <p class="mt-2 w-full text-sm text-gray-500">
            Desde aqui podras adsministrar ver los detalles de tu inscripcion,
            las disciplinas/pruebas en las que participaras y administrar los
            equipos en los que participaras.
          </p>
        </div>
        <div class="sm:col-span-2 flex items-center">
          <i-button @click="descargarComprobante">
            <svg
              v-if="isLoading"
              role="status"
              class="w-5 h-5 mr-3 text-gray-200 animate-spin fill-maincolor-600"
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
            <span v-else>Descargar Comprobante</span></i-button
          >
        </div>
      </div>
    </div>
    <div class="pb-5 mb-5 border-b border-gray-200">
      <h3 class="text-lg leading-6 font-medium text-gray-900">Pruebas</h3>
      <p class="mt-2 mb-2 w-full text-sm text-gray-500">
        Selecciona las pruebas en las que desees participar.
      </p>

      <div class="mb-5">
        <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
          <div class="sm:col-span-10">
            <select-input
              v-model="selectedPrueba"
              :options="pruebas"
              width="w-full"
              textProp="descripcion"
              valueProp="id"
            />
          </div>
          <div class="sm:col-span-2 flex">
            <i-button class="ml-auto" @click="addPrueba"
              >Seleccionar prueba</i-button
            >
          </div>
        </div>
      </div>

      <div class="">
        <p class="mt-2 mb-2 w-full text-sm text-gray-500">
          A continuacion se muestran las pruebas en las que participaras.
        </p>

        <alert-card v-show="errorsPruebas">
          <div class="flex">
            <div class="flex-shrink-0">
              <XCircleIcon class="h-5 w-5 text-red-400" aria-hidden="true" />
            </div>
            <div class="ml-3">
              <h3 class="text-sm font-medium text-red-800">Alerta</h3>
              <div class="mt-2 text-sm text-red-700">
                <ul role="list" class="list-disc pl-5 space-y-1">
                  <li class="text-xs">
                    {{ errorsPruebas }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </alert-card>

        <dd
          class="mt-2 text-sm text-gray-900 sm:mt-5 sm:col-span-2"
          v-for="pruebaInscripcion in pruebasInscripcion"
          :key="pruebaInscripcion.id"
        >
          <ul
            role="list"
            class="border border-gray-200 rounded-md divide-y divide-gray-200"
          >
            <li
              class="pl-3 pr-4 py-3 flex items-center justify-between text-sm"
            >
              <div class="w-0 flex-1 flex items-center">
                <hero-icon
                  icon="CheckIcon"
                  class="flex-shrink-0 h-5 w-5 text-green-400"
                ></hero-icon>
                <span class="ml-2 flex-1 w-0 truncate">
                  {{ pruebaInscripcion.prueba }}
                </span>
              </div>
              <div class="ml-4 flex-shrink-0 flex space-x-4">
                <button
                  @click="removerPrueba(pruebaInscripcion.id)"
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
                  "
                >
                  Remover
                </button>
              </div>
            </li>
          </ul>
        </dd>
      </div>
    </div>
    <div class="pb-5 border-b border-gray-200">
      <h3 class="text-lg leading-6 font-medium text-gray-900">Equipos</h3>
      <p class="mt-2 mb-2 w-full text-sm text-gray-500">
        Administra los equipos de los que eres capitan/perteneces.
      </p>

      <div class="mb-5">
        <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
          <div class="sm:col-span-5">
            <select-input
              v-model="form.prueba_id"
              :options="pruebas"
              width="w-full"
              textProp="descripcion"
              valueProp="id"
            />
          </div>
          <div class="sm:col-span-5">
            <text-input
              class="-mt-1"
              width="max-w-3xl"
              :required="true"
              v-model="form.nombre_equipo"
            />
          </div>
          <div class="sm:col-span-2 flex">
            <i-button class="ml-auto" @click="addEquipo">Crear Equipo</i-button>
          </div>
        </div>
      </div>

      <alert-card v-show="errorsEquipos">
        <div class="flex">
          <div class="flex-shrink-0">
            <XCircleIcon class="h-5 w-5 text-red-400" aria-hidden="true" />
          </div>
          <div class="ml-3">
            <h3 class="text-sm font-medium text-red-800">Alerta</h3>
            <div class="mt-2 text-sm text-red-700">
              <ul role="list" class="list-disc pl-5 space-y-1">
                <li class="text-xs">
                  {{ errorsEquipos }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </alert-card>

      <div class="">
        <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
          <div class="sm:col-span-6">
            <div class="bg-white py-5 border-b border-gray-200">
              <h3 class="text-lg leading-6 font-medium text-maincolor-500">
                Mis Equipos
              </h3>
              <p class="mt-1 text-sm text-gray-500">
                Aqui se muestran los equipos a los que perteneces o eres
                capitan.
              </p>
            </div>
            <div class="mt-5" v-if="equipos.length > 0">
              <dd
                class="mt-2 text-sm text-gray-900 sm:mt-5 sm:col-span-2"
                v-for="equipo in equipos"
                :key="equipo.id"
              >
                <ul
                  role="list"
                  class="
                    border border-gray-200
                    rounded-md
                    divide-y divide-gray-200
                  "
                >
                  <li
                    class="
                      pl-3
                      pr-4
                      py-3
                      flex
                      items-center
                      justify-between
                      text-sm
                    "
                  >
                    <div class="w-0 flex-1 flex items-center">
                      <hero-icon
                        v-if="equipo.creador"
                        icon="StarIcon"
                        class="flex-shrink-0 h-5 w-5 text-yellow-400"
                      ></hero-icon>
                      <hero-icon
                        v-else
                        icon="CheckIcon"
                        class="flex-shrink-0 h-5 w-5 text-green-400"
                      ></hero-icon>
                      <span
                        @click="
                          getMiembrosEquipo(
                            equipo.id,
                            equipo.inscripcion_prueba
                          )
                        "
                        class="
                          ml-2
                          flex-1
                          w-0
                          truncate
                          hover:cursor-pointer hover:underline
                          text-blue-500
                        "
                      >
                        {{ equipo.nombre_equipo }}
                      </span>
                      <span
                        class="
                          hover:cursor-pointer
                          text-blue-500
                          flex
                          hover:underline
                          items-center
                        "
                        @click="descargarComprobanteEquipo(equipo.id)"
                      >
                        <span v-if="equipo.isLoading">Descargando...</span>
                        <span v-else>Descargar comprobante</span>
                        <loading-icon class="ml-2" v-if="equipo.isLoading" />
                        <hero-icon
                          v-else
                          icon="DocumentDownloadIcon"
                          class="h-6 w-6 ml-2"
                        />
                      </span>
                    </div>
                  </li>
                </ul>
              </dd>
            </div>
            <div v-else>
              <dd class="mt-2 text-sm text-gray-900 sm:mt-5 sm:col-span-2">
                <ul
                  role="list"
                  class="
                    border border-gray-200
                    rounded-md
                    divide-y divide-gray-200
                  "
                >
                  <li
                    class="
                      pl-3
                      pr-4
                      py-3
                      flex
                      items-center
                      justify-between
                      text-sm
                    "
                  >
                    <div class="w-0 flex-1 flex items-center">
                      <hero-icon
                        icon="InformationCircleIcon"
                        class="flex-shrink-0 h-5 w-5 text-blue-400"
                      ></hero-icon>
                      <span class="ml-2 flex-1 w-0 truncate">
                        No estas en ningun equipo, crea uno o pide que agreguen
                        a un equipo.
                      </span>
                    </div>
                  </li>
                </ul>
              </dd>
            </div>
          </div>
          <div class="sm:col-span-6">
            <div class="bg-white py-5 border-b border-gray-200">
              <h3 class="text-lg leading-6 font-medium text-maincolor-500">
                Integrantes
              </h3>
              <p class="mt-1 text-sm text-gray-500">
                Desde aqui puedes ver los integrantes de tus equipos y agregar /
                eliminar si eres capitan
              </p>
            </div>
            <div v-if="selectedEquipo">
              <div class="sm:mt-5">
                <div class="flex -mx-2">
                  <div class="mx-2 w-2/3">
                    <text-input
                      class="-mt-1"
                      width="max-w-3xl"
                      :required="true"
                      v-model="formIntegrante.folio_inscripcion"
                    />
                  </div>
                  <div class="mx-2 w-1/3">
                    <i-button block @click="addIntegrante"
                      >Agregar a equipo</i-button
                    >
                  </div>
                </div>
              </div>
              <alert-card v-show="errorsEquiposIntegrantes" class="mt-5">
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
                        <li class="text-xs">
                          {{ errorsEquiposIntegrantes }}
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </alert-card>
              <dd
                class="mt-2 text-sm text-gray-900 sm:col-span-2"
                v-for="integrante in integrantes"
                :key="integrante.id"
              >
                <ul
                  role="list"
                  class="
                    border border-gray-200
                    rounded-md
                    divide-y divide-gray-200
                  "
                >
                  <li
                    class="
                      pl-3
                      pr-4
                      py-3
                      flex
                      items-center
                      justify-between
                      text-sm
                    "
                  >
                    <div class="w-0 flex-1 flex items-center">
                      <hero-icon
                        v-if="integrante.creador"
                        icon="StarIcon"
                        class="flex-shrink-0 h-5 w-5 text-yellow-400"
                      ></hero-icon>
                      <hero-icon
                        v-else
                        icon="CheckIcon"
                        class="flex-shrink-0 h-5 w-5 text-green-400"
                      ></hero-icon>
                      <span class="ml-2 flex-1 w-0 truncate">
                        {{ integrante.folio_inscripcion }}
                        {{
                          data.folio_inscripcion ===
                          integrante.folio_inscripcion
                            ? "(tu)"
                            : ""
                        }}
                        {{
                          integrante.creador
                            ? "(capitan)"
                            : ""
                        }}
                        <br />
                        <span class="mt-1 text-sm text-gray-500">{{
                          integrante.nombre
                        }}</span>
                      </span>
                    </div>

                    <div class="ml-4 flex-shrink-0 flex space-x-4">
                      <button
                        @click="removerIntegrante(integrante.id)"
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
                        "
                      >
                        Remover
                      </button>
                    </div>
                  </li>
                </ul>
              </dd>
            </div>
            <div v-else>
              <dd class="mt-2 text-sm text-gray-900 sm:mt-5 sm:col-span-2">
                <ul
                  role="list"
                  class="
                    border border-gray-200
                    rounded-md
                    divide-y divide-gray-200
                  "
                >
                  <li
                    class="
                      pl-3
                      pr-4
                      py-3
                      flex
                      items-center
                      justify-between
                      text-sm
                    "
                  >
                    <div class="w-0 flex-1 flex items-center">
                      <hero-icon
                        icon="InformationCircleIcon"
                        class="flex-shrink-0 h-5 w-5 text-blue-400"
                      ></hero-icon>
                      <span class="ml-2 flex-1 w-0 truncate">
                        Selecciona un equipo para ver sus integrantes
                      </span>
                    </div>
                  </li>
                </ul>
              </dd>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { reactive, ref } from "vue";
import SelectInput from "@/components/forms/SelectInput.vue";
import PoliolimpiadasService from "@/services/convocatorias/PoliolimpiadasService.js";
import IButton from "@/components/common/IButton.vue";
import AlertCard from "@/components/common/AlertCard.vue";
import ExportService from "@/services/misc/ExportService";
import { useNotificationHelper } from "@/helpers/NotificationsHelper";
import textInput from "@/components/forms/TextInput.vue";
import HeroIcon from "@/components/common/HeroIcon.vue";
import LoadingIcon from "@/components/common/LoadingIcon.vue";

export default {
  components: {
    SelectInput,
    IButton,
    AlertCard,
    textInput,
    HeroIcon,
    LoadingIcon,
  },
  props: {
    data: {
      type: Object,
      default: () => {},
    },
  },
  setup(props) {
    const selectedPrueba = ref(null);
    const selectedEquipo = ref(null);
    const selectedInscripcionPrueba = ref(null);
    const disciplinaEquipo = ref(null);
    const form = reactive({
      prueba_id: null,
      nombre_equipo: null,
    });

    const defaultForm = {
      prueba_id: null,
      nombre_equipo: null,
    };

    const formIntegrante = ref({
      equipo_id: null,
      folio_inscripcion: null,
    });

    const defaultFormIntegrante = {
      equipo_id: null,
      folio_inscripcion: null,
    };
    const pruebas = ref([]);
    const disciplinas = ref([]);
    const equipos = ref([]);
    const integrantes = ref([]);
    const pruebasInscripcion = ref([]);
    const errorsPruebas = ref(null);
    const errorsEquipos = ref(null);
    const errorsEquiposIntegrantes = ref(null);
    const isLoading = ref(false);

    const notificationHelper = useNotificationHelper();

    function getPruebas() {
      PoliolimpiadasService.getAllPruebas().then((response) => {
        pruebas.value = response.data.data;
      });
    }

    function addEquipo() {
      errorsEquipos.value = null;
      PoliolimpiadasService.addEquipo(form)
        .then((response) => {
          getEquipos();
        })
        .catch((error) => {
          errorsEquipos.value = error.response.data.data;
        });
    }

    function addIntegrante() {
      errorsEquiposIntegrantes.value = null;
      formIntegrante.value.equipo_id = selectedEquipo.value;
      PoliolimpiadasService.addIntegrante(formIntegrante.value)
        .then((response) => {
          getIntegrantesEquipo(
            selectedEquipo.value,
            selectedInscripcionPrueba.value
          );
          Object.assign(formIntegrante.value, defaultFormIntegrante);
        })
        .catch((error) => {
          errorsEquiposIntegrantes.value = error.response.data.data;
        });
    }

    function getEquipos() {
      PoliolimpiadasService.getEquipos()
        .then((response) => {
          equipos.value = response.data.data;
        })
        .catch((error) => {
          // errorsEquipos.value = error.response.data.data;
        });
    }

    function addPrueba() {
      errorsPruebas.value = null;
      PoliolimpiadasService.addPrueba({ prueba: selectedPrueba.value })
        .then((response) => {
          listPruebas();
        })
        .catch((error) => {
          errorsPruebas.value = error.response.data.data;
        });
    }

    function listPruebas() {
      PoliolimpiadasService.getAllPruebasInscripcion().then((response) => {
        pruebasInscripcion.value = response.data.data;
      });
    }

    function removerPrueba(id) {
      PoliolimpiadasService.removerPrueba(id).then(() => {
        notificationHelper.showNotification({
          variant: "success",
          titulo: "Exito",
          message: "Prueba eliminada existosamente.",
        });
        listPruebas();
      });
    }

    function removerIntegrante(id) {
      PoliolimpiadasService.removerIntegrante(id).then(() => {
        notificationHelper.showNotification({
          variant: "success",
          titulo: "Exito",
          message: "Integrante eliminada existosamente.",
        });
        getIntegrantesEquipo(
          selectedEquipo.value,
          selectedInscripcionPrueba.value
        );
      });
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

    function downloadLink(response) {
      const filename = getFilename(response);
      const blob = new Blob([response.data], {
        type: response.headers["content-type"],
      });
      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = filename;
      link.click();
    }

    function descargarComprobante() {
      isLoading.value = true;
      ExportService.exportComprobanteInscripcion()
        .then((response) => {
          downloadLink(response);
        })
        .finally(() => {
          isLoading.value = false;
        });
    }

    function descargarComprobanteEquipo(id) {
      let equipo = equipos.value.find((e) => e.id === id);

      if (equipo.isLoading && equipo.isLoading === true) {
        return;
      }

      equipo.isLoading = true;

      ExportService.exportComprobanteInscripcionEquipo(id)
        .then((response) => {
          downloadLink(response);
        })
        .finally(() => {
          equipo.isLoading = false;
        });
    }

    function getIntegrantesEquipo(id, inscripcionPrueba) {
      PoliolimpiadasService.getAllIntegrantesEquipo({
        equipo: id,
        inscripcion_prueba: inscripcionPrueba,
      }).then((response) => {
        integrantes.value = response.data.data;
      });
    }

    function getMiembrosEquipo(equipoId, inscripcionPrueba) {
      selectedEquipo.value = equipoId;
      selectedInscripcionPrueba.value = inscripcionPrueba;
      getIntegrantesEquipo(equipoId, inscripcionPrueba);
    }

    return {
      selectedPrueba,
      getPruebas,
      pruebas,
      disciplinas,
      addPrueba,
      listPruebas,
      pruebasInscripcion,
      errorsPruebas,
      removerPrueba,
      descargarComprobante,
      isLoading,
      disciplinaEquipo,
      form,
      addEquipo,
      errorsEquipos,
      errorsEquiposIntegrantes,
      getEquipos,
      equipos,
      integrantes,
      removerIntegrante,
      selectedEquipo,
      getMiembrosEquipo,
      descargarComprobanteEquipo,
      formIntegrante,
      addIntegrante,
    };
  },
  mounted() {
    this.getPruebas();
    this.listPruebas();
    this.getEquipos();
  },
};
</script>