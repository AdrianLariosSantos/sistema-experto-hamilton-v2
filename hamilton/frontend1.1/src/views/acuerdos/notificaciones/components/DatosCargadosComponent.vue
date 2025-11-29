<template>
  <component :is="currentComponent" :data="data" />
</template>
<script lang="ts">
import { defineComponent, defineAsyncComponent, ref, watch } from "vue";
const ValidarCorreoComponent = import("./ValidarCorreoComponent.vue");
const DescargaComponent = import("./DescargaComponent.vue");

export default defineComponent({
  components: {
    "descarga-component": defineAsyncComponent(() => DescargaComponent),
    "validar-correo-component": defineAsyncComponent(
      () => ValidarCorreoComponent
    ),
  },
  props: {
    data: {
      type: Object,
      default: () => {},
    },
  },
  setup(props) {
    let currentComponent = ref("validar-correo-component");

    function selectComponent() {
      console.log("subscribe");

      if (props.data && props.data.validacion_correo === true) {
        currentComponent.value = "descarga-component";
      } else {
        currentComponent.value = "validar-correo-component";
      }
    }

    watch(
      () => props.data,
      (newValue, oldValue) => {
          selectComponent();
      }
    );

    return {
      currentComponent,
      selectComponent,
    };
  },
  mounted() {
    console.log(this.data.validacion_correo);

    this.selectComponent();
  },
});
</script>
