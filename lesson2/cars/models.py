from sqlalchemy import Column, String, Integer
from database import Base

class Car(Base):
    __tablename__ = 'cars' 
    id = Column(Integer, primary_key=True)
    model = Column(String(100))
    desc = Column(String)
    
