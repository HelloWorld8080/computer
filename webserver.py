import os
import json
from flask import Flask
from flask_cors import CORS
from flask import request
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
        "gainMode": cap.getGainMode(),
        "gain": cap.getGain(),
        "Sharpness":cap.getSharpness()
    }
    return json.dumps(data)
    
@app.route('/setParameter')
def setParameter():
    # exposureAutoMode= request.args.get('exposureAutoMode')
    exposure_time=request.args.get('exposureTime')
    gainMode= request.args.get('gainMode')
    gain = request.args.get('gain')
    sharpness = request.args.get('sharpness')
    # cap.setExposureAutoMode(int(exposureAutoMode))
    cap.setSharpness(int(sharpness))
    # if cap.getExposureAutoMode() !=0 or cap.getExposureAutoMode() !=1: 
    #     cap.setExposureTime(float(exposure_time))
    # cap.setGainMode(exposureAutoMode)
    # if cap.getExposureAutoMode() !=0 or cap.getExposureAutoMode() !=1:
    #     cap.setGain(float(gain))
    return "设置成功"

@app.route('/shot')
def shot():
    result_path, filepath = cameraShot()
    with open(result_path, 'r', encoding='utf-8') as fr:
        return json.load(fr)

if __name__ == '__main__':
    print('web服务启动')
    app.run(host="0.0.0.0", port=5000)