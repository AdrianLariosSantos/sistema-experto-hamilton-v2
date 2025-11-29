<template>
  <div>
    <form
      class="space-y-8 divide-y divide-gray-200"
      @submit.prevent="guardarDatos"
    >
      <div class="space-y-8 divide-y divide-gray-200">
        <div>
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Datos de inscripción
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Los campos marcados con un <span class="text-red-500">*</span> son
              obligatorios.
            </p>
          </div>

          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <!-- NOMBRE -->
            <div class="sm:col-span-4">
              <label-form text="Nombre" class="text-left" required />
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
              <label-form text="Primer Apellido" class="text-left" required />
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

            <!-- FECHA DE NACIMIENTO -->
            <div class="sm:col-span-4">
              <label-form text="Fecha de Nacimiento" class="text-left" />
              <div class="mt-1">
                <flat-pickr
                  class="
                    block
                    w-full
                    shadow-sm
                    focus:ring-maincolor-500 focus:border-maincolor-500
                    sm:text-sm
                    border-gray-300
                    rounded-md
                    max-w-3xl
                  "
                  v-model="form.fecha_nacimiento"
                  :config="configFechaNacimiento"
                  required
                ></flat-pickr>
              </div>
            </div>
            <!-- EDAD -->
            <div class="sm:col-span-4">
              <label-form text="Edad" class="text-left" />
              <div class="mt-1">
                <text-input
                  width="w-full"
                  :required="true"
                  type="number"
                  v-model="form.edad"
                />
              </div>
            </div>
            <!-- CURP -->
            <div class="sm:col-span-6">
              <label-form text="CURP" class="text-left" />
              <div class="mt-1">
                <text-input
                  width="w-full"
                  :required="true"
                  type="text"
                  v-model="form.curp"
                />
              </div>
            </div>
            <!-- RFC -->
            <div class="sm:col-span-6">
              <label-form text="RFC" class="text-left" />
              <div class="mt-1">
                <text-input
                  width="w-full"
                  :required="true"
                  type="text"
                  v-model="form.rfc"
                />
              </div>
            </div>
          </div>
        </div>

        <div class="pt-8">
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Datos de contacto
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Ingresa tus datos de contacto.
            </p>
          </div>
          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <!-- CALLE -->
            <div class="sm:col-span-6">
              <label-form text="Telefono" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="number"
                  v-model="form.telefono"
                />
              </div>
            </div>
            <!-- Telefono de emergencias -->
            <div class="sm:col-span-6">
              <label-form
                text="Telefono de emergencias"
                class="text-left"
                required
              />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="number"
                  v-model="form.telefono_emergencias"
                />
              </div>
            </div>
          </div>
        </div>

        <div class="pt-8">
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Datos laborales
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Ingresa tu grado, area de adscripcion y demas detalles laborales.
            </p>
          </div>
          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <!-- numero de empleado -->
            <div class="sm:col-span-4">
              <label-form
                text="Numero de empleado"
                class="text-left"
                required
              />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="text"
                  v-model="form.numero_empleado"
                />
              </div>
            </div>
            <!-- grado -->
            <div class="sm:col-span-4">
              <label-form text="Grado" class="text-left" />
              <div class="mt-1">
                <select-input
                  v-model="form.grado"
                  :options="grados"
                  value-prop="descripcion"
                  width="max-w-3xl"
                />
              </div>
            </div>
            <!-- AREA -->
            <div class="sm:col-span-4">
              <label-form text="Área" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="text"
                  v-model="form.area"
                />
              </div>
            </div>
            <!-- ADSCRIPCION -->
            <div class="sm:col-span-4">
              <label-form text="Adscripcion" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="text"
                  v-model="form.adscripcion"
                />
              </div>
            </div>
            <!-- NOMBRE DIRECTOR -->
            <div class="sm:col-span-4">
              <label-form
                text="Nombre de tu director"
                class="text-left"
                required
              />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="text"
                  v-model="form.nombre_director"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="pt-8">
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Datos de salud
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Especifica edad, peso y tus alergias.
            </p>
          </div>
          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <!-- PESO -->
            <div class="sm:col-span-2">
              <label-form text="Peso" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="number"
                  v-model="form.peso"
                />
              </div>
            </div>
            <!-- ADSCRIPCION -->
            <div class="sm:col-span-2">
              <label-form text="Estatura" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="number"
                  v-model="form.estatura"
                />
              </div>
            </div>
            <!-- NOMBRE DIRECTOR -->
            <div class="sm:col-span-8">
              <label-form text="Alergias" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="w-full"
                  :required="true"
                  type="text"
                  v-model="form.alergias"
                  helper-text="Ingresa tus alergias cada una separada por una coma. Ej: Polen,Penicilina,Picadura de Abeja"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="pt-8">
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Documentos
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Sube en el formato indicado los archivos necesarios para completar
              tu inscripcion.
            </p>
          </div>
          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <!-- PESO -->
            <div class="sm:col-span-4">
              <label-form text="INE" class="text-left" required></label-form>
              <div class="mt-1">
                <upload-component
                  ref="uploadRefIne"
                  v-model="form.ine"
                  nombre="ine"
                />
              </div>
            </div>
            <div class="sm:col-span-4">
              <label-form
                text="Certificado medico actual"
                class="text-left"
                required
              ></label-form>
              <div class="mt-1">
                <upload-component
                  ref="uploadRefCert"
                  v-model="form.certificado_medico"
                  nombre="certificado_medico"
                />
              </div>
            </div>
            <div class="sm:col-span-4">
              <label-form
                text="Ultimo talon de pago"
                class="text-left"
                required
              ></label-form>
              <div class="mt-1">
                <upload-component
                  ref="uploadRefPago"
                  v-model="form.ultimo_pago"
                  nombre="ultimo_pago"
                />
              </div>
            </div>
            <div class="sm:col-span-4">
              <label-form
                text="Credencial de la institucion"
                class="text-left"
                required
              ></label-form>
              <div class="mt-1">
                <upload-component
                  ref="uploadRefCred"
                  v-model="form.credencial"
                  nombre="credencial"
                />
              </div>
            </div>
            <div class="sm:col-span-4">
              <label-form
                text="Fotografia o selfie"
                class="text-left"
                required
              ></label-form>
              <div class="mt-1">
                <upload-component
                  ref="uploadRefFoto"
                  v-model="form.fotografia"
                  nombre="fotografia"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pt-5">
        <div class="flex justify-end">
          <i-button type="submit" variant="maincolor">Guardar</i-button>
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

    <modal-tailwind
      :open="openFailed"
      @close="openFailed = false"
      :type="modalType"
      :title="modalTitle"
      :text="modalText"
    />
  </div>
