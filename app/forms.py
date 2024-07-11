from flask_wtf import FlaskForm #导入FlaskForm基类，用于定义表单。
from wtforms import StringField, PasswordField, BooleanField, SubmitField #导入WTForms中的表单字段类。
from wtforms.validators import DataRequired #导入一个验证器，用于验证字段是否为空。

class LoginForm(FlaskForm): #定义一个继承自FlaskForm的表单类
    username = StringField('Username', validators=[DataRequired()]) #定义一个名为username的字符串字段，并添加DataRequired验证器，确保该字段不能为空。
    password = PasswordField('Password', validators=[DataRequired()]) #定义一个名为password的密码字段，并添加DataRequired验证器。
    remember_me = BooleanField('Remember Me') #定义一个名为remember_me的布尔字段，用于“记住我”选项。
    submit = SubmitField('Sign In') # 定义一个提交按钮