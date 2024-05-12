<template>
  <div class="border-b-2 border-black flex justify-end items-center">
    <input
      :name="name"
      class="w-full bg-transparent placeholder-green placeholder-opacity-[92%]"
      :placeholder="label"
    />
  </div>
</template>
<script setup>
defineProps(['name', 'label']);
</script>
