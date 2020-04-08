import base64
import hmac


def token(productId, masterKey):
    """获取加密后的token值"""
    version = '2018-10-31'
    res = 'products/%s' % productId
    et = 1644653420
    method = 'sha1'
    key = base64.b64decode(masterKey)
    org = str(et) + '\n' + method + '\n' + res + '\n' + version
    sign_b = hmac.new(key=key, msg=org.encode(), digestmod=method)
    sign = base64.b64encode(sign_b.digest()).decode()
    sign1 = base64.b64encode(sign_b.digest())
    token = 'version=%s&res=%s&et=%s&method=%s&sign=%s' % (version, res, et, method, sign)
    return token


if __name__ == '__main__':
    id = '102502'
    masterKey = 'YThlMzRmNTIwOWJkOGYzYmI5ZWQ='
    # print(token(id,access_key))
    a = token(id, masterKey)
    print(a)
