from flask_restx import Resource, Namespace
from app.database import db
from app.models import Movie, MoviesSchema
from flask import request

movie_ns = Namespace('movies')

movie_schema = MoviesSchema()
movies_schema = MoviesSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):

        movies_query = db.session.query(Movie)

        args = request.args

        director_id = args.get('director_id')
        if director_id is not None:
            movies_query = movies_query.filter(Movie.director_id == director_id)
            print(movies_query)

        genre_id = args.get('genre_id')
        if genre_id is not None:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)

        movies = movies_query.all()

        return movies_schema.dump(movies), 200

    def post(self):
        movie = movie_schema.load(request.json)
        new_movie = Movie(**movie)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        try:
            movie = db.session.query(Movie).filter(Movie.id == mid).one()
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404

    def put(self, mid):
        db.session.query(Movie).filter(Movie.id == mid).update(request.json)
        db.session.commit()

        return "", 204

    def delete(self, mid):
        db.session.query(Movie).filter(Movie.id == mid).delete()
        db.session.commit()
        return "", 204
