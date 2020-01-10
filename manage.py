from StudentManage_WTF.student import create_app,session
from flask import Flask,request

app = create_app()
@app.before_request
def islogin():
    if request.path == "/s_login":
        return None
    if not session.get("user"):
        return "您尚未登录，请先登录！！"
@app.template_filter()
def getGender(arg):
    return '男' if str(arg) == "1" else '女'

app.run(debug=True)
