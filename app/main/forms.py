from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, Length, Email, Regexp
from ..models import Role, User
from wtforms import ValidationError


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


# 用户级别的用户资料表单
class EditProfileForm(FlaskForm):
    name = StringField("Real name", validators=[Length(0, 64)])
    location = StringField("Location", validators=[Length(0, 64)])
    about_me = TextAreaField("About me")
    submit = SubmitField("Submit")


# 管理员级别的用户资料编辑器
class EditProfileAdminForm(FlaskForm):
    email = StringField("Email", validators=[Required(), Length(1, 64), Email()])
    username = StringField("Username",
                           validators=[Required(), Length(1, 64),
                                       Regexp(r"^[a-zA-Z][a-zA-Z0-9_.]*$", 0,
                                              "Username must have only letters,numbers,dots or underscores.")])
    confirmed = BooleanField("Confirmed")
    role = SelectField("Role", coerce=int)
    name = StringField("Real name", validators=[Length(1, 64)])
    location = StringField("Location", validators=[Length(1, 64)])
    about_me = TextAreaField("About me")
    submit = SubmitField("Submit")

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.username.data and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")


# 博客文章
class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField("Submit")