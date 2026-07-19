from database import session
from models import Movie
from sqlalchemy import func

class MovieServices:
    def add_movie(self,
                  title,
                  genre,
                  director,
                  year,
                  done,
                  rate):
        movie = session.query(Movie).filter_by(title = title, year = year , director = director).first()
        if movie:
            return False
        movie = Movie(title=title,
                     genre=genre,
                     director=director,
                     year=year,
                     done=done,
                     rate=rate
                     )
        session.add(movie)
        session.commit()
        return True
    def delete_movie(self,
                    title,
                    year,
                    director):
        movie = session.query(Movie).filter_by(title = title, year = year , director = director).first()
        if not movie:
            return False
        session.delete(movie)
        session.commit()
        return True
    def search_movie(self,
                    title,
                    year):
        movie = session.query(Movie).filter_by(title = title, year = year).first()
        if not movie:
            return False
        return movie
    def update_movie(self,
                     title,
                     year,
                     director,
                     new_title,
                     new_year,
                     new_director,
                     new_rate
                     ):
        movie = session.query(Movie).filter_by(title = title, year = year,director=director).first()
        if not movie:
            return False
        if new_title is not None:
            movie.title = new_title
        if new_director is not None:
            movie.director = new_director
        if new_year is not None:
            movie.year = new_year
        if new_rate is not None:
            movie.rating = new_rate
        session.commit()
        return True
    def search_movie_by_genre(self,
                              genre):
        movie = session.query(Movie).filter_by(genre = genre).all()
        if not movie:
            return False
        return movie
    
        
    
    
           
