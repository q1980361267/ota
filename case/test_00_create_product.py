from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

from lib import settings,getSignature


class Test_createProduct(unittest.TestCase):
    """创建产品接口"""
    #类执行前初始
    @classmethod
    def setUpClass(cls):
        #关闭https的证书校验
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    @classmethod
    def tearDownClass(cls):
        pass

    #方法前初始
    def setUp(self):
        self.url = settings.get_url()+'/products'
        self.accessKey = settings.getAccesskey()
        self.accessKeySecret = settings.getAccessKeySecret()
        self.headers = settings.getHeaders()
        self.signatureNonce = int(time.time())
    def tearDown(self):
        pass

    def test_00(self):  #执行逻辑::设置入参，参数正确填写
        """创建产品-成功"""

        params = {
            'accessKeyId': self.accessKey,
            'signatureNonce': self.signatureNonce,
        }
        body ={
            'name': 'product_mqtt_1',
            'protocolType': 1,
            'nodeType': 1,
            'model': 1,
            'dataFormat': 1,
            'authenticationMethod': 1
        }
        signature = getSignature.get_signature(params, body, self.accessKeySecret, 'POST')
        params['signature'] = signature
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        #断言success字段中的值
        self.assertIn('true', r.text.lower())
        logging.info(f"case:创建产品-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

if __name__ == '__main__':
    unittest.main()