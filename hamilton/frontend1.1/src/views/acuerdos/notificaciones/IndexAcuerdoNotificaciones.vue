<template>
  <div class="min-h-full">
    <div class="pb-5 border-b border-gray-200 sm:pb-0">
      <h3 class="text-lg leading-6 font-medium text-gray-900">
        Actualizacion de domicilio
      </h3>
      <h4 class="mt-1 text-sm text-gray-500">
        Para oir y recibir notificaciones para dar cumplimiento al acuerdo
        00/2022
      </h4>
      <div class="mt-3 sm:mt-4">
        <div class="sm:hidden">
          <label for="current-tab" class="sr-only">Select a tab</label>
          <select
            id="current-tab"
            name="current-tab"
            class="
              block
              w-full
              pl-3
              pr-10
              py-2
              text-base
              border-gray-300
              focus:outline-none focus:ring-indigo-500 focus:border-indigo-500
              sm:text-sm
              rounded-md
            "
          >
            <option v-for="tab in tabs" :key="tab.name" :selected="tab.current">
              {{ tab.name }}
            </option>
          </select>
        </div>
        <div class="hidden sm:block">
          <nav class="-mb-px flex space-x-8">
            <a
              v-for="tab in tabs"
              :key="tab.name"
              :class="[
                tab.current
                  ? 'border-maincolor-500 text-maincolor-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
                'whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm',
              ]"
              :aria-current="tab.current ? 'page' : undefined"
            >
              {{ tab.name }}
            </a>
          </nav>
        </div>
      </div>
    </div>
    <div class="mt-10">
      <component
        :is="currentComponent"
        :data="exists"
        @saved="getExistsData"
        @change-to-registro="changeTab"
      >
      </component>
    </div>
  </div>
</template>

<script lang="ts">
import { defineAsyncComponent, defineComponent, reactive, ref } from "vue";
const ConvocatoriaComponent = import("./components/ConvocatoriaComponent.vue");
const RegistroComponent = import("./components/RegistroComponent.vue");
const DatosCargadosComponent = import(
  "./components/DatosCargadosComponent.vue"
);
import DatosService from "@/services/datos/DatosService";
import { useDataStore } from "@/store/datos";
import axios from "axios";

export default defineComponent({
  components: {
    "convocatoria-component": defineAsyncComponent(() => ConvocatoriaComponent),
    "registro-component": defineAsyncComponent(() => RegistroComponent),
    "datos-cargados-component": defineAsyncComponent(() => DatosCargadosComponent),
  },
  setup() {
    const tabs = reactive([
      {
        id: 1,
        name: "Tu registro",
        href: "#",
        current: true,
        component: "registro-component",
      },
    ]);

    const exists = ref({
      datos_contacto: false,
      cuip: "",
      numero_empleado: 0,
    });

    const store = useDataStore();

    let currentComponent = ref("registro-component");

    function changeTab(tab) {
      tabs.forEach((e) => {
        if (tab.id !== e.id) {
          e.current = false;
        } else {
          e.current = true;
          currentComponent.value = e.component;
        }
      });
    }

    function getExistsData() {
      return DatosService.getExistsData()
        .then((response) => {
          if (response.data) {
            exists.value = response.data.data;
            currentComponent.value = "datos-cargados-component";
          } else {
            currentComponent.value = "registro-component";
          }
        })
        .catch((error) => {
          if (axios.isAxiosError(error)) {
            // es error de axios (peticion)
          } else {
            // no es error de axios
          }
        });
    }

    store.$subscribe(onVerify);

    function onVerify() {
      console.log("reload");
      getExistsData();
    }

    return {
      tabs,
      changeTab,
      currentComponent,
      ConvocatoriaComponent,
      RegistroComponent,
      getExistsData,
      exists,
    };
  },
  async mounted() {
    await this.getExistsData();
  },
});
</script>
