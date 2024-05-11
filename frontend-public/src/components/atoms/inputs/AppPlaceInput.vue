<template>
  <div class="border-b-2 border-black col-span-2">
    <vue-google-autocomplete
      id="map"
      class="w-full h-full bg-transparent placeholder-green placeholder-opacity-[92%]"
      placeholder="Місце"
      v-on:placechanged="getAddressData"
      country="ua"
    >
    </vue-google-autocomplete>
  </div>
  <GoogleMap class="w-full h-[500px]" :center="center" :zoom="15">
    <Marker :options="{ position: center }" />
  </GoogleMap>
</template>

<script setup>
import { ref } from 'vue';
import { GoogleMap, Marker } from 'vue3-google-map';
import VueGoogleAutocomplete from 'vue-google-autocomplete';

const center = ref({ lat: 40.689247, lng: -74.044502 });
</script>

<style lang="scss" scoped></style>