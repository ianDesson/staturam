const getAccessToken = require("./getAccessToken.js").getAccessToken;
const submitJob = require("./submitJob.js").submitJob;


function idk() {
  const accessToken = getAccessToken().then(response => {
    submitJob(response, './src/services/api/test.jpeg');
  })
  .catch((error) => {
    console.log(error)
  });
}
idk();