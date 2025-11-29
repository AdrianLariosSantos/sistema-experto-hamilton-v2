<template>
  <div>
    <input
      :id="id"
      :name="name"
      :type="type"
      class="
        block
        w-full
        shadow-sm
        focus:ring-maincolor-500 focus:border-maincolor-500
        sm:text-sm
        border-gray-300
        rounded-md
        mt-1
        mb-1
      "
      :class="[width, classe, disabled ? 'cursor-not-allowed bg-gray-100' : '']"
      v-model="currentValue"
      :required="required"
      :disabled="disabled"
      :maxlength="maxlength"
      :pattern="pattern"
      :placeholder="placeholder"
    />
    <p class="text-sm text-gray-500 w-full">{{helperText}}</p>
  </div>
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
    helperText: String,
    pattern: String,
    maxlength: String,
    placeholder: String,
    min: [String, Date],
    max: [String, Date],
    type: {
      type: String,
      default: "text",
    },
    width: {
      type: String,
      default: "sm:max-w-xs",
    },
    modelValue: {
      type: [String, Number] as PropType<string | number>,
      default: "",
    },
    required: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    upper: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { emit }) {
    const currentValue = ref("");

    watch(currentValue, (newValue, oldValue) => {
      let val = newValue;
      if (props.upper) {
        val = val.toUpperCase();
      }
      emit("update:modelValue", val);
    });

    watch(
      () => props.modelValue,
      (newValue, oldValue) => {
        if (newValue !== oldValue) {
          currentValue.value = newValue ? newValue.toString() : "";
        }
      },
      { immediate: true }
    );

    return { currentValue };
  },
});
</script>
