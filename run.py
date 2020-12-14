#!/usr/bin/env python
# -*- coding: utf-8 -*-
from createChapter import Chapter
from createRoomURL import RoomURL
from work import Work
from teach_research import Teach_research
from common import Common
import sys

# courseTitle = "直播测试课"
# classname = "一班"
# timefromname = "一时段"
# user = 12389898989

courseTitle = sys.argv[1]
classname = sys.argv[2]
timefromname = sys.argv[3]
worktype = sys.argv[4]

# 获取courseId
courseId = Common().get_courseId(courseTitle)

# 创建小节、上架小节、返回小节ID
chapter_id, chaptername = Chapter(courseId).chapter_online()

# 编辑上下课时间，生成教室，返回roomID、scheduleId，userphone
RoomId, scheduleId, user = RoomURL(courseId, classname, timefromname, chapter_id, courseTitle).click_roombtn()

# 输出教室地址

teacherRUL = "https://qa-live-test.igetcool.com/weblivev2/?roomId=" + str(RoomId) + "&scheduleId=" + str(scheduleId)

# 创建课后练习，发布练习。worktype:1,常规题；2，填空题；3，卡片题
work_state = Work(scheduleId, courseId, chapter_id).add_work(worktype)

# 发企业微信
Common().oneclck_wechat_message(teacherRUL, chaptername, courseTitle, classname, timefromname, user, work_state)

# 教研系统关联ppt

Teach_research(courseId, scheduleId).add_ppt()

# 输出至工作台

print("小节名称：", chaptername)
print("教室地址：", teacherRUL)
print("可用账号：", user)
