<template>
  <div class="min-h-screen overflow-x-hidden flex flex-col">
    <navbar-horizontal />
    <main class="flex-grow">
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <!-- Replace with your content -->
        <div class="px-4 py-4 sm:px-0">
          <router-view v-slot="{ Component }">
            <Transition name="fade" mode="out-in">
              <component :is="Component" />
            </Transition>
          </router-view>
        </div>
        <!-- /End replace -->
      </div>
    </main>
    <horizontal-footer />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useRouter, useRoute } from "vue-router";
import NavbarHorizontal from "@/components/horizontal/NavbarHorizontal.vue";
import LandingFooter from "./components/HorizontalFooter.vue";

export default defineComponent({
  components: {
    NavbarHorizontal,
    LandingFooter,
  },
  setup() {
    const router = useRouter();
    const route = useRoute();

    return { router, route };
  },
});
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s cubic-bezier(0, 0.5, 0.5, 1);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>