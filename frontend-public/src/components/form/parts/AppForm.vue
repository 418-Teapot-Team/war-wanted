<template>
  <section class="grid grid-cols-5 gap-9">
    <div class=" col-span-3">
      <div class="flex flex-col gap-4">
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Час"
            class="flex-auto w-full h-full bg-transparent border-transparent focus:border-transparent focus:ring-0" />
        </div>
        <PlaceInput />
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Контакнтий номер"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <select v-model="person_state" id="person_state" name="person_state"
            class="border-b border-t-0 border-l-0 border-r-0 border-grey-dark text-gray-800 ps-3 bg-transparent focus:border-transparent focus:ring-0 block w-full">
            <option class="text-gray-400" value="" disabled>Оберіть стан</option>
            <option value="male">Живий</option>
            <option value="female">Неживий</option>
            <option value="other">У полоні</option>
          </select>
        </div>
      </div>
      <div class="flex justify-center">
        <button @click="toggle_more_info">
          <DoubleArrowDown />
        </button>
      </div>
      <div v-if="add_more_info" class="grid grid-rows-7 grid-flow-col gap-4">
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Ім'я"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Прізвище"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="По батькові"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Вік"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Зріст"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Колір волосся"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Колір очей"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>

        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Стать"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Зовнішній вигляд"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
          <input type="text" placeholder="Особливі характеристики"
            class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0" />
        </div>
        <div class="bg-transparent flex justify-between h-9">
          <textarea placeholder="Опис ..."
            class="border-b border-t-0 border-l-0 border-r-0 border-grey-dark flex-auto w-full h-48 bg-transparent focus:border-transparent focus:ring-0"></textarea>
        </div>
      </div>
    </div>
    <div class="col-span-2">
      <AppPhotoInput />
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import DoubleArrowDown from '@/components/icons/DoubleArrowDown.vue';
import PlaceInput from '../../atoms/inputs/AppPlaceInput.vue';
import AppPhotoInput from '@/components/atoms/inputs/AppPhotoInput.vue';
const person_state = ref('');
const add_more_info = ref(false);

const toggle_more_info = () => {
  add_more_info.value = !add_more_info.value;
};
</script>

<style lang="scss" scoped></style>
