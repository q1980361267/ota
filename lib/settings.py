from lib import getProductInfo, getToken


def get_openApiUrl():
    """获得公用的url"""
    # url = 'http://api.heclouds.com:9090/oes/api/v1'

    # 测试环境地址
    url = 'https://test.api.heclouds.com/oes/api/v1'
    return url


def get_southUrl():
    """获得南向接口地址"""
    # 测试环境
    url = 'http://10.12.6.24:31794/ota'
    return url


def getHeaders():
    """获取公用的headers数据"""
    headers = {
        'Content-Type': 'application/json',
        'platform': '1'
    }
    return headers


def getSouthApiHeaders():
    productId = getProductInfo.getProductId()
    productMasterkey = getProductInfo.getProductMasterkey()
    token = getToken.token(productId, productMasterkey)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    return headers

def getAccesskey():
    """获得公用的accessKey参数"""
    # 测试环境accessKey
    accessKey = 'WVcrj0t7plUrgqrz'
    return accessKey


def getAccessKeySecret():
    """获得公用的accessKeySecret参数"""
    # 测试环境accessKeySecret
    accessKeySecret = 'QHnRyeFzgM9noUBBRCXFXTrIZtgN0iV9voVY'
    return accessKeySecret
