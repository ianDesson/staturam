const axios = require("axios");
const FormData = require("form-data");
const fs = require("fs");
const $ = require("jquery");


const readFileDataAsBase64 = (file) => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = (event) => {
        resolve(event.target.result);
    };

    reader.onerror = (err) => {
        reject(err);
    };

    reader.readAsBinaryString(file);
});
}

const submitJob = async (accessToken, file) => {
  /* let data = new FormData();
  console.log("__dirname", __dirname);
  data.append("media", file);
  data.append("heads", "true");
  data.append("work_type", "json");
  console.log("POST for Job Submission");
  let response = await axios({
    url: "https://api.wrnch.ai/v1/jobs",
    method: "post",
    headers: {
      Authorization: `Bearer ${accessToken}`
    },
    data: {
      heads: true,
      work_type: "json"
    }
  })
    .then(response => {
      console.log("submitJob response", response);
    })
    .catch(error => {
      // Error
      console.log(error);
    }); */

  var result = await readFileDataAsBase64(file);
  var form = new FormData();
  form.append("heads", "true");
  form.append("work_type", "annotated_media");
  form.append("media", result/* "/home/fox/Dev/staturam/src/services/api/test.jpeg" */);
  console.log('idk', result)
  var settings = {
    url: "https://api.wrnch.ai/v1/jobs",
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Cache-Control": "no-cache",
      "Content-Type":
        "multipart/form-data;",
      "cache-control": "no-cache"
    },
    mimeType: "multipart/form-data",
    data: form
  };

  /* $.ajax(settings).done(function(response) {
    console.log(response);
  }); */
  await axios({settings}).then(response => {
    console.log('response from job', response)
  }).catch(error => {
    console.error(error);
  })
};

module.exports = {
  submitJob: submitJob
};
