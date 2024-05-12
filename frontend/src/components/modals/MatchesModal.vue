<template>
  <div
    class="fixed top-0 left-0 right-0 bottom-0 z-10 bg-black/20 flex justify-center items-center max-h-screen overflow-y-auto"
  >
    <div class="bg-backdrop w-[1100px] h-[650px] m-10 overflow-y-auto">
      <button class="right-0" @click="closeModal">X</button>
      <div
        class="flex flex-col items-center md:items-start gap-y-10 md:gap-y-0 md:flex-row px-10 py-2 gap-x-10 xl:gap-x-20"
      >
        <div>
          <div class="flex justify-center items-center max-h-[50svh] w-72">
            <img src="/images/Thumb.jpeg" class="w-full h-full object-contain" />
          </div>
          <div class="flex flex-col justify-start items-start gap-y-3 pt-3">
            <span class="text-2xl font-semibold">Petremko Sidorenko</span>
            <span class="text-lg text-green-800">Знайдено</span>

            <span class="flex justify-start items-center gap-x-2"
              ><PhoneIcon class="w-5 h-5" /><span>+38 (067) 452 43 23</span></span
            >
            <span class="flex justify-start items-baseline gap-x-3"
              ><LocationIcon class="w-4 h-4" /><span>Avdiivka</span></span
            >
          </div>
        </div>
        <div class="text-md lg:text-xl">
          <ul class="grid gap-1 xl:flex flex-col justify-start items-start xl:gap-y-2">
            <li class="flex justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Стать: </span>
              <span class="pl-2">Чоловіча</span>
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
            <li class="flex flex-col justify-start gap-y-1 items-baseline">
              <span class="text-xl font-semibold">Особливі ознаки: </span>
              <span class=""
                >Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat officia ullam totam
                consequatur quisquam eius vitae ratione numquam dolore! Soluta ex distinctio quaerat
                sint dicta eaque sit quidem cumque nesciunt.</span
              >
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import { useModalStore } from '@/components/stores/matchesModal';
import PhoneIcon from '@/components/icons/PhoneIcon.vue';
import LocationIcon from '@/components/icons/LocationIcon.vue';

const modalStore = useModalStore();

function closeModal() {
  modalStore.openModal(false);
}
</script>
