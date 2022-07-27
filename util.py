import os
import numpy as np
import cv2
from pyzbar import pyzbar as pbar
from PIL import Image, ImageDraw, ImageFont
from camera import cap
import json
import time 

def cameraShot():
    # ret, frame = cap.read()
    frame = cap.get_image(width=800)
    blur_img = cv2.GaussianBlur(frame, (0, 0), 5)
    frame = cv2.addWeighted(frame, 1.5, blur_img, -0.5, 0)
    now = time.time()
    key = 'img_' + str(int(now))
    pathdir = os.path.join('result', key)
    if os.path.exists(pathdir) == False:
        os.makedirs(pathdir)
    img_path = os.path.join(pathdir, 'image.jpg')
    cv2.imwrite(img_path, frame)  # 保存路径
    decode(img_path, pathdir, key)
    # cap.release()
    print("拍照完成")
    return os.path.join(pathdir, "image_result.json"), 'img_' + str(int(now))
def setExportTime(exportTime):
    cap.set_exposure_time(exportTime)
def setExposureAutoMode(swich):
    cap.usetExposureAutoMode(swich)

def setGain(swich = 0):
    cap.usetGain(swich)
def decode(img_path,pathdir,key):
    image = cv2.imread(img_path)
    barcodes = pbar.decode(image)
    length = len(barcodes)
    # print(list(range(0,7)))
    # print("码的个数：", list(range(0,length)))
    num = list(range(length))
    # print(num)
    t = dict(zip(num, barcodes))
    results = []
    for i,barcode in t.items():
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 条形码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # 不能显示中文
        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        # 更换为：
        img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # 参数（字体，默认大小）
        font = ImageFont.truetype('fontx/simfang.ttf', 25)
        # 字体颜色（rgb)
        fillColor = (0, 255, 0)
        # 文字输出位置
        position = (x, y - 30)
        # 输出内容
        #str = barcodeData
        str = "成功"
        # 需要先把输出的中文字符转换成Unicode编码形式(  str.decode("utf-8)   )
        draw = ImageDraw.Draw(img_PIL)
        draw.text(position, str, font=font, fill=fillColor)
        # 使用PIL中的save方法保存图片到本地
        # img_PIL.save('02.jpg', 'jpeg')
        # path = './result/'
        # img_PIL.save(path, 'jpg')
        # 转换回OpenCV格式
        image = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        # 向终端打印条形码数据和条形码类型
        #print("扫描结果==》 类别： {0} 内容： {1}".format(barcodeType, barcodeData))
        result = {}
        result["index"] = i
        result["type"] = barcodeType
        result["content"] = barcodeData
        results.append(result)
    #将results按照序号改成字典，进而转化为json格式
    print("results:",results)
    print('\n')
    data = {}
    img_str = os.path.join(pathdir,'image_result.png')
    cv2.imwrite(img_str, image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    json_result = os.path.join(pathdir,"image_result.json")
    data["image"] = img_path  # 保存原图路径
    data["image_result"] = img_str  # 保存识别结果图片路径
    data["key"] = key
    data["data"] = results # 保存Json识别结果
    with open(json_result, "w", encoding='utf-8') as fw:
        fw.write(json.dumps(data))