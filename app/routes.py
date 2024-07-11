from flask import render_template #这些导入包括渲染模板、闪现消息、重定向和URL生成功能。
from app import app
from app.forms import LoginForm
from flask import flash, redirect,url_for

@app.route('/') #定义主页路由,这个函数定义了 / 和 /index 路由,渲染 index.html 模板，并传递 user 和 posts 数据。
@app.route('/index') 
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST']) #定义登录页路由,这个函数定义了 /login 路由，并允许GET和POST请求
def login():
    form = LoginForm() #创建一个 LoginForm 实例。
    if form.validate_on_submit(): #如果表单验证成功，闪现一条消息并重定向到主页。
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form) #如果验证失败，重新渲染 login.html 模板，并传递表单实例。
