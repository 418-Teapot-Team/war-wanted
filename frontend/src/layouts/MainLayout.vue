<template>
  <AppHeader />
  <main class="flex w-full justify-center items-start mt-0 md:pt-16">
    <div class="container flex flex-col justify-center items-center pt-8 pb-8">
      <router-view />
    </div>
  </main>
</template>

<script setup>
import AppHeader from '@/components/partial/AppHeader.vue';
</script>
