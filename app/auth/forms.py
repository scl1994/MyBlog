from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    email = StringField("邮箱", validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField("用户名", validators=[DataRequired(), Length(1, 64),
                                               Regexp(r"^[a-zA-z][a-zA-z0-9._]*$", 0,
                                                      "Usernames must have only letters,numbers,dots or underscores.")])
    password = PasswordField("密码", validators=[DataRequired(),
                                                     EqualTo("password2", message="Password must match.")])

    password2 = PasswordField("确认密码", validators=[DataRequired()])
    submit = SubmitField("注册")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in user")


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[DataRequired()])
    password = PasswordField("New Password", validators=[DataRequired(),
                                                         EqualTo("password2", message="Password must match.")])
    password2 = PasswordField("Confirm New Password", validators=[DataRequired()])
    submit = SubmitField("Update Password")


class PasswordResetRequestForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField("Reset Password")


class PasswordResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("New Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm New Password",
                              validators=[DataRequired(), EqualTo("password", message="Password must match!")])
    submit = SubmitField("Reset Password")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError("Unknown email address!")


# 改变邮箱地址
class ChangeEmailForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already register!")