</template>

<script>
import { defineComponent, ref, watch } from "vue";
import labelForm from "@/components/forms/LabelForm.vue";
import textInput from "@/components/forms/TextInput.vue";
import SelectInput from "@/components/forms/SelectInput.vue";
import flatPickr from "vue-flatpickr-component";
import IButton from "@/components/common/IButton.vue";
import { Spanish } from "flatpickr/dist/l10n/es.js";
import "flatpickr/dist/flatpickr.css";
import PoliolimpiadasService from "@/services/convocatorias/PoliolimpiadasService";
import ModalTailwind from "@/components/common/ModalTailwind.vue";
import UploadComponent from "./UploadComponent.vue";
import axios from "axios";

export default defineComponent({
  emits: ["saved"],
  components: {
    labelForm,
    textInput,
    SelectInput,
    flatPickr,
    IButton,
    ModalTailwind,
    UploadComponent,
  },
  setup(props, { emit }) {
    const open = ref(false);
    const openFailed = ref(false);
    const modalType = ref("success");
    const modalTitle = ref("¡Muchas Gracias!");
    const modalText = ref("Tus datos fueron registrados con éxito.");
    const uploadRefIne = ref(null);
    const uploadRefCert = ref(null);
    const uploadRefPago = ref(null);
    const uploadRefCred = ref(null);
    const uploadRefFoto = ref(null);

    const form = ref({
      nombre: "Luis",
      primer_apellido: "Contreras",
      segundo_apellido: "Muñoz",
      edad: "20",
      fecha_nacimiento: "1995-08-14",
      rfc: "COML950814",
      curp: "COML950814HMCNXS07",
      telefono: "5532844802",
      telefono_emergencias: "5532844802",
      numero_empleado: "1139218",
      grado: "POLICIA",
      cuip: "COML950814H123456789",
      area: "DDSI",
      adscripcion: "DDSI",
      nombre_director: "DIRECTOR",
      peso: "99",
      estatura: "170",
      alergias: "None",
      ine: null,
      certificado_medico: null,
      ultimo_pago: null,
      credencial: null,
      fotografia: null,
    });

    const configFechaNacimiento = {
      wrap: true,
      dateFormat: "Y-m-d",
      locale: Spanish,
      maxDate: new Date(),
    };

    const grados = [
      {
        id: 1,
        descripcion: "POLICIA",
      },
      {
        id: 2,
        descripcion: "POLICIA TERCERO/A",
      },
      {
        id: 3,
        descripcion: "POLICIA SEGUNDO/A",
      },
      {
        id: 4,
        descripcion: "SUBOFICIAL",
      },
      {
        id: 5,
        descripcion: "OFICIAL",
      },
      {
        id: 6,
        descripcion: "SUBINSPECTOR/A",
      },
      {
        id: 7,
        descripcion: "INSPECTOR/A",
      },
      {
        id: 8,
        descripcion: "INSPECTOR/A JEFE",
      },
      {
        id: 9,
        descripcion: "INSPECTOR/A GENERAL",
      },
      {
        id: 10,
        descripcion: "COMISARIO/A",
      },
      {
        id: 11,
        descripcion: "COMISARIO/A JEFE",
      },
      {
        id: 12,
        descripcion: "COMISARIO/A GENERAL",
      },
      {
        id: 13,
        descripcion: "OTRO",
      },
      {
        id: 14,
        descripcion: "POLICIA PRIMERO/A",
      },
    ];

    const errors = ref({
      nombre: [],
      primer_apellido: [],
      segundo_apellido: [],
      edad: [],
      fecha_nacimiento: [],
      rfc: [],
      curp: [],
      telefono: [],
      telefono_emergencias: [],
      numero_empleado: [],
      grado: [],
      cuip: [],
      area: [],
      adscripcion: [],
      nombre_director: [],
      peso: [],
      estatura: [],
      alergias: [],
      ine: [],
      certificado_medico: [],
      ultimo_pago: [],
      credencial: [],
      fotografia: [],
    });

    const defaultErrors = {
      nombre: [],
      primer_apellido: [],
      segundo_apellido: [],
      edad: [],
      fecha_nacimiento: [],
      rfc: [],
      curp: [],
      telefono: [],
      telefono_emergencias: [],
      numero_empleado: [],
      grado: [],
      cuip: [],
      area: [],
      adscripcion: [],
      nombre_director: [],
      peso: [],
      estatura: [],
      alergias: [],
      ine: [],
      certificado_medico: [],
      ultimo_pago: [],
      credencial: [],
      fotografia: [],
    };

    const defaultForm = {
      nombre: null,
      primer_apellido: null,
      segundo_apellido: null,
      edad: null,
      fecha_nacimiento: null,
      rfc: null,
      curp: null,
      telefono: null,
      telefono_emergencias: null,
      numero_empleado: null,
      grado: null,
      cuip: null,
      area: null,
      adscripcion: null,
      nombre_director: null,
      peso: null,
      estatura: null,
      alergias: null,
      ine: null,
      certificado_medico: null,
      ultimo_pago: null,
      credencial: null,
      fotografia: null,
    };

    watch(
      () => form.value.fecha_nacimiento,
      (newValue, oldValue) => {
        form.value.edad = fechaNacimiento(newValue).toString();
      }
    );

    function fechaNacimiento(dobS) {
      const dob = new Date(dobS);
      const diffms = Date.now() - dob.getTime();
      const agedt = new Date(diffms);
      return Math.abs(agedt.getUTCFullYear() - 1970);
    }

    function guardarDatos() {
      const formData = new FormData();
      formData.append("nombre", form.value.nombre);
      formData.append("primer_apellido", form.value.primer_apellido);
      formData.append("segundo_apellido", form.value.segundo_apellido);
      formData.append("edad", form.value.edad);
      formData.append("fecha_nacimiento", form.value.fecha_nacimiento);
      formData.append("rfc", form.value.rfc);
      formData.append("curp", form.value.curp);
      formData.append("telefono", form.value.telefono);
      formData.append("telefono_emergencias", form.value.telefono_emergencias);
      formData.append("numero_empleado", form.value.numero_empleado);
      formData.append("grado", form.value.grado);
      formData.append("cuip", form.value.cuip);
      formData.append("area", form.value.area);
      formData.append("adscripcion", form.value.adscripcion);
      formData.append("nombre_director", form.value.nombre_director);
      formData.append("peso", form.value.peso);
      formData.append("estatura", form.value.estatura);
      formData.append("alergias", form.value.alergias);

      if (form.value.ine) {
        formData.append("ine", form.value.ine);
      }
      if (form.value.certificado_medico) {
        formData.append("certificado_medico", form.value.certificado_medico);
      }
      if (form.value.ultimo_pago) {
        formData.append("ultimo_pago", form.value.ultimo_pago);
      }
      if (form.value.credencial) {
        formData.append("credencial", form.value.credencial);
      }
      if (form.value.fotografia) {
        formData.append("fotografia", form.value.fotografia);
      }

      Object.assign(errors, defaultErrors);

      PoliolimpiadasService.create(formData)
        .then(() => {
          success();
          resetForm();
        })
        .catch((error) => {
          console.log(error);
          if (axios.isAxiosError(error)) {
            const { response } = error;

            if (response && response.status === 400) {
              if (Object.prototype.hasOwnProperty.call(response.data, "data")) {
                Object.assign(errors.value, response.data.data);
              } else {
                Object.assign(errors.value, response.data);
              }
            }
          } else {
            // no es error de axios
          }

          // errorMsg();
        })
        .finally(() => {
          //
        });
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
      openFailed.value = true;
    }

    function onCloseModal() {
      open.value = false;
      emitReloadComponents();
    }

    function emitReloadComponents() {
      console.log("emit registro");
      emit("saved", true);
    }

    function resetForm() {
      Object.assign(form.value, defaultForm);
      uploadRefIne.value.clearFiles()
      uploadRefCert.value.clearFiles()
      uploadRefPago.value.clearFiles()
      uploadRefCred.value.clearFiles()
      uploadRefFoto.value.clearFiles()
    }

    return {
      form,
      errors,
      grados,
      guardarDatos,
      open,
      openFailed,
      modalType,
      modalTitle,
      modalText,
      onCloseModal,
      configFechaNacimiento,
      uploadRefIne,
      uploadRefCert,
      uploadRefPago,
      uploadRefCred,
      uploadRefFoto,
    };
  },
});
</script>
