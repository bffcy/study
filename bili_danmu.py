import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import wordcloud

#https://blog.csdn.net/qq_42582489/article/details/107800766?utm_medium=distribute.pc_relevant.none-task-blog-searchFromBaidu-2.not_use_machine_learn_pai&depth_1-utm_source=distribute.pc_relevant.none-task-blog-searchFromBaidu-2.not_use_machine_learn_pai
#https://blog.csdn.net/weixin_43996337/article/details/103206063?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.not_use_machine_learn_pai&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.not_use_machine_learn_pai


cid = input("请输入cid：")
saveFile = input("请输入保存文件名：")

# 弹幕保存文件
file_name = saveFile + '.csv'

# 获取页面 cid = 262035539
url = "https://comment.bilibili.com/" + str(cid) + ".xml"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
request = requests.get(url=url, headers=headers)
request.encoding = 'utf-8'

# 提取弹幕
soup = BeautifulSoup(request.text, 'lxml')
results = soup.find_all('d')

# 数据处理
data = [data.text for data in results]
# 正则去掉多余的空格和换行 for i in data:
#    i = re.sub('', '\s+', i)

# 查看数量
print("弹幕数量为：{}".format(len(data)))

# 输出到文件
df = pd.DataFrame(data)
df.to_csv(file_name, index=False, header=None, encoding="utf_8_sig")
print("写入文件成功")


# 从外部.txt文件中读取大段文本，存入变量txt中
f = open('F:/StudyCode/es6/' + saveFile + '.csv',encoding='utf-8')
txt = f.read()

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# 将txt变量传入w的generate()方法，给词云输入文字
w.generate(txt)

# 将词云图片导出到当前文件夹
w.to_file('F:/StudyCode/es6/' + saveFile + '词云.png')
print("词云生成成功")