<template>
  <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" fill="none" :stroke="color" class="hover:stroke-primary">
    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
    <g id="SVGRepo_iconCarrier">
      <line x1="20" y1="20" x2="44" y2="44"></line>
      <line x1="44" y1="20" x2="20" y2="44"></line>
      <rect x="8" y="8" width="48" height="48"></rect>
    </g>
  </svg>
</template>

<script setup>
import { ref, watch } from 'vue';

const color = ref('red'); // Default color

// Props
const props = defineProps({
  colorProp: String // Prop for passing color value
});

// Watch for changes in color prop
watch(() => props.colorProp, (newValue) => {
  color.value = newValue; // Update the color value
});
</script>
