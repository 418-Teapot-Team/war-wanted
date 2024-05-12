import axios from 'axios';

const headers = {
  Accept: 'application/json',
  'X-Requested-With': 'XMLHttpRequest',
  // Remove 'Content-Type' header to let Axios handle it automatically
};

class HttpClient {
  #instance = null;

  get httpClient() {
    return this.#instance !== null ? this.#instance : this.initHttpClient();
  }

  initHttpClient() {
    const http = axios.create({
      // Provide your base API URL here
      baseURL: import.meta.env.VITE_BASE_API,
      headers,
    });

    http.interceptors.response.use(
      (response) => response,
      (error) => {
        return this.#handleError(error);
      }
    );
    this.#instance = http;
    return http;
  }

  #handleError(error) {
    const errorData = {
      code: error.status,
      message: error?.response?.data?.message ? error?.response?.data?.message : error.message,
      status: error.statusText,
    };
    console.error(error);
    return Promise.reject(errorData);
  }

  request(config) {
    return this.httpClient.request(config);
  }

  get(url, config) {
    return this.httpClient.get(url, config);
  }

  post(url, data, config) {
    const formData = new FormData();
    // Append each key-value pair from the data object to the FormData object
    for (const key in data) {
      formData.append(key, data[key]);
    }
    // If config is provided, merge headers, etc.
    return this.httpClient.post(url, formData, config);
  }

  put(url, data, config) {
    const formData = new FormData();
    for (const key in data) {
      formData.append(key, data[key]);
    }
    return this.httpClient.put(url, formData, config);
  }

  delete(url, config) {
    return this.httpClient.delete(url, config);
  }
}

export const httpClient = new HttpClient();
