<template>
  <button
    ref="el"
    @click="onClick"
    @mouseenter="startAnimation"
    @mouseleave="stopAnimation"
    :type="type"
    class="px-6 h-10 flex justify-center items-center rounded-full bg-black text-white hover:shadow-sm"
  >
    <span>{{ text }} </span>
  </button>
</template>
<script setup>
import { ref } from 'vue';

defineProps(['type', 'text', 'variant']);
const emit = defineEmits(['click']);

const el = ref(null);

function startAnimation() {
  el.value.classList.add('animate-gradient');
}

function stopAnimation() {
  el.value.classList.remove('animate-gradient');
}

function onClick() {
  emit('click');
}
</script>
<style lang="scss" scoped>
.animate-gradient {
  background-image: linear-gradient(
    90deg,
    #244132,
    #295236,
    #2f5c3a,
    #34653e,
    #3a6e42,
    #407747,
    #46804b,
    #4c8950,
    #528254,
    #578c58,
    #5d955c
  );
  background-size: 400% 400%;
  animation: gradient 5s infinite linear; /* cubic-bezier easing */
}

@keyframes gradient {
  0%,
  100% {
    background-position: 0% 50%;
  }
  20% {
    background-position: 20% 50%;
  }
  40% {
    background-position: 40% 50%;
  }
  60% {
    background-position: 60% 50%;
  }
  80% {
    background-position: 80% 50%;
  }
}
</style>
