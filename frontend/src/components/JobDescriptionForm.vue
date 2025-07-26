// JobDescriptionForm.vue

<script setup lang="ts">
import { ref } from 'vue';
import { addJob, listResumes } from '@/composables/useApi';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import ResumeRanking from './ResumeRanking.vue';

const title = ref('');
const description = ref('');
const jobId = ref<string | null>(null);
const loading = ref(false);
const successMsg = ref('');
const resumes = ref<any[]>([]);
const resumesLoading = ref(false);

const submitJob = async () => {
  loading.value = true;
  successMsg.value = '';
  try {
    const response = await addJob({
      title: title.value,
      description: description.value
    });
    console.log('Job submitted:', response.data.job_id);
    jobId.value = response.data.job_id;
    successMsg.value = 'Job posted successfully!';
  } catch (err) {
    console.error('Error submitting job:', err);
  } finally {
    loading.value = false;
  }
};

const fetchResumes = async () => {
  resumesLoading.value = true;
  try {
    const response = await listResumes();
    resumes.value = response.data;
  } catch (err) {
    console.error('Error fetching resumes:', err);
  } finally {
    resumesLoading.value = false;
  }
};
</script>
<template>
  <div class="form-container">
    <h2 class="form-title">Enter Job Description</h2>
    <div class="form-fields">
      <div class="field-group">
        <label class="field-label">Job Title</label>
        <InputText v-model="title" placeholder="Job Title" class="input-text" />
      </div>
      <div class="field-group">
        <label class="field-label">Job Description</label>
        <Textarea v-model="description" placeholder="Job Description" rows="6" class="textarea" />
      </div>
    </div>
    <Button label="Submit" icon="pi pi-check" @click="submitJob" :disabled="loading" class="submit-btn" />
    <p v-if="successMsg" class="success-message">{{ successMsg }}</p>
    <p v-if="jobId" class="success-message">Job created with ID: {{ jobId }}</p>
    <div v-if="jobId">
      Job created with ID: {{ jobId }}
      <ResumeRanking :jobId="jobId" :autoFetch="true" />
    </div>
    <Button label="List All Resumes" icon="pi pi-list" @click="fetchResumes" :disabled="resumesLoading" class="submit-btn" style="margin-top: 1rem;" />
    <ul v-if="resumes.length" style="margin-top: 1rem;">
      <li v-for="resume in resumes" :key="resume.id">
        {{ resume.name }} - {{ resume.title }} (ID: {{ resume.id }})
      </li>
    </ul>
  </div>
</template>

<style scoped>
.form-container {
  padding: 1rem;
  background: #fff;
  border-radius: 8px;
  max-width: 500px;
  margin: 0 auto;
}

.form-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.form-fields {
  margin-bottom: 1rem;
}

.field-group {
  margin-bottom: 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  padding: 0.5rem;
  background: #f9f9f9;
}

.field-label {
  display: block;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.input-text,
.textarea {
  width: 100%;
  box-sizing: border-box;
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 4px;
  font-size: 1rem;
}

.textarea {
  resize: vertical;
}

.submit-btn {
  display: inline-block;
  padding: 0.5rem 1.5rem;
  font-size: 1rem;
  border-radius: 4px;
  background: #2563eb;
  color: #fff;
  border: none;
  cursor: pointer;
}

.submit-btn:disabled {
  background: #a5b4fc;
  cursor: not-allowed;
}

.success-message {
  margin-top: 1rem;
  color: #16a34a;
  font-weight: 500;
}
</style>
