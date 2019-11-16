import requests
import json
from time import sleep

LOGIN_URL = 'https://api.wrnch.ai/v1/login'
JOBS_URL = 'https://api.wrnch.ai/v1/jobs'
API_KEY = "5412df2d-e08f-4ec1-8210-96859c2aa5c3"

resp_auth = requests.post(LOGIN_URL,data={'api_key':API_KEY})
print(resp_auth.text)
# the jwt token is valid for an hour
JWT_TOKEN = json.loads(resp_auth.text)['access_token']

with open('test.jpg', 'rb') as f:
    resp_sub_job = requests.post(JOBS_URL,
                                 headers={'Authorization':f'Bearer {JWT_TOKEN}'},
                                 files={'media':f},
                                 data={'work_type':'json'}
                                )

job_id = json.loads(resp_sub_job.text)['job_id']
print('Status code:',resp_sub_job.status_code)
print('Response:',resp_sub_job.text)

GET_JOB_URL = JOBS_URL + '/' +job_id
print(GET_JOB_URL)

sleep(1)

resp_get_job = requests.get(GET_JOB_URL,headers={'Authorization':f'Bearer {JWT_TOKEN}'})
print('Status code:', resp_get_job.status_code)
print('\nResponse:',resp_get_job.text)

cloud_pose_estimation = json.loads(resp_get_job.text)
cloud_xLWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][30]
cloud_xLKNEE = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][8]

print(cloud_xLWRIST)
print(cloud_xLKNEE)
