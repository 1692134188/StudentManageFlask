#1：安装WTForms！ps：别安装错了，不是WTForm
from wtforms.fields import simple,core
from wtforms import Form,validators,widgets

class LoginForm(Form):
    username =simple.StringField(
        label="用户名",
        validators=[
            validators.data_required(message="用户名不能为空")
        ],
        widget=widgets.TextInput(),
        render_kw={"class":"my_username"}
    )
    password =simple.StringField(
        label="密码",
        validators=[
            validators.data_required(message="密码不能为空！")
        ],
        widget=widgets.PasswordInput()
    )
    submit=simple.SubmitField(
        label="提交"

    )


