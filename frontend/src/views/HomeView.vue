<template>
  <div class="grid grid-cols-1 xl:grid-cols-2 gap-8 w-full">
    <AppCard v-for="item in data" :key="item.id" :data="item" />
  </div>
</template>

<script setup>
import AppCard from '@/components/AppCard.vue';

import { useIndexStore } from '@/stores';
import { onBeforeMount, ref } from 'vue';
const store = useIndexStore();

const data = ref([]);

onBeforeMount(() => {
  store.fetchAll().then((res) => {
    data.value = res.result;
  });
});
</script>
