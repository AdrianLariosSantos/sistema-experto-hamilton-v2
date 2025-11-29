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
              Datos Personales
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

            <!-- NUMERO DE EMPLEADO -->
            <div class="sm:col-span-6">
              <label-form
                text="Número de empleado"
                class="text-left"
                required
              />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="number"
                  v-model="form.numero_empleado"
                />
              </div>
            </div>

            <!-- CUIP -->
            <div class="sm:col-span-6">
              <label-form text="CUIP" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  v-model="form.cuip"
                />
                <field-errors :errors="errors.cuip" />
              </div>
            </div>
          </div>
        </div>

        <div class="pt-8">
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Datos de Dirección
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Ingresa un domicilio de la CIUDAD DE MEXICO.
            </p>
          </div>
          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <!-- CALLE -->
            <div class="sm:col-span-4">
              <label-form text="Calle" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  v-model="form.calle"
                />
              </div>
            </div>
            <!-- CALLE -->
            <div class="sm:col-span-4">
              <label-form text="Entre calle..." class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  v-model="form.entre_calle_1"
                />
              </div>
            </div>
            <!-- CALLE -->
            <div class="sm:col-span-4">
              <label-form text="Y calle..." class="text-left" />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="false"
                  v-model="form.entre_calle_2"
                />
              </div>
            </div>
            <!-- NUM EXT -->
            <div class="sm:col-span-4">
              <label-form text="Numero exterior" class="text-left" required />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  v-model="form.numero_exterior"
                />
              </div>
            </div>
            <!-- NUM INT -->
            <div class="sm:col-span-4">
              <label-form text="Numero interior" class="text-left" />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="false"
                  v-model="form.numero_interior"
                />
              </div>
            </div>
            <!-- Alcaldia -->
            <div class="sm:col-span-12">
              <label-form text="Alcaldia" class="text-left" required />
              <div class="mt-1">
                <select-input
                  v-model="form.alcaldia"
                  :options="alcaldias"
                  width="w-full"
                  textProp="descripcion"
                  valueProp="object"
                />
              </div>
            </div>
            <!-- Codigo postal -->
            <div class="sm:col-span-6">
              <label-form text="Codigo Postal" class="text-left" required />
              <div class="mt-1">
                <select-input
                  v-model="form.codigo_postal"
                  :options="codigos_postales"
                  textProp="codigo"
                  valueProp="codigo"
                  width="w-full"
                  :disabled="form.alcaldia === null"
                />
              </div>
            </div>
            <!-- Colonia -->
            <div class="sm:col-span-6">
              <label-form text="Colonia" class="text-left" required />
              <div class="mt-1">
                <select-input
                  v-model="form.colonia"
                  :options="colonias"
                  valueProp="descripcion"
                  width="w-full"
                  :disabled="form.alcaldia === null"
                />
              </div>
            </div>
          </div>
        </div>

        <div class="pt-8">
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Datos de Contacto
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Ingresa un correo electronico al que tengas acceso y un numero
              telefonico.
            </p>
          </div>

          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <!-- CALLE -->
            <div class="sm:col-span-4">
              <label-form
                text="Correo electronico"
                class="text-left"
                required
              />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  type="email"
                  v-model="form.correo_electronico"
                />
              </div>
            </div>
            <!-- CALLE -->
            <div class="sm:col-span-4">
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
            <!-- CALLE -->
            <div class="sm:col-span-4">
              <label-form text="Extension" class="text-left" />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  type="number"
                  v-model="form.extension"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="pt-8">
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Documentacion
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Deberas subir un documento que avale que el domicilio
              proporcionado existe dentro de la ciudad de mexico, puede ser un
              comprobante de domicilio vigente no mayor a 3 meses.
            </p>
          </div>

          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-12">
            <div class="sm:col-span-12">
              <label-form
                text="Comprobante de domicilio"
                class="text-left"
                required
              ></label-form>
              <div class="mt-1">
                <el-upload
                  ref="uploadRef"
                  class="upload-demo"
                  drag
                  :auto-upload="false"
                  :on-change="onSelectFile"
                  :on-remove="onRemove"
                  :on-success="onSuccess"
                  :limit="1"
                >
                  <el-icon class="el-icon--upload"><upload-filled /></el-icon>
                  <div class="el-upload__text">
                    Arrastra un archivo aqui o <em>haz clic para subir</em>
                  </div>
                  <template #tip>
                    <div
                      class="el-upload__tip block md:flex md:justify-between"
                    >
                      <span> Archivos PNG, JPG o PDF no mayores a 1MB </span>
                      <span v-if="fileRequired" class="text-red-500">
                        {{ fileHelperText }}
                      </span>
                    </div>
                  </template>
                  <template v-slot:file="{ file }">
                    <dd
                      class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2"
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
                              icon="PaperClipIcon"
                              class="flex-shrink-0 h-5 w-5 text-gray-400"
                            ></hero-icon>
                            <span class="ml-2 flex-1 w-0 truncate">
                              {{ file.name }}
                            </span>
                          </div>
                          <div class="ml-4 flex-shrink-0 flex space-x-4">
                            <button
                              @click="deleteFile(file)"
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
                  </template>
                </el-upload>
              </div>
            </div>

            <div class="sm:col-span-6">
              <label-form
                text="Documento a nombre de..."
                class="text-left"
                required
              />
              <div class="mt-1">
                <text-input
                  width="max-w-3xl"
                  :required="true"
                  v-model="form.nombre_comprobante_domicilio"
                />
              </div>
            </div>

            <div class="sm:col-span-6">
              <label-form text="Tipo de documento" class="text-left" required />
              <div class="mt-1">
                <select-input
                  v-model="form.tipo_comprobante_domicilio"
                  :options="comprobantes"
                  width="max-w-3xl"
                  :required="true"
                />
              </div>
            </div>

            <div class="sm:col-span-6">
              <label-form
                text="Fecha del documento"
                class="text-left"
                required
              />
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
                  v-model="form.fecha_comprobante_domiclio"
                  :config="configFechaNacimiento"
                  required
                ></flat-pickr>
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

