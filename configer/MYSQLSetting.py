from StudentManage_WTF.Tools.Helper.DBHelper.MYSQLHelper import MYSQLHelper


def getMYSQLHelper():
    return MYSQLHelper("127.0.0.1", 3306, "root", "", "StudentManage_WTF")
