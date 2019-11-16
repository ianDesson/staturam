const axios = require("axios");
require("dotenv").config();

/*
 * Note: This requires setting a .env file in the root directory
 * that specifies your API_KEY
 */
const getAccessToken = async () => {
  console.log('POST for access_token');
  let response = await axios
    .post("https://api.wrnch.ai/v1/login", { api_key: process.env.API_KEY })
    return response.data.access_token;
};

module.exports = {
  getAccessToken: getAccessToken
}