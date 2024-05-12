<template>
  <div
    class="fixed top-0 left-0 right-0 bottom-0 z-10 bg-black/20 flex justify-center items-center max-h-screen overflow-y-auto"
    v-if="userData"
  >
    <div class="bg-backdrop w-[1100px] h-[550px] m-10 overflow-y-auto relative">
      <button class="absolute right-2 top-2" @click="closeModal">
        <CloseIcon class="w-4 h-4" />
      </button>
      <div
        class="flex flex-col items-center md:items-start gap-y-10 md:gap-y-0 md:flex-row px-10 py-5 gap-x-10 xl:gap-x-20"
      >
        <div>
          <div class="flex justify-center items-center max-h-[50svh] w-72">
            <img
              :src="
                userData?.image_path
                  ? 'https://storage.googleapis.com/dataface-hackaton/' + userData?.image_path
                  : '/images/Thumb.jpeg'
              "
              class="w-full h-full object-contain"
            />
          </div>
          <div class="flex flex-col justify-start items-start gap-y-3 pt-3">
            <span class="text-2xl font-semibold">{{
              `${userData?.name} ${userData?.surname}`
            }}</span>
            <span class="text-lg text-green-800">{{ userData?.condition }}</span>

            <span class="flex justify-start items-center gap-x-2"
              ><PhoneIcon class="w-5 h-5" /><span>{{ userData?.found_by_number }}</span></span
            >
            <span class="flex justify-start items-baseline gap-x-3"
              ><LocationIcon class="w-4 h-4" /><span>{{ userData?.country_of_origin }}</span></span
            >
          </div>
        </div>
        <div class="text-md lg:text-xl">
          <ul class="grid gap-1 xl:flex flex-col justify-start items-start xl:gap-y-2">
            <li class="flex justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Стать: </span>
              <span class="pl-2">{{ userData?.gender }}</span>
            </li>

            <li class="flex justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Країна походження: </span>
              <span class="pl-2">{{ userData?.country_of_origin }}</span>
            </li>
            <li class="flex justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Вік: </span>
              <span class="pl-2">{{ userData?.age }}</span>
            </li>
            <li class="flex justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Зріст: </span>
              <span class="pl-2">174см.</span>
            </li>

            <li class="flex justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Колір очей: </span>
              <span class="pl-2">{{ userData?.eyes_color }}</span>
            </li>
            <li class="flex justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Колір волосся: </span>
              <span class="pl-2">{{ userData?.hair_color }}</span>
            </li>
            <li class="flex justify-start items-baseline">
              <span class="text-xl font-semibold">Розмір ноги: </span>
              <span class="pl-2">{{ userData?.foot_size }}</span>
            </li>
            <li class="flex flex-col justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Особливі ознаки: </span>
              <span class="">{{ userData?.specific_signs }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onBeforeMount, computed, watch } from 'vue';
import { useModalStore } from '@/components/stores/matchesModal';
import PhoneIcon from '@/components/icons/PhoneIcon.vue';
import LocationIcon from '@/components/icons/LocationIcon.vue';
import CloseIcon from '../icons/CloseIcon.vue';
import { useIndexStore } from '@/stores';

const store = useIndexStore();
const modalStore = useModalStore();

function closeModal() {
  modalStore.openModal(false);
}

const userId = computed(() => modalStore.selectedItemId);
const userData = ref(null);

watch(
  userId,
  (val) => {
    store.fetchPossible(val).then((res) => {
      userData.value = res;
      console.log(res);
    });
  },
  {
    immediate: true,
  }
);

onBeforeMount(() => {});
</script>
