# -*- coding: utf-8 -*-
import operator ,requests,time,datetime

#返回token
def get_police_login_token(admin,PW):
    #登录页面
    url = "http://vp.pyis.safecenter.com:80/mis/media.mediauserdispatch.loginfromserver/global"
    #历史视频
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    loginv = {'account':'','password':'','equipmentId':''}

    loginv["account"] = admin
    loginv["password"] = PW

    ses = requests.session()
    r = ses.post(url,json = loginv ,headers = headers)
    result = r.json()
    tests = result['data']['token']
    ses.close()
    return tests
#返回历史视频数据，
#userHVInfo = {
#             "count":"",     历史视频总数
#             "name":"",        第一个上传用户的名称
#             "createTime":"",  页面显示的上传时间
#             "address":"",     页面显示的位置信息
#             "title":"",       页面显示的视频文件的标题
#             "duration":""     页面显示的视频文件的时间长度
#         }

def get_historyVideo_info(token,fileType = '2',currentPage = '1',key = ''):
    headers1 = {'Content-Type': 'application/json; charset=UTF-8',
                    'authorization': ''
                    }
    userHVInfo = {
            "count":"",
            "name":"",
            "createTime":"",
            "address":"",
            "title":"",
            "duration":""
        }
    url1 = "http://vp.pyis.safecenter.com:80/mis/media.mediauserfile.getmediauserfilebypagefromserver/global"

    ses = requests.session()
    HVvalues = {'fileType':'2','pageSize':'10','currentPage':'1','key':''}
    headers1['authorization'] = token
    HVvalues['key'] = key
    HVvalues['fileType'] = fileType
    HVvalues['currentPage'] = currentPage

    r = ses.post(url1,json = HVvalues,headers = headers1)
    result = r.json()
    userHVInfo['count'] = result['data']['totalRecord']
    infolist = result['data']['list']
    print(infolist)
    userinfo = infolist[0]
    ses.close()
    userHVInfo['name'] = userinfo['name']
    userHVInfo['title'] = userinfo['title']
    userHVInfo['address'] = userinfo['address']
    createTime = userinfo['createTime']
    duration = userinfo['duration']

    #取视频时长
    hour = int(duration//3600)
    minute = int(duration//60)
    second = duration%60
    if hour<10:
        h = "0" + str(hour)
    elif hour>=10 and hour <60:
        h = str(hour)
    if minute<10:
        m = "0" + str(minute)
    elif minute>=10 and minute <60:
        m = str(minute)
    if second<10:
        s = "0" + str(second)
    elif second>=10 and second <60:
        s = str(second)
    userHVInfo["duration"] = h + ":" + m + ":" + s

    #取显示上次时间
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    year = createTime[:4]
    nowyear = now[:4]
    month = createTime[5:7]
    nowmonth = now[5:7]
    day = createTime[8:10]
    nowday = now[8:10]
    today=datetime.date.today()
    yesterday=today-datetime.timedelta(days=1)
    if year == nowyear:
        if month == nowmonth and day == nowday:
            userHVInfo['createTime'] = createTime[11:-3]
        elif str(createTime[:10]) == str(yesterday):
            userHVInfo['createTime'] = "昨天 "+str(createTime)[11:-3]
        else:
            userHVInfo['createTime'] = createTime.replace("-",".")[5:-3]
    else:
        userHVInfo['createTime'] = createTime.replace("-",".")
    return userHVInfo








