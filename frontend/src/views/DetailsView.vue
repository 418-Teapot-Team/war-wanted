<template>
  <section id="details" class="grid grid-cols-1 md:grid-cols-2 grid-rows-2 h-full w-full gap-8">
    <div>
      <div class="flex justify-center items-center max-h-[50svh]">
        <img src="/images/Thumb.jpeg" class="w-full h-full object-contain" />
      </div>
    </div>
    <div class="flex flex-col justify-start items-start gap-y-2">
      <span class="text-2xl font-semibold">Petremko Sidorenko</span>
      <span class="text-lg text-green-800">Знайдено</span>

      <span class="flex justify-start items-center gap-x-2"
        ><PhoneIcon class="w-5 h-5" /><span>+38 (067) 452 43 23</span></span
      >
      <span class="flex justify-start items-baseline gap-x-1"
        ><LocationIcon class="w-4 h-4" /><span>Avdiivka</span></span
      >
      <FoundMap class="h-full" />
    </div>
    <div>
      <ul class="flex flex-col justify-start items-start gap-y-3">
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Стать: </span>
          <span class="pl-2">Чоловіча</span>
        </li>
        <li class="flex flex-col justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Особливі ознаки: </span>
          <span class=""
            >Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat officia ullam totam
            consequatur quisquam eius vitae ratione numquam dolore! Soluta ex distinctio quaerat
            sint dicta eaque sit quidem cumque nesciunt.</span
          >
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Країна походження: </span>
          <span class="pl-2">Азербайджан</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Вік: </span>
          <span class="pl-2">31</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Зріст: </span>
          <span class="pl-2">174см.</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Колір очей: </span>
          <span class="pl-2">Блакитний</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Колір волосся: </span>
          <span class="pl-2">Чорний</span>
        </li>
        <li class="flex justify-start items-baseline">
          <span class="text-xl font-semibold">Розмір ноги: </span>
          <span class="pl-2">43</span>
        </li>
      </ul>
    </div>
    <div>
      <Matches />
    </div>
  </section>
</template>
<script setup>
import PhoneIcon from '@/components/icons/PhoneIcon.vue';
import LocationIcon from '@/components/icons/LocationIcon.vue';
import Matches from '@/components/Matches.vue';
import FoundMap from '@/components/atoms/map/FoundMap.vue';
</script>
