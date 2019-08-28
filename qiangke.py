#-*- coding: utf-8 -*-
import urllib.request
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
from PIL import Image
import capcha
import info
import requests

def qiang(dict1):
    #列一下要用的url
    #登陆页
    url_login = 'https://gsdb.bjtu.edu.cn/client/login/'
    #选课页
    course_url = 'https://gsdb.bjtu.edu.cn/course_selection/select/'
    #验证码页
    yanzhengmaurl = 'https://gsdb.bjtu.edu.cn/get_check_code_image/'
    #提交选课信息的url
    submit_url = 'https://gsdb.bjtu.edu.cn/course_selection/select/select/'

    #用户名密码
    personalInfo = info.PersonalInfo()
    data = personalInfo.login_info
    # print(data)
    # post_data=urllib.request.urlopen(data)
    post_data=urllib.parse.urlencode(data)
    # print('post_data:',post_data)
    # post_data=urllib.request.urlopen(data)
    #加一个header吧,加不加好像都行0.0
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}


    # 初始化一个CookieJar来处理Cookie
    cookieJar=http.cookiejar.CookieJar()
    # 实例化一个全局opener
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJar))

    # 获取cookie
    req = urllib.request.Request(url_login,post_data.encode(encoding='UTF8'),headers)
    result = opener.open(req)
    # 访问课程主页 这个时候每一次访问都自动带着cookie信息了
    #result = opener.open(course_url).read()
    # 显示结果
    # print(result)


    #获取验证码，并将验证码图片保存在当前文件夹
    codeimg = opener.open(yanzhengmaurl).read()
    # result = opener.open(yanzhengmaurl)
    with open('code.png','wb') as fn:
        fn.write(codeimg)
    #img = Image.open('code.png')
    #img.show()

    #在这一步骤提交要选的课
    code = capcha.capcha().strip('\n')
    # print '看看电脑这个二货识别的结果对不对？',code1.strip()
    # input_text = raw_input('y/n>>>')

    #这一步有待优化
    # if input_text == 'y':
    #     code = code1.strip('\n')
    #     print 'code:',code
    # else:
    #     code = raw_input('没时间解释了，快输入正确的验证码>>>')

#>>>>>>>>>>>>>>>>>>>
    # data_list = [("a", "bb1"), ("a", "bb2"), ("a", "bb3")]
    # #request.post(url, data=data_list)
    # data_list = [("checkbox", "19559"), ("checkcode", code)]
    # #req3 = requests.post(submit_url, data=data_list)
    # req3 = urllib.request.Request(submit_url, data=data_list)
    # print('>>>>>>>>>>>>>>>>>>>>>>')
    # print req3.text

#>>>>>>>>>>>>>>>>>>
    # dictMerged = dict1.copy()
    # dictMerged.update(dict2)
    dict2 = {
        'checkcode': code
    }
    submit_data = dict1.copy()
    submit_data.update(dict2)
    # submit_data = {
    #     'checkbox':['19559','20180'],
    #     'checkcode':'1234'
    # }
    #print '哇咔咔咔',submit_data
    submit_data=urllib.parse.urlencode(submit_data)
    #print submit_data

    req2 = urllib.request.Request(submit_url,submit_data.encode(encoding='UTF8'))
    html = opener.open(req2).read()

    #抓一下返回结果
    array = []
    soup = BeautifulSoup(html,'lxml')
    a = soup.find_all("div", class_= ['alert','alert-block','alert-error','fade in'])
    # print(a)
    for i in a:
        array.append(i)
    str1 = str(array[0])
    str2=str1.splitlines()
    str3=str2[3].strip()


    return str3



# if __name__ == '__main__':
#     infomation = info.PersonalInfo()
#     infomation.set_info('19114059', '请输入你的密码')
#     # dict1 = {'checkbox':['19559','20180']}
#     # dict2 = {'123': '12'}
#     # dictMerged = dict1.copy()
#     # dictMerged.update(dict2)
#     # data = urllib.parse.urlencode(dictMerged)
#     dict1 = {'checkbox':'26090'}#城市交通分析与设计'26090',
#     qiang(dict1)