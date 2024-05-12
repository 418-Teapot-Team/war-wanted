<template>
  <div
    class="bg-backdrop flex flex-col justify-start items-center w-full gap-y-1 px-8 py-8 sm:py-4 relative"
  >
    <span class="flex justify-end items-end gap-x-1 absolute right-2 sm:right-8 top-2 sm:top-4">
      <CalendarIcon class="w-5 h-5" />
      <span class="text-xs text-gray-600">{{ data.found_date }}</span></span
    >
    <div class="flex justify-start flex-col sm:flex-row items-center w-full gap-x-4">
      <div class="flex justify-center items-center max-h-[214px] max-w-[214px]">
        <img
          :src="
            data?.image_path
              ? 'https://storage.googleapis.com/dataface-hackaton/' + data.image_path
              : '/images/Thumb.jpeg'
          "
          width="214"
          height="214"
        />
      </div>
      <div
        class="flex flex-col justify-start items-center sm:items-start gap-y-2 sm:gap-y-0.5 w-full"
      >
        <span class="text-2xl font-semibold">{{ `${data.name} ${data.surname}` }}</span>
        <span class="text-lg text-green-800">{{ data.conditon }}</span>

        <span class="flex justify-start items-center gap-x-2"
          ><PhoneIcon class="w-5 h-5" /><span>{{ data.found_by_phone }}</span></span
        >
        <span class="flex justify-start items-baseline gap-x-1"
          ><LocationIcon class="w-4 h-4" /><span>{{ data.country_of_origin }}</span></span
        >
        <div class="w-full flex justify-center sm:justify-end items-center gap-x-4">
          <span class="text-sm font-semibold text-gray-600"
            >Знайдено: {{ data.possible_matches_sum }}</span
          >
          <AppButton type="button" text="Детальніше" @click="$router.push('/details/' + data.id)" />
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import AppButton from './atoms/buttons/AppButton.vue';
import CalendarIcon from './icons/CalendarIcon.vue';
import LocationIcon from './icons/LocationIcon.vue';
import PhoneIcon from './icons/PhoneIcon.vue';

defineProps(['data']);
</script>
