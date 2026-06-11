from sqlalchemy import Column, String, Integer, DateTime, func
from database import Base

class Car(Base):
    __tablename__ = 'cars' 
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String(100), nullable= False,index = True)
    desc = Column(String(500), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())