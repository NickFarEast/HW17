import os.path

DATABASE_FILE_PATH = os.path.join(os.getcwd(), 'test.db')


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
