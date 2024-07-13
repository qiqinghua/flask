from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm): #定义一个继承自FlaskForm的表单类
    username = StringField('Username', validators=[DataRequired()]) #定义一个名为username的字符串字段，并添加DataRequired验证器，确保该字段不能为空。
    password = PasswordField('Password', validators=[DataRequired()]) #定义一个名为password的密码字段，并添加DataRequired验证器。
    remember_me = BooleanField('Remember Me') #定义一个名为remember_me的布尔字段，用于“记住我”选项。
    submit = SubmitField('Sign In') # 定义一个提交按钮

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')