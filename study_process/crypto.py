#!/usr/bin/env python3
from Crypto.Cipher import AES
import Crypto
import base64


# key='0CoJUm6Qyw8W8jud'  # 仅第一次加密密钥 
# data='{"id":"1320098329","c":"[{\"id\":\"1320098329\"}]","csrf_token":""}' # 待加密数据
IV = "0102030405060708"  # 偏移量IV
## wangyi:
# Alqn7oQ8CNZeN+ZTf7Gz2sJ6nkn6/cBD7AM8QCSX7OZPHnhQDkxgZJrzcrBw60g3mnS2jSJgZASeaqr6d+ZHNxiibt8BkXLhbiYProdKRsI=
## my:
# Alqn7oQ8CNZeN+ZTf7Gz2tc1IjvmwiDMOh/u+fci1lmmDacaghCknlD1icS6GcOMyWLFlLkcsypbSVtNBpaL+A==
# 填充方式
BLOCK_SIZE = AES.block_size
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def my_encrypt(data:str, key) -> str:
    # print('将加密:', data)
    obj=AES.new(key, AES.MODE_CBC, IV)


    e1=obj.encrypt(pad(data))


    e2 = base64.b64encode(e1)
    return str(e2)[2:-1]

