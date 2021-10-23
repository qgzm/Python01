# 使用者：姜海波
# 创建时间：2021/10/23  11:31

import requests


req=input('请输入你想要搜索的人物')
url=f'https://cn.bing.com/search?q={req}'
head={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}
resp=requests.get(url,head)
print(resp)
print(resp.text)





url = "https://fanyi.baidu.com/sug"
s=input('请输入你想要翻译的英文单词')
dat={'kw': s}       #kw不能更改
# 发送请求
resp=requests.post(url,data=dat)
print(resp.json())



url="https://movie.douban.com/j/chart/top_list"

pargam={
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'
}

resp=requests.get(url,params=pargam,headers=headers)
print(resp.request.url)



print(resp.json())
resp.close()        #关掉resp