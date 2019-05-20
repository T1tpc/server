#! -*- coding:utf-8 -*-

import tornado.web
import json
from database.models import db_Session,person

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        uid=self.get_argument('uid')
        password=self.get_argument('password')
        db=db_Session()
        user = db.query(person).filter(person.uid == uid).first()
        if user is None:
            self.write(json.dumps({'status':-1, 'msg':'用户不存在'}))
        elif user.password != password:
            self.write(json.dumps({'status':-1, 'msg':'密码错误'}))
        else:
            self.write(json.dumps({'status':0, 'msg':'登录成功', 'user_info':{'uid':user.uid,'c_id':user.c_id,'s_id':user.s_id,'job':user.job,'tel_num':user.tel_num,'password':user.password,'permission':user.permission,'username':user.username}}))
        db.close()

class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        company_account = self.get_argument('company_account')
        s_id = self.get_argument('section_id')
        job = self.get_argument('job')
        tel_num = self.get_argument('tel_num')
        username = self.get_argument('username')
        uid = self.get_argument('uid')
        password = self.get_argument('password')
        db = db_Session()
        try:
            check = db.query(person).filter(person.uid == uid).first()
            if check is not None:
                self.write({'status': -1,'msg':'工号重复，注册失败'})
                return
            db.add(person(uid=uid, username=username,password=password,job=job,s_id=s_id,c_id=company_account,tel_num=tel_num,permission=company_account+s_id+job))
            db.commit()
            self.write({'status': 0,'msg':'注册成功'})
        except Exception as e:
            print(e)
            db.rollback()
            self.write({'status': -1,'msg':'系统错误'})
        finally:
            db.close()
