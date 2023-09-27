import axios from "axios"

const tasksApi = axios.create({
  baseURL: "http://localhost:8000/tasks/api/v1/tasks/"
});

export const getAllTasks = () => tasksApi.get("/");

export const getTask = (id: unknown) => tasksApi.get(`/${id}`);

export const createTask = (task: unknown) => tasksApi.post("/", task);

export const deleteTask = (id: unknown) => tasksApi.delete(`/${id}`);

export const updateTask = (id: unknown, task: unknown) => tasksApi.put(`/${id}/`, task);
