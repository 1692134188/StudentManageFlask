from flask import Blueprint
from flask import render_template
from StudentManage_WTF.Tools.Helper.DBHelper.MYSQLHelper import MYSQLHelper
# 每个蓝图都可以为自己独立出一套template模板文件夹,如果不写则共享项目目录中的templates
sv = Blueprint("sv", __name__, template_folder="templates")


@sv.route("/s_view")
def studentView():
    # 获取sql帮助类对象
    sqlhelper = MYSQLHelper("127.0.0.1", 3306, "root", "", "StudentManage_WTF")
    # 拼接sql语句
    sql = "select * from Student where 1=1"
    studentList = sqlhelper.fetch_all(sql, ())
    return render_template("s_view.html", studentList=studentList)

