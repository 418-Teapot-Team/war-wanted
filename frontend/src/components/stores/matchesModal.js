import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useModalStore = defineStore('states', () => {
  const isModalOpen = ref(false);

  function openModal(status) {
    isModalOpen.value = status;
  }

  return {
    openModal,
    isModalOpen,
  };
});
