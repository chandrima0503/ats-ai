<script setup lang="ts">
import { ref } from "vue";
import { uploadResume } from "@/composables/useApi";

const file = ref<File | null>(null);

const onUpload = async () => {
  if (!file.value) return;
  const { data } = await uploadResume(file.value);
  console.log("Uploaded", data);
};
</script>

<template>
  <input type="file" @change="e => file = (e.target as HTMLInputElement).files?.[0] || null" />
  <button @click="onUpload">Upload</button>
</template>