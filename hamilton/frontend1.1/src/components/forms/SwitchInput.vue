<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="mt-2">
    <SwitchGroup as="div" class="flex items-center justify-between">
      <span class="flex-grow flex flex-col">
        <SwitchLabel
          as="span"
          class="text-sm font-medium text-gray-700"
          passive
          >{{ title }}</SwitchLabel
        >
        <SwitchDescription as="span" class="text-sm text-gray-500">{{
          message
        }}</SwitchDescription>
      </span>
      <Switch
        v-model="currentValue"
        :class="[
          currentValue ? 'bg-maincolor-600' : 'bg-gray-200',
          'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-maincolor-500',
        ]"
      >
        <span
          aria-hidden="true"
          :class="[
            currentValue ? 'translate-x-5' : 'translate-x-0',
            'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200',
          ]"
        />
      </Switch>
    </SwitchGroup>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from "vue";
import {
  Switch,
  SwitchDescription,
  SwitchGroup,
  SwitchLabel,
} from "@headlessui/vue";

export default defineComponent({
  emits: ["update:modelValue"],
  props: {
    title: String,
    message: String,
    modelValue: {
      type: Boolean,
      default: false,
    },
    required: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { emit }) {
    const currentValue = ref(false);

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
  components: {
    Switch,
    SwitchDescription,
    SwitchGroup,
    SwitchLabel,
  },
});
</script>
