import tornado.web
import json
from database.models import db_Session,person,Jmission,Pmission
from sqlalchemy import and_

class ShowMissionHandler (tornado.web.RequestHandler):
    def post(self):
        mid = self.get_argument('mid')
        db = db_Session()
        mission = db.query(Pmission).filter(Pmission.p_id == int(mid)).first()
        self.write(json.dumps({'status':0,'user_info':{'p_id':mission.p_id,'topic':mission.topic,'checktime':mission.checktime,'endtime':mission.endtime,'desc':mission.desc}}))
        db.close()


class AbandonMissionHandler (tornado.web.RequestHandler):
    def post(self):
        mid = self.get_argument('mid')
        db = db_Session()
        mission = db.query(Pmission).filter(Pmission.p_id == int(mid)).first()
        self.write(json.dumps({'status':0,'msg':'已放弃该任务'}))
        mission.state = '已放弃'
        db.commit()
        db.close()


class CompleteMissionHandler (tornado.web.RequestHandler):
    def post(self):
        mid = self.get_argument('mid')
        db = db_Session()
        mission = db.query(Pmission).filter(Pmission.p_id == int(mid)).first()
        self.write(json.dumps({'status':0,'msg':'已完成该任务'}))
        mission.state = '已完成'
        db.commit()
        db.close() 
