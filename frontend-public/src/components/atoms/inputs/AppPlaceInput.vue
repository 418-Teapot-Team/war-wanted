<template>
  <section>
    <div class="grid grid-rows-7 grid-cols-4 gap-4">
      <div v-for="(input, index) in inputs" :key="index" class="border-b-2 border-black col-span-2">
        <input
          :type="input.type"
          :placeholder="input.label"
          class="w-full h-full bg-transparent placeholder-green placeholder-opacity-[92%]"
        />
      </div>
      <div class="border-b-2 border-black col-span-2">
        <vue-google-autocomplete
          id="map"
          class="w-full h-full bg-transparent placeholder-green placeholder-opacity-[92%]"
          placeholder="Start typing"
          v-on:placechanged="getAddressData"
          country="ua"
        >
        </vue-google-autocomplete>
      </div>
    </div>
  </section>
  <GoogleMap style="width: 100%; height: 500px" :center="center" :zoom="15">
    <Marker :options="{ position: center }" />
  </GoogleMap>
</template>

<script setup>
import { ref } from 'vue';
import { GoogleMap, Marker } from 'vue3-google-map';
import VueGoogleAutocomplete from 'vue-google-autocomplete';

const center = ref({ lat: 40.689247, lng: -74.044502 });

const inputs = ref([
  {
    type: 'text',
    label: "Ім'я",
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Прізвище',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'По батькові',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Вік',
    icon: '',
    validateFunction: 'validateAge',
  },
  {
    type: 'text',
    label: 'Зріст',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Колір волосся',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Колір очей',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Час',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Місце',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Стать',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Стан',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Зовнішній вигляд',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Особливі характеристики',
    icon: '',
    validateFunction: '',
  },
  {
    type: 'text',
    label: 'Опис ...',
    icon: '',
    validateFunction: '',
  },
]);
</script>

<style lang="scss" scoped></style>