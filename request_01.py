import requests

# login_data = {
#     "email": '7237672@qq.com',
#     "password": 'abc123456'
# }
# 实例化session方法
# session = requests.session()

# 发送请求，并提供数据
# response = requests.post(url='http://yushu.talelin.com/login', data=login_data)
# response = session.post(url='http://yushu.talelin.com/login', data=login_data)
# print(response.text)
# person_response = requests.get('http://yushu.talelin.com/personal')
# person_response = session.get('http://yushu.talelin.com/personal')
# print(person_response.text)

# 使用代理访问
# posix = {
#     'http':'http://218.106.63.212:21080',
#     "https":'http://218.106.63.212:21080'
# }
# # SSL证书默认verify是开启的需要验证，设置为False关闭，或者指定路径可以解决证书报错的问题
# response_po = requests.get('http://pv.sohu.com/cityjson', proxies=posix, verify=False)
# print(response_po.text)


# 编程实战
for i in range(1,5):
    url = 'http://yushu.talelin.com/book/search?q=python&page={}'.format(i)
    response = requests.get(url=url)
    html_file_name = 'page_{}.html'.format(i)
    with open(html_file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print('{}文件已下载好'.format(html_file_name))
