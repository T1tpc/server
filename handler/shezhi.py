#! -*- coding:utf-8 -*-

import tornado.web
import json
from database.models import db_Session,person

class PasswordHandler (tornado.web.RequestHandler):
    def post(self):
        uid = self.get_argument('uid')
        oldpassword = self.get_argument('oldpassword')
        newpassword = self.get_argument('newpassword')
        db = db_Session()
        user = db.query(person).filter(person.uid==uid).first()
        if user.password!=oldpassword:
            self.write(json.dumps({'status':-1,'msg':'密码输入错误，无法更改'}))
        else :
            self.write(json.dumps({'status':0,'msg':'更改成功！'}))
            user.password = newpassword
            db.commit()
            db.close()


class SecJobHandler (tornado.web.RequestHandler):
    def post(self):
        uid = self.get_argument('uid')
        newsec = self.get_argument('new_sec')
        newjob = self.get_argument('new_job')
        db = db_Session()
        user = db.query(person).filter(person.uid==uid).first()
        self.write(json.dumps({'status':0,'msg':'职位变更成功！'}))
        user.s_id = newsec
        user.job = newjob
        user.permission = user.c_id+newsec+newjob
        db.commit()
        db.close()
