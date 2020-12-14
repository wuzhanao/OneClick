#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
import time
from jsonpath import jsonpath

# courseTitle = "直播测试课·王萌"
class Common(object):
    '''
    公共类
    '''

    @classmethod
    def get_CmsToken(cls, ENV='qatest'):
        '''
        获取cmstoken
        :param ENV:
        :return:
        '''
        if 'qatest' in ENV:
            login_uri = 'http://qa-cms-test.igetcool.com/login/v3.json'
            accessToken = 'YeYFBobcKOQ1IGYjJDxK5rQ9KByUdg'
            res = requests.post(url=login_uri, data={'accessToken': accessToken})
            token = res.json()['data']['authorization']
            return {'Authorization': token}
        elif 'online' in ENV:
            login_uri = 'http://cms.igetcool.com/login/v3.json'
            accessToken = 'mAGzajgg9ddfOLG1kouDrrZbWPqq3Y'
            res = requests.post(url=login_uri, data={'accessToken': accessToken})
            return res.json()['data']['authorization']

    def mytime(self, time):

        """
        返回一个距离当前时间+time的一个时间,time单位为分钟
        :return:
        """

        now = datetime.datetime.now()
        delta_min = datetime.timedelta(minutes=time)
        n_min = now + delta_min

        my_time = n_min.strftime('%Y-%m-%d %H:%M:%S')
        print(my_time)
        return my_time

    def timestamp(self):

        """
        返回一个时间戳
        :return:
        """
        # print(int(time.time()))
        return int(time.time())

    def get_courseId(self, courseTitle):
        '''
        根据课程title获取课程ID
        :return:
        '''

        Title_url = 'http://qa-cms-test.igetcool.com/course/live/findCourseOrCourseTimeOrClassById.json?'
        data = {
            "courseId": '',
            "type": 0
        }
        req = requests.get(Title_url, params=data, headers=self.get_CmsToken())

        for i in range(100):
            if jsonpath(req.json(), "$.data[" + str(i) + "].name")[0] == courseTitle:
                courseId = jsonpath(req.json(), "$.data[" + str(i) + "].id")[0]
                print("成功获取courseId",courseId)
                return courseId
            else:
                print("courseId获取中")

    def oneclck_wechat_message(self, url, chaptername, courseTitle, classname, timefromname, user, work_state):
        '''
        发送企业微信机器人消息
        '''

        message_text = '*************************** ' + "灵云教室创建成功。" + '**************************' + '\n' + \
                        "教室地址：" + str(url) + '\n' + \
                        "小节：" + str(chaptername) + '\n' + \
                        "课程：" + str(courseTitle) + '\n' + \
                        "班级： " + str(classname) + '\n' + \
                        "时段： " + str(timefromname) + '\n' + \
                        "课件： " + "已关联PPT" + '\n' + \
                        "课后练习： " + str(work_state) + '\n' + \
                        "可用账号：" + str(user) + '\n' + \
                       '************************************************************************'
        try:
            # webhook_api = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=eca166df-6483-499f-8a95-2dcedcbfbe07"
            webhook_api = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=0088f3d5-4319-4162-9889-0c2bdf3dae8f"
            data = {
                "msgtype": "text",
                "text": {
                    "content": message_text,
                }
            }
            r = requests.post(webhook_api, json=data, verify=False)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    r = Common()
    # r.get_jiaoyan_token()
    r.jiaoyan_login()
    # r.get_courseId(courseTitle)
    # r.mytime(10)
    # r.mytime(30)