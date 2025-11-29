<template>
  <TransitionRoot as="template" :show="isOpen">
    <Dialog as="div" class="relative z-10" @close="isOpen = false">
      <TransitionChild
        as="template"
        enter="ease-out duration-300"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in duration-200"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
        />
      </TransitionChild>

      <div class="fixed z-10 inset-0 overflow-y-auto">
        <div
          class="
            flex
            items-end
            sm:items-center
            justify-center
            min-h-full
            p-4
            text-center
            sm:p-0
          "
        >
          <TransitionChild
            as="template"
            enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100"
            leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          >
            <DialogPanel
              class="
                relative
                bg-white
                rounded-lg
                px-4
                pt-5
                pb-4
                text-left
                overflow-hidden
                shadow-xl
                transform
                transition-all
                sm:my-8 sm:max-w-sm sm:w-full sm:p-6
              "
            >
              <div>
                <div
                  class="
                    mx-auto
                    flex
                    items-center
                    justify-center
                    h-12
                    w-12
                    rounded-full
                  "
                  :class="[colorType]"
                >
                  <CheckIcon
                    class="h-6 w-6 text-green-600"
                    aria-hidden="true"
                    v-if="type === 'success'"
                  />
                  <XIcon
                    class="h-6 w-6 text-red-600"
                    aria-hidden="true"
                    v-else-if="type === 'error'"
                  />
                </div>
                <div class="mt-3 text-center sm:mt-5">
                  <DialogTitle
                    as="h3"
                    class="text-lg leading-6 font-medium text-gray-900"
                  >
                    {{ title }}
                  </DialogTitle>
                  <div class="mt-2">
                    <p class="text-sm text-gray-500">
                      {{ text }}
                    </p>
                  </div>
                </div>
              </div>
              <div class="mt-5 sm:mt-6">
                <button
                  type="button"
                  class="
                    inline-flex
                    justify-center
                    w-full
                    rounded-md
                    border border-transparent
                    shadow-sm
                    px-4
                    py-2
                    bg-maincolor-600
                    text-base
                    font-medium
                    text-white
                    hover:bg-maincolor-700
                    focus:outline-none
                    focus:ring-2
                    focus:ring-offset-2
                    focus:ring-maincolor-500
                    sm:text-sm
                  "
                  @click="isOpen = false"
                >
                  Cerrar
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { CheckIcon, XIcon } from "@heroicons/vue/outline";

export default defineComponent({
  emits: ["close"],
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
    CheckIcon,
    XIcon,
  },
  props: {
    open: {
      type: Boolean,
      default: false,
    },
    type: {
      type: String,
      default: "success",
    },
    title: {
      type: String,
      default: "",
    },
    text: {
      type: String,
      default: "",
    },
  },
  setup(props, { emit }) {
    const isOpen = computed({
      get() {
        return props.open;
      },
      set(newValue) {
        emit("close", newValue);
      },
    });

    const colorType = computed(() => {
      let classe = "bg-greeen-100";
      if (props.type === "error") {
        classe = "bg-red-100";
      }

      return classe;
    });

    return { isOpen, colorType };
  },
});
</script>
