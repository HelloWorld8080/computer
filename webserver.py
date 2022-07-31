import os
import json
from xmlrpc.client import boolean
from flask import Flask
from flask_cors import CORS
from flask import request
from numpy import int0
from camera import cap
import requests
requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
s = requests.session()
s.keep_alive = False
app = Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/get_result')
def get_result():
    data = []
    for filepath in os.listdir('result'):
        path = os.path.join(os.path.join('result', filepath), 'image_result.json')
        with open(path, 'r', encoding='utf-8') as fr:
            data.append(json.load(fr))
    return json.dumps(data)

@app.route('/getParameter')
def getParameter():

    data = {
        # "exposureAutoMode":cap.getExposureAutoMode(),
        "exposureTime": cap.getExposureTime(),
        # "gainMode": cap.getGainMode(),
        "gain": round(cap.getGain()/10, 2),
        # "sharpnessEnable":cap.getSharpnessEnable(),
        "sharpness":cap.getSharpness(),
        "lineDebouncerTime":cap.getSharpness()
    }
    return json.dumps(data)
    
@app.route('/setParameter')
def setParameter():
    # exposureAutoMode= request.args.get('exposureAutoMode')
    # exposure_time= request.args.get('exposureTime') if bool(request.args.get('exposureTime')) else get
    exposure_time = float(request.args.get('exposureTime'))
    # gainMode= request.args.get('gainMode')
    gain = float(request.args.get('gain'))*10
    # sharpnessEnable = False if request.args.get('sharpnessEnable')=="0" else True
    sharpness = int(request.args.get('sharpness'))
    lineDebouncerTime = int(request.args.get('lineDebouncerTime'))
    # cap.setExposureAutoMode(int(exposureAutoMode))
    # cap.setSharpnessEnable(sharpnessEnable)
    # if cap.getSharpnessEnable(): 
    
    # if cap.getExposureAutoMode() !=0 or cap.getExposureAutoMode() !=1: 
    
    # cap.setGainMode(exposureAutoMode)
    # if cap.getExposureAutoMode() !=0 or cap.getExposureAutoMode() !=1:
    cap.setExposureTime(exposure_time)
    # cap.set_Value("enum_value","GainAuto",0)
    cap.setGain(gain)
    cap.setSharpness(sharpness)
    cap.setLineDebouncerTime(lineDebouncerTime)
    return "设置成功"
@app.route('/hasDetectCode')
def hasDetectCode():
    return cap.hasDetectCode()
    
@app.route('/shot')
def shot():
    result_path = cap.cameraShot()
    with open(result_path, 'r', encoding='utf-8') as fr:
        return json.load(fr)

if __name__ == '__main__':
    print('web服务启动')
    app.run(host="0.0.0.0", port=5000)