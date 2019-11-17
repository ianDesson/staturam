import PySimpleGUI as sg
import requests
import json
import math
from time import sleep

# Constants
FRONT_UP = 0;
FRONT_MID = 1;
FRONT_DOWN = 2;
LEFT_UP = 3;
LEFT_MID = 4;
LEFT_DOWN = 5;
RIGHT_UP = 6;
RIGHT_MID = 7;
RIGHT_DOWN = 8;

layout = [[sg.Text('Exercising the right way!', size=(30, 1), font=("Helvetica", 15), text_color='blue')],
          [sg.Text('Find out how well you exercise with bicep curl!', size=(35,1), font=("Helvetica", 15), text_color='black')],
          [sg.Text('Select the viewpoint and upload your image:', size=(35,1), font=("Helvetica", 12), text_color='black')],
          [sg.Radio('Bar up', "RADIO1", default=True), sg.Radio('Bar mid', "RADIO1"), sg.Radio('Bar down', "RADIO1")],
          [sg.Submit(), sg.Cancel()]
          ]

layoutResults = [[sg.Text('Results!!', size=(30, 1), font=("Helvetica", 15), text_color='blue')],
                 [sg.Exit()]
                 ]

"""[sg.PopupGetFile("Upload image to compare",
                        default_path="",
                        default_extension="",
                        save_as=False,
                        file_types=(('ALL Files', '*.*'),),
                        no_window=False,
                        size=(None, None),
                        button_color=None,
                        background_color=None,
                        text_color=None,
                        icon=None,
                        font=None,
                        no_titlebar=False,
                        grab_anywhere=False,
                        keep_on_top=False,
                        location=(None, None),
                        initial_folder=None), sg.InputText('filePath', key='filePath')],
"""
    #]

#[sg.Image(r'C:\Users\Diego Be\staturam\Plan M\batomamadodelado.png')]
#text = 

event = 'begin'
window = sg.Window('Nacho').Layout(layout)
#event, values = window.Read()
#print(event, values)

vp = 0

event, values = window.Read()
    
if event != 'Cancel':
    if values[0] is True:
        vp = LEFT_UP
    elif values[1] is True:
        vp = LEFT_MID
    else:
        vp = LEFT_DOWN

    window.Close()

    text = [sg.PopupGetFile("Upload image to compare",
            default_path="",
            default_extension="",
            save_as=False,
            file_types=(('ALL Files', '*.*'),),
            no_window=False,
            size=(None, None),
            button_color=None,
            background_color=None,
            text_color=None,
            icon=None,
            font=None,
            no_titlebar=False,
            grab_anywhere=False,
            keep_on_top=False,
            location=(None, None),
            initial_folder=None)]

    window = sg.Window('Nacho Results').Layout(layoutResults)

    event, values = window.Read()

    window.Close()
else:
    window.Close()

#event, values = window.Read()
print(event, values, viewpoint, text)

