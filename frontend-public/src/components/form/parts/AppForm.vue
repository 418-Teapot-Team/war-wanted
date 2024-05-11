<template>
    <section>
        <div class="grid grid-rows-7 grid-flow-col gap-4">
            <div v-for="(input, index) in inputs" :key="index" class=" border-b border-gray-400 ">
                <input :type="input.type" :placeholder="input.label" class="w-full h-full">
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue';


const inputs = ref([
    {
        "type": "text",
        "label": "Ім'я",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Прізвище",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "По батькові",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Вік",
        "icon": "",
        "validateFunction": "validateAge",
    },
    {
        "type": "text",
        "label": "Зріст",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Колір волосся",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Колір очей",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Час",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Місце",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Стать",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Стан",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Зовнішній вигляд",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Особливі характеристики",
        "icon": "",
        "validateFunction": "",
    },
    {
        "type": "text",
        "label": "Опис ...",
        "icon": "",
        "validateFunction": "",
    },
])
</script>

<style lang="scss" scoped></style>