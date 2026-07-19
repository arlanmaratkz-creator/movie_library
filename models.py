from database import Base
from sqlalchemy import  Column , Integer , String , Boolean , ForeignKey
from sqlalchemy.orm import relationship 

class Movie(Base):
    __tablename__ = "Movies"
    id = Column(Integer , primary_key=True)
    title = Column(String,nulluable = False)
    genre = Column(String)
    director = Column(String)
    year = Column(Integer)
    done = Column(String)
    rating = Column(String)

    
