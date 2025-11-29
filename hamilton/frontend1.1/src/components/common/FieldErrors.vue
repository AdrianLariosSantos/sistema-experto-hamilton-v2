<template>
  <span v-show="errors.length > 0" class="mt-2 text-xs text-red-600">
    <p v-for="(error, i) in errors" :key="i" class="tw-mb-0">
      {{ error }}
    </p>
  </span>
</template>
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    props: {
        errors: {
            type: Array,
            default: () => []
        }
    },
    setup() {
        // 
    },
})
</script>
