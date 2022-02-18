import requests

cookies = {
    'JSESSIONID': 'FF838E61C119E587F8929F2800468CC8',
    'vjuid': '8798',
    'vjvd': '4e5892342a29df0583c22eba924bff00',
    'vt': '159870686',
    'UUkey': '323efdd3e456b30eb5fab1e4f14bee5f',
}

headers = {
    'Host': 'yqdwxx.sau.edu.cn',
    'Accept': 'text/plain, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://yqdwxx.sau.edu.cn',
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800122c) NetType/WIFI Language/zh_CN',
    'Connection': 'keep-alive',
    'Referer': 'https://yqdwxx.sau.edu.cn/index.jsp?code=ypWbQxWidP_udNxAWnmVCVxSdYld7hs-wBJCEZgDZAY&state=STATE',
    'Content-Length': '105',
}

data = '{"userid":"183401010121","latitude":"35.77362060546875","longitude":"115.06565856933594","accuracy":"35"}'

response = requests.post('https://yqdwxx.sau.edu.cn/YQDLWZ', headers=headers, cookies=cookies, data=data)

print(response.text)
