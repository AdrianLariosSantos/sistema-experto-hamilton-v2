<template>
  <!-- Punto de inicio del template -->
  <div class="h-full">
    <component :is="layout">
      <router-view />
    </component>
    <!-- <scroll-to-top v-if="enableScrollToTop" /> -->
    <notification/>
  </div>
</template>

<script lang="ts">
const LayoutHorizontal = import(
  "@/components/layouts/horizontal/IndexHorizontal.vue"
);
const LayoutFull = import("@/components/layouts/full/IndexFull.vue");
const Notification = import("@/components/common/Notification.vue");
import { defineAsyncComponent } from "vue";
import { useRouter, useRoute } from "vue-router";
import { defineComponent } from "vue";

export default defineComponent({
  components: {
    "layout-horizontal": defineAsyncComponent(() => LayoutHorizontal),
    "layout-full": defineAsyncComponent(() => LayoutFull),
    Notification
  },
  setup() {
    const router = useRouter();
    const route = useRoute();

    return { router, route };
  },
  computed: {
    layout() {
      if (this.route.meta.layout === "full") {
        return "layout-full";
      } else if (this.route.meta.layout === "horizontal") {
        return "layout-horizontal";
      }
    },
    contentLayoutType() {
      return "horizontal";
    },
  },
});
</script>
