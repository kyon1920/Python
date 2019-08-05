from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired    # 验证规则

class LoginForm(FlaskForm):
    name = StringField(label='用户名',validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码',validators=[DataRequired('密码不能为空')])
    submit = SubmitField(label='提交')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Navigator97'

@app.route('/')
def HTMLtest():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('HTMLtest.html')
@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html',name=username)

if __name__ == '__main__':
    app.run(debug=True)