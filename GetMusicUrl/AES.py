from Crypto.Cipher import AES
import base64
from .configs import configs

BLOCK_SIZE = AES.block_size
# 填充方式
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE).encode('utf8')


def my_encrypt(data: str, key: str) -> str:
    # print('将加密:', data)
    b_data = data.encode('utf8')
    b_key = key.encode('utf8')
    IV = configs['AES']['IV'].encode('utf8')
    obj = AES.new(b_key, AES.MODE_CBC, IV)
    e1 = obj.encrypt(pad(b_data))
    e2 = base64.b64encode(e1)
    return str(e2)[2:-1]