"""
LOGIN_URL = 'https://api.wrnch.ai/v1/login'
JOBS_URL = 'https://api.wrnch.ai/v1/jobs'
API_KEY = "5412df2d-e08f-4ec1-8210-96859c2aa5c3"

resp_auth = requests.post(LOGIN_URL,data={'api_key':API_KEY})
print(resp_auth.text)
# the jwt token is valid for an hour
JWT_TOKEN = json.loads(resp_auth.text)['access_token']

with open(text, 'rb') as f:
    resp_sub_job = requests.post(JOBS_URL,
                                 headers={'Authorization':f'Bearer {JWT_TOKEN}'},
                                 files={'media':f},
                                 data={'work_type':'json'}
                                )

job_id = json.loads(resp_sub_job.text)['job_id']
print('Status code:',resp_sub_job.status_code)
print('Response:',resp_sub_job.text)


#job_id = "56d5ffae-4d57-46ee-a794-171a4d81b6a6"

GET_JOB_URL = JOBS_URL + '/' + job_id
print(GET_JOB_URL)

#sleep(1)

resp_get_job = requests.get(GET_JOB_URL,headers={'Authorization':f'Bearer {JWT_TOKEN}'})
status = resp_get_job.status_code
print('Status code:', status)

while status != 200:
    resp_get_job = requests.get(GET_JOB_URL,headers={'Authorization':f'Bearer {JWT_TOKEN}'})
    status = resp_get_job.status_code
    print('Status code:', status)

print('\nResponse:',resp_get_job.text)

values = json.loads(resp_get_job.text)

# Calculations
def calculateAngle (x1, x2, y1, y2):
    return math.atan(abs((x1 - x2) / (y1 - y2))) * (180 / math.pi);

def calculateArmAngle(x1, x2, x3, y1, y2, y3):
    angle1 = math.atan((y1 - y2) / (x1 - x2)) * (180 / math.pi)
    angle2 = math.atan((y3 - y2) / (x3 - x2)) * (180 / math.pi)
    result = abs(angle1 - angle2)
    if result > 180:
        return 180 - result
    else:
        return result

def compareAngles(correct_angle, measured_angle, error):
    if abs(measured_angle - correct_angle) <= error or abs((180 - measured_angle) - correct_angle) <= 180:
        return true
    else:
        return false

# TODO: Fix error value
def compare(lean, sew, hse, leanCorrect, sewCorrect, hseCorrect):
    if compareAngles(lean, leanCorrect, 3) and compareAngles(sew,  sewCorrect, 8) and (hse,  hseCorrect, 1.5):
        return true
    else:
        return false

# TODO: Fix
# For the front side it would be better to specify in the caller of this function an AND with right and left values.
def isCorrectPosture(viewpoint, leanAngle, SEWAngle, HSEAngle):
    if viewpoint == LEFT_UP:
        return compare(leanAngle, SEWAngle, HSEAngle, , , )
    if viewpoint == LEFT_MID:
        return compare(leanAngle, SEWAngle, HSEAngle, , , )
    if viewpoint == LEFT_DOWN:
        return compare(leanAngle, SEWAngle, HSEAngle, 3, 155, 1.75)
        case RIGHT_UP:
            return compare(leanAngle, SEWAngle, HSEAngle, 4.5, 75, 40)
        case RIGHT_MID:
            return compare(leanAngle, SEWAngle, HSEAngle, , , )
        case RIGHT_DOWN:
            return compare(leanAngle, SEWAngle, HSEAngle, , , )
    default:
        return false

# 2D coordinates
# Left side:
lhip_x = values['frames'][0]['persons'][0]['pose2d']['joints'][6]
lhip_y = values['frames'][0]['persons'][0]['pose2d']['joints'][7]
lshoulder_x = values['frames'][0]['persons'][0]['pose2d']['joints'][26]
lshoulder_y = values['frames'][0]['persons'][0]['pose2d']['joints'][27]
lelbow_x = values['frames'][0]['persons'][0]['pose2d']['joints'][28]
lelbow_y = values['frames'][0]['persons'][0]['pose2d']['joints'][29]
lwrist_x = values['frames'][0]['persons'][0]['pose2d']['joints'][30]
lwrist_y = values['frames'][0]['persons'][0]['pose2d']['joints'][31]

# Right side:
rhip_x = values['frames'][0]['persons'][0]['pose2d']['joints'][4]
rhip_y = values['frames'][0]['persons'][0]['pose2d']['joints'][5]
rshoulder_x = values['frames'][0]['persons'][0]['pose2d']['joints'][24]
rshoulder_y = values['frames'][0]['persons'][0]['pose2d']['joints'][25]
relbow_x = values['frames'][0]['persons'][0]['pose2d']['joints'][22]
relbow_y = values['frames'][0]['persons'][0]['pose2d']['joints'][23]
rwrist_x = values['frames'][0]['persons'][0]['pose2d']['joints'][20]
rwrist_y = values['frames'][0]['persons'][0]['pose2d']['joints'][21]

#2D angles
#Left side:
left_leaning_angle = calculateAngle(lhip_x, lshoulder_x, lhip_y, lshoulder_y);
left_SEW_angle = calculateArmAngle(lshoulder_x, lelbow_x, lwrist_x, lshoulder_y, lelbow_y, lwrist_y);
left_HSE_angle = calculateArmAngle(lhip_x, lshoulder_x, lelbow_x, lhip_y, lshoulder_y, lelbow_y);

#Right side:
right_leaning_angle = calculateAngle(rhip_x, rshoulder_x, rhip_y, rshoulder_y);
right_SEW_angle = calculateArmAngle(rshoulder_x, relbow_x, rwrist_x, rshoulder_y, relbow_y, rwrist_y);
right_HSE_angle = calculateArmAngle(rhip_x, rshoulder_x, relbow_x, rhip_y, rshoulder_y, relbow_y);

print("2D")
print("Left side:")
print("Leaning angle: " + str(left_leaning_angle))
print("Shoulder/Elbow/Wrist 2D angle: " + str(left_SEW_angle))
print("Hip/Shoulder/Elbow 2D angle: " + str(left_HSE_angle))
print("Right side:")
print("Leaning angle: " + str(right_leaning_angle))
print("Shoulder/Elbow/Wrist 2D angle: " + str(right_SEW_angle))
print("Hip/Shoulder/Elbow 2D angle: " + str(right_HSE_angle))
"""
