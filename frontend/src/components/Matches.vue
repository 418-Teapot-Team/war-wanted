<template>
  <span class="text-xl font-semibold">Співпадіння</span>
  <MatchesModal v-if="isMatchesModalOpen" />
  <div v-if="userData" class="max-h-[50svh] overflow-y-auto pt-2">
    <div
      v-for="item in userData.possible_matches"
      :key="item.id"
      :data="item"
      class="bg-backdrop flex flex-col justify-start items-center w-full gap-y-1 px-6 py-1 relative mb-1"
    >
      <div class="flex justify-start flex-col sm:flex-row items-center w-full gap-x-4">
        <div class="flex justify-center items-center">
          <img
            :src="
              userData?.found_person.image_path
                ? 'https://storage.googleapis.com/dataface-hackaton/' +
                  userData.found_person.image_path
                : '/images/Thumb.jpeg'
            "
            width="64"
            height="64"
          />
        </div>
        <div
          class="flex md:grid grid-cols-2 lg:flex justify-start items-center gap-y-2 sm:gap-y-0.5 w-full"
        >
          <div class="col-span-2 flex flex-col justify-center gap-y-0.5 items-start w-full">
            <span class="text-sm font-semibold">{{ `${item.name} ${item.surname}` }}</span>
            <span class="text-xs text-green-800">{{ item.condition }}</span>
          </div>
          <div class="flex flex-col justify-start items-start gap-0.5 w-full">
            <span class="flex text-xs justify-start items-center gap-x-2 lg:w-36 xl:w-fit"
              ><PhoneIcon class="w-4 h-4" /><span>{{ item.found_by_number }}</span></span
            >
            <span class="flex text-xs justify-start items-baseline gap-x-1"
              ><LocationIcon class="w-4 h-4" /><span>{{ item.country_of_origin }}</span></span
            >
          </div>
          <div class="col-span-3 w-full flex flex-col justify-center gap-y-0.5 items-end gap-x-4">
            <span class="flex justify-end items-center gap-x-1 right-2 top-2">
              <CalendarIcon class="w-5 h-5" />
              <span class="text-xs text-gray-600">{{ item.found_date }}</span></span
            >
            <div class="flex justify-end items-baseline gap-x-2">
              <div class="w-6 h-6 flex justify-center items-center">
                <TickIcon class="w-5 h-5 pt-0.5 cursor-pointer" />
              </div>
              <div class="w-5 h-5 flex justify-center items-center">
                <TimerIcon class="w-5 h-5 cursor-pointer" />
              </div>
              <div class="w-6 h-6 flex justify-center items-center">
                <button @click="openMatchModal(item.id)">
                  <ViewIcon class="w-5 h-5 cursor-pointer" />
                </button>
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
import MatchesModal from './modals/MatchesModal.vue';

import { ref, onBeforeMount, computed } from 'vue';
import { useModalStore } from '@/components/stores/matchesModal';
import { useIndexStore } from '@/stores';
import { useRoute } from 'vue-router';

const route = useRoute();
const store = useIndexStore();
const modalStore = useModalStore();

const isMatchesModalOpen = computed(() => modalStore.isModalOpen);

function openMatchModal(itemId) {
  modalStore.setSelectedItemId(itemId);
}

const userData = ref(null);

onBeforeMount(() => {
  store.fetch(route.params.id).then((res) => {
    userData.value = res;
  });
});
</script>
