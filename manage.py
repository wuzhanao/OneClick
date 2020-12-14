#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from common import Common as C
from jsonpath import jsonpath


# workId = "537801164004134912"
# scheduleId = "537801155206971392"
# coursePid = "419215261709049856"
# chapterPid = "537804450390634496"

class Class_Manage(object):

    '''
    班课-发布作业
    '''

    def __init__(self, scheduleId, coursePid, chapterPid):
        self.scheduleId = scheduleId
        self.coursePid = coursePid
        self.chapterPid = chapterPid
        # self.auth = {"Authorization": "RPpDiT6ASqSejwmrJKIVPfDMKFBrnT"}
        self.auth = {"Authorization": "i2GPlOsPKk3oc5WXcmUM4EHDYIoEGD"}

    def work_push(self):
        '''
        发布作业
        :return:
        '''
        self.workId = self.get_workid()
        url = "http://qa-course-test.igetcool.com/admin/mgt/work/issue?"
        data = {
            "workId": self.workId,
            "scheduleId": self.scheduleId,
            "lastCommitTime": C().mytime(720)
        }
        req = requests.get(url=url, params=data, headers= self.auth)
        print(req.json())

    def get_workid(self,):
        '''
        获取workid
        :return:
        '''
        url = "http://qa-course-test.igetcool.com/admin/chapter/work/query?"
        data = {
            "coursePid": self.coursePid,
            "chapterPid": self.chapterPid
        }
        req = requests.get(url=url, params=data, headers=self.auth)
        print("workid:", req.json())
        workId = jsonpath(req.json(), "$.data.workList[0].workPid")[0]
        print(workId)
        return workId

# if __name__ == '__main__':
#
#     r = Class_Manage(scheduleId, coursePid, chapterPid)
#     # r.work_push()
#     r.get_workid()