import { httpClient } from '@/utils/HttpClient';
import { AUTH_TOKEN_KEY } from '@/utils/constants';
import { defineStore } from 'pinia';

const BASE_API = import.meta.env.VITE_BASE_API;

export const useIndexStore = defineStore('index', () => {
  async function login(email, password) {
    try {
      const res = await httpClient.post(BASE_API + '/auth/signin', {
        email,
        password,
      });
      localStorage.setItem(AUTH_TOKEN_KEY, res.data.access_token);
    } catch (e) {
      throw new Error(e);
    }
  }
  async function fetchAll() {
    try {
      const res = await httpClient.get(BASE_API + '/matches/');
      return res.data;
    } catch (e) {
      throw new Error(e);
    }
  }

  async function fetch(id) {
    try {
      const res = await httpClient.get(BASE_API + `/matches/${id}`);
      return res.data;
    } catch (e) {
      throw new Error(e);
    }
  }

  return {
    login,
    fetchAll,
    fetch,
  };
});
