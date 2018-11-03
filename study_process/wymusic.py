import json
import random
import math
from crypto import my_encrypt

import requests

# 一个预设的随机值
random_a = 'YcZ5UuQRqVpwyBqA'

XD3x_emj = {
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

Xmd = ["色", "流感", "这边", "弱", "嘴唇", "亲", 
        "开心", "呲牙", "憨笑", "猫", "皱眉", "幽灵", 
        "蛋糕", "发怒", "大哭", "兔子", "星星", "钟情", 
        "牵手", "公鸡", "爱意", "禁止", "狗", "亲亲", 
        "叉", "礼物", "晕", "呆", "生病", "钻石", 
        "拜", "怒", "示爱", "汗", "小鸡", "痛苦", 
        "撇嘴", "惶恐", "口罩", "吐舌", "心碎", "生气", 
        "可爱", "鬼脸", "跳舞", "男孩", "奸笑", "猪", 
        "圈", "便便", "外星", "圣诞"]

# d = '{"ids":"[1293886117]","br":128000,"csrf_token":""}'
# e = '010001'
# f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
# g = '0CoJUm6Qyw8W8jud'

def asrsea(d, e, f, g): 
    """
    原js:
    var h = {}
        , i = a(16);
    return h.encText = b(d, g), h.encText = b(h.encText, i), h.encSecKey = c(i, e, f), h
    """
    h = dict()
    i = a(16)
    print('data:', d)
    h['encText'] = b(d, g)
    print('h[encText]: ', h['encText'])

    h['encText'] = b(h['encText'], i)
    print('h[encText]: ', h['encText'])
    
    h['encSecKey'] = c(i, e, f)
    print('h[encSecKey]: ', h['encSecKey'])
    return h


def a(a):
    """注释为原js写法
    
    生成16个随机字符 --又耍我,居然是随机的,就是随便咯
    反正服务器又不知道真假随机,那么只要返回16个字符就行

    由于函数c里解释的那样,这里直接返回预设值: random_a
    """
    """
    # 这里是我自己实现的原函数a的复现(虽然用不上~)
    # d,e
    b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    c = ""
    # for (d = 0; a > d; d += 1)
    for d in range(a):
        # e = Math.random() * b.length,
        e = random.random() * len(b)
        #e = Math.floor(e),
        e = math.floor(e)
        # c += b.charAt(e);
        c += b[e]
    return c
    """
    return random_a

def b(a:str, b:str) -> str:
    """ 这就是一个AES加密函数,负责将数据a与密钥b加密,偏移量固定为"0102030405060708" 
    原js:
    var c = CryptoJS.enc.Utf8.parse(b)
        , d = CryptoJS.enc.Utf8.parse("0102030405060708")
        , e = CryptoJS.enc.Utf8.parse(a)
        , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
    
    a -> e, b -> c, "01020606060708" -> d
    e:数据, c:密钥, d:偏移量, f:最终结果
    选择pkcs[57]padding作为填充方式
    """
    data = a
    key = b
    # key = b # 两次加密使用key不同,第一次固定值,第二次是随机值
    # IV = "0102030405060708"

    f = my_encrypt(data, key)  # aes加密,使用定值 
    return f
    
def c(a, b, c):
    """
    原js
    var d, e;
    return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    
    a: 之前生成的随机值 b:010001
    """
    ## 这里开始一个骚操作
    ### 由于rsa暂时找不到好的库复现,且rsa只是用公钥加密一个我之前自己生成的随机串(即函数a)
    ### 那么我可以指定一个随机串s,用网页版的直接计算出结果rsa(s),把a生成的随机值变为定值s
    ### 以后一直用这个rsa(s)就行,因为服务端不可能知道我这是不是随机

    # 假设的随机值 random_a
    # 那么:
    return "801ebdd452ce91d8e635ed02f2ec61d51160de298c835953e1aca50a0d9976c35f9a97522e167faa3ef11e4c8ef4e3c9ddb63e87425ef391c3bc95fe01b82cfdfe2f34e5d73beb8ae25e7c87e9e62e4e3fa0ca5f8a184f968000f1c2016e6b4e77e01336f219fd8d1c24267b8662052d01568bfab7fc2080329f3ca0be91b8d7"






def main():
    i2x = {
    'br': 128000,
    'csrf_token': "",
    'ids': "[1320098328]"
    }
    # var bZH3x = window.asrsea(JSON.stringify(i2x), bwx3x(["流泪", "强"]), bwx3x(XD3x.md), bwx3x(["爱心", "女孩", "惊恐", "大笑"]));
    # 很显然后面三个参数都是定值,直接写下
    r = asrsea(json.dumps(i2x), 
        "010001", 
        "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7",
        "0CoJUm6Qyw8W8jud")
    
    print("开始发送url请求")
    
    url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
        }
    data = {
        'params': r['encText'],
        'encSecKey': r['encSecKey']
    }
    data2 = {
        'params': 'gjnLYQ4wQ7tEEQpBtcBU3Svha7LR2IMLJvLm88rSikGPMsReKfoOQ2yC5xPgy7W3hYgIINdCCDjXhPvVpCI+Sj3lgGvdti24eXlusQ1lSJZehBM++uDnhBgKbqu2REz3',
        'encSecKey': '56796f571ed478969b096bbfb30b861a40248dddc5070e881f5061880e6a361ebd0aead43d86c5213dc9c5c0ca1046f06616935202a515ab1c4db003f892565f172d7b20394c2d50b6f35c25ecec44c73be8f91024f01d08cf18c103675177bf391a452510e07bc9702b1f325cd924328e4276b3a476d1f033e0f610788b44fd'
    }
    print(data)
    r = requests.post(url, headers=headers, data=data)
    print("\nresponse: ",r.text)


if __name__ == "__main__":
    main()


# def bwx3x(cQA5F) {
#     m2x = []
#     bf3x(cQA5F, function(cQy5D) {
#         m2x.push(XD3x.emj[cQy5D])
#     })
#     return m2x.join("")
# }

# def bf3x(j2x:list, cL5Q:f, O2x) {
#     if (!j2x || !j2x.length || !he8W(cL5Q))  # 八成是骗人,都直接返回了还玩什么编码
#         return this;
#     if (!!j2x.forEach) {
#         j2x.forEach(cL5Q, O2x);
#         return this  # 这里的return应该是没用上
#     }
#     for (var i = 0, l = j2x.length; i < l; i++)
#         cL5Q.call(O2x, j2x[i], i, j2x);
#     return this
# }

# def he8W(i2x:f) {
#     return Ii8a(i2x, "function")
# }

# def Ii8a(i2x:f, t2x:str) {
#     # 最后返回了True,可能是骗我的!!!
#     try {
#         t2x = t2x.toLowerCase();
#         if (i2x === null)
#             return t2x == "null";
#         if (i2x === undefined)
#             return t2x == "undefined";
#         return bd3x.toString.call(i2x).toLowerCase() == "[object " + t2x + "]"
#     } catch (e) {
#         return !1
#     }
# }



