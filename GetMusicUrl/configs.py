
random_a = 'YcZ5UuQRqVpwyBqA'  # 刻意的随机值
# 用某music的公钥对以上随机值加密的结果
rsa_random_a = '801ebdd452ce91d8e635ed02f2ec61d51160de298c835953e1aca50a0d9976c35f9a97522e167faa3ef11e4c8ef4e3c9ddb63e87425ef391c3bc95fe01b82cfdfe2f34e5d73beb8ae25e7c87e9e62e4e3fa0ca5f8a184f968000f1c2016e6b4e77e01336f219fd8d1c24267b8662052d01568bfab7fc2080329f3ca0be91b8d7'

url_params = {
    'br': 128000,
    'csrf_token': "",
    'ids': "[0123456789]"
}

detail_params = {
    'id': '0',
    'c': '[{"id":"0000"}]',
    'csrf_token': ''
}

emj2hex = {
    "色": "00e0b", "流感": "509f6", "这边": "259df", "弱": "8642d",
    "嘴唇": "bc356", "亲": "62901", "开心": "477df", "呲牙": "22677",
    "憨笑": "ec152", "猫": "b5ff6", "皱眉": "8ace6", "幽灵": "15bb7",
    "蛋糕": "b7251", "发怒": "52b3a", "大哭": "b17a8", "兔子": "76aea",
    "星星": "8a5aa", "钟情": "76d2e", "牵手": "41762", "公鸡": "9ec4e",
    "爱意": "e341f", "禁止": "56135", "狗": "fccf6", "亲亲": "95280",
    "叉": "104e0", "礼物": "312ec", "晕": "bda92", "呆": "557c9",
    "生病": "38701", "钻石": "14af6", "拜": "c9d05", "怒": "c4f7f",
    "示爱": "0c368", "汗": "5b7a4", "小鸡": "6bee2", "痛苦": "55932",
    "撇嘴": "575cc", "惶恐": "e10b4", "口罩": "24d81", "吐舌": "3cfe4",
    "心碎": "875d3", "生气": "e8204", "可爱": "7b97d", "鬼脸": "def52",
    "跳舞": "741d5", "男孩": "46b8e", "奸笑": "289dc", "猪": "6935b",
    "圈": "3ece0", "便便": "462db", "外星": "0a22b", "圣诞": "8e7",
    "流泪": "01000", "强": "1", "爱心": "0CoJU", "女孩": "m6Qyw",
    "惊恐": "8W8ju", "大笑": "d"
}

emjs = ["色", "流感", "这边", "弱", "嘴唇", "亲",
        "开心", "呲牙", "憨笑", "猫", "皱眉", "幽灵",
        "蛋糕", "发怒", "大哭", "兔子", "星星", "钟情",
        "牵手", "公鸡", "爱意", "禁止", "狗", "亲亲",
        "叉", "礼物", "晕", "呆", "生病", "钻石",
        "拜", "怒", "示爱", "汗", "小鸡", "痛苦",
        "撇嘴", "惶恐", "口罩", "吐舌", "心碎", "生气",
        "可爱", "鬼脸", "跳舞", "男孩", "奸笑", "猪",
        "圈", "便便", "外星", "圣诞"]

AES = {
    'IV': "0102030405060708",  # AES加密中的偏移量IV
    'first_key': '0CoJUm6Qyw8W8jud',  # AES 密钥，这里只是第一次的那个固定默认密钥
    'second_key': random_a  # AES 密钥，这是第二次的所谓随机值密钥
}

configs = {
    'emj': emjs,
    'emj2hex': emj2hex,
    'url_params': url_params,
    'url_for_url': 'https://music.163.com/weapi/song/enhance/player/url?csrf_token=',
    'detail_params': detail_params,
    'url_for_detail': 'https://music.163.com/weapi/v3/song/detail?csrf_token=',
    'AES': AES,
    # 为了逻辑的顺畅，这里略做重复
    'random_a': random_a,
    'rsa_random_a': rsa_random_a
}

User_Agent = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
]
