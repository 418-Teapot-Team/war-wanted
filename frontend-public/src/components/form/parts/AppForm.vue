<template>
  <section class="flex flex-col gap-3">
    <div class="flex flex-col gap-4">
      <AppTimeInput />
      <AppPlaceInput />
      <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
        <input
          type="text"
          placeholder="Контакнтий номер"
          class="flex-auto w-full h-full bg-transparent focus:border-transparent focus:ring-0"
        />
      </div>
      <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
        <select
          v-model="person_state"
          id="person_state"
          name="person_state"
          class="border-b border-t-0 border-l-0 border-r-0 border-grey-dark text-gray-800 ps-3 bg-transparent focus:border-transparent focus:ring-0 block w-full"
        >
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
      <AppPlainInput name="name" label="Ім'я" />
      <AppPlainInput name="lastname" label="Прізвище" />
      <AppPlainInput name="patronymic" label="По батькові" />
      <AppPlainInput name="age" label="Вік" />
      <AppPlainInput name="height" label="Зріст" />
      <AppPlainInput name="eyes_color" label="Колір очей" />
      <AppPlainInput name="hair_color" label="Колір волосся" />
      <AppPlainInput name="foot_size" label="Розмір ноги" />
      <AppPlainInput name="gender" label="Стать" />
      <AppPlainInput name="condition" label="Стан" />
      <AppPlainInput name="appearence" label="Зовнішній вигляд" />
      <AppPlainInput name="specific_signs" label="Особливі прикмети" />
      <AppPhoneInput label="Ваш телефон" />
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import DoubleArrowDown from '@/components/icons/DoubleArrowDown.vue';
import AppPlaceInput from '@/components/atoms/inputs/AppPlaceInput.vue';
import AppTimeInput from '@/components/atoms/inputs/AppTimeInput.vue';
import AppPlainInput from '@/components/atoms/inputs/AppPlainInput.vue';
import AppPhoneInput from '@/components/atoms/inputs/AppPhoneInput.vue';
const person_state = ref('');
const add_more_info = ref(false);

const toggle_more_info = () => {
  add_more_info.value = !add_more_info.value;
};
</script>

<style lang="scss" scoped></style>
