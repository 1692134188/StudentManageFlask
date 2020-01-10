from flask import Blueprint
from flask import render_template, request, session, redirect
from StudentManage_WTF.Tools.Helper.DBHelper.MYSQLHelper import MYSQLHelper
from StudentManage_WTF.UserLogin.ModelForm.LoginModel import LoginForm

# 每个蓝图都可以为自己独立出一套template模板文件夹,如果不写则共享项目目录中的templates
sl = Blueprint("sl", __name__, template_folder="templates")


@sl.route("/s_login", methods=("GET", "POSt"))
def userLogin():
    if request.method == "GET":
        loginForm = LoginForm()
        return render_template("s_login.html", loginForm=loginForm)
    else:
        lf = LoginForm(request.form)
        if lf.validate():
            username = request.form.get("username")
            password = request.form.get("password")
            # 获取sql帮助类对象
            sqlhelper = MYSQLHelper("127.0.0.1", 3306, "root", "", "StudentManage_WTF")
            # 拼接sql语句
            sql = "select id,username from user where username='%s' and password='%s'" % (username, password)
            res = sqlhelper.fetch_all(sql, ())
            print(res)
            if res:
                session["user"] = res
                return redirect("/s_view")
            else:
                session["user"] = None
                lf.username.errors.append("用户名或密码错误！")
                return render_template("s_login.html", loginForm=lf)
        else:
            return render_template("s_login.html", loginForm=lf)
