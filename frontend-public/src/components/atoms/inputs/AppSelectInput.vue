<template>
  <div class="border-b-2 border-gray-800 bg-transparent flex justify-between h-9 w-full">
    <select v-model="selectedValue" name="states" id="states"
      class="bg-inherit border outline-none border-transparent focus:border-transparent focus:ring-0 w-full">
      <option disabled selected>{{ label }}</option>
      <option v-for="(option, index) in options" :key="index" :value="option.id">
        {{ option.label }}
      </option>
    </select>
    <!-- <v-select class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" v-model="model"
      :options="options" :label="label" :reduce="(option) => option[dataKey]" v-bind="$attrs" /> -->
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useFoundData } from '@/stores/foundData';

const store = useFoundData()
const selectedValue = ref('');

// const updateInfo = () => {
//   store.data[`${name}`] = selectedValue.value;
//   console.log(store.data[`${name}`]);
// }
const props = defineProps(['name', 'options', 'label', 'dataKey']);

watch(selectedValue, () => {
  store.data[`${props.name}`] = selectedValue.value;
  console.log(`${props.name}`)
  console.log(store.data[`${props.name}`]);
})


</script>

<style scoped>
/* Apply custom styles only within this component */
.vs__dropdown-toggle {
  border: none !important;
}
</style>
