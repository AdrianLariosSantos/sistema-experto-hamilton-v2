<template>
  <div>
    <div class="bg-gray-100" id="inicio">
      <div class="container mx-auto px-10 md:px-20 py-20">
        <div class="main-section flex w-full">
          <div class="flex flex-col justify-center w-full lg:w-3/5">
            <h1 class="text-5xl font-bold mb-5">
              Primer Rodada de Niños Visibles en Bici 2023
            </h1>
            <p class="text-xl text-gray-600 mb-10">
              Llena el siguiente formulario para confirmar tu registro a la rodada.
            </p>
            <div>
              <button
                @click="gotoform"
                type="button"
                class="
                  inline-flex
                  items-center
                  px-4
                  py-2
                  border border-transparent
                  text-sm
                  font-medium
                  rounded-md
                  shadow-sm
                  text-white
                  bg-maincolor-600
                  hover:bg-maincolor-700
                  focus:outline-none
                  focus:ring-2
                  focus:ring-offset-2
                  focus:ring-maincolor-500
                "
              >
                Registrar
              </button>
            </div>
          </div>
          <div class="hidden lg:block lg:w-2/5">
            <img
              src="@/assets/images/pages/landing/acciones-relevantes-3.png"
              class="rounded-tr-xl rounded-br-xl"
              alt=""
            />
          </div>
        </div>
      </div>
    </div>
    <div class="bg-white">
      <div class="container mx-auto px-10 md:px-20 py-20">
        <div class="mb-10">
          <div class="pb-5 border-b border-gray-200">
            <h3 class="text-2xl leading-6 font-medium text-gray-900">
              Información General
            </h3>
          </div>
          <p class="text-lg text-gray-600 mb-5 mt-2">
            Texto descriptivo sobre la Primer Rodada Infantil de Niños Visibles en Bici 2023
          </p>
        </div>
        <div class="mb-10">
          <div class="pb-5">
            <h3 class="text-xl leading-6 font-medium text-gray-900">
              Recomendaciones para el llenado del registro a la rodada
            </h3>
          </div>
          <ul class="list-disc list-inside ml-5">
            <li class="text-lg text-gray-600">
              Recomendacion 1.
            </li>
            <li class="text-lg text-gray-600">
              Recomendacion 2.
            </li>
            <li class="text-lg text-gray-600">
              Recomendacion 3.
            </li>
          </ul>
        </div>
        <div>
          <p class="text-sm text-gray-600 italic mt-2">
            La información capturada está sujeta a análisis, valoración y a la
            disponibilidad presupuestal.
          </p>
          <p class="text-sm text-gray-600 italic">
            Tu registro no garantiza el otorgamiento de alguna condecoración,
            estimulo, reconocimiento, recompensa o constancia.
          </p>
        </div>
      </div>
    </div>
    <div class="bg-gray-100" id="mainform">
      <div class="container mx-auto p-10 md:px-20 py-20">
        <div class="pb-5 border-b border-gray-200">
          <h3 class="text-2xl leading-6 font-medium text-gray-900">
            Registro de Asistencia
          </h3>
          <p class="mt-2 max-w-4xl text-sm text-gray-500">
            El llenado de todos los campos es obligatorio
          </p>
        </div>
        <div class="mt-5">
          <form
            class="space-y-8 divide-y divide-gray-200"
            @submit.prevent="confirmacionForm"
          >
            <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5">
              <div class="">
                <div>
                  <h3 class="text-lg leading-6 font-medium text-gray-900">
                    Datos Generales
                  </h3>
                  <p class="mt-1 max-w-2xl text-sm text-gray-500">
                    Datos del tutor.
                  </p>
                </div>

                <!-- CAMPOS -->
                <div
                  class="
                    mt-6
                    grid grid-cols-1
                    gap-y-6 gap-x-4
                    sm:grid-cols-12
                    border-b
                    pb-10
                  "
                >
                  <!-- NOMBRE -->
                  <div class="sm:col-span-4">
                    <label-form text="Nombre" required class="text-left" />
                    <div class="mt-1">
                      <text-input
                        width="max-w-3xl"
                        :required="true"
                        v-model="form.nombre"
                      />
                    </div>
                  </div>

                  <!-- PRIMER APELLIDO -->
                  <div class="sm:col-span-4">
                    <label-form
                      text="Primer Apellido"
                      required
                      class="text-left"
                    />
                    <div class="mt-1">
                      <text-input
                        width="max-w-3xl"
                        :required="true"
                        v-model="form.primer_apellido"
                      />
                    </div>
                  </div>

                  <!-- SEGUNDO APELLIDO -->
                  <div class="sm:col-span-4">
                    <label-form text="Segundo Apellido" class="text-left" />
                    <div class="mt-1">
                      <text-input
                        width="max-w-3xl"
                        :required="false"
                        v-model="form.segundo_apellido"
                      />
                    </div>
                  </div>
                  <!-- NUMERO DE EMPLEADO -->
                  <div class="sm:col-span-4">
                    <label-form
                      text="Número de empleado (En caso de pertenecer a la SSC CDMX, P.B.I o Policía Auxiliar)"
                      required
                      class="text-left"
                    />
                    <div class="mt-1">
                      <text-input
                        width="max-w-3xl"
                        :required="false"
                        type="text"
                        pattern="\d*"
                        maxlength="7"
                        v-model="form.numero_empleado"
                      />
                    </div>
                  </div>
                  <!-- ADSCRIPCION -->
                  <div class="sm:col-span-4">
                    <label-form
                      text="Area de Adscripción"
                      required
                      class="text-left"
                    />
                    <!-- <div class="mt-1">
                      <text-input
                        width="max-w-3xl"
                        :required="true"
                        v-model="form.adscripcion"
                      />
                    </div> -->
                    <div class="mt-1">
                      <select-input
                        v-model="form.adscripcion"
                        :options="adscripciones"
                        width="max-w-3xl"
                        :required="true"
                        value-prop="descripcion"
                      />
                    </div>
                    <div
                      v-if="
                        form.adscripcion === 'Otra adscripción (especificar)'
                      "
                      class="mt-1"
                    >
                      <text-input
                        width="max-w-3xl"
                        :required="true"
                        v-model="form.adscripcion_descripcion"
                        placeholder="Especifica tú adscripción"
                      />
                    </div>
                  </div>
                  <!-- EDAD -->
                  <div class="sm:col-span-4">
                    <label-form text="Edad" required class="text-left" />
                    <div class="mt-1">
                      <text-input
                        width="max-w-3xl"
                        :required="true"
                        type="number"
                        v-model="form.edad"
                      />
                    </div>
                  </div>
                  <!-- GENERO -->
                  <div class="sm:col-span-4">
                    <label-form text="Sexo" required class="text-left" />
                    <div class="mt-1">
                      <select-input
                        v-model="form.genero"
                        :options="generos"
                        value-prop="descripcion"
                        width="max-w-3xl"
                      />
                    </div>
                  </div>
                  <!-- ALCALDIA -->
                  <div class="sm:col-span-4">
                    <label-form text="Alcaldia" required class="text-left" />
                    <div class="mt-1">
                      <select-input
                        v-model="form.corporacion"
                        :options="alcaldias"
                        width="max-w-3xl"
                        :required="true"
                        value-prop="descripcion"
                      />
                    </div>
                  </div>
                  <!-- NO NINOS QUE PARTICIPAN Y EDAD -->
                  <div class="sm:col-span-4">
                    <label-form text="Número de niños que participan y su edad" required class="text-left" />
                    <div class="mt-1">
                      <text-input
                        width="max-w-3xl"
                        :required="true"
                        type="number"
                        v-model="form.edad"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="pt-5">
              <div class="flex justify-end">
                <button
                  type="submit"
                  class="
                    ml-3
                    inline-flex
                    justify-center
                    py-2
                    px-4
                    border border-transparent
                    shadow-sm
                    text-sm
                    font-medium
                    rounded-md
                    text-white
                    bg-maincolor-600
                    hover:bg-maincolor-700
                    focus:outline-none
                    focus:ring-2
                    focus:ring-offset-2
                    focus:ring-maincolor-500
                  "
                  >
                  <span v-if="isLoading" class="inline-flex">
                    <loading-icon />
                    Guardando...
                  </span>
                  <span v-else> Registrar </span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <TransitionRoot as="template" :show="open">
      <Dialog as="div" class="relative z-10" @close="open = false">
        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div
            class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
          />
        </TransitionChild>

        <div class="fixed z-10 inset-0 overflow-y-auto">
          <div
            class="
              flex
              items-end
              sm:items-center
              justify-center
              min-h-full
              p-4
              text-center
              sm:p-0
            "
          >
            <TransitionChild
              as="template"
              enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100"
              leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            >
              <DialogPanel
                class="
                  relative
                  bg-white
                  rounded-lg
                  px-4
                  pt-5
                  pb-4
                  text-left
                  overflow-hidden
                  shadow-xl
                  transform
                  transition-all
                  sm:my-8 sm:max-w-sm sm:w-full sm:p-6
                "
              >
                <div>
                  <div
                    class="
                      mx-auto
                      flex
                      items-center
                      justify-center
                      h-12
                      w-12
                      rounded-full
                      bg-green-100
                    "
                  >
                    <CheckIcon
                      class="h-6 w-6 text-green-600"
                      aria-hidden="true"
                    />
                  </div>
                  <div class="mt-3 text-center sm:mt-5">
                    <DialogTitle
                      as="h3"
                      class="text-lg leading-6 font-medium text-gray-900"
                    >
                      ¡Muchas Gracias!
                    </DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">
                        Tus datos fueron registrados con éxito.
                      </p>
                      <p class="mt-3">Su folio de registro es:</p>
                      <p class="text-sm">
                        {{ folio_Hr }}
                      </p>
                    </div>
                  </div>
                </div>
                <div class="mt-5 sm:mt-6">
                  <button
                    type="button"
                    class="
                      inline-flex
                      justify-center
                      w-full
                      rounded-md
                      border border-transparent
                      shadow-sm
                      px-4
                      py-2
                      bg-maincolor-600
                      text-base
                      font-medium
                      text-white
                      hover:bg-maincolor-700
                      focus:outline-none
                      focus:ring-2
                      focus:ring-offset-2
                      focus:ring-maincolor-500
                      sm:text-sm
                    "
                    @click="closeAndReset()"
                  >
                    Cerrar
                  </button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
    <!-- MODAL CONFIRMACION FORMULARIO -->
    <TransitionRoot as="template" :show="openConfirmacion">
      <Dialog as="div" class="relative z-10" @close="openConfirmacion = false">
        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div
            class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
          />
        </TransitionChild>

        <div class="fixed z-10 inset-0 overflow-y-auto">
          <div
            class="
              flex
              items-end
              sm:items-center
              justify-center
              min-h-full
              p-4
              text-center
              sm:p-0
            "
          >
            <TransitionChild
              as="template"
              enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100"
              leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            >
              <DialogPanel
                class="
                  relative
                  bg-white
                  rounded-lg
                  px-4
                  pt-5
                  pb-4
                  text-left
                  overflow-hidden
                  shadow-xl
                  transform
                  transition-all
                  sm:my-8 sm:max-w-sm sm:w-full sm:p-6
                "
              >
                <div>
                  <div
                    class="
                      mx-auto
                      flex
                      items-center
                      justify-center
                      h-12
                      w-12
                      rounded-full
                      bg-orange-100
                    "
                  >
                    <ExclamationCircleIcon
                      class="h-6 w-6 text-orange-600"
                      aria-hidden="true"
                    />
                  </div>
                  <div class="mt-3 text-center sm:mt-5">
                    <DialogTitle
                      as="h3"
                      class="text-lg leading-6 font-medium text-gray-900"
                    >
                      ¿Está seguro de enviar el registro?
                    </DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">
                        Asegúrate de escribir correctamente tú número telefónico
                        y correo electrónico, de lo contrario personal de la
                        Dirección General de Carrera Policial no podrá ponerse
                        en contacto contigo.
                      </p>
                    </div>
                  </div>
                </div>
                <div class="mt-5 sm:mt-6 flex justify-center">
                  <!-- inline-flex -->
                  <button
                    type="button"
                    class="
                      mx-5
                      w-30
                      rounded-md
                      border border-transparent
                      shadow-sm
                      px-4
                      py-2
                      bg-red-600
                      text-base
                      font-medium
                      text-white
                      hover:bg-red-700
                      focus:outline-none
                      focus:ring-2
                      focus:ring-offset-2
                      focus:ring-red-500
                      sm:text-sm
                    "
                    @click="openConfirmacion = false"
                  >
                    Cancelar
                  </button>
                  <!-- inline-flex -->
                  <button
                    type="button"
                    class="
                      mx-5
                      w-30
                      rounded-md
                      border border-transparent
                      shadow-sm
                      px-4
                      py-2
                      bg-maincolor-600
                      text-base
                      font-medium
                      text-white
                      hover:bg-maincolor-700
                      focus:outline-none
                      focus:ring-2
                      focus:ring-offset-2
                      focus:ring-maincolor-500
                      sm:text-sm
                    "
                    @click="submit()"
                  >
                    Si, enviar
                  </button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </div>
