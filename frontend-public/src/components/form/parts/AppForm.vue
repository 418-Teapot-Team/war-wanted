<template>
    <section>
        <div class="grid grid-rows-7 grid-flow-col gap-4">
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Ім'я" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Прізвище" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="По батькові" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Вік" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Зріст" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Колір волосся" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Колір очей" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Час" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class="border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Місце" class="flex-auto w-full h-full bg-transparent">
                <button @click="openMap" class=" w-full h-full bg-transparent w-9">
                    <img src="/images/map.png" alt="" class="w-full h-full object-contain">
                </button>
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Стать" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Стан" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Зовнішній вигляд" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" border-b border-gray-800 bg-transparent flex justify-between h-9">
                <input type="text" placeholder="Особливі характеристики" class="flex-auto w-full h-full bg-transparent">
            </div>
            <div class=" bg-transparent flex justify-between h-9">
                <textarea placeholder="Опис ..."
                    class=" border-b border-t-0 border-l-0 border-r-0 border-grey-dark flex-auto w-full h-full bg-transparent"></textarea>
            </div>
        </div>
    </section>
</template>

<script setup>
// import { ref } from 'vue';

const openMap = () => {
    console.log("map is opened");
}

</script>

<style lang="scss" scoped></style>