<template>
  <GoogleMap class="w-full h-[250px]" :center="markerPoint" :zoom="15">
    <Marker :options="{ position: markerPoint }" />
  </GoogleMap>
</template>

<script setup>
import { ref } from 'vue';
import { GoogleMap, Marker } from 'vue3-google-map';
const markerPoint = ref({ lat: 49.8322405, lng: 23.99730411 });
</script>