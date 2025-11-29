<template>
  <label
    for="about"
    class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"
    :class="classe"
  >
    {{ text }} <span v-if="required" class="text-red-500">*</span>
  </label>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup(props) {
    props.text;
    props.classe;
  },
  props: {
    text: String,
    classe: String,
    required: Boolean
  },
});
</script>