</template>


<script lang="ts">
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import labelForm from "./LabelForm.vue";
import textInput from "@/components/forms/TextInput.vue";
import textAreaInput from "@/components/forms/TextAreaInput.vue";
import { defineComponent, reactive, ref, watch } from "vue";
import SelectInput from "@/components/forms/SelectInput.vue";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { Spanish } from "flatpickr/dist/l10n/es.js";
import HechosRelevantesService from "@/services/carrera-policial/HechosRelevantesService";
import { CheckIcon, ExclamationCircleIcon } from "@heroicons/vue/outline";
import SwitchInput from "@/components/forms/SwitchInput.vue";
import LoadingIcon from "@/components/common/LoadingIcon.vue";

const d = new Date(); // today!
const today = new Date(); // today!

d.setMonth(today.getMonth() - 1, 1);

const d2 = new Date(); // today!
d2.setDate(d2.getDate() - 6574);

export default defineComponent({
  components: {
    labelForm,
    textInput,
    SelectInput,
    textAreaInput,
    flatPickr,
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
    CheckIcon,
    ExclamationCircleIcon,
    SwitchInput,
    LoadingIcon,
  },
  setup() {
    const open = ref(false);
    const isLoading = ref(false);
    const openConfirmacion = ref(false);

    const form = ref({
      nombre: "",
      primer_apellido: "",
      segundo_apellido: "",
      corporacion: null,
      numero_empleado: "",
      genero: null,
      fecha_nacimiento: "1990-01-01",
      edad: "",
      adscripcion: "",
      adscripcion_descripcion: "",
      antiguedad: "",
      telefono_fijo: "",
      telefono_celular: "",
      correo_contacto: "",
      fecha_evento: "",
      narracion_hechos: "",
      carpeta_investigacion_folio: "",
      carpeta_investigacion: false,
      rfc: "",
      curp: "",
    });
    const defaultForm = {
      nombre: "",
      primer_apellido: "",
      segundo_apellido: "",
      corporacion: null,
      numero_empleado: "",
      genero: null,
      fecha_nacimiento: "1990-01-01",
      edad: "",
      adscripcion: "",
      adscripcion_descripcion: "",
      antiguedad: "",
      telefono_fijo: "",
      telefono_celular: "",
      correo_contacto: "",
      fecha_evento: "",
      narracion_hechos: "",
      carpeta_investigacion_folio: "",
      carpeta_investigacion: false,
      rfc: "",
      curp: "",
    };
    const errors = reactive({
      nombre: [],
      primer_apellido: [],
      segundo_apellido: [],
      corporacion: [],
      numero_empleado: [],
      genero: [],
      fecha_nacimiento: [],
      edad: [],
      adscripcion: [],
      adscripcion_descripcion: [],
      antiguedad: [],
      telefono_fijo: [],
      telefono_celular: [],
      correo_contacto: [],
      fecha_evento: [],
      narracion_hechos: [],
      carpeta_investigacion_folio: [],
      carpeta_investigacion: [],
      rfc: [],
      curp: [],
    });
    const defaultErrors = {
      nombre: [],
      primer_apellido: [],
      segundo_apellido: [],
      corporacion: [],
      numero_empleado: [],
      genero: [],
      fecha_nacimiento: [],
      edad: [],
      adscripcion: [],
      adscripcion_descripcion: [],
      antiguedad: [],
      telefono_fijo: [],
      telefono_celular: [],
      correo_contacto: [],
      fecha_evento: [],
      narracion_hechos: [],
      carpeta_investigacion_folio: [],
      carpeta_investigacion: [],
      rfc: [],
      curp: [],
    };
    const generos = reactive([
      { id: 1, descripcion: "Hombre" },
      { id: 2, descripcion: "Mujer" },
    ]);
    const corporaciones = reactive([
      { id: 1, descripcion: "POLICIA PREVENTIVA" },
      { id: 2, descripcion: "POLICIA AUXILIAR" },
      { id: 3, descripcion: "POLICIA BANCARIA INDUSTRIAL" },
    ]);
    const adscripciones = reactive([
      { id: 1, descripcion: "Dirección de Ayudantía" },
      { id: 2, descripcion: "Dirección de Unidad de Contacto del Secretario" },
      { id: 3, descripcion: "Dirección Ejecutiva de Comunicación Social" },
      { id: 4, descripcion: "Dirección General de Asuntos Internos" },
      { id: 5, descripcion: "Dirección General de Asuntos Jurídicos" },
      { id: 6, descripcion: "Dirección General de la Policía Auxiliar" },
      {
        id: 7,
        descripcion: "Dirección General de la Policía Bancaria e Industrial",
      },
      { id: 8, descripcion: "Oficialía Mayor" },
      { id: 9, descripcion: "Subsecretaría de Control de Tránsito" },
      { id: 10, descripcion: "Subsecretaría de Desarrollo Institucional" },
      {
        id: 11,
        descripcion: "Subsecretaría de Inteligencia e Investigación Policial",
      },
      { id: 12, descripcion: "Subsecretaría de Operación Policial" },
      {
        id: 13,
        descripcion:
          "Subsecretaría de Participación Ciudadana y Prevención del Delito",
      },
      { id: 14, descripcion: "Otra adscripción (especificar)" },
    ]);
    const alcaldias = reactive([
      { id: 1, descripcion: "ÁLVARO OBREGÓN" },
      { id: 2, descripcion: "AZCAPOTZALCO" },
      { id: 3, descripcion: "BENITO JUÁREZ" },
      { id: 4, descripcion: "COYOACÁN" },
      { id: 5, descripcion: "CUAJIMALPA DE MORELOS" },
      { id: 6, descripcion: "CUAUHTÉMOC" },
      { id: 7, descripcion: "GUSTAVO A. MADERO" },
      { id: 8, descripcion: "IZTACALCO" },
      { id: 9, descripcion: "IZTAPALAPA" },
      { id: 10, descripcion: "LA MAGDALENA CONTRERAS" },
      { id: 11, descripcion: "MIGUEL HIDALGO" },
      { id: 12, descripcion: "MILPA ALTA" },
      { id: 13, descripcion: "TLÁHUAC" },
      { id: 14, descripcion: "TLALPAN" },
      { id: 15, descripcion: "VENUSTIANO CARRANZA" },
      { id: 16, descripcion: "XOCHIMILCO" }
    ]);
    const config = reactive({
      wrap: true, // set wrap to true only when using 'input-group'
      dateFormat: "Y-m-d",
      locale: Spanish, // locale for this instance only
      allowInput: true,
      minDate: d,
      maxDate: new Date(),
    });
    const configFechaNacimiento = reactive({
      wrap: true,
      dateFormat: "Y-m-d",
      locale: Spanish,
      allowInput: true,
      maxDate: d2,
    });

    const folio_Hr = ref(null);

    watch(
      () => form.value.fecha_nacimiento,
      (newValue, oldValue) => {
        form.value.edad = fechaNacimiento(newValue).toString();
      }
    );

    function fechaNacimiento(dobS: string) {
      const dob = new Date(dobS);
      const diffms = Date.now() - dob.getTime();
      const agedt = new Date(diffms);
      return Math.abs(agedt.getUTCFullYear() - 1970);
    }

    function success() {
      open.value = true;
    }

    function gotoform() {
      const element = document.getElementById("mainform");
      element!.scrollIntoView();
    }

    function resetForm() {
      Object.assign(form.value, defaultForm);
    }

    function closeAndReset() {
      open.value = false;
      resetForm();
      folio_Hr.value = null;
    }

    function confirmacionForm() {
      openConfirmacion.value = true;
    }

    function submit() {
      openConfirmacion.value = false;
      isLoading.value = true;
      Object.assign(errors, defaultErrors);
      HechosRelevantesService.create(form.value)
        .then((response) => {
          folio_Hr.value = response.data.data.folio;
          success();
          // resetForm();
        })
        .catch((error: any) => {
          const { response } = error;
          if (response.status === 400) {
            Object.assign(errors, response.data);
          }
        })
        .finally(() => {
          isLoading.value = false;
        });
    }

    return {
      form,
      generos,
      defaultForm,
      errors,
      defaultErrors,
      config,
      configFechaNacimiento,
      submit,
      open,
      gotoform,
      corporaciones,
      alcaldias,
      isLoading,
      adscripciones,
      folio_Hr,
      closeAndReset,
      openConfirmacion,
      confirmacionForm,
    };
  },
});
</script>


<style>
</style>