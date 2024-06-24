import axios from 'axios';

const baseURL = import.meta.env.VITE_BASE_URL;

const fetchInventory = axios.create({
  baseURL,
});

fetchInventory.interceptors.request.use(
  (config) => {
    // Optionally, you can add authorization or other headers here if needed
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default fetchInventory;
