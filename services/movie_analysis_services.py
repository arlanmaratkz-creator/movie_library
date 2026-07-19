from database import session
from models import Movie
from sqlalchemy import func

class MovieAnalysis:
    def avg_rate(self):
        average = session.query(func.avg(Movie.rating)).scalar()
        return average
    def best_movie(self):
        best_movie = session.query(Movie)\
            .order_by(Movie.rating.desc())\
                .first()
        return best_movie
    def worst_movie(self):
        worst_movie = session.query(Movie)\
            .order_by(Movie.rating)\
            .first()
        return worst_movie
    def watched_count(self):
        watched = session.query(Movie)\
            .filter_by(done=True)\
            .count()
        return watched
    def unwatched_count(self):
        not_watched = session.query(Movie)\
            .filter_by(done=False)\
            .count()
        return not_watched
    def movie_count(self):
        count = session.query(Movie).count()
        return count