//foundData
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { httpClient } from '@/utils/HttpClient';

// const api = import.meta.env.VITE_BASE_API;
const api = 'http://34.107.31.175:8001/api';

export const useFoundData = defineStore('foundData', () => {
  // const volunteers = ref([
  //   {
  //     image: '/images/Profile.png',
  //     full_name: 'Mykola Balii',
  //     phone: '3809798672',
  //   },
  // ]);

  const image = ref(null);
  const data = ref({
    found_date: '2024-04-09 10:22',
    found_lon: '49.83189875686011',
    found_lat: '24.008762581071814',
    found_by_number: '+380998992929',
    condition: 'dead',
      age: 18,
    height: 180,
  });

  async function postFoundData() {
    // Convert Uint8Array to Blob
    const imageBlob = new Blob([image.value], { type: 'image/jpeg' }); // Change 'image/jpeg' to the appropriate MIME type if needed

    const formData = new FormData();
    formData.append('image', imageBlob);
    formData.append('data', JSON.stringify(data.value));

    console.log([...formData.entries()]);
    // httpClient
    //   .post(api + '/found/add', formData)
    //   .then((response) => {
    //     // Handle response
    //     console.log('Upload successful:', response.message);
    //   })
    //   .catch((error) => {
    //     // Handle error
    //     console.error('Upload failed:', error);
    //   });

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
