import request_01

# 通过get请求数据
# response = requests.get(url='http://www.qq.com')
# print(response.text)

# data = {
#     "name": "yezhian"
# }
# response_post = requests.post(url="http://httpbin.org/post", data=data)
# print(response_post)

# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }
# response = requests.get(url='http://httpbin.org/get', params=data)
# print(response.text)

# response = requests.get('https://www.imooc.com/static/img/index/logo.png')
# # print(response.text)
# with open('imooc.png', 'wb') as f:
#     f.write(response.content)
# header= {
#     'User-Agent': 'yezhian'
# }
# response = requests.get('http://httpbin.org/ip', headers=header, timeout=1)  # 设置请求时间
# data = response.json()
# print(data['origin'])
# print(response.status_code)
# print(response.headers)  # 返回头
# print(response.request.headers)  # 请求头

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='hello world')
response = requests.get(url=url, cookies=cookies)
print(response.cookies)

