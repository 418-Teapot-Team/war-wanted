<template>
  <div class="border-b-2 border-gray-800 bg-transparent flex justify-between h-9">
    <vee-field v-model="data" v-maska data-maska="+38(0##)-###-##-##" type="text" :placeholder="label"
      class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" name="found_by_number"
      @input="updateInfo" />
    <ErrorMessage name="found_by_number" class="text-red-500 text-xs" />
  </div>
</template>
<script setup>
import { ref } from 'vue';
import { useFoundData } from '@/stores/foundData';

const store = useFoundData()
const data = ref('')

const updateInfo = () => {
  if (data.value.length < 19) {

    var clearedStr = data.value.replace(/\D/g, '');
    clearedStr = '+' + clearedStr;
    store.data["found_by_number"] = clearedStr;
    console.log(store.data["found_by_number"]);
  }
}

defineProps(['label']);
</script>
