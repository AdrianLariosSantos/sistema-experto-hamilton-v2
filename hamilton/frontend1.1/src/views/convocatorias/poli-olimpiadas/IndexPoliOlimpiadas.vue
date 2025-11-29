<template>
  <div class="min-h-full">
    <div class="pb-5 border-b border-gray-200 sm:pb-0">
      <h3 class="text-lg leading-6 font-medium text-gray-900">
        Poli Olimpiadas 2022
      </h3>
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
              focus:outline-none
              focus:ring-maincolor-500
              focus:border-maincolor-500
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
              @click="changeTab(tab)"
              class="cursor-pointer"
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
      <component :is="currentComponent" :data="exists" @change-to-registro="changeTab" @saved="getExistsData">
      </component>
    </div>
  </div>
</template>

<script lang="ts">
import { defineAsyncComponent, defineComponent, reactive, ref } from "vue";
const ConvocatoriaComponent = import("./components/ConvocatoriaComponent.vue");
const RegistroComponent = import("./components/RegistroComponent.vue");
const InscripcionComponent = import("./components/InscripcionComponent.vue");
import PoliolimpiadasService from "@/services/convocatorias/PoliolimpiadasService";
import { usePoliOlimpiadasStore } from "@/store/poliolimpiadas";
import axios from "axios";

export default defineComponent({
  components: {
    "convocatoria-component": defineAsyncComponent(() => ConvocatoriaComponent),
    "registro-component": defineAsyncComponent(() => RegistroComponent),
    "inscripcion-component": defineAsyncComponent(() => InscripcionComponent),
  },
  setup() {
    const tabs = reactive([
      {
        id: 1,
        name: "Convocatoria",
        href: "#",
        current: true,
        component: "convocatoria-component",
      },
      {
        id: 2,
        name: "Tu registro",
        href: "#",
        current: false,
        component: "inscripcion-component",
      },
    ]);

    let currentComponent = ref("");

    const exists = ref(null);

    const store = usePoliOlimpiadasStore()

    store.$subscribe(onVerify);

    function onVerify() {
      console.log("reload");
      getExistsData();
    }


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
      return PoliolimpiadasService.getExistsData()
        .then((response) => {
          if (response.data) {
            exists.value = response.data.data;
            changeTab({ id: 2 });
            currentComponent.value = "inscripcion-component";
          } else {
            currentComponent.value = "convocatoria-component";
          }
        })
        .catch((error) => {
          if (axios.isAxiosError(error)) {
            currentComponent.value = "convocatoria-component";
          } else {
            // no es error de axios
          }
        });
    }

    return {
      tabs,
      changeTab,
      currentComponent,
      ConvocatoriaComponent,
      RegistroComponent,
      getExistsData,
      exists
    };
  },
  async mounted() {
    console.log("asd");

    await this.getExistsData();
  },
});
</script>
