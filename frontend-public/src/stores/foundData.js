//foundData
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { httpClient } from '@/utils/HttpClient';

const api = import.meta.env.VITE_BASE_API;

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
        name: 'Ivan',
        surname: 'Ivanov',
        surname: 'Ivanov',
    });
    
   const formData = new FormData();
    formData.append('image', image);
    formData.append('data', data)
    
    async function postFoundData() {
        httpClient
          .post('/found/add', formData)
          .then((response) => {
            // Handle response
            console.log('Upload successful:', response.data);
          })
          .catch((error) => {
            // Handle error
            console.error('Upload failed:', error);
          });
    const response = await fetch(api + '/volunteers/all');
    if (response.ok) {
      this.volunteers = await response.json();
    } else {
      console.error('HTTP-Error: ' + response.status);
    }
  }

  return {
    volunteers,
    fetchVolunteerData,
  };
});
