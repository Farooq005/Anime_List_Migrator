from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StagingAnime(Base):
    __tablename__ = "staging_anime"
    
    staging_id = Column(Integer, primary_key=True)
    platform = Column(String(10))
    external_id = Column(String(20))
    title = Column(String(255))
    episodes = Column(Integer)
    score = Column(Numeric(3,1))
    status = Column(String(20))
    progress = Column(Integer)
    platform_specific = Column(JSON)
