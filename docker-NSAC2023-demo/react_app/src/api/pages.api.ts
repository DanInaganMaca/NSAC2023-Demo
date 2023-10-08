import axios from "axios"
import { environment } from "../environments/environment.dev";

const endpoint: string = environment.production ? environment.remoteBackendUrl : environment.backendUrl;

const pagesApi = axios.create({
  baseURL: `${endpoint}/pages`
});

export const getAll = () => pagesApi.get("/");

export const getOne = (code: unknown) => pagesApi.get(`/by_code/${code}`);

export const create = (page: unknown) => pagesApi.post("/", page);

export const remove = (id: unknown) => pagesApi.delete(`/${id}`);

export const update = (id: unknown, page: unknown) => pagesApi.put(`/${id}/`, page);
