import axios from "axios";

export function postClient(client) {
  return axios.post('http://127.0.0.1:8000/api/v1/clientes', client);
}