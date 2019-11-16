import axios from 'axios';
require('dotenv').config();



const getAccessToken = () => {
  axios.post('https://api.wrnch.ai/v1/login', {
    'Content-Type': 'application/json',
    'api-key': process.env.API_KEY,
  });
};