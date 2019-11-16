const axios = require("axios");
const FormData = require("form-data");
const fs = require('fs');

const submitJob = async (accessToken, pathToFile) => {
  let data = new FormData();
  data.append("media", pathToFile);
  data.append("heads", "true");
  data.append("work_type", "json");
  console.log("POST for Job Submission");
  let response = await axios({
    url: "https://api.wrnch.ai/v1/jobs",
    method: 'post',
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
    files: {
      media: fs.createReadStream(pathToFile),
    },
    data:  {
      'heads': true,
      'work_type': 'json'
    } 
  })
    .catch(error => {
      // Error
      console.log(error);
    }); 
    return response.data.job_id;
};

module.exports = {
  submitJob: submitJob
};
