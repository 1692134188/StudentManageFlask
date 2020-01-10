from flask import Blueprint
from flask import render_template, request, redirect
from StudentManage_WTF.student_oper.ModelForm.StudentModel import StudentForm
from StudentManage_WTF.configer.MYSQLSetting import getMYSQLHelper

# 每个蓝图都可以为自己独立出一套template模板文件夹,如果不写则共享项目目录中的templates
sa = Blueprint("sa", __name__, template_folder="templates")
sqlhelper = getMYSQLHelper()


@sa.route("/s_add", methods=('GET', 'POST'))
def studentAdd():
    if request.method == "GET":
        stu = StudentForm()
        return render_template("s_add_modify.html", curTitle="新增", curAction="/s_add", stu=stu)
    else:
        stu = StudentForm(request.form)
        if stu.validate():
            # 获取sql帮助类对象
            # 拼接sql语句
            sql = "insert into student (studentname,age,gender) values('%s',%s,%s);" % (
                stu.StudentName.data, stu.Age.data, stu.Gender.data)
            res = sqlhelper.insert_one(sql, ())
            return redirect("/s_view")
        else:
            return render_template("s_add_modify.html", curTitle="新增", curAction="/s_add", stu=stu)


@sa.route("/s_update/<int:id>", methods=('GET', 'POST'))
def studentUpdate(id):
    if request.method == "GET":
        sql = "select * from student where ID='%s'" % (id)
        curStu = sqlhelper.fetch_all(sql, ())
        if curStu:
            curStu = StudentForm(**curStu[0])  # 神来之笔
        return render_template("s_add_modify.html", curTitle="编辑", curAction="/s_update/" + str(id), stu=curStu)
    else:
        stu = StudentForm(request.form)
        if stu.validate():
            sql = "update student set studentname='%s',age='%s',gender='%s' where ID='%s'" \
                  % (stu.StudentName.data, stu.Age.data, stu.Gender.data, id)
            res = sqlhelper.update(sql, ())
            return redirect("/s_view")
        else:
            return render_template("s_add_modify.html", curTitle="编辑", curAction="/s_update/" + str(id), stu=stu)


@sa.route("/s_del", methods=('GET', 'POST'))
def studentDel():
    id = request.args.get('id')
    sql = "delete from student where ID='%s'" % (id)
    curStu = sqlhelper.update(sql, ())
    return redirect("/s_view")
