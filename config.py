import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN")
    FLASKY_SENDER = "Flasky Admin<%s>" % FLASKY_ADMIN

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 465
