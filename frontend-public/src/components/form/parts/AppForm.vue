<template>
  <section
    class="grid grid-cols-4 lg:grid-cols-5 h-full gap-9 overflow-auto lg:overflow-hidden p-2"
  >
    <div class="col-span-4 lg:col-span-3">
      <div class="flex flex-col gap-4">
        <div class="col-span-4 lg:col-span-2 block lg:hidden">
          <AppPhotoInput />
        </div>
        <AppTimeInput />
        <PlaceInput />
        <AppPhoneInput label="Ваш номер телефону" />
        <AppSelectInput v-model="state" label="Оберіть стан" dataKey="id" :options="states" />
      </div>
      <div class="flex justify-center">
        <button class="p-3" @click="toggle_more_info">
          <DoubleArrowDown />
        </button>
      </div>
      <div v-if="add_more_info" class="grid grid-rows-7 sm:grid-flow-col gap-y-6 gap-x-6">
        <AppPlainInput name="name" label="Ім'я" type="text" />
        <AppPlainInput name="lastname" label="Прізвище" type="text" />
        <AppPlainInput name="patronymic" label="По батькові" type="text" />
        <AppPlainInput name="age" label="Вік" type="number" />
        <AppPlainInput name="height" label="Зріст" type="number" />
        <AppPlainInput name="eyes_color" label="Колір очей" type="text" />
        <AppPlainInput name="hair_color" label="Колір волосся" type="text" />
        <AppPlainInput name="foot_size" label="Розмір ноги" type="number" />
        <AppSelectInput v-model="gender" label="Стать" dataKey="id" :options="genders" />
        <AppPlainInput name="condition" label="Стан" />
        <AppPlainInput name="appearence" label="Зовнішній вигляд" type="text" />
        <AppPlainInput name="specific_signs" label="Особливі прикмети" type="text" />

        <div class="bg-transparent flex justify-between h-9">
          <textarea
            placeholder="Опис ..."
            class="border-[2px] border-black flex-auto w-full h-[100px] bg-transparent focus:border-transparent focus:ring-0"
          ></textarea>
        </div>
      </div>
      <div class="flex justify-center mt-5">
        <!-- TODO: захуячити переливання -->
        <button
          class="rounded-md bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 transition-colors duration-300 ease-in-out"
          @click="sendData">
          Відправити
        </button>
      </div>
    </div>
    <div class="col-span-4 lg:col-span-2 hidden lg:block">
      <AppPhotoInput />
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import DoubleArrowDown from '@/components/icons/DoubleArrowDown.vue';
import AppSelectInput from '@/components/atoms/inputs/AppSelectInput.vue';
import AppPlainInput from '@/components/atoms/inputs/AppPlainInput.vue';
import AppPhoneInput from '@/components/atoms/inputs/AppPhoneInput.vue';
import PlaceInput from '../../atoms/inputs/AppPlaceInput.vue';
import AppPhotoInput from '@/components/atoms/inputs/AppPhotoInput.vue';
import AppTimeInput from '@/components/atoms/inputs/AppTimeInput.vue';
import { useFoundData } from '@/stores/foundData';

const foundDataStore = useFoundData();

const add_more_info = ref(false);

const state = ref(null);
const gender = ref(null);

const sendData = () => {
  foundDataStore.postFoundData();
}

const toggle_more_info = () => {
  add_more_info.value = !add_more_info.value;
};

const genders = ref([
  {
    label: 'Чоловік',
    id: 'male',
  },
  {
    label: 'Жінка',
    id: 'female',
  },
]);
const states = ref([
  {
    label: 'Живий',
    id: 'alive',
  },
  {
    label: 'Мертвий',
    id: 'dead',
  },
  {
    label: 'Полонений',
    id: 'captured',
  },
]);
</script>

<style lang="scss" scoped></style>
