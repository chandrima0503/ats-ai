import axios from "axios";

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000" });

export const uploadResume = (file: File) => {
  const form = new FormData();
  form.append("file", file);
  return api.post("/resumes", form);
};

export const addJob = (data: { title: string; description: string }) => api.post("/jobs", data);

export const getMatches = (jobId: string) => api.get(`/jobs/${jobId}/rank`);

export const chatResume = (resumeId: string, question: string) =>
  api.get("/match/chat", { params: { resume_id: resumeId, question } });

export const listResumes = () => api.get("/resumes/");