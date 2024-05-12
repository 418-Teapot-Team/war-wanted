<template>
  <div class="border-b-2 border-gray-800 bg-transparent h-9">
    <input :name="name" class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0"
      :placeholder="label" :type="type" @input="updateInfo" v-model="data" />
  </div>
</template>
<script setup>
import { ref } from 'vue';
import { useFoundData } from '@/stores/foundData';

const store = useFoundData()
const data = ref()

const props = defineProps(['name', 'label', 'type']);

const updateInfo = () => {
  store.data[`${props.name}`] = data.value;
}
</script>
