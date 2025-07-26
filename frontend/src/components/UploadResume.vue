<script setup lang="ts">
import { ref } from "vue";
import { uploadResume } from "@/composables/useApi";

const file = ref<File | null>(null);
const jobsSupportMsg = ref<string>("");

function handleFileChange(e: Event) {
  const target = e.target as HTMLInputElement;
  file.value = target.files?.[0] || null;
}

const onUpload = async () => {
  if (!file.value) return;
  const { data } = await uploadResume(file.value);
  console.log("Uploaded", data);
  jobsSupportMsg.value = "Support for /jobs/ is enabled!";
};
</script>

<template>
  <div class="upload-resume-page">
    <h1>Upload Resume</h1>
    <input type="file" @change="handleFileChange" />
    <button @click="onUpload" :disabled="!file">Upload</button>
    <div v-if="jobsSupportMsg" class="success-msg">
      {{ jobsSupportMsg }}
      <router-link to="/jobs" style="margin-left: 8px;">Go to Jobs</router-link>
    </div>
  </div>
</template>

<style scoped>
.upload-resume-page {
  max-width: 400px;
  margin: 40px auto;
  padding: 24px;
  border: 1px solid #eee;
  border-radius: 8px;
  background: #fafafa;
}
h1 {
  margin-bottom: 16px;
}
input[type="file"] {
  margin-bottom: 12px;
}
button {
  margin-bottom: 12px;
}
.success-msg {
  color: green;
  margin-top: 12px;
}
</style>