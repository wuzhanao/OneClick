#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from manage import Class_Manage


# courseId = "419215261709049856"
# scheduleId = "536071970788081664"
# chapter_id = "536432072716378112"

class Work(object):

    '''
    教研-提交作业
    '''

    def __init__(self, scheduleId, courseId, chapter_id):
        self.courseId = courseId
        self.auth = {"Authorization": "x6mxjSg8NGx6npIKqeBOzu6QjOkFW4"}
        self.auth_banke = {"Authorization": "RPpDiT6ASqSejwmrJKIVPfDMKFBrnT"}
        self.chapter_id = chapter_id
        self.scheduleId = scheduleId
        self.CM = Class_Manage(self.scheduleId, self.courseId, self.chapter_id)

    def add_work(self,worktype):

        url = "http://qa-course-test.igetcool.com/admin/chapter/work/add"

        if worktype == '无':
            return "未创建课后练习"

        elif worktype == '常规题（全部）':
            data_1 = {
               "answerType": "1,2,3,4",
               "chapterPid": self.chapter_id,
               "coursePid": self.courseId,
               "generalComment": "常规题-文本+图片+音频+视频",
               "homeWorks": [{"type":"4","content":"<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #e67e23;\"><strong>训练重点：用思维导图复习学过的语文工具。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong>请你回忆在《泉灵的语文课》中学过的语文工具，找到你想推荐的工具，写出它的</strong><strong>使用方法、实际运用的例子和好处</strong><strong>。根据示例，画出完整的思维导图。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong>把你的答案拍照提交至少年得到</strong><strong>APP</strong><strong>。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\"><strong><img src=\"https://coolcdn.igetcool.com/p/2020/11/6e6798cf8244a6d703b06755880cdd67.png?_762x493.png\" alt=\"\" width=\"246\" height=\"159\"></strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\"><strong>小提示：</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">1. 工具①别忘了写哦。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">2.&nbsp; “例子”可以写一写你在哪里，具体怎么用的这个语文工具。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">3. 可以在少年得APP“书房”内，查看每一课的复习卡片，帮你回忆工具的用法。</span></p>","expand":""}],
               "questionType": 0,
               "title": "常规题-文本+图片+音频+视频",
               "trainingFocus": "常规题-文本+图片+音频+视频"
           }
            req_1 = requests.post(url=url,json=data_1,headers= self.auth)
            print("常规题（全部）", req_1.json())
            # 发布作业
            self.CM.work_push()
            return "常规题创建成功"

        elif worktype == '常规题（文本）':
            data_2 = {
                "answerType": "1",
                "chapterPid": self.chapter_id,
                "coursePid": self.courseId,
                "generalComment": "常规题-文本",
                "homeWorks": [{"type": "4",
                               "content": "<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #e67e23;\"><strong>训练重点：用思维导图复习学过的语文工具。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong>请你回忆在《泉灵的语文课》中学过的语文工具，找到你想推荐的工具，写出它的</strong><strong>使用方法、实际运用的例子和好处</strong><strong>。根据示例，画出完整的思维导图。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong>把你的答案拍照提交至少年得到</strong><strong>APP</strong><strong>。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\"><strong><img src=\"https://coolcdn.igetcool.com/p/2020/11/6e6798cf8244a6d703b06755880cdd67.png?_762x493.png\" alt=\"\" width=\"246\" height=\"159\"></strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\"><strong>小提示：</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">1. 工具①别忘了写哦。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">2.&nbsp; “例子”可以写一写你在哪里，具体怎么用的这个语文工具。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">3. 可以在少年得APP“书房”内，查看每一课的复习卡片，帮你回忆工具的用法。</span></p>",
                               "expand": ""}],
                "questionType": 0,
                "title": "常规题-文本",
                "trainingFocus": "常规题-文本"
            }
            requests.post(url=url, json=data_2, headers=self.auth)
            # 发布作业
            self.CM.work_push()
            return "常规题创建成功"
        elif worktype == '常规题（文本+图片）':
            data_3 = {
                "answerType": "1,2",
                "chapterPid": self.chapter_id,
                "coursePid": self.courseId,
                "generalComment": "常规题-文本+图片",
                "homeWorks": [{"type": "4",
                               "content": "<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #e67e23;\"><strong>训练重点：用思维导图复习学过的语文工具。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong>请你回忆在《泉灵的语文课》中学过的语文工具，找到你想推荐的工具，写出它的</strong><strong>使用方法、实际运用的例子和好处</strong><strong>。根据示例，画出完整的思维导图。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong>把你的答案拍照提交至少年得到</strong><strong>APP</strong><strong>。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\"><strong><img src=\"https://coolcdn.igetcool.com/p/2020/11/6e6798cf8244a6d703b06755880cdd67.png?_762x493.png\" alt=\"\" width=\"246\" height=\"159\"></strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\"><strong>小提示：</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">1. 工具①别忘了写哦。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">2.&nbsp; “例子”可以写一写你在哪里，具体怎么用的这个语文工具。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">3. 可以在少年得APP“书房”内，查看每一课的复习卡片，帮你回忆工具的用法。</span></p>",
                               "expand": ""}],
                "questionType": 0,
                "title": "常规题-文本+图片",
                "trainingFocus": "常规题-文本+图片"
            }
            requests.post(url=url, json=data_3, headers=self.auth)
            # 发布作业
            self.CM.work_push()
            return "常规题创建成功"
        elif worktype == '常规题（音频+视频）':
            data_4 = {
                "answerType": "3,4",
                "chapterPid": self.chapter_id,
                "coursePid": self.courseId,
                "generalComment": "常规题-音频+视频",
                "homeWorks": [{"type": "4",
                               "content": "<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #e67e23;\"><strong>训练重点：用思维导图复习学过的语文工具。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong>请你回忆在《泉灵的语文课》中学过的语文工具，找到你想推荐的工具，写出它的</strong><strong>使用方法、实际运用的例子和好处</strong><strong>。根据示例，画出完整的思维导图。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong>把你的答案拍照提交至少年得到</strong><strong>APP</strong><strong>。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\"><strong><img src=\"https://coolcdn.igetcool.com/p/2020/11/6e6798cf8244a6d703b06755880cdd67.png?_762x493.png\" alt=\"\" width=\"246\" height=\"159\"></strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\"><strong>小提示：</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">1. 工具①别忘了写哦。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">2.&nbsp; “例子”可以写一写你在哪里，具体怎么用的这个语文工具。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"color: #e67e23; font-size: 14pt;\">3. 可以在少年得APP“书房”内，查看每一课的复习卡片，帮你回忆工具的用法。</span></p>",
                               "expand": ""}],
                "questionType": 0,
                "title": "常规题-音频+视频",
                "trainingFocus": "常规题-音频+视频"
            }
            requests.post(url=url, json=data_4, headers=self.auth)
            # 发布作业
            self.CM.work_push()
            return "常规题创建成功"

        elif worktype == '填空题':
            data_5 = {
                "answerType": "null",
                "chapterPid": self.chapter_id,
                "coursePid": self.courseId,
                "generalComment": "填空题-文字+图片",
                "homeWorks":[{"type": "4",
                              "content": "<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #ff4400;\"><strong>训练重点：在生活中仔细观察动作，找准动词进行描述，让表达更准确生动。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #000000;\"><strong><span style=\"font-size: 14pt;\">请参考下面的图片，在横线上填上合适的动词，把西红柿炒鸡蛋的过程补充完整。 </span></strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #000000;\"><span style=\"font-size: 14pt;\"><img src=\"https://coolcdn.igetcool.com/p/2020/10/8a8190ecda3ae95241e5b1d4e9e0172b.jpg?_1236x572.jpg\" alt=\"\" width=\"248\" height=\"115\"></span></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #000000;\"><span style=\"font-size: 14pt;\">&nbsp; &nbsp; &nbsp; &nbsp;先把西红柿切好，再把鸡蛋 <span style=\"text-decoration: underline;\">&nbsp;1 </span>倒进一个碗中，用筷子快速 <span style=\"text-decoration: underline;\">&nbsp;2 </span>&nbsp;鸡蛋。然后往锅里&nbsp;<span style=\"text-decoration: underline;\">&nbsp; 3&nbsp;&nbsp;</span> 油，油热后把鸡蛋液倒在锅里，用铲子翻炒。鸡蛋炒熟后，把鸡蛋盛出来，再把西红柿倒在锅里&nbsp;<span style=\"text-decoration: underline;\">&nbsp; 4&nbsp; </span>，<span style=\"text-decoration: underline;\">&nbsp; 5&nbsp; </span>盐，把炒好的鸡蛋倒在锅里和西红柿一起翻炒。最后把炒好的菜 <span style=\"text-decoration: underline;\">&nbsp;6&nbsp;</span> 出来装盘。</span></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #000000;\"><span style=\"font-size: 14pt;\">请把答案用<span style=\"color: #ff6600;\">文字</span>记录下来，上传到少年得到APP。</span></span></p>\n<p style=\"margin: 10px 0px;\">&nbsp;</p>",
                              "expand": ""}],
                "questionType": 1,
                "title": "填空题-文字+图片",
                "trainingFocus": "填空题-文字+图片"
            }
            requests.post(url=url, json=data_5, headers=self.auth)

            # 班课系统创建填空题
            banke_url = "http://qa-course-test.igetcool.com/admin/chapter/work/edit"
            data_6 = {
                "chapterPid": self.chapter_id,
                "coursePid": self.courseId,
                "generalComment": "填空题-文字+图片",
                "homeWorks": [{"type": "4",
                               "content": "<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #ff4400;\"><strong>训练重点：在生活中仔细观察动作，找准动词进行描述，让表达更准确生动。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #000000;\"><strong><span style=\"font-size: 14pt;\">请参考下面的图片，在横线上填上合适的动词，把西红柿炒鸡蛋的过程补充完整。 </span></strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #000000;\"><span style=\"font-size: 14pt;\"><img src=\"https://coolcdn.igetcool.com/p/2020/10/8a8190ecda3ae95241e5b1d4e9e0172b.jpg?_1236x572.jpg\" alt=\"\" width=\"248\" height=\"115\"></span></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #000000;\"><span style=\"font-size: 14pt;\">&nbsp; &nbsp; &nbsp; &nbsp;先把西红柿切好，再把鸡蛋 <span style=\"text-decoration: underline;\">&nbsp;1 </span>倒进一个碗中，用筷子快速 <span style=\"text-decoration: underline;\">&nbsp;2 </span>&nbsp;鸡蛋。然后往锅里&nbsp;<span style=\"text-decoration: underline;\">&nbsp; 3&nbsp;&nbsp;</span> 油，油热后把鸡蛋液倒在锅里，用铲子翻炒。鸡蛋炒熟后，把鸡蛋盛出来，再把西红柿倒在锅里&nbsp;<span style=\"text-decoration: underline;\">&nbsp; 4&nbsp; </span>，<span style=\"text-decoration: underline;\">&nbsp; 5&nbsp; </span>盐，把炒好的鸡蛋倒在锅里和西红柿一起翻炒。最后把炒好的菜 <span style=\"text-decoration: underline;\">&nbsp;6&nbsp;</span> 出来装盘。</span></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt; color: #000000;\"><span style=\"font-size: 14pt;\">请把答案用<span style=\"color: #ff6600;\">文字</span>记录下来，上传到少年得到APP。</span></span></p>\n<p style=\"margin: 10px 0px;\">&nbsp;</p>",
                               "expand": "{\"content\":[{\"key\":\"072643041230973141606739136305\",\"type\":\"blank-text\",\"content\":\"<p>先把西红柿切好，再把鸡蛋 #blank1#  倒进一个碗中，用筷子快##blank2##blank3##blank4##blank5##blank6##blank7#blank2# 鸡蛋。然后往锅里#blank3# 油，油热后把鸡蛋液倒在锅里，用铲子翻炒。鸡蛋炒熟后，把鸡蛋盛出来，再把西红柿倒在锅里#blank4#，#blank5# 盐，把炒好的鸡蛋倒在锅里和西红柿一起翻炒。最后把炒好的菜#blank6#出来装盘。</p>↵\",\"children\":[\"1\",\"2\",\"3\",\"4\",\"5\",\"6\",\"7\",\"3\",\"4\",\"5\",\"6\"],\"markdown\":\"先把西红柿切好，再把鸡蛋 #blank1#  倒进一个碗中，用筷子快##blank2##blank3##blank4##blank5##blank6##blank7#blank2# 鸡蛋。然后往锅里#blank3# 油，油热后把鸡蛋液倒在锅里，用铲子翻炒。鸡蛋炒熟后，把鸡蛋盛出来，再把西红柿倒在锅里#blank4#，#blank5# 盐，把炒好的鸡蛋倒在锅里和西红柿一起翻炒。最后把炒好的菜#blank6#出来装盘。\"},{\"key\":\"0109011857187465421606739241161\",\"type\":\"blank-image\",\"content\":\"https://coolcdn.igetcool.com/p/2020/11/19c35769ec028e2ca9d29cbcbb06329a.jpg?_1012x304.jpg\",\"children\":[\"8\"],\"width\":375,\"height\":112}],\"blanksJson\":{\"1\":{\"number\":10,\"placeholder\":\"\",\"type\":\"blank-text\",\"key\":\"072643041230973141606739136305\"},\"2\":{\"number\":10,\"placeholder\":\"\",\"type\":\"blank-text\",\"key\":\"072643041230973141606739136305\"},\"3\":{\"number\":10,\"placeholder\":\"\",\"type\":\"blank-text\",\"key\":\"072643041230973141606739136305\"},\"4\":{\"number\":10,\"placeholder\":\"\",\"type\":\"blank-text\",\"key\":\"072643041230973141606739136305\"},\"5\":{\"number\":10,\"placeholder\":\"\",\"type\":\"blank-text\",\"key\":\"072643041230973141606739136305\"},\"6\":{\"number\":10,\"placeholder\":\"\",\"type\":\"blank-text\",\"key\":\"072643041230973141606739136305\"},\"7\":{\"number\":10,\"placeholder\":\"\",\"type\":\"blank-text\",\"key\":\"072643041230973141606739136305\"},\"8\":{\"number\":20,\"placeholder\":\"\",\"type\":\"blank-image\",\"key\":\"0109011857187465421606739241161\",\"width\":140,\"height\":37,\"x\":205.34759358288773,\"y\":14.037433155080215}}}"
                                }],
                "questionType": 1,
                "workPid": self.CM.get_workid()
            }
            rr = requests.post(url=banke_url, json=data_6, headers=self.auth_banke)
            print("班课提交填空题：", rr.json())
            # 发布作业
            self.CM.work_push()
            return "填空题题创建成功"

        elif worktype == '卡片题':
            card_url = "http://qa-course-test.igetcool.com/admin/operations/card/material/association"
            data_7 = {
                "cards": "65,63",
                "chapterId": self.chapter_id,
                "courseId": self.courseId
            }
            rrr = requests.post(url=card_url, json=data_7, headers=self.auth)
            print("hahah",rrr.json())
            data_8 = {
                "answerType": "null",
                "chapterPid": self.chapter_id,
                "coursePid": self.courseId,
                "generalComment": "卡片题",
                "homeWorks":[{"type":"4","content":"<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\"><strong style=\"color: #e67e23;\">训练重点：完成人物形象卡片，积累更多的人物</strong><strong style=\"color: #e67e23;\">素材。</strong></span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\">请选择<strong>李白或孙悟空</strong>，查找<strong>资料</strong>，完成<strong>人物形象卡片</strong>。</span></p>\n<p style=\"margin: 10px 0px;\"><span style=\"font-size: 14pt;\">要求：请把人物形象卡片填写完整。</span></p>\n<p style=\"margin: 10px 0px;\"><img src=\"https://coolcdn.igetcool.com/p/2020/10/31c7f33494ffb8036bbc117134c4ce2a.png?_944x720.png\" alt=\"\" width=\"263\" height=\"201\"></p>","expand":""}],
                "questionType": 2,
                "title": "卡片题",
                "trainingFocus": "卡片题"
            }
            requests.post(url=url, json=data_8, headers=self.auth)
            # 发布作业
            self.CM.work_push()
            return "卡片题创建成功"

        else:
            return "创建失败"


# if __name__ == '__main__':
#     r = Work(courseId, chapter_id)
    # r.add_work('1')