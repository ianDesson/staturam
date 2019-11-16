const axios = require("axios");

const FormData = require("form-data");
require("dotenv").config();

const $ = require("jquery");

/*
 * Note: This requires setting a .env file in the root directory
 * that specifies your API_KEY
 */
const getAccessToken = async () => {
  console.log("POST for access_token");
  await axios.post("https://api.wrnch.ai/v1/login", {
    api_key: 'aafde657-5b01-4718-8902-78db258ea0b0'
  }).then((response) => {
    console.log('response', response)
    return response.data.access_token;
  });
  /* var form = new FormData();
  form.append("api_key", 'aafde657-5b01-4718-8902-78db258ea0b0');

  var settings = {
    async: true,
    crossDomain: true,
    url: "https://api.wrnch.ai/v1/login",
    method: "POST",
    processData: false,
    contentType: false,
    mimeType: "multipart/form-data",
    data: form
  };

  await $.ajax(settings).then(function(response) {
    console.log('response', response);
    return response.access_token
  }).catch(error => {
    console.log(error)
  }); */
};

module.exports = {
  getAccessToken: getAccessToken
};
