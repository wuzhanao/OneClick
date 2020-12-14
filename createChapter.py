#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from common import Common as C
from jsonpath import jsonpath

# courseId = '535675127998566400'

class Chapter(object):


    def __init__(self, courseId):
        '''
        初始化
        '''
        self.courseId = courseId
        self.count = self.get_chapt_count()

    def create_chapter(self):
        '''
        创建小节
        :return:
        '''
        chpter_url = 'https://qa-course-test.igetcool.com/admin/course/live/createChapter?'
        chapterTitle = "第" + str(self.count+1) + "课" + str(C().timestamp())
        data= {
            "livePattern" : "0",
            "screenRatio" : "0",
            "chapterTitle" : chapterTitle,
            "sort" : self.count + 1,
            "courseId" : self.courseId,
            "videoImageUrl" : "https://coolcdn.igetcool.com/p/2020/11/481108fcd322123d820a94477672ae66.png?_600x336.png",
            "pptDefaultImg" : "300",
            "techDefaultImg" : "",
            "liveType" : "1",
            "labelId" : "0",
            "chapterType" : "1"
        }
        aa = requests.post(url=chpter_url, params=data,headers=C.get_CmsToken())
        # print(aa.text)
        # print(aa.url)
        print(chapterTitle)
        return chapterTitle

    def get_chapt_count(self):
        '''
        获取小节列表,返回当前小节数
        :return:
        '''
        chapt_list_url = 'https://qa-course-test.igetcool.com/admin/course/live/findChapterByCourseId?'
        data = {"courseId": self.courseId, "pageIndex": "1"}
        req = requests.get(url=chapt_list_url, params=data, headers=C.get_CmsToken())
        count = jsonpath(req.json(), "$.data.total")[0]
        print(req.url)
        # chapterId = jsonpath(req.json(), "$.data.list[*].chapterId")[0]
        # print(req.json())
        return count

    def get_chapt_chapterid(self):
        '''
        创建小节，并获取新建小节ID
        :return:
        '''
        self._chapterTitle = self.create_chapter()
        chapt_list_url = 'https://qa-course-test.igetcool.com/admin/course/live/findChapterByCourseId?'
        data = {"courseId": self.courseId, "pageIndex": "1"}
        req = requests.get(url=chapt_list_url, params=data, headers=C.get_CmsToken())
        for i in range (self.count):
            # print(jsonpath(req.json(), "$.data.list[" + str(i) + "].chapterTitle")[0])
            if jsonpath(req.json(), "$.data.list[" + str(i) + "].chapterTitle")[0] == self._chapterTitle:
                chapterId = jsonpath(req.json(), "$.data.list[" + str(i) + "].chapterId")[0]
                print(chapterId)
                return chapterId
            else:
                print("未查到chapterId")

    def chapter_online(self):
        '''
        上架小节
        :return:
        '''
        chapterId = self.get_chapt_chapterid()
        chapter_online_url = 'http://qa-cms-test.igetcool.com/course/live/doChapterOnlineById.json'
        data = {"chapterId": chapterId}
        req = requests.post(chapter_online_url, params=data, headers=C.get_CmsToken())
        r = req.json()
        # print(r)
        # assert jsonpath(r, "$.code")[0] == 10000
        return chapterId, self._chapterTitle

# if __name__ == '__main__':
#     fc = Chapter()
#     # fc.create_chapter(courseId)
#     # fc.get_chapt_count(courseId)
#     # fc.get_chapt_chapterid(courseId)
#     fc.chapter_online()