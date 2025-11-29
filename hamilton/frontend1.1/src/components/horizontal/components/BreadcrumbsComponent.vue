<template>
  <nav class="flex md:ml-5 md:pl-5 md:border-l-2 md:border-gray-300 h-7" aria-label="Breadcrumb">
    <ol role="list" class="flex items-center space-x-4">
      <li>
        <div>
          <a href="#" class="text-maincolor-300 hover:text-maincolor-700">
            <hero-icon
              icon="HomeIcon"
              class="flex-shrink-0 h-5 w-5"
            ></hero-icon>
            <span class="sr-only">Inicio</span>
          </a>
        </div>
      </li>
      <li v-for="breadcrumb in breadcrumbs" :key="breadcrumb.name">
        <div class="flex items-center">
          <svg
            class="flex-shrink-0 h-5 w-5 text-gray-400"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 20 20"
            aria-hidden="true"
          >
            <path d="M5.555 17.776l8-16 .894.448-8 16-.894-.448z" />
          </svg>
          <a
            :href="breadcrumb.href"
            class="ml-4 text-sm font-medium text-gray-500 "
            :class="breadcrumb.active ? 'text-maincolor-300 hover:text-maincolor-700' : ''"
            :aria-current="breadcrumb.active ? 'page' : undefined"
            >{{ breadcrumb.text }}</a
          >
        </div>
      </li>
    </ol>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import HeroIcon from "@/components/common/HeroIcon.vue";

export default defineComponent({
  components: {
    HeroIcon,
  },
  props: {
    breadcrumbs: {
      type: Array,
      default: () => [],
    },
  },
  setup() {
    const pages = [
      { name: "Projects", href: "#", current: false },
      { name: "Project Nero", href: "#", current: true },
    ];

    return {
      pages
    }
  },
});
</script>
