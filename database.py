from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base , sessionmaker 

Base = declarative_base()

engine = create_engine('sqlite:///movie.db')

SessionLocal = sessionmaker(bind = engine)

session = SessionLocal()