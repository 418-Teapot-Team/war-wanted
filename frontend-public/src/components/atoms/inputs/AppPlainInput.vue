<template>
  <div class="border-b-2 border-gray-800 bg-transparent h-9">
    <input :name="name" class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0"
      :placeholder="label" :type="type" />
  </div>
</template>
<script setup>
defineProps(['name', 'label', 'type']);
</script>
