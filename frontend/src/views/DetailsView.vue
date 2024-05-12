<template>
  <section
    v-if="userData"
    id="details"
    class="grid grid-cols-1 md:grid-cols-2 grid-rows-2 h-full w-full gap-8"
  >
    <div>
      <div class="flex justify-center items-center max-h-[50svh]">
        <img
          :src="
            userData?.found_person.image_path
              ? 'https://storage.googleapis.com/dataface-hackaton/' +
                userData.found_person.image_path
              : '/images/Thumb.jpeg'
          "
          class="w-full object-contain h-[50svh]"
        />
      </div>
    </div>
    <div class="flex flex-col justify-start items-start gap-y-2">
      <span class="text-2xl font-semibold">{{
        `${userData.found_person.name} ${userData.found_person.surname}`
      }}</span>
      <span class="text-lg text-green-800">{{ userData.found_person.condition }}</span>

      <span class="flex justify-start items-center gap-x-2"
        ><PhoneIcon class="w-5 h-5" /><span>{{ userData.found_person.found_by_number }}</span></span
      >
      <span class="flex justify-start items-baseline gap-x-1"
        ><LocationIcon class="w-4 h-4" />{{ userData.found_person.country_of_origin }}<span></span
      ></span>
      <FoundMap class="h-full" :pos="pos" />
    </div>
    <div>
      <ul class="flex flex-col justify-start items-start gap-y-3">
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Стать: </span>
          <span class="pl-2">{{ userData.found_person.gender }}</span>
        </li>
        <li class="flex flex-col justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Особливі ознаки: </span>
          <span class="">{{ userData.found_person.specific_signs }}</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Країна походження: </span>
          <span class="pl-2">{{ userData.found_person.country_of_origin }}</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Вік: </span>
          <span class="pl-2">{{ userData.found_person.age }}</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Зріст: </span>
          <span class="pl-2">{{ userData.found_person.height }} см.</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Колір очей: </span>
          <span class="pl-2">{{ userData.found_person.eyes_color }}</span>
        </li>
        <li class="flex justify-start gap-y-1 items-baseline">
          <span class="text-xl font-semibold">Колір волосся: </span>
          <span class="pl-2">{{ userData.found_person.hair_color }}</span>
        </li>
        <li class="flex justify-start items-baseline">
          <span class="text-xl font-semibold">Розмір ноги: </span>
          <span class="pl-2">{{ userData.found_person.foot_size }}</span>
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
import { ref, onBeforeMount, computed } from 'vue';
import { useIndexStore } from '@/stores';
import { useRoute } from 'vue-router';

const route = useRoute();
const store = useIndexStore();

const userData = ref(null);

onBeforeMount(() => {
  store.fetch(route.params.id).then((res) => {
    userData.value = res;
  });
});

const pos = computed(() => {
  if (userData.value) {
    return {
      lat: userData.value.found_person.found_lat,
      lng: userData.value.found_person.found_lan,
    };
  } else {
    return null;
  }
});
</script>
