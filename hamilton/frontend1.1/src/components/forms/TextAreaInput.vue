<template>
  <textarea
    :id="id"
    :name="name"
    rows="3"
    class="
      shadow-sm
      block
      w-full
      focus:ring-maincolor-500 focus:border-maincolor-500
      sm:text-sm
      border border-gray-300
      rounded-md
    "
    :class="[width, classe]"
    v-model="currentValue"
    :required="required"
    :disabled="disabled"
  />
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { ref, watch } from "vue";

export default defineComponent({
  emits: ["update:modelValue"],
  props: {
    classe: String,
    id: String,
    name: String,
    width: {
      type: String,
      default: "sm:max-w-xs",
    },
    modelValue: String,
    required: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { emit }) {
    const currentValue = ref("");

    watch(currentValue, (newValue, oldValue) => {
      emit("update:modelValue", newValue);
    });

    watch(
      () => props.modelValue,
      (newValue, oldValue) => {
          
        if (newValue !== oldValue) {
          currentValue.value = newValue;
        }
      }
    );

    return { currentValue };
  },
});
</script>
