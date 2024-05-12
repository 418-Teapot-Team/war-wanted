//foundData
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { httpClient } from '@/utils/HttpClient';
import { useToast } from 'vue-toast-notification';

const $toast = useToast();

// const api = import.meta.env.VITE_BASE_API;
const api = 'http://34.107.31.175:8001/api';

export const useFoundData = defineStore('foundData', () => {
  const image = ref(null);
  const data = ref({});

  async function postFoundData() {
    // Convert Uint8Array to Blob
    const formData = new FormData();
    console.log(this.image);
    if (this.image) {
      const imageBlob = new Blob([image.value], { type: 'image/jpeg' }); // Change 'image/jpeg' to the appropriate MIME type if needed
      formData.append('image', imageBlob);
    }
    formData.append('data', JSON.stringify(data.value));

    console.log([...formData.entries()]);

    // Make a POST request with fetch
    fetch(api + '/found/add', {
      method: 'POST',
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(response.message);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Success:', data);
        this.data.value = {};
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  return {
    image,
    data,
    postFoundData,
  };
});
