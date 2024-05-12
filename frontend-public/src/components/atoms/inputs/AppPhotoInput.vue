<template>
    <div class="bg-gray-100 p-8 shadow-md">
        <div class=" text-center">
            <div v-if="!files.length">
                <input type="file" multiple name="file" id="fileInput"
                    class="opacity-0 overflow-hidden absolute w-px h-px" @change="onChange" ref="file"
                    accept=".jpg,.jpeg,.png,.webp" />
                <label for="fileInput" class="text-xl block cursor-pointer">
                    <div v-if="isDragging">Release to drop files here.</div>
                    <div v-else>Drop files here or <u class="text-primary">click here</u> to upload.</div>
                </label>
            </div>
            <div v-if="files.length" class="flex flex-col gap-2 justify-center items-center mt-8">
                <div v-for="file in files" :key="file.name"
                    class="flex relative py-3 border border-black/20 rounded-md w-full h-full justify-center">
                    <!-- CLOSE BUTTON -->
                    <!-- <div @click="remove" class="absolute right-0 top-0 cursor-pointer hover:stroke-primary">
                        <CloseIcon class="w-8 h-8" />
                    </div> -->
                    <div>
                        <img class="rounded bg-gray-500" :src="generateThumbnail(file)" />

                    </div>
                </div>
                <div @click="remove" class="cursor-pointer hover:stroke-primary">
                    <CloseIcon colorProp="red" class="w-8 h-8" />
                </div>
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
    console.log(files.value[0])
    if (files.value.length) {
        emit('onUpload', files.value[0]);
    }
}
</script>

<style lang="scss" scoped></style>
