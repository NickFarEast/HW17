from flask_restx import Resource, Namespace
from app.database import db
from app.models import Genre, GenresSchema
from flask import request

genres_ns = Namespace('genres')

genre_schema = GenresSchema()
genres_schema = GenresSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Функция для отображения всех жанров в базе"""
        all_genres = db.session.query(Genre).all()

        return genres_schema.dumps(all_genres), 200

    def post(self):
        """Функция для записи нового жанра в базу"""
        genre = genre_schema.load(request.json)
        new_genre = Genre(**genre)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        """Функция для получения жанра из базы по ID"""
        try:
            genre = db.session.query(Genre).filter(Genre.id == gid).one()
            return genres_schema.dump(genre), 200
        except Exception as e:
            return "", 404

    def put(self, gid):
        """Функция для внесения изменения в базу по ID"""
        db.session.query(Genre).filter(Genre.id == gid).update(request.json)
        db.session.commit()

        return "", 204

    def delete(self, gid):
        """Функция для удаления из базы по ID"""
        db.session.query(Genre).filter(Genre.id == gid).delete()
        db.session.commit()
        return "", 204