from models import *


db = db_Session()
try:
    db.add(company(c_id='10530',c_name='湘潭大学'))
    db.add(section(s_id='01',section_name='学工办',c_id='10530'))
    db.add(job(s_id='01',job_name='主任',j_id='01',level='1'))
    db.add(job(s_id='01',job_name='干事',j_id='02',level='2'))
    db.add(job(s_id='01',job_name='职员',j_id='03',level='3'))
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()
