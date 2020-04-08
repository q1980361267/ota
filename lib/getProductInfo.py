from urllib import parse
import time
import requests
import urllib3

from lib import settings, getSignature

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getProductInfo():
    """获得创建产品的信息"""
    url = settings.get_openApiUrl() + '/products'
    accessKey = settings.getAccesskey()
    accessKeySecret = settings.getAccessKeySecret()
    headers = settings.getHeaders()
    signatureNonce = int(time.time())

    params = {
        'accessKeyId': accessKey,
        'currentPage': '1',
        'pageSize': '10',
        'signatureNonce': signatureNonce
    }
    body = {}
    signature = getSignature.get_signature(params, body, accessKeySecret, 'GET')
    params['signature'] = signature
    r = requests.get(url=url, params=params, headers=headers, verify=False)
    # print(r.json())
    return r


def getProductId():
    """获得创建的产品id"""
    r = getProductInfo()
    data = r.json()['data']
    content = data['content']
    pid = content[0].get('id')
    # print(pid)
    return pid


def getProductIdSecond():
    """获得创建产品的id"""
    r = getProductInfo()
    data = r.json()['data']
    content = data['content']
    pid_second = content[1].get('id')
    # print(pid_second)
    return pid_second


def getProductMasterkey():
    """获取创建的产品masterkey"""
    r = getProductInfo()
    data = r.json()['data']
    content = data['content']
    pro_mk = content[0].get('masterKey')
    return pro_mk
# a = getProductId()
# print(a)
# getGatewayProductIdSecond()
