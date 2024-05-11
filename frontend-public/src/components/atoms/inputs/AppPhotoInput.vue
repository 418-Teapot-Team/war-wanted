<template>
    <div class="bg-black/20 z-10 fixed top-0 left-0 right-0 bottom-0 flex justify-center items-center"
        @click="closeModal">
        <div class="w-[320px] sm:w-[380px] md:w-[460px] lg:w-[620px] text-center shadow-sm bg-gray-100 border border-black/20 px-16 pt-16 pb-8 relative flex flex-col justify-center items-center gap-y-8"
            @click.stop>
            <div @click="closeModal" class="absolute right-4 top-4 cursor-pointer hover:stroke-primary">
                <CloseIcon class="w-8 h-8" />
            </div>
            <div v-if="!files.length"
                class="border border-dashed border-primary min-h-44 flex justify-center items-center w-full"
                @dragover="dragover" @dragleave="dragleave" @drop="drop">
                <input type="file" multiple name="file" id="fileInput"
                    class="opacity-0 overflow-hidden absolute w-px h-px" @change="onChange" ref="file"
                    accept=".jpg,.jpeg,.png,.webp" />

                <label for="fileInput" class="text-xl block cursor-pointer">
                    <div v-if="isDragging">Release to drop files here.</div>
                    <div v-else>Drop files here or <u class="text-primary">click here</u> to upload.</div>
                </label>
            </div>
            <div class="flex justify-center items-center mt-8" v-if="files.length">
                <div v-for="file in files" :key="file.name"
                    class="flex relative pt-10 px-12 pb-4 border border-black/20">
                    <div @click="remove" class="absolute right-0 top-0 cursor-pointer hover:stroke-primary">
                        <CloseIcon class="w-8 h-8" />
                    </div>
                    <div>
                        <img class="w-24 h-24 rounded bg-gray-500" :src="generateThumbnail(file)" />
                        <p :title="file.name">
                            {{ makeName(file.name) }}
                        </p>
                    </div>
                </div>
            </div>
            <div class="w-full flex justify-center items-center">
                <AppButton type="bUtton" @on-click="upload" text="Завантажити" is-bold />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import CloseIcon from '@/components/icons/CloseIcon.vue';
import AppButton from '@/components/atoms/buttons/AppButton.vue';

const emit = defineEmits(['onUpload', 'closeModal']);

const isDragging = ref(false);
const files = ref([]);

const file = ref(null);

function onChange() {
    files.value = [file.value.files[0]];
}

function generateThumbnail(file) {
    let fileSrc = URL.createObjectURL(file);
    setTimeout(() => {
        URL.revokeObjectURL(fileSrc);
    }, 1000);
    return fileSrc;
}

function makeName(name) {
    return name.split('.')[0].substring(0, 3) + '...' + name.split('.')[name.split('.').length - 1];
}

function remove() {
    files.value = [];
}

function dragover(e) {
    e.preventDefault();
    isDragging.value = true;
}

function dragleave() {
    isDragging.value = false;
}

function drop(e) {
    e.preventDefault();
    file.value.files = e.dataTransfer.files;
    onChange();
    isDragging.value = false;
}

function closeModal() {
    emit('closeModal');
}

function upload() {
    if (files.value.length) {
        emit('onUpload', files.value[0]);
    }
}
</script>
