#! -*- coding:utf-8 -*-

import tornado.web
import json
from database.models import db_Session,person,Jmission,Pmission
from sqlalchemy import and_

class New_MissionHandler (tornado.web.RequestHandler):
    def post(self):
        c_id=self.get_argument('c_id')
        section = self.get_argument('s_id')
        job = int(self.get_argument('job'))
        db=db_Session()
        user = db.query(person).filter(and_(person.c_id==c_id,person.s_id==section)).filter(person.job==(job+1)).all()
        if len(user) == 0:
            self.write(json.dumps({'status':-1, 'msg':'你的权限不够！'}))
        else:
            data = []
            for i in user:
                data.append({'username':i.username,'uid':i.uid})
            self.write(json.dumps({'status':0,'user_info':data}))


class UpdateHandler (tornado.web.RequestHandler):
    def post(self):
        topic = self.get_argument('topic')
        desc = self.get_argument('desc')
        exc = self.get_argument('exc')
        checktime = self.get_argument('Checktime')
        endtime = self.get_argument('Endtime')
        order = self.get_argument('order')
        db = db_Session()
        db.add(Pmission(topic=topic,desc=desc,exc=exc,checktime=checktime,endtime=endtime,state='未完成',order=order))
        db.commit()
        self.write({'status':0,'msg':'新建任务成功'})
        db.close


class UserDataHandler (tornado.web.RequestHandler):
    def post(self):
        uid = self.get_argument('uid')
        db = db_Session()
        user = db.query(person).filter(person.uid == uid).first()
        self.write(json.dumps({'status':0,'user_info':{'c_id':user.c_id,'s_id':user.s_id,'job_level':user.job,'permission':user.permission}}))
        db.close
