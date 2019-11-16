const axios = require("axios");
require("dotenv").config();

/*
 * Note: This requires setting a .env file in the root directory
 * that specifies your API_KEY
 */
const getAccessToken = () => {
  console.log('POST for access_token');
  axios
    .post("https://api.wrnch.ai/v1/login", { api_key: process.env.API_KEY })
    .then(response => {
      // Passed
      console.log('Response status:',response.status, response.statusText);
      return response.data.access_token;
    })
    .catch(error => {
      // Error
      console.log(error.response.data);
      console.log(error.response.status);
      console.log(error.response.headers);
      if (error.request) {
        console.log(error.request);
      }
    });
};

export default getAccessToken;