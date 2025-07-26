<!-- ResumeRanking.vue -->
<script setup lang="ts">
import { ref, watch } from 'vue';
import { getMatches } from '@/composables/useApi';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import { useRouter } from 'vue-router';

const props = defineProps<{
  jobId?: string | null;
  autoFetch?: boolean;
}>();

const jobIdInput = ref(props.jobId ?? '');
const rankings = ref<any[]>([]);
const loading = ref(false);
const router = useRouter();

const fetchRankings = async () => {
  if (!jobIdInput.value) return;
  loading.value = true;
  try {
    const result = await getMatches(jobIdInput.value);
    // Map to objects with name and index
    rankings.value = result.data.map((item: any, idx: number) => ({
      name: item,
      index: idx + 1
    }));
  } catch (err) {
    console.error('Error fetching rankings:', err);
  } finally {
    loading.value = false;
  }
};

const clearRankings = () => {
  rankings.value = [];
  jobIdInput.value = '';
  router.push({ path: '/' });
};

// Automatically fetch when jobId changes and autoFetch is true
watch(
  () => props.jobId,
  (newJobId) => {
    if (props.autoFetch && newJobId) {
      jobIdInput.value = newJobId;
      fetchRankings();
    }
  },
  { immediate: true }
);
</script>
<template>
  <div class="resume-ranking-container">
    <h2 class="resume-ranking-title">Ranked Candidates</h2>
    <div class="resume-ranking-input-group">
      <InputText v-model="jobIdInput" placeholder="Enter Job ID" class="resume-ranking-input" />
      <Button label="Fetch Rankings" icon="pi pi-search" class="resume-ranking-button" @click="fetchRankings" :disabled="loading" />
      <Button label="Clear" icon="pi pi-times" class="resume-ranking-button" @click="clearRankings" severity="secondary" />
    </div>
    
    <DataTable :value="rankings" v-if="rankings.length" class="resume-ranking-table">
      <Column field="index" header="Rank" />
      <Column field="name" header="Name" />
    </DataTable>
  </div>
</template>

<style scoped>
.resume-ranking-container {
  padding: 1rem;
}

.resume-ranking-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.resume-ranking-input-group {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-width: 400px;
}

.resume-ranking-input {
  width: 100%;
}

.resume-ranking-button {
  margin-top: 0.5rem;
  width: 100%;
}

.resume-ranking-table {
  margin-top: 1rem;
}
</style>
