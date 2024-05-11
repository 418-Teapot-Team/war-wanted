<template>
  <button @click="onClick" :type="type" class="px-3 py-1 rounded-md bg-primary">{{ text }}</button>
</template>
<script setup>
defineProps(['type', 'text', 'variant']);
const emit = defineEmits(['click']);

function onClick() {
  emit('click');
}
</script>
