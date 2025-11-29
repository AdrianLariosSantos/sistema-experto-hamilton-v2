<template>
  <div>
    <landing-header />
    <contents />
    <landing-footer />
  </div>
</template>

<script lang="ts">
import landingHeader from "@/components/landing/LandingHeader.vue";
import landingFooter from "@/components/landing/LandingFooter.vue";
import contents from "./components/MainContent.vue";
import { defineComponent } from "vue";

export default defineComponent({
  components: {
    landingHeader,
    landingFooter,
    contents,
  },
  setup() {},
});
</script>