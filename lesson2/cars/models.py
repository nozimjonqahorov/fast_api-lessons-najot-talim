from sqlalchemy import Column, String, Integer
from database import Base

class Car(Base):
    __tablename__ = 'cars' 
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String(100), nullable= False,index = True)
    desc = Column(String(500), nullable=False)
    
