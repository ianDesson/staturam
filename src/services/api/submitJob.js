const axios = require("axios");
const FormData = require("form-data");
const fs = require("fs");
const $ = require("jquery");

const submitJob = async (accessToken, file) => {
  let data = new FormData();
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
  }).catch(error => {
    // Error
    console.log(error);
  });
  return response.data.job_id;
/*   var form = new FormData();
  form.append("heads", "true");
  form.append("work_type", "annotated_media");
  form.append("media", file);

  var settings = {
    async: true,
    crossDomain: true,
    url: "https://api.wrnch.ai/v1/jobs",
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      
      "Cache-Control": "no-cache",
      "Content-Type":
        "multipart/form-data; boundary=--------------------------238034221584743182722821",
      "cache-control": "no-cache"
    },
    processData: false,
    contentType: false,
    mimeType: "multipart/form-data",
    data: form
  };

  await $.ajax(settings)
    .done(function(response) {
      console.log("response pls", response);
    })
    .catch(error => {
      console.log(error);
    }); */
};

module.exports = {
  submitJob: submitJob
};
