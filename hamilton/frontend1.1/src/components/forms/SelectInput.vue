<template>
  <select
    :id="id"
    :name="name"
    autocomplete="country-name"
    class="
      block
      focus:ring-maincolor-500 focus:border-maincolor-500
      w-full
      shadow-sm
      sm:text-sm
      border-gray-300
      rounded-md
    "
    :class="[width, classe, disabled ? 'cursor-not-allowed bg-gray-100': '']"
    v-model="currentValue"
    :required="required"
    :disabled="disabled"
  >
    <option :value="null">----- SELECCIONA UNA OPCIÓN -----</option>
    <option v-for="option in options" :key="option.id" :value="valueProp === 'object' ? option : option[valueProp]">
      {{ option[textProp] }}
    </option>
  </select>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { ref, watch, PropType } from "vue";

export default defineComponent({
  emits: ["update:modelValue"],
  props: {
    classe: String,
    id: String,
    name: String,
    type: {
      type: String,
      default: "text",
    },
    width: {
      type: String,
      default: "sm:max-w-xs",
    },
    modelValue: {
      type: [Number , String , Object],
      default: null,
    },
    required: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    options: {
      type: Array,
      default: () => [],
    },
    valueProp: {
      type: String,
      default: "id",
    },
    textProp: {
      type: String,
      default: "descripcion",
    },
  },
  setup(props, { emit }) {
    const currentValue = ref(null);

    watch(currentValue, (newValue, oldValue) => {
      emit("update:modelValue", newValue);
    });

    watch(
      () => props.modelValue,
      (newValue, oldValue) => {
        if (newValue !== oldValue) {
          currentValue.value = newValue ? newValue : null;
        }
      },
      { immediate: true }
    );

    return { currentValue };
  },
});
</script>
