import axios from "axios";
import { BASE_URL } from "../constant";
import { ACCEPT_JSON, ACCESS_TOKEN } from "../constant";


const api = axios.create({
    baseURL: BASE_URL,
    headers: {
        'Accept': ACCEPT_JSON.accept
    }
})


api.interceptors.request.use(
    (config) => {
        const access_token = localStorage.getItem(ACCESS_TOKEN);
        if (access_token) {
            config.headers.Authorization = access_token;
        }
        return config
    },
    (error) => Promise.reject(error)
)

export default api
