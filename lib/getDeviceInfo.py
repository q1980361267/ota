from urllib import parse
import time
import requests
import urllib3

from lib import settings, getSignature, getProductInfo

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getDeviceInfo():
    """获得创建的网关节点产品的信息"""
    url = settings.get_openApiUrl() + '/devices/multi'
    accessKey = settings.getAccesskey()
    accessKeySecret = settings.getAccessKeySecret()
    headers = settings.getHeaders()
    signatureNonce = int(time.time())
    productId = getProductInfo.getProductId()
    masterkey = getProductInfo.getProductMasterkey()

    params = {
        'accessKeyId': accessKey,
        'currentPage': '1',
        'masterkey' : masterkey,
        'pageSize': '10',
        'productId' : productId,
        'signatureNonce': signatureNonce
    }
    body = {}
    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, headers=headers, verify=False)
    # print(r.json())
    return r


def getDeviceId():
    """获得创建的设备id"""
    r = getDeviceInfo()
    data = r.json()['data']
    content = data['content']
    did = content[0].get('id')
    # print(pid)
    return did


def getDeviceApikey():
    r = getDeviceInfo()
    data = r.json()['data']
    content = data['content']
    dev_ak = content[0].get('apiKey')
    return dev_ak
# a = getDeviceId()
# b = getDeviceApikey()
# print(a)
# print(b)
