<template>
  <GoogleMap class="w-full h-[250px]" :center="pos" :zoom="15">
    <Marker :options="{ position: pos }" />
  </GoogleMap>
</template>

<script setup>
import { ref } from 'vue';
import { GoogleMap, Marker } from 'vue3-google-map';
const { pos } = defineProps('pos');
</script>