<template>
  <header
    class="h-fit z-10 relative md:fixed md:h-16 w-full bg-white border-b border-gray-300 shadow-sm flex flex-col md:flex-row justify-between items-center px-4 py-4 md:py-0 gap-y-6"
  >
    <img
      @click="$router.push('/')"
      src="/images/Logo.png"
      alt="Logo"
      width="114"
      height="48"
      class="cursor-pointer"
    />
    <div class="flex flex-col sm:flex-row gap-y-2 sm:gap-y-0 justify-start gap-x-4 items-center">
      <AppPlainInput v-model="search" placeholder="Пошук" class="w-60" />
      <AppButton type="button" text="Знайти" />
    </div>
  </header>
</template>
<script setup>
import { ref } from 'vue';
import AppPlainInput from '../atoms/inputs/AppPlainInput.vue';
import AppButton from '../atoms/buttons/AppButton.vue';

const search = ref('');
</script>
