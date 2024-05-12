<template>
  <div>
    <div class="border-b-2 border-black flex justify-end items-center">
      <vue-google-autocomplete
        id="place"
        class="w-full bg-transparent"
        placeholder="Місце"
        v-on:placechanged="getAddressData"
        country="ua"
        :value="markerData"
      ></vue-google-autocomplete>
      <button @click="toggleMap">
        <img class="w-7 h-7 pb-1" src="/images/map.png" alt="" />
      </button>
    </div>

    <GoogleMap
      v-if="isMapOpen"
      class="w-full h-[500px]"
      :center="center"
      :zoom="15"
      @click="placeMarker"
    >
      <Marker v-if="markerPosition" :options="{ position: markerPosition }" />
    </GoogleMap>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { GoogleMap, Marker } from 'vue3-google-map';
import VueGoogleAutocomplete from 'vue-google-autocomplete';
import { useFoundData } from '@/stores/foundData';

const store = useFoundData()

const center = ref({ lat: 49.8322405, lng: 23.99730411 });
const isMapOpen = ref(false);
const markerPosition = ref(null);
const markerData = ref(null);

function toggleMap() {
  isMapOpen.value = !isMapOpen.value;
}

function placeMarker(event) {
  markerPosition.value = { lat: event.latLng.lat(), lng: event.latLng.lng() };
  markerData.value = `(${event.latLng.lat()}, ${event.latLng.lng()})`;
  store.data["found_lat"] = `${event.latLng.lat()}`;
  store.data["found_lon"] = `${event.latLng.lng()}`;
}

function getAddressData(place) {
  markerPosition.value = `(${place.geometry.location.lat()}, ${place.geometry.location.lng()})`;
}
</script>

<style lang="scss" scoped></style>
