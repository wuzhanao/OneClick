#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from jsonpath import jsonpath
from login import Login_request
from requests.auth import HTTPBasicAuth
from time import sleep
import sys

# 外部输入只能是"测试"或者"线上"

# env = sys.argv[1]

courseId = 508799453602340864
classId = 508801457665957888
timeFrameId = 508801457590460416


class DownloadApp(object):

    # courseId = 508799453602340864
    # classId = 508801457665957888
    # timeFrameId = 508801457590460416

    def __init__(self):
        # self.req = self.login_setup()
        self.baseurl = "http://qa-cms-test.igetcool.com"
        self.header = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            # 'Content-Type': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self.get_CmsToken('qatest'),
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'qa-course-test.igetcool.com',
            'Origin': 'http://qa-cms-test.igetcool.com',
            'Referer': 'http://qa-cms-test.igetcool.com/courseCourseConfig'
        }
        self.timeout = 10

    def getappversion(self, ENV):
        # 获取APP版本列表
        versionlist = '/course/live/findClassScheduleByClassId.json?'
        versionlist_url = self.baseurl + versionlist
        date = {
            'courseId': courseId,
            'type': 0,
            'classId': classId,
            'timeFrameId': timeFrameId
        }
        getrep = requests.get(url=versionlist_url, params=date, headers={'Authorization': self.get_CmsToken(ENV)})
        print(getrep.json())

        return getrep

    def end_class(self, ENV):
        # 下课
        end_clas_url = 'https://qa-live-test.igetcool.com/signal/api/teacher/command/110000599/end_class/send'
        data = {
            'clientAt': '1606120427272',
            'roomId': '110000599',
            'toId': -1,
            'token': 'TJ+v3JDy0UpPINvdjRXOxxB8T+SY0Aw1wbLV1cfAf08=@iiy7.cn.rongnav.com;iiy7.cn.rongcfg.com',
            'version': '10',
            'cmdName': 'end_class',
            'content': '下课'
        }
        send = requests.post(url=end_clas_url, json=data, headers={'Authorization': self.get_CmsToken(ENV)})
        print(send.json())

    def update_class(self, ENV):
        # 编辑上下课时间
        # 坑 ：from-data类型不要放在data中传，要拼在链接里
        # update_url = 'http://qa-course-test.igetcool.com/admin/course/live/updateClassScheduleById?scheduleId=508808831701458944'\
        #              '&liveStartTime=2020-11-23 19:58:55&liveEndTime=2020-11-23 20:54:57'
        update_url = 'http://qa-course-test.igetcool.com/admin/course/live/updateClassScheduleById'

        param = {"scheduleId": "508808831701458944",
                 "liveStartTime": "2020-11-25 19:58:55",
                 "liveEndTime": "2020-11-25 20:54:57"}
        update_req = requests.post(url=update_url, params=param, headers={'Authorization': self.get_CmsToken(ENV)})
        # print(update_req.json())

    def re_class(self):
        # 重新生成教室

        re_url = 'http://qa-course-test.igetcool.com/admin/course/live/doRebuildClassScheduleRoom?scheduleId=508808831701458944'
        re_req = requests.post(url=re_url, headers=self.header)
        print(re_req.cookies)
        print(re_req.json())

    def get_CmsToken(self, ENV):

        if 'qatest' in ENV:
            login_uri = 'http://qa-cms-test.igetcool.com/login/v3.json'
            accessToken = 'YeYFBobcKOQ1IGYjJDxK5rQ9KByUdg'
            res = requests.post(url=login_uri, data={'accessToken': accessToken})
            return res.json()['data']['authorization']
        elif 'online' in ENV:
            login_uri = 'http://cms.igetcool.com/login/v3.json'
            accessToken = 'mAGzajgg9ddfOLG1kouDrrZbWPqq3Y'
            res = requests.post(url=login_uri, data={'accessToken': accessToken})
            return res.json()['data']['authorization']

    def get_Cms(self, ENV):

        url = 'http://qa-cms-test.igetcool.com/common/module/list.json?module=free_zone'
        res = requests.get(url=url, headers={'Authorization': self.get_CmsToken(ENV)})
        print(res.json())


if __name__ == '__main__':
    getapp = DownloadApp()
    # getapp.login_setup()
    # getapp.get_post()
    # print(getapp.get_Cms('qatest'))
    # print(getapp.getappversion('qatest'))
    # print(getapp.end_class('qatest'))
    print(getapp.update_class('qatest'))
    # print(getapp.re_class())
