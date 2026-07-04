import generateRandomKey from '../utils/generateRandomKey.js';

const apiUrl = window.config.apiUrl;

const apiHandler = {
  endpoints: {
    history: `${apiUrl}/api/v1/history`,
    health: `${apiUrl}/health`,
  },

  get: async function(endpoint, options = {}) {
    var key = localStorage.getItem('session_key');
    if (key == null) {
      key = generateRandomKey();
      localStorage.setItem('session_key', key);
    }

    options.method = 'GET';
    options.headers = {
      'Content-Type': 'application/json',
      'X-Calc-Session-Key': key,
    };

    return await fetch(endpoint, options);
  },
  post: async function(endpoint, body, options = {}) {
    var key = localStorage.getItem('session_key');
    if (key == null) {
      key = generateRandomKey();
      localStorage.setItem('session_key', key);
    }

    options.method = 'POST';
    options.body = JSON.stringify(body);
    options.headers = {
      'Content-Type': 'application/json',
      'X-Calc-Session-Key': key,
    };
    return await fetch(endpoint, options);
  },
};

const getHealthCheck = () => {
  return apiHandler.get(apiHandler.endpoints.health);
};

const getHistory = () => {
  return apiHandler.get(apiHandler.endpoints.history);
};

const saveHistory = (data) => {
  return apiHandler.post(apiHandler.endpoints.history, data);
};

const clearHistory = () => {
  return apiHandler.post(apiHandler.endpoints.history + '/delete')
};

export {
  getHealthCheck,
  getHistory,
  saveHistory,
  clearHistory,
}
