import numpy as np
import cv2
import time
import os
import sys
from pathPro import ROOT
from PIL import Image, ImageDraw, ImageFont
import json
from pyzbar import pyzbar as pbar
# sys.path.append("/opt/MVS/Samples/aarch64/Python/MvImport")
# os.environ['MVCAM_COMMON_RUNENV'] = "/opt/MVS/lib"
# from MvCameraControl_class import *

sys.path.append(os.path.join(ROOT,"MVS/Samples/aarch64/Python/MvImport"))
os.environ['MVCAM_COMMON_RUNENV'] = os.path.join(ROOT,"MVS/lib")

from MvCameraControl_class import *

# from MVS.MvCameraControl_class import * #调用了MvCameraControl_class.py文件
from pathPro import ROOT

class HKCamera():
    def __init__(self, CameraIdx=0, log_path=None):
        # enumerate all the camera devices
        deviceList = self.enum_devices()

        # generate a camera instance
        self.camera = self.open_camera(deviceList, CameraIdx, log_path)
        self.start_camera()
    def __del__(self):
        if self.camera is None:
            return

        # 停止取流
        ret = self.camera.MV_CC_StopGrabbing()
        if ret != 0:
            raise Exception("stop grabbing fail! ret[0x%x]" % ret)

        # 关闭设备
        ret = self.camera.MV_CC_CloseDevice()
        if ret != 0:
            raise Exception("close deivce fail! ret[0x%x]" % ret)

        # 销毁句柄
        ret = self.camera.MV_CC_DestroyHandle()
        if ret != 0:
            raise Exception("destroy handle fail! ret[0x%x]" % ret)

    @staticmethod
    def enum_devices(device=0, device_way=False):
        """
        device = 0  枚举网口、USB口、未知设备、cameralink 设备
        device = 1 枚举GenTL设备
        """
        if device_way == False:
            if device == 0:
                cameraType = MV_GIGE_DEVICE | MV_USB_DEVICE | MV_UNKNOW_DEVICE | MV_1394_DEVICE | MV_CAMERALINK_DEVICE
                deviceList = MV_CC_DEVICE_INFO_LIST()
                
                # 枚举设备
                ret = MvCamera.MV_CC_EnumDevices(cameraType, deviceList)
                if ret != 0:
                    raise Exception("devicelist: %s enum devices fail! ret[0x%x]" %(
                    deviceList.nDeviceNum,
                    ret))
                return deviceList
            else:
                pass
        elif device_way == True:
            pass

    def open_camera(self, deviceList, CameraIdx, log_path):
        # generate a camera instance
        camera = MvCamera()

        # 选择设备并创建句柄
        stDeviceList = cast(deviceList.pDeviceInfo[CameraIdx], POINTER(MV_CC_DEVICE_INFO)).contents
        if log_path is not None:
            ret = self.camera.MV_CC_SetSDKLogPath(log_path)
            if ret != 0:
                raise Exception("set Log path  fail! ret[0x%x]" % ret)

            # 创建句柄,生成日志
            ret = camera.MV_CC_CreateHandle(stDeviceList)
            if ret != 0:
                raise Exception("create handle fail! ret[0x%x]" % ret)
        else:
            # 创建句柄,不生成日志
            ret = camera.MV_CC_CreateHandleWithoutLog(stDeviceList)
            if ret != 0:
                raise Exception("create handle fail! ret[0x%x]" % ret)

        # 打开相机
        ret = camera.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
        if ret != 0:
            # if ret != 2147484163: 
            raise Exception("open device fail! ret[0x%x]" % ret)
        ret = camera.MV_CC_FeatureLoad(os.path.join(ROOT,"MV-CA050-12UM_K27297324.mfs"))
        if ret != 0:
            raise Exception("Path %s FeatureLoad fail! ret[0x%x]" % (os.path.join(ROOT,"MV-CA050-12UM_K27297324.mfs"),ret))
            
        return camera

    def start_camera(self):
        stParam = MVCC_INTVALUE()
        memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))

        ret = self.camera.MV_CC_GetIntValue("PayloadSize", stParam)
        if ret != 0:
            raise Exception("get payload size fail! ret[0x%x]" % ret)

        self.nDataSize = stParam.nCurValue
        self.pData = (c_ubyte * self.nDataSize)()
        self.stFrameInfo = MV_FRAME_OUT_INFO_EX()
        memset(byref(self.stFrameInfo), 0, sizeof(self.stFrameInfo))

        self.camera.MV_CC_StartGrabbing()

    def get_image(self, width=None):
        """
        :param cam:     相机实例
        :active_way:主动取流方式的不同方法 分别是（getImagebuffer）（getoneframetimeout）
        :return:
        """
        ret = self.camera.MV_CC_GetOneFrameTimeout(self.pData, self.nDataSize, self.stFrameInfo, 500)
        if ret == 0:
            image = np.asarray(self.pData).reshape((self.stFrameInfo.nHeight, self.stFrameInfo.nWidth))
            # cv2.imwrite("./image.bmp", image) 
            return image  
        else:
            return None
    
    def cameraShot(self):
        frame = self.get_image()
        now = time.time()
        key = 'img_' + str(int(now))
        pathdir = os.path.join('static/result', key)
        if os.path.exists(os.path.join(ROOT,pathdir)) == False:
            os.makedirs(os.path.join(ROOT,pathdir))
        img_path = os.path.join(pathdir, 'image.bmp')
        cv2.imwrite(os.path.join(ROOT,img_path), frame)
        self.saveResults(pathdir)
        print("拍照完成")
        return os.path.join(os.path.join(ROOT,pathdir), "image_result.json")
    def hasDetectCode(self):
        frame = self.get_image()
        trigger = str(len(pbar.decode(frame)))
        if trigger == '0':
            return json.dumps({"trigger":"0","pathdir":""})
        now = time.time()
        key = 'img_' + str(int(now))
        pathdir = os.path.join('static/result', key)
        if os.path.exists(os.path.join(ROOT,pathdir)) == False:
            os.makedirs(os.path.join(ROOT,pathdir))
        img_path = os.path.join(pathdir, 'image.bmp')
        cv2.imwrite(os.path.join(ROOT,img_path), frame)
        return json.dumps({"trigger":trigger,"pathdir":pathdir})

    def saveResults(self,pathdir):
        img_path = os.path.join(pathdir,"image.bmp")
        image = cv2.imread(os.path.join(ROOT,img_path))
        barcodes =  pbar.decode(image)
        length = len(barcodes)
        num = list(range(length))
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
            # 更换为：
            img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # 参数（字体，默认大小）
            font = ImageFont.truetype(os.path.join(ROOT,'fontx/simfang.ttf'), 100)
            # 字体颜色（rgb)
            fillColor = (255,0, 0)
            # 文字输出位置
            position = (x, y - 30)
            # 输出内容
            #str = barcodeData
            text = str(i)
            # 需要先把输出的中文字符转换成Unicode编码形式(  str.decode("utf-8)   )
            draw = ImageDraw.Draw(img_PIL)
            draw.text(position, text, font=font, fill=fillColor)
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
        img_str = os.path.join(pathdir,'image_result.bmp')
        cv2.imwrite(os.path.join(ROOT,img_str), image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        json_result = os.path.join(pathdir,"image_result.json")
        data["image"] = img_path  # 保存原图路径
        data["image_result"] = img_str  # 保存识别结果图片路径
        data["key"] = pathdir
        data["data"] = results # 保存Json识别结果
        with open(os.path.join(ROOT,json_result), "w", encoding='utf-8') as fw:
            fw.write(json.dumps(data))
    def get_Value(self, param_type, node_name):
        """
        :param cam:            相机实例
        :param_type:           获取节点值得类型
        :param node_name:      节点名 可选 int 、float 、enum 、bool 、string 型节点
        :return:               节点值
        """
        if param_type == "int_value":
            stParam = MVCC_INTVALUE() if node_name=="Sharpness" else MVCC_INTVALUE_EX()
            if node_name=="Sharpness":
                memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))
            else:
                memset(byref(stParam), 0, sizeof(MVCC_INTVALUE_EX))
            ret = self.camera.MV_CC_GetIntValue(node_name, stParam)
            if ret != 0:
                raise Exception("获取 int 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stParam.nCurValue

        elif param_type == "float_value":
            stFloatValue = MVCC_FLOATVALUE()
            memset(byref(stFloatValue), 0, sizeof(MVCC_FLOATVALUE))
            ret = self.camera.MV_CC_GetFloatValue(node_name, stFloatValue)
            if ret != 0:
                raise Exception("获取 float 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stFloatValue.fCurValue

        elif param_type == "enum_value":
            stEnumValue = MVCC_ENUMVALUE()
            memset(byref(stEnumValue), 0, sizeof(MVCC_ENUMVALUE))
            ret = self.camera.MV_CC_GetEnumValue(node_name, stEnumValue)
            if ret != 0:
                raise Exception("获取 enum 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stEnumValue.nCurValue

        elif param_type == "bool_value":
            stBool = c_bool(False)
            ret = self.camera.MV_CC_GetBoolValue(node_name, stBool)
            if ret != 0:
                raise Exception("获取 bool 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stBool.value

        elif param_type == "string_value":
            stStringValue = MVCC_STRINGVALUE()
            memset(byref(stStringValue), 0, sizeof(MVCC_STRINGVALUE))
            ret = self.camera.MV_CC_GetStringValue(node_name, stStringValue)
            if ret != 0:
                raise Exception("获取 string 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stStringValue.chCurValue

        else:
            return None

    def set_Value(self, param_type, node_name, node_value = 0):
        """
        :param cam:               相机实例
        :param param_type:        需要设置的节点值得类型
            int:
            float:
            enum:     参考于客户端中该选项的 Enum Entry Value 值即可
            bool:     对应 0 为关，1 为开
            string:   输入值为数字或者英文字符，不能为汉字
        :param node_name:         需要设置的节点名
        :param node_value:        设置给节点的值
        :return:
        """
        if param_type == "int_value":
            ret = self.camera.MV_CC_SetIntValue(node_name, int(node_value))
            if ret != 0:
                raise Exception("设置 int 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "float_value":
            ret = self.camera.MV_CC_SetFloatValue(node_name, float(node_value))
            if ret != 0:
                raise Exception("设置 float 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "enum_value":
            ret = self.camera.MV_CC_SetEnumValue(node_name, node_value)
            if ret != 0:
                raise Exception("设置 enum 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "bool_value":
            ret = self.camera.MV_CC_SetBoolValue(node_name, node_value)
            if ret != 0:
                raise Exception("设置 bool 型数据节点 %s 失败 ！ 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "string_value":
            ret = self.camera.MV_CC_SetStringValue(node_name, str(node_value))
            if ret != 0:
                raise Exception("设置 string 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
        elif param_type == "command_value":
            ret = self.camera.MV_CC_SetCommandValue(node_name)
        if ret != 0:
            raise Exception("设置 Command 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
    #开启自动曝光模式
    # def setExposureAutoMode(self, node_value = 0):
    #     nRet = self.camera.MV_CC_SetExposureAutoMode(node_value)
    #     if nRet != 0:
    #         raise Exception("Set ExposureAutoMode fail! nRet [0x%x]\n", nRet)
    # def getExposureAutoMode(self):
    #     return self.camera.MV_CC_GetExposureAutoMode()
    # def setExposureAuto(self, node_value = 0):
    #     self.set_Value("enum_value",node_name="ExposureAuto",node_value=node_value)
    # def getExposureAuto(self):
    #     return self.get_Value("enum_value",node_name="ExposureAuto")
    def setExposureTime(self, exp_time):
        self.set_Value(param_type="float_value", node_name="ExposureTime", node_value=exp_time)
    def getExposureTime(self):
        return self.get_Value("float_value","ExposureTime")

    #设置增益模式
    # def setGainMode(self,value):
    #     self.set_Value(param_type="int_value", node_name="GainMode", node_value=value)
    # def getGainMode(self):
    #     return self.camera.MV_CC_GetGainMode()
    #设置增益
    def setGain(self, gain):
        self.set_Value(param_type="float_value", node_name="Gain", node_value=gain)
    def getGain(self):
        return self.get_Value("float_value","Gain")

    # def setSharpnessEnable(self, node_value):
    #     self.set_Value("bool_value","SharpnessEnable",node_value)
    # def getSharpnessEnable(self):
    #     return self.get_Value("bool_value","SharpnessEnable") 

    def setSharpness(self, node_value):
        self.set_Value("int_value","Sharpness",node_value)
    def getSharpness(self):
        print(self.camera)
        return self.get_Value("int_value","Sharpness") 
    def setLineDebouncerTime(self, node_value):
        self.set_Value("int_value","LineDebouncerTime",node_value)
    def getLineDebouncerTime(self):
        self.get_Value("int_value","LineDebouncerTime")

cap = HKCamera()
