<template>
    <div class="bg-transparent flex justify-between h-9">
        <textarea v-model="data" @input="debouncedUpdateInfo" placeholder="Опис... (зовнішній вигляд, додаткові ознаки)"
            class="border-[2px] border-black flex-auto w-full h-[100px] bg-transparent focus:ring-0"></textarea>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useFoundData } from '@/stores/foundData';
import { debounce } from 'lodash';

const store = useFoundData()
const data = ref()

defineProps(['name', 'label', 'type']);

// Define a debounced version of the updateInfo function
const debouncedUpdateInfo = debounce(() => {
    store.data["appearence"] = data.value;
    console.log(store.data["appearence"]);
}, 500); // Adjust the debounce delay as needed (e.g., 500 milliseconds)

</script>

<style lang="scss" scoped></style>
