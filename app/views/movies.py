from flask_restx import Resource, Namespace
from app.database import db

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = db.session.query(Movie).all()
        return movies_schema.dumps(all_movies, ensure_ascii=False), 200


@movie_ns.route('/<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        try:
            movie = db.session.query(Movie).filter(Movie.id == mid).one()
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404