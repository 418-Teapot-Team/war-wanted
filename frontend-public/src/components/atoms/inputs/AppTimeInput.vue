<template>
  <section class="border-b-2 border-gray-800 bg-transparent h-9 flex ">
    <button @click="toggleDateTimePicker" class="w-full h-full flex justify-start">
      <div class="">
        <p class="flex-auto h-full bg-transparent focus:border-transparent focus:ring-0" :class="{
          'text-gray-400':
            !(selectedDate && selectedTime)
        }">
          {{ selectedDate && selectedTime ? 'Дата: ' + selectedDate + ' Час: ' + selectedTime : 'Час взаємодії' }}
        </p>
      </div>
    </button>
    <div>
      <!-- HTML -->
      <div class="relative inline-block">
        <button id="datetimePickerToggle" class="focus:outline-none " @click="toggleDateTimePicker">
          <DateTimeIcon />
        </button>
        <div v-if="isDateTimePickerOpen" id="datetimePickerDropdown"
          class="absolute top-full left-0 mt-2 bg-white border border-gray-300 rounded-md shadow-lg z-10">
          <!-- Date picker -->
          <input @input="updateInfo" type="date"
            class="block w-full px-4 py-2 border-b border-gray-300 focus:outline-none" v-model="tempSelectedDate">

          <!-- Time picker -->
          <input type="time" class="block w-full px-4 py-2 focus:outline-none" v-model="tempSelectedTime">

          <!-- Confirm button -->
          <button
            class="block w-full px-4 py-2 bg-gray-200 text-gray-800 rounded-b-md hover:bg-gray-300 focus:outline-none"
            @click="confirmDateTime">
            Confirm
          </button>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import DateTimeIcon from '@/components/icons/DateTimeIcon.vue';
import { useFoundData } from '@/stores/foundData';

const store = useFoundData()

defineProps(['name', 'label', 'type']);

const updateInfoDate = () => {
  store.data['found_date'] = selectedDate.value + ' ' + selectedTime.value;
  console.log(store.data['found_date']);
}

const selectedDate = ref('');
const selectedTime = ref('');

const tempSelectedDate = ref('');
const tempSelectedTime = ref('');


const isDateTimePickerOpen = ref(false);

function toggleDateTimePicker() {
  isDateTimePickerOpen.value = !isDateTimePickerOpen.value;
}

function confirmDateTime() {
  // Handle selectedDate and selectedTime values
  selectedDate.value = tempSelectedDate.value;
  selectedTime.value = tempSelectedTime.value;
  console.log('Selected Date:', selectedDate.value);
  console.log('Selected Time:', selectedTime.value);
  updateInfoDate();
  toggleDateTimePicker();
}
</script>


<style lang="scss" scoped></style>
