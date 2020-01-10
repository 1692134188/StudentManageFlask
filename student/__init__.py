# 程序初始化
from flask import Flask,session
from StudentManage_WTF.student_view import s_view
from StudentManage_WTF.student_oper import s_add_modify_del
from StudentManage_WTF.UserLogin import s_login

# 创建一个app对象
def create_app():
    app = Flask(__name__,template_folder="../templates")
    app.register_blueprint(s_login.sl)
    # # 把学生列表蓝图，注册过来
    app.register_blueprint(s_view.sv)
    app.register_blueprint(s_add_modify_del.sa)
    app.secret_key="Hello,Flask"
    return app

if __name__ == '__main__':
    app = create_app()
