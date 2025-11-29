<template>
  <div>
    <component :is="currentComponent" @saved="getExistsData" :data="data"> </component>
  </div>
</template>
<script>
import { defineAsyncComponent, defineComponent, ref, watch } from "vue";
const RegistroComponent = import("./RegistroComponent.vue");
const DetalleInscripcionComponent = import("./DetalleInscripcionComponent.vue");

export default defineComponent({
  emits: ["saved"],

  components: {
    "registro-component": defineAsyncComponent(() => RegistroComponent),
    "detalle-inscripcion-component": defineAsyncComponent(
      () => DetalleInscripcionComponent
    ),
  },

  props: {
    data: {
      type: Object,
      default: () => {},
    },
  },
  setup(props, { emit }) {
    let currentComponent = ref("");

    watch(() => props.data, (_, __) => {
        chooseComponent()
    })

    function getExistsData() {
      console.log("emit inscripcion");
      emit("saved", true);
    }

    function chooseComponent() {
        if (props.data) {
            currentComponent.value = "detalle-inscripcion-component";
        } else {
            currentComponent.value = "registro-component";
        }
    }

    return { currentComponent, getExistsData, chooseComponent };
  },
  async mounted() {
    this.chooseComponent()
  },
});
</script>