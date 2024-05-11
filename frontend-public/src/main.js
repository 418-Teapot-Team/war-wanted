import './assets/main.scss';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';

import VeeValidatePlugin from '@/includes/validation';
import Toast from '@/includes/toast';
import VueSelect from '@/includes/v-select';
import Maska from '@/includes/maska';

const app = createApp(App);

// includes
app.use(createPinia());
app.use(router);
app.use(VeeValidatePlugin);
app.use(Toast);
app.use(VueSelect);
app.use(Maska);

app.mount('#app');
