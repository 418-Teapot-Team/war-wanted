<template>
  <span class="text-xl font-semibold">Співпадіння</span>
  <div class="max-h-[50svh] overflow-y-auto pt-2">
    <div
      class="bg-backdrop flex flex-col justify-start items-center w-full gap-y-1 px-6 py-1 relative"
    >
      <div class="flex justify-start flex-col sm:flex-row items-center w-full gap-x-4">
        <div class="flex justify-center items-center">
          <img src="/images/Thumb.jpeg" width="64" height="64" />
        </div>
        <div class="flex justify-start items-center gap-y-2 sm:gap-y-0.5 w-full">
          <div class="flex flex-col justify-center gapy-0.5 items-start w-full">
            <span class="text-sm font-semibold">Petremko Sidorenko</span>
            <span class="text-xs text-green-800">Знайдено</span>
          </div>
          <div class="flex flex-col justify-start items-start gap-0.5 w-full">
            <span class="flex text-xs justify-start items-center gap-x-2"
              ><PhoneIcon class="w-4 h-4" /><span>+38 (067) 452 43 23</span></span
            >
            <span class="flex text-xs justify-start items-baseline gap-x-1"
              ><LocationIcon class="w-4 h-4" /><span>Avdiivka</span></span
            >
          </div>
          <div class="w-full flex flex-col justify-center gap-y-0.5 items-end gap-x-4">
            <span class="flex justify-end items-center gap-x-1 right-2 top-2">
              <CalendarIcon class="w-5 h-5" />
              <span class="text-xs text-gray-600">25.04.2024</span></span
            >
            <div class="flex justify-end items-baseline gap-x-2">
              <div class="w-6 h-6 flex justify-center items-center">
                <TickIcon class="w-5 h-5 pt-0.5 cursor-pointer" />
              </div>
              <div class="w-5 h-5 flex justify-center items-center">
                <TimerIcon class="w-5 h-5 cursor-pointer" />
              </div>
              <div class="w-6 h-6 flex justify-center items-center">
                <ViewIcon class="w-5 h-5 cursor-pointer" />
              </div>
              <div class="w-6 h-6 ml-5 flex justify-center items-center">
                <DenyIcon class="w-5 h-5 cursor-pointer" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import CalendarIcon from './icons/CalendarIcon.vue';
import DenyIcon from './icons/DenyIcon.vue';
import LocationIcon from './icons/LocationIcon.vue';
import PhoneIcon from './icons/PhoneIcon.vue';
import TickIcon from './icons/TickIcon.vue';
import TimerIcon from './icons/TimerIcon.vue';
import ViewIcon from './icons/ViewIcon.vue';
</script>
