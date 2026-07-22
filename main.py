from database import Base, engine
from models import Movie
from menu import start_menu


Base.metadata.create_all(engine)


if __name__ == "__main__":
    start_menu()