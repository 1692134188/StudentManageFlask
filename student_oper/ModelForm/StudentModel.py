from wtforms.fields import simple, core
from wtforms import widgets, validators, Form


class StudentForm(Form):
    ID = simple.StringField(
        widget=widgets.HiddenInput
    ),
    StudentName = simple.StringField(
        label="姓名",
        validators=[
            validators.data_required(message="学生姓名不能为空！"),
            validators.Length(min=2, max=20, message="学生姓名长度必须大于2位，小于20位")
        ]
    )
    Age = core.StringField(
        label="年龄",
        validators=[
            validators.data_required(message="学生年龄不能为空！"),
            validators.Regexp(regex="^\d+$", message="学生年龄必须为数字")
        ]
    )
    Gender = core.RadioField(
        label="性别",
        coerce=int,  # 保存到数据中的值为int类型
        choices=(
            (0, '女'), (1, '男')
        ),
        default=1
    )
    submit = simple.SubmitField(
        label="提交"
    )
