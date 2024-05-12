<template>
  <div class="border-b-2 border-black flex justify-end items-center">
    <vee-field
      v-maska
      data-maska="+38(0##)-###-##-##"
      type="text"
      :placeholder="label"
      class="w-full bg-transparent placeholder-green placeholder-opacity-[92%]"
      name="found_by_number"
    />
    <ErrorMessage name="found_by_number" class="text-red-500 text-xs" />
  </div>
</template>
<script setup>
defineProps(['label']);
</script>
