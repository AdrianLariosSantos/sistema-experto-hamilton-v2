<template>
  <component :class="classe" :is="getIcon()" />
</template>

<script lang="ts">
import { defineComponent, defineAsyncComponent } from "vue";

export default defineComponent({
  props: {
    icon: String,
    classe: {
      type: String,
      default: "XIcon",
    },
    type: {
      type: String,
      default: "outline",
    },
  },
  setup(props) {
    function getIcon() {
      return defineAsyncComponent(
        () =>
          import(`@heroicons/vue/outline/esm/${props.icon}`)
      );
    }

    return {
      getIcon,
    };
  },
});
</script>
