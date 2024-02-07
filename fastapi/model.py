from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Translate(Base):
    __tablename__ = 'translates'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, index=True)
    category = Column(String, index=True)
    description = Column(String, index=True)
    is_income = Column(Boolean, index=True)
    date = Column(String, index=True)