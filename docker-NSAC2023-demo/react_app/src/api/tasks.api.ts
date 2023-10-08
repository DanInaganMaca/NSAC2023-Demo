import axios from "axios"
import { environment } from "../environments/environment.dev";

const endpoint: string = environment.production ? environment.remoteBackendUrl : environment.backendUrl;

const tasksApi = axios.create({
  baseURL: `${endpoint}/tasks`
});

export const getAllTasks = () => tasksApi.get("/");

export const getTask = (id: unknown) => tasksApi.get(`/${id}`);

export const createTask = (task: unknown) => tasksApi.post("/", task);

export const deleteTask = (id: unknown) => tasksApi.delete(`/${id}`);

export const updateTask = (id: unknown, task: unknown) => tasksApi.put(`/${id}/`, task);
