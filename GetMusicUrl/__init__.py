import json
from .configs import configs, User_Agent
from .AES import my_encrypt
import requests


class Music:
    def __init__(self):
        self._url_params = configs['url_params']
        self._detail_params = configs['detail_params']
        self.headers = {
            'User-Agent': User_Agent[0]
        }
        self.data = {}

    def set_id(self, _id):
        self.url_params = _id
        self.detail_params = _id

    @property
    def detail_params(self):
        return json.dumps(self._detail_params)

    @detail_params.setter
    def detail_params(self, _id: str):
        self._detail_params['id'] = _id
        self._detail_params['c'] = '[{"id":"' + _id + '"}]'


    @property
    def url_params(self):
        return json.dumps(self._url_params)

    @url_params.setter
    def url_params(self, _id: str):
        self._url_params['ids'] = '[' + _id + ']'

    def _get_random_a(self):
        """生成随机的字符串，这里不按照原实现做"""
        return configs['random_a']  # 直接返回定值

    def _get_rsa(self):
        """rsa加密"""
        return configs['rsa_random_a']

    def _get_requests_data(self, data, key):
        """生成一个requests所要求的params和encSecKey参数

        首先获取一个随机字符串s
        对数据data使用密钥key进行AES加密获得h
        对h使用新生成的随机串s加密获得encText
        对生成的随机串进行rsa公钥加密获得encSecKey

        以上的key 都是定值
        """
        s = self._get_random_a()
        h = my_encrypt(data, key)
        encText = my_encrypt(h, s)
        encSeckey = self._get_rsa()
        return encText, encSeckey

    def get_music_url(self):
        encText, encSecKey = self._get_requests_data(self.url_params, configs['AES']['first_key'])
        self.data['params'] = encText
        self.data['encSecKey'] = encSecKey
        r = requests.post(configs['url_for_url'], headers=self.headers, data=self.data)
        return r.content.decode('utf8')

    def get_music_detail(self):
        encText, encSecKey = self._get_requests_data(self.detail_params, configs['AES']['first_key'])
        self.data['params'] = encText
        self.data['encSecKey'] = encSecKey
        r = requests.post(configs['url_for_detail'], headers=self.headers, data=self.data)
        return r.content.decode('utf8')

