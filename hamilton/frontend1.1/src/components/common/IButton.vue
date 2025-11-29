<template>
    <button
      :type="type"
      class="
        items-center
        border border-transparent
        font-medium
        rounded-md
        shadow-sm
        text-white
        focus:outline-none
        focus:ring-2
        focus:ring-offset-2
      "
      :class="[this.class, classe, variant, {'w-full': block }]"
      @click="router.push(to)"
    >
      <slot/>
    </button>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  props: {
    size: {
      type: String,
      default: "default",
    },
    type: {
      type: String,
      default: "button",
    },
    variant: {
      type: String,
      default: "default",
    },
    class: {
      type: String,
      default: ""
    },
    block: {
      type: Boolean,
      default: false
    },
    to: {
      type: Object,
      default: () => {
        return {
          'path': '#'
        }
      }
    }
  },
  setup(props) {

    const router = useRouter();

    let classe = "px-4 py-2 text-sm";

    if (props.size === "xs") {
      classe = "px-2.5 py-1.5 text-xs";
    } else if (props.size === "sm") {
      classe = "px-3 py-2 text-sm";
    } else if (props.size === "lg") {
      classe = "px-4 py-2 text-base";
    } else if (props.size === "xl") {
      classe = "px-6 py-3 text-base";
    }

    let variant = "bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500"
    if (props.variant === 'orange') {
      variant = `bg-orange-600 hover:bg-orange-700 focus:ring-orange-500`
    } else if (props.variant === 'maincolor') {
      variant = `bg-maincolor-600 hover:bg-maincolor-700 focus:ring-maincolor-500`

    }

    return { classe, variant, router };
  },
});
</script>
