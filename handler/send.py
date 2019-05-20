import tornado.web
import json
from database.models import db_Session,person,Jmission,Pmission
from sqlalchemy import and_

class SendJmissionHandler (tornado.web.RequestHandler):
    def post(self):
        one= self.get_argument('one')
        db = db_Session()
        mission = db.query(Pmission).filter(Pmission.exc==one).all()
        if len(mission)==0:
            self.write(json.dumps({'status':-1, 'msg':'当前没有接收任务'}))
        else:
            data = []
            for i in mission:
                data.append({'p_id':i.p_id,'topic':i.topic,'order':i.order,'state':i.state})
            self.write(json.dumps({'status':0,'user_info':data}))


class SendPmissionHandler (tornado.web.RequestHandler):
    def post(self):
        one= self.get_argument('one')
        db = db_Session()
        mission = db.query(Pmission).filter(Pmission.order==one).all()
        if len(mission)==0:
            self.write(json.dumps({'status':-1, 'msg':'当前没有派发任务'}))
        else:
            data = []
            for i in mission:
                data.append({'p_id':i.p_id,'topic':i.topic,'exc':i.exc,'state':i.state}) 
            self.write(json.dumps({'status':0,'user_info':data}))
