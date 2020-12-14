#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from common import Common as C
from jsonpath import jsonpath

# courseId = '535675127998566400'
# courseId = '508066404656832512'
# scheduleId = '535696683323752448'

class RoomURL(object):
    '''
    教导主任-排期-生成教室-获取上课url
    '''
    def __init__(self, courseId, classname, timefromname, chapter_id,courseTitle):
        self.courseId = courseId
        self.classname = classname
        self.timefromname = timefromname
        self.chapter_id = chapter_id
        self.courseTitle = courseTitle


    def update_class(self):
        '''
        编辑上下时间
        :param ENV:
        :return:
        '''
        scheduleId = self.get_scheduleId()

        update_url = 'http://qa-course-test.igetcool.com/admin/course/live/updateClassScheduleById'

        params = {"scheduleId": scheduleId,
                 "liveStartTime": C().mytime(time=10),
                 "liveEndTime": C().mytime(time=40)
                 }
        update_req = requests.post(url=update_url, params=params, headers=C.get_CmsToken())
        print(update_req.json())

    def click_roombtn(self):
        '''
        点击生成教室，获取roomID，返回手机号
        :return:
        '''
        self.update_class()
        scheduleId = self.get_scheduleId()
        userphon = self.get_userphon()
        # 点击接口一
        clickroomurl = 'https://qa-course-test.igetcool.com/admin/course/live/doCreateClassScheduleRoom?'
        params = {"scheduleId": scheduleId}
        clik_req = requests.post(url=clickroomurl, params=params, headers=C.get_CmsToken())
        # print(clik_req.json())
        # 点击接口二
        url = 'https://qa-course-test.igetcool.com/admin/course/live/saveLingCloudScheduleRoom?'
        data = {
            "scheduleId": scheduleId
            }
        req = requests.get(url=url, params=data, headers=C.get_CmsToken())
        # print(req.json())
        # 获取roomID接口
        roomid_url = 'http://qa-cms-test.igetcool.com/course/live/findClassScheduleByClassId.json?'
        data_a = {
            "courseId": self.courseId,
            "type": 0,
            "classId": self.classid,
            "timeFrameId": self.timefromid
        }
        req_a = requests.get(url=roomid_url, params=data_a, headers=C.get_CmsToken())

        for i in range(100):
            print(i)
            if jsonpath(req_a.json(), "$.data[" + str(i) + "].scheduleId")[0] == scheduleId:
                # print(jsonpath(req_a.json(), "$.data[" + str(i) + "].liveSource.roomId")[0])
                print("成功获取roomId")
                return jsonpath(req_a.json(), "$.data[" + str(i) + "].liveSource.roomId")[0], scheduleId, userphon
            else:
                print("未获取roomId")

    def timefrom_id(self):
        '''
        获取时段id
        :return:
        '''
        timefrom_url = 'http://qa-cms-test.igetcool.com/course/live/findCourseOrCourseTimeOrClassById.json?'
        data = {
            "id": self.courseId,
            "type": 1
        }
        req = requests.get(timefrom_url, params=data, headers=C.get_CmsToken())
        for i in range(20):
            if jsonpath(req.json(), "$.data[" + str(i) + "].name")[0] == self.timefromname:
                # print(jsonpath(req.json(), "$.data[" + str(i) + "].id")[0])
                return jsonpath(req.json(), "$.data[" + str(i) + "].id")[0]
            else:
                print("时段id获取中")


    def class_id(self):
        '''
        获取班级id
        :return:
        '''
        timefrom_id = self.timefrom_id()
        timefrom_url = 'http://qa-cms-test.igetcool.com/course/live/findCourseOrCourseTimeOrClassById.json?'
        data = {
            "id": timefrom_id,
            "type": 2
        }
        req = requests.get(timefrom_url, params=data, headers=C.get_CmsToken())
        for i in range(20):
            if jsonpath(req.json(), "$.data[" + str(i) + "].name")[0] == self.classname:
                print(jsonpath(req.json(), "$.data[" + str(i) + "].id")[0])
                print(timefrom_id)
                return jsonpath(req.json(), "$.data[" + str(i) + "].id")[0], timefrom_id
            else:
                print("班级id获取中")

    def get_scheduleId(self):
        '''
        从教导主任小节列表获取scheduleId
        :return:
        '''
        # 获取时段、班级id
        self.classid, self.timefromid = self.class_id()

        timefrom_url = 'http://qa-cms-test.igetcool.com/course/live/findClassScheduleByClassId.json?'
        data = {
            "courseId": self.courseId,
            "classId": self.classid,
            "type": 0,
            "timeFrameId": self.timefrom_id
            }
        req = requests.get(timefrom_url, params=data, headers=C.get_CmsToken())
        for i in range(100):
            print(i)
            if jsonpath(req.json(), "$.data[" + str(i) + "].chapterId")[0] == self.chapter_id:
                print(jsonpath(req.json(), "$.data[" + str(i) + "].scheduleId")[0])
                print(self.timefromid)
                print("成功获取scheduleId")
                return jsonpath(req.json(), "$.data[" + str(i) + "].scheduleId")[0]
            else:
                print("未获取scheduleId")


    def get_userphon(self):
        '''
        获取班级下用户手机
        :return:
        '''

        phone_url = "http://qa-cms-test.igetcool.com/course/class/list.json?"
        data = {
            "coursePid":self.courseId,
            "courseTitle": self.courseTitle,
            "pageIndex": 1,
            "pageSize": 10,
            "classPid": self.classid
        }
        req = requests.get(url=phone_url, params=data, headers=C.get_CmsToken())
        pages = jsonpath(req.json(), "$.data.pages")
        # 获取最后一页账号
        data_1 = {
            "coursePid":self.courseId,
            "courseTitle": self.courseTitle,
            "pageIndex": pages,
            "pageSize": 10,
            "classPid": self.classid
        }
        req = requests.get(url=phone_url, params=data_1, headers=C.get_CmsToken())
        userphone = jsonpath(req.json(), "$.data.list[*].userPhone")
        print("用户手机", userphone)
        return userphone




# if __name__ == '__main__':
    # re = RoomURL()
    # re.update_class('535696683323752448')
    # re.click_roombtn(scheduleId)
    # re.timefrom_id(courseId)
    # re.class_id(courseId)
    # re.get_scheduleId()