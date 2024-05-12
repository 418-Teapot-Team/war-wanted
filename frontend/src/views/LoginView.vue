<template>
  <div class="w-full h-screen flex justify-center items-center">
    <form class="bg-backdrop p-8 flex flex-col gap-y-4 items-center" @submit.prevent="submit">
      <h1 class="text-xl">Вхід</h1>
      <AppPlainInput placeholder="E-mail" class="w-56" v-model.trim="email" />
      <AppPlainInput type="password" placeholder="Пароль" class="w-56" v-model.trim="password" />
      <AppButton text="Увійти" type="submit" />
    </form>
  </div>
</template>
<script setup>
import AppPlainInput from '@/components/atoms/inputs/AppPlainInput.vue';
import AppButton from '@/components/atoms/buttons/AppButton.vue';
import { ref } from 'vue';
import { useIndexStore } from '@/stores';
import { useRouter } from 'vue-router';

const store = useIndexStore();
const email = ref('');
const password = ref('');
const router = useRouter();

function submit() {
  store.login(email.value, password.value).then(() => {
    router.push('/');
  });
}
</script>
