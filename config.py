import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件服务器
    MAIL_SERVER = "smtp.qq.com"
    # 邮件发送端口号
    MAIL_PORT = 465
    # 是否使用SSL加密
    MAIL_USE_SSL = True
    # 邮件发送账号
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # 邮件登录密码
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # 邮件主题
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN")
    # 邮件发送人信息
    FLASKY_MAIL_SENDER = "Flasky Admin<%s>" % FLASKY_ADMIN
    # 每页显示的博客文章的数量
    FLASKY_POSTS_PER_PAGE = 20
    # 每页显示的关注着的数量
    FLASKY_FOLLOWERS_PER_PAGE = 50
    # 每页评论数量
    FLASKY_COMMENTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


# 开发数据库链接
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        r"postgresql://postgres:123456@localhost/blog-dev"


# 测试数据库链接
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        r"postgresql://postgres:python@123@localhost/blog-test"


# 生产数据库链接
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        r"postgresql://postgres:python@123@localhost/blog-product"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    # 默认开发数据库
    "default": DevelopmentConfig
}