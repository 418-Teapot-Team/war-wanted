<template>
  <div class="relative w-full" tabindex="0" ref="inputWrapper">
    <input
      v-model="model"
      :type="type ? type : 'text'"
      :placeholder="placeholder"
      :disabled="!!disabled"
      class="border-b border-solid border-black bg-gray-50 h-10 w-full focus:bg-gray-100 hover:bg-gray-100 duration-100 px-2"
      @focus="isFocused = true"
      @blur="isFocused = false"
      tabindex="1"
    />
    <div
      tabindex="0"
      class="absolute bottom-0 bg-black transition-all left-1/2 transform -translate-x-1/2 h-0.5 duration-300 ease-in-out"
      :class="{
        'w-0': !isFocused,
        'w-full': isFocused,
      }"
    ></div>
  </div>
</template>
<script setup>
import { ref } from 'vue';

defineProps(['type', 'placeholder', 'disabled']);
const inputWrapper = ref(null);
const isFocused = ref(false);
const model = defineModel();
</script>
