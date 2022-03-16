from flask_restx import Resource, Namespace
from app.database import db
from app.models import Director, DirectorsSchema
from flask import request

directors_ns = Namespace('directors')

director_schema = DirectorsSchema()
directors_schema = DirectorsSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """Функция для отображения всех режиссеров в базе"""
        all_directors = db.session.query(Director).all()

        return directors_schema.dumps(all_directors), 200

    def post(self):
        """Функция для записи нового режиссера в базу"""
        director = director_schema.load(request.json)
        new_director = Director(**director)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        """Функция для получения режиссера из базы по ID"""
        try:
            director = db.session.query(Director).filter(Director.id == did).one()
            return directors_schema.dump(director), 200
        except Exception as e:
            return "", 404

    def put(self, did):
        """Функция для внесения изменения в базу по ID"""
        db.session.query(Director).filter(Director.id == did).update(request.json)
        db.session.commit()

        return "", 204

    def delete(self, did):
        """Функция для удаления из базы по ID"""
        db.session.query(Director).filter(Director.id == did).delete()
        db.session.commit()
        return "", 204