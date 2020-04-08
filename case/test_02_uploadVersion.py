from urllib import parse
import unittest
import time
import requests
import logging
import urllib3
import json

from lib import settings, getSignature, getProductInfo, getToken, getDeviceInfo


class Test_uploadVersion(unittest.TestCase):
    """ota设备上报版本接口"""

    # 类执行前初始
    @classmethod
    def setUpClass(cls):
        # 关闭https的证书校验
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    @classmethod
    def tearDownClass(cls):
        pass

    # 方法前初始
    def setUp(self):
        self.url = settings.get_southUrl() + '/device/version'
        self.productId = getProductInfo.getProductId()
        self.productMasterkey = getProductInfo.getProductMasterkey()
        self.token = getToken.token(self.productId, self.productMasterkey)
        self.devId = getDeviceInfo.getDeviceId()
        self.accessKey = settings.getAccesskey()
        self.accessKeySecret = settings.getAccessKeySecret()
        self.headers = settings.getSouthApiHeaders()

    def tearDown(self):
        pass

    def test_00(self):  # 执行逻辑::设置入参，参数正确填写
        """ota设备上报版本接口-成功"""

        params = {
            'dev_id': self.devId
        }
        body = {
            "f_version": "1.0",
            "s_version": "1.0"
        }
        r = requests.post(url=self.url, params=params, data=json.dumps(body), headers=self.headers, verify=False)
        # success = r.json()['success']
        # 断言success字段中的值
        self.assertIn('success', r.text.lower())
        logging.info(
            f"case:ota设备上报版本-成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
