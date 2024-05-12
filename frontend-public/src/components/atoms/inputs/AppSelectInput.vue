<template>
  <div class="border-b-2 border-gray-800 bg-transparent flex justify-between h-9">
    <select v-model="selectedValue" name="states" id="states"
      class=" bg-inherit border outline-none border-transparent focus:border-transparent focus:ring-0">
      <option disabled selected>{{ label }}</option>
      <option v-for="(option, index) in options" :key="index" :value="option.id">{{ option.label }}</option>
    </select>
    <!-- <v-select class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" v-model="model"
      :options="options" :label="label" :reduce="(option) => option[dataKey]" v-bind="$attrs" /> -->
  </div>
</template>

<script setup>
import { defineModel, ref } from 'vue';

defineProps(['options', 'label', 'dataKey']);
const model = defineModel();

const selectedValue = ref('');
</script>

<style scoped>
/* Apply custom styles only within this component */
.vs__dropdown-toggle {
  border: none !important;
}
</style>
