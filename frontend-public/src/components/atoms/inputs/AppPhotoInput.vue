<template>
    <div class="bg-gray-100 p-8 shadow-md" @dragover.prevent="dragover" @dragleave="dragleave" @drop="drop">
        <div class="text-center">
            <div v-if="!files.length">
                <label for="fileInput" class="text-xl block cursor-pointer">
                    <div v-if="isDragging">Release to drop files here.</div>
                    <div v-else>Drop files here or <u class="text-primary">click here</u> to upload.</div>
                </label>
                <input type="file" multiple name="file" id="fileInput"
                    class="opacity-0 overflow-hidden absolute w-px h-px" @change="onChange" ref="file"
                    accept=".jpg,.jpeg" />
            </div>
            <div v-else class="flex flex-col gap-2 justify-center items-center mt-8">
                <div v-for="file in files" :key="file.name"
                    class="flex relative py-3 border border-black/20 rounded-md w-full h-full justify-center">
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
import { useFoundData } from '@/stores/foundData';

const store = useFoundData()

const isDragging = ref(false);
const files = ref([]);

const file = ref(null);

function onChange() {
    console.log('value changed');
    files.value = [file.value.files[0]];
    setImage()
}


const setImage = () => {
    console.log(typeof (files.value[0]))
    console.log(files.value[0])

    fileToByteArray(files.value[0])
        .then(byteArray => {
            console.log("Byte array:", byteArray);
            // You can use the byte array here
            store.image = byteArray;
        })
        .catch(error => {
            console.error("Error converting file to byte array:", error);
        });


}

// Assuming 'file' is your file object
function fileToByteArray(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();

        reader.onload = function () {
            const arrayBuffer = this.result;
            const byteArray = new Uint8Array(arrayBuffer);
            resolve(byteArray);
        };

        reader.onerror = function (error) {
            reject(error);
        };

        reader.readAsArrayBuffer(file);
    });
}

function generateThumbnail(file) {
    let fileSrc = URL.createObjectURL(file);
    setTimeout(() => {
        URL.revokeObjectURL(fileSrc);
    }, 1000);
    return fileSrc;
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
    isDragging.value = false;
    const droppedFiles = e.dataTransfer.files;
    files.value = Array.from(droppedFiles);
}

</script>

<style lang="scss" scoped></style>
