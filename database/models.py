from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import sys
import os

sys.path.append('../')
from config import config

os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'
engine = create_engine('oracle://{}:{}@{}/{}'.format(config.DATABASE_USER, config.DATABASE_PASS,
                                                     config.DATABASE_HOST, config.DATABASE_NAME),
                       pool_size=300, max_overflow=300)
Base = declarative_base()
db_Session = sessionmaker(bind=engine)
# ################
# MODEL CLASS
# ###############
class person(Base):
    __tablename__ = 'person'
    uid = Column('uid', String(128), primary_key=True)
    username = Column('username', String(32))
    permission  = Column('permission',String(32))
    tel_num = Column('tel_num',String(16))
    password = Column('password',String(16))
    c_id = Column('c_id',String(32))
    s_id = Column('s_id',String(32))
    job = Column('job',BigInteger)

class company(Base):
    __tablename__ ='company'
    c_id = Column('c_id',String(32),primary_key=True)
    c_name = Column('c_name',String(64))
    
class Pmission(Base):
    __tablename__ = 'Pmission'
    p_id = Column('P_id', BigInteger, Sequence('seq_pmission'), primary_key=True)
    topic = Column('topic',String(128))
    desc = Column('desc',String(128))
    exc = Column('exc',String(32))
    state = Column('state',String(32))
    checktime = Column('checktime',String(32))
    endtime = Column('endtime',String(32))
    order = Column('order',String(32))

class Jmission(Base):
    __tablename__ = 'Jmission'
    g_id = Column('g_id',BigInteger,primary_key=True)
    topic = Column('topic',String(128))
    desc = Column('desc',String(128))
    state = Column('state',String(32))
    checktime = Column('checktime',String(32))
    endtime = Column('endtime',String(32))
    
class section(Base):
    __tablename__='section'
    s_id = Column('s_id',String(32),primary_key=True)
    section_name = Column('section_name',String(64))
    c_id = Column('c_id',String(32))
    
class job(Base):
    __tablename__='job'
    j_id=Column('j_id',String(32),primary_key=True)
    job_name=Column('job_name',String(64))
    level = Column('level',String(32))
    s_id = Column('s_id',String(32))

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
