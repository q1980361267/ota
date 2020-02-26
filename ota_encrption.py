import base64
import hmac
from urllib.parse import quote
def token(id,access_key):
    version = '2018-10-31'
    res = 'products/%s' % id
    et = 1644653420
    method = 'sha1'
    key = base64.b64decode(access_key)
    org = str(et) + '\n' + method + '\n' + res + '\n' + version
    sign_b = hmac.new(key=key, msg=org.encode(), digestmod=method)
    sign = base64.b64encode(sign_b.digest()).decode()
    token = 'version=%s&res=%s&et=%s&method=%s&sign=%s' % (version, res, et, method, sign)
    return token
if __name__ == '__main__':
    id = '102251'
    access_key = 'NDAzMGY0NDA0N2IwMjJkNDcxNDM='
    print(token(id,access_key))