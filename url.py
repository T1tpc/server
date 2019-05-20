from handler.register import LoginHandler, RegisterHandler
from handler.mission import New_MissionHandler,UpdateHandler,UserDataHandler
from handler.shezhi import PasswordHandler,SecJobHandler
from handler.send import SendJmissionHandler,SendPmissionHandler
from handler.manage import ShowMissionHandler,AbandonMissionHandler,CompleteMissionHandler

url = [
    (r'/login',LoginHandler),
    (r'/register',RegisterHandler),
    (r'/Mission',New_MissionHandler),
    (r'/Update',UpdateHandler),
    (r'/UserData',UserDataHandler),
    (r'/password',PasswordHandler),
    (r'/secjob',SecJobHandler),
    (r'/getjmission',SendJmissionHandler),
    (r'/getpmission',SendPmissionHandler),
    (r'/showmission',ShowMissionHandler),
    (r'/abandon',AbandonMissionHandler),
    (r'/complete',CompleteMissionHandler),
]
