<template>
  <div class="border-b-2 border-gray-800 bg-transparent flex justify-between h-9">
    <v-select
      class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0"
      v-model="model"
      :options="options"
      :label="label"
      :reduce="(option) => option[`${dataKey}`]"
    />
  </div>
</template>
<script setup>
import { defineModel } from 'vue';

defineProps(['options', 'label', 'dataKey']);

const model = defineModel();
</script>
<style>
.vs__dropdown-toggle {
  border: 0px !important;
}
.input {
  --vs-controls-color: rgb(0, 0, 0);

  --vs-dropdown-bg: rgb(250 250 250);
  --vs-dropdown-color: rgb(250 250 250);
  --vs-dropdown-option-color: #000;

  --vs-selected-bg: #fff;
  --vs-selected-color: #000;

  --vs-search-input-color: #eeeeee;

  --vs-dropdown-option--active-bg: #eeeeee;
  --vs-dropdown-option--active-color: #000;
}
</style>