<template>
  <div class="bg-white border-b-4 border-doradobienestar-600">
    <div class="container mx-auto py-5 px-10 md:px-20">
      <div class="flex items-center justify-between">
        <div class="flex-1 min-w-0 w-full md:w-3/5 xl:w-4/5">
          <img
            src="@/assets/images/brand/logo-ssc.png"
            class="h-16  w-auto"
            alt=""
          />
        </div>
        <div
          class="mt-0 md:ml-4 hidden md:block md:w-2/5 xl:w-1/5 border-l-2 min-h-10 md:min-h-16 px-5 text-gray-500 "
        >
          <p class="">
            <span class="hover:text-blue-500 hover:underline"
              ><a href="http://www.cdmx.gob.mx/">CDMX</a></span
            >
            /
            <span class="hover:text-blue-500 hover:underline"
              ><a
                href="https://www.ciudadanos.cdmx.gob.mx/gobierno/gabinete/secretarias"
                >Secretarías</a
              ></span
            >
            / <span class="font-bold">SSC</span>
          </p>
          <p class="mt-2">
            <span class="hover:text-blue-500 hover:underline"
              ><a href="https://www.ssc.cdmx.gob.mx/unidad-de-transparencia"
                >Transparencia</a
              ></span
            >
          </p>
          <p>
            <span class="hover:text-blue-500 hover:underline"
              ><a href="https://www.ssc.cdmx.gob.mx/unidad-de-transparencia"
                >Atención Ciudadana</a
              ></span
            >
          </p>
          <p>
            <span class="hover:text-blue-500 hover:underline"
              ><a href="https://www.ssc.cdmx.gob.mx/unidad-de-transparencia"
                >Tramites y Servicios</a
              ></span
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {
    function gotoform() {
      const element = document.getElementById("mainform");
      element.scrollIntoView();
    }

    return {
      gotoform,
    };
  },
});
</script>

<style>
</style>