import requests
import random
import time

class post:
    def __init__(self, task_province, task_city, task_coordinate, task_username,
    task_stu_id, task_phone, task_institution, task_form_id,
    vjuid, vjvd, vt, UUkey):
        super().__init__()
        self.task_province = task_province
        self.task_city = task_city
        self.task_coordinate = task_coordinate
        self.task_username = task_username
        self.task_stu_id = task_stu_id
        self.task_phone = task_phone
        self.task_institution = task_institution
        self.task_form_id = task_form_id
        self.cookies = {
            'vjuid': vjuid,
            'vjvd': vjvd,
            'vt': vt,
            'UUkey': UUkey,
        }

        self.headers = {
            'Host': 'app.sau.edu.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://app.sau.edu.cn',
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.18(0x17001231) NetType/WIFI Language/zh_CN',
            'Connection': 'keep-alive',
            'Referer': 'https://app.sau.edu.cn/form/wap/default?formid=10',
            'Content-Length': '536',
        }

        self.locate_headers = {
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

        self.params = (
            ('formid', '10'),
        )

    def locate(self):
        if (len(self.task_coordinate.split(',')) == 2):
            cookie = self.cookies
            cookie['JSESSIONID'] = 'FF838E61C119E587F8929F2800468CC8'
            data = '{"userid":' + self.task_stu_id + ',"latitude":' + self.task_coordinate.split(',')[0] + ',"longitude":' + self.task_coordinate.split(',')[1] + ',"accuracy":"35"}'
            response = requests.post('https://yqdwxx.sau.edu.cn/YQDLWZ', headers = self.locate_headers, cookies = self.cookies, data = data)

            # print(response.text)
            # print(data)
            return(str(response.status_code))
        else:
            return('404')

    def clock_in(self):
        self.data = {
        'xingming': self.task_username,
        'xuehao': self.task_stu_id,
        'shoujihao': self.task_phone,
        'danweiyuanxi': self.task_institution,
        'dangqiansuozaishengfen': self.task_province,
        'dangqiansuozaichengshi': self.task_city,
        'shifouyuhubeiwuhanrenyuanmiqie': '否',
        'shifoujiankangqingkuang': '是',
        'shifoujiechuguohubeihuoqitayou': '否',
        'fanhuididian': '',
        'shifouweigelirenyuan': '否',
        'shentishifouyoubushizhengzhuan': '否',
        'shifouyoufare': '否',
        'qitaxinxi': '',
        'tiwen': '36.' + str(random.randint(1,5)),
        'tiwen1': '36.' + str(random.randint(1,5)),
        'tiwen2': '36.' + str(random.randint(1,5)),
        'riqi': time.strftime('%Y-%m-%d'),
        'id': self.task_form_id
        }

        response = requests.post('https://app.sau.edu.cn/form/wap/default/save', headers = self.headers, params = self.params, cookies = self.cookies, data = self.data)
        return response.json()

if __name__ == "__main__":
    response = post()
    print(response.task_username, response.clock_in()['m'], response.data['riqi'], response.data['tiwen'], response.data['tiwen1'], response.data['tiwen2'])