<script lang="ts">
import { defineComponent, ref, watch } from "vue";
import labelForm from "@/components/forms/LabelForm.vue";
import textInput from "@/components/forms/TextInput.vue";
import SelectInput from "@/components/forms/SelectInput.vue";
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { Spanish } from "flatpickr/dist/l10n/es.js";
import IButton from "@/components/common/IButton.vue";
import "element-plus/es/components/upload/style/css";
import { ElUpload, ElIcon } from "element-plus";
import { UploadFilled } from "@element-plus/icons-vue";
import HeroIcon from "@/components/common/HeroIcon.vue";
import AcuerdosService from "@/services/acuerdos/AcuerdosService";
import ModalTailwind from "@/components/common/ModalTailwind.vue";
import DatosService from "@/services/datos/DatosService";
import AlcaldiasService from "@/services/catalogos/AlcaldiasService";
import CodigoPostalService from "@/services/juez-civico/CodigoPostalService";
import ColoniasService from "@/services/juez-civico/ColoniasService";
import axios from "axios";

export default defineComponent({
  emits: ["saved"],
  components: {
    labelForm,
    textInput,
    SelectInput,
    flatPickr,
    IButton,
    ElUpload,
    ElIcon,
    UploadFilled,
    HeroIcon,
    ModalTailwind,
  },
  setup(props, { emit }) {
    const open = ref(false);
    const openFailed = ref(false);
    const fileRequired = ref(false);
    const isLoadingSelects = ref(false);
    const modalType = ref("success");
    const modalTitle = ref("¡Muchas Gracias!");
    const modalText = ref("Tus datos fueron registrados con éxito.");
    const fileHelperText = ref(
      "El documento de comprobante de domicilio el obligatorio"
    );
    const uploadRef = ref(null);
    const codigos_postales = ref([]);
    const colonias = ref([]);

    const form = ref({
      nombre: "adasd",
      primer_apellido: "asdasd",
      segundo_apellido: "adasd",
      numero_empleado: "13123",
      cuip: "asdasdasd",
      calle: "asdasd",
      entre_calle_1: "asdas",
      entre_calle_2: "asdasd",
      numero_exterior: "123",
      numero_interior: "1231",
      codigo_postal: null,
      colonia: null,
      alcaldia: null,
      correo_electronico: "sdfsdfsdf@Asdad.com",
      telefono: "12312",
      extension: null,
      comprobante_domicilio: null,
      tipo_comprobante_domicilio: 1,
      fecha_comprobante_domiclio: "2022-05-03",
      nombre_comprobante_domicilio: "123123",
      telefono_comprobante_domicilio: "2312",
    });

    const errors = ref({
      nombre: [],
      primer_apellido: [],
      segundo_apellido: [],
      numero_empleado: [],
      cuip: [],
      calle: [],
      entre_calle_1: [],
      entre_calle_2: [],
      numero_exterior: [],
      numero_interior: [],
      codigo_postal: [],
      colonia: [],
      alcaldia: [],
      correo_electronico: [],
      telefono: [],
      extension: [],
      comprobante_domicilio: [],
      tipo_comprobante_domicilio: [],
      fecha_comprobante_domiclio: [],
      nombre_comprobante_domicilio: [],
      telefono_comprobante_domicilio: [],
    });

    const defaultErrors = {
      nombre: [],
      primer_apellido: [],
      segundo_apellido: [],
      numero_empleado: [],
      cuip: [],
      calle: [],
      entre_calle_1: [],
      entre_calle_2: [],
      numero_exterior: [],
      numero_interior: [],
      codigo_postal: [],
      colonia: [],
      alcaldia: [],
      correo_electronico: [],
      telefono: [],
      extension: [],
      comprobante_domicilio: [],
      tipo_comprobante_domicilio: [],
      fecha_comprobante_domiclio: [],
      nombre_comprobante_domicilio: [],
      telefono_comprobante_domicilio: [],
    };

    const defaultForm = {
      nombre: null,
      primer_apellido: null,
      segundo_apellido: null,
      numero_empleado: null,
      cuip: null,
      calle: null,
      entre_calle_1: null,
      entre_calle_2: null,
      numero_exterior: null,
      numero_interior: null,
      codigo_postal: null,
      colonia: null,
      alcaldia: null,
      correo_electronico: null,
      telefono: null,
      extension: null,
      comprobante_domicilio: null,
      tipo_comprobante_domicilio: null,
      fecha_comprobante_domiclio: null,
      nombre_comprobante_domicilio: null,
      telefono_comprobante_domicilio: null,
    };

    const alcaldias = ref([
      {
        id: 1,
        descripcion: "ALVARO OBREGON",
      },
      {
        id: 2,
        descripcion: "AZCAPOTZALCO",
      },
      {
        id: 3,
        descripcion: "BENITO JUAREZ",
      },
      {
        id: 4,
        descripcion: "COYOACAN",
      },
      {
        id: 5,
        descripcion: "CUAJIMALPA DE MORELOS",
      },
      {
        id: 6,
        descripcion: "CUAUHTEMOC",
      },
      {
        id: 7,
        descripcion: "GUSTAVO A MADERO",
      },
      {
        id: 8,
        descripcion: "IZTACALCO",
      },
      {
        id: 9,
        descripcion: "IZTAPALAPA",
      },
      {
        id: 10,
        descripcion: "LA MAGDALENA CONTRERAS",
      },
      {
        id: 11,
        descripcion: "MIGUEL HIDALGO",
      },
      {
        id: 12,
        descripcion: "MILPA ALTA",
      },
      {
        id: 13,
        descripcion: "TLAHUAC",
      },
      {
        id: 14,
        descripcion: "TLALPAN",
      },
      {
        id: 15,
        descripcion: "VENUSTIANO CARRANZA",
      },
      {
        id: 16,
        descripcion: "XOCHIMILCO",
      },
    ]);

    const comprobantes = [
      { id: 1, descripcion: "Estado de cuenta" },
      { id: 2, descripcion: "Ultimo recibo del impuesto predial" },
      {
        id: 3,
        descripcion:
          "Último recibo de los servicios de luz, gas, televisión de paga, internet, teléfono o de agua",
      },
    ];

    const configFechaNacimiento = {
      wrap: true,
      dateFormat: "Y-m-d",
      locale: Spanish,
      maxDate: new Date(),
    };

    watch(
      () => form.value.alcaldia,
      (newValue, oldValue) => {
        if (newValue && newValue !== oldValue) {
          onSelectAlcaldia(newValue.id);
        }
      }
    );

    function onSelectFile(evt) {
      console.log("onSelectFile");
      console.log(evt);
      if (evt.raw) {
        form.value.comprobante_domicilio = evt.raw;
        const elUploadDragger = document.querySelector(".el-upload-dragger");
        elUploadDragger.style.cssText = " ";
        fileHelperText.value = "";
      } else {
        fileHelperText.value = "El documento no es un archivo valido";
      }
    }

    function onRemove(evt) {
      console.log("onRemove");
      console.log(evt);
      form.value.comprobante_domicilio = null;
    }

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
      openFailed.value = true;
    }

    function resetForm() {
      Object.assign(form.value, defaultForm);

      uploadRef.value?.clearFiles();
    }

    function validateFile() {
      let valid = true;
      if (!form.value.comprobante_domicilio) {
        fileRequired.value = true;
        const elUploadDragger = document.querySelector(".el-upload-dragger");
        elUploadDragger.style.cssText += " border-color: red;";
        fileHelperText.value =
          "El documento de comprobante de domicilio el obligatorio";
        valid = false;
      }
      return valid;
    }

    function guardarDatos() {
      // if (!validateFile()) {
      //   return;
      // }

      const formData = new FormData();
      formData.append("nombre", form.value.nombre);
      formData.append("primer_apellido", form.value.primer_apellido);
      formData.append("segundo_apellido", form.value.segundo_apellido);
      formData.append("numero_empleado", form.value.numero_empleado);
      formData.append("cuip", form.value.cuip);
      formData.append("calle", form.value.calle);
      formData.append("entre_calle_1", form.value.entre_calle_1);
      formData.append("entre_calle_2", form.value.entre_calle_2);
      formData.append("numero_exterior", form.value.numero_exterior);
      formData.append("numero_interior", form.value.numero_interior);
      formData.append("codigo_postal", form.value.codigo_postal);
      formData.append("colonia", form.value.colonia);
      formData.append(
        "alcaldia",
        form.value.alcaldia ? form.value.alcaldia.id.toString() : ""
      );
      formData.append("correo_electronico", form.value.correo_electronico);
      formData.append("telefono", form.value.telefono);
      formData.append("extension", form.value.extension ?? "");

      formData.append(
        "tipo_comprobante_domicilio",
        form.value.tipo_comprobante_domicilio.toString()
      );
      formData.append(
        "fecha_comprobante_domiclio",
        form.value.fecha_comprobante_domiclio
      );
      formData.append(
        "nombre_comprobante_domicilio",
        form.value.nombre_comprobante_domicilio
      );
      formData.append(
        "telefono_comprobante_domicilio",
        form.value.telefono_comprobante_domicilio
      );

      if (form.value.comprobante_domicilio) {
        formData.append(
          "comprobante_domicilio",
          form.value.comprobante_domicilio
        );
      }

      Object.assign(errors, defaultErrors);
      AcuerdosService.create(formData)
        .then(() => {
          success();
          resetForm();
          // emitReloadComponents();
        })
        .catch(error => {
          if (axios.isAxiosError(error)) {
            const { response } = error;
            console.log("response");
            console.log(error);

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

          errorMsg();
        })
        .finally(() => {
          //
        });
    }

    function emitReloadComponents() {
      emit("saved", true);
    }

    function deleteFile(file: any) {
      uploadRef.value?.handleRemove(file);
    }

    function onDragEnter() {
      console.log("onDragEnter");
      let el = document.getElementById("file-upload-div");
      el!.classList.add("border-indigo-500");
    }

    function onDragLeave() {
      console.log("onDragLeave");
      let el = document.getElementById("file-upload-div");
      el!.classList.remove("border-indigo-500");
    }

    function openFileSelect() {
      const upload = document.getElementById("file-upload");
      if (upload !== null) {
        upload.click();
      }
    }

    function getDataEmpleado() {
      DatosService.getDatosEmpleadoSap();
    }

    function onCloseModal() {
      open.value = false;
      emitReloadComponents();
    }

    function getAlcaldiasJC() {
      AlcaldiasService.getAlcaldias().then((response) => {
        alcaldias.value = response.data.data;
      });
    }

    function getCodigosPostalesJC(newValue: Number) {
      return CodigoPostalService.getCodigosPostalesJC({ alcaldia: newValue });
    }

    function getColoniasJC(newValue: Number) {
      return ColoniasService.getColoniasJC({ alcaldia: newValue });
    }

    async function onSelectAlcaldia(newValue: Number) {
      isLoadingSelects.value = true;
      Promise.all([
        getCodigosPostalesJC(newValue),
        getColoniasJC(newValue),
      ]).then((values) => {
        codigos_postales.value = values[0].data.data;
        colonias.value = values[1].data.data;

        isLoadingSelects.value = false;
      });
      // await getCodigosPostalesJC()
      // await getColoniasJC()
    }

    return {
      form,
      alcaldias,
      onSelectFile,
      comprobantes,
      configFechaNacimiento,
      guardarDatos,
      openFileSelect,
      onDragEnter,
      onDragLeave,
      deleteFile,
      onRemove,
      open,
      fileRequired,
      onSuccess,
      fileHelperText,
      modalType,
      modalTitle,
      modalText,
      errors,
      getDataEmpleado,
      uploadRef,
      onCloseModal,
      getAlcaldiasJC,
      getCodigosPostalesJC,
      getColoniasJC,
      onSelectAlcaldia,
      isLoadingSelects,
      codigos_postales,
      colonias,
      openFailed,
    };
  },
  mounted() {
    this.getDataEmpleado();
    this.getAlcaldiasJC();
  },
});
</script>

<style>
.el-upload-list__item-file-name {
  color: rgb(24, 74, 124);
}
</style>