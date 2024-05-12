import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useModalStore = defineStore('states', () => {
  const isModalOpen = ref(false);
  const selectedItemId = ref(null);

  function setSelectedItemId(itemId) {
    if (itemId) {
      selectedItemId.value = itemId;
      console.log(selectedItemId.value);
      isModalOpen.value = true;
    } else {
      isModalOpen.value = false;
    }
  }

  function openModal(status) {
    isModalOpen.value = status;
  }

  return {
    openModal,
    isModalOpen,
    setSelectedItemId,
    selectedItemId,
  };
});
