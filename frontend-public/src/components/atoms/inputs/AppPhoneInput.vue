<template>
  <div class="border-b-2 border-gray-800 bg-transparent flex justify-between h-9">
    <vee-field
      v-maska
      data-maska="+38(0##)-###-##-##"
      type="text"
      :placeholder="label"
      class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0"
      name="found_by_number"
    />
    <ErrorMessage name="found_by_number" class="text-red-500 text-xs" />
  </div>
</template>
<script setup>
defineProps(['label']);
</script>
