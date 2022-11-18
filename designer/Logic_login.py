import sys
import login,service
import Logic_main
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets


# 注意这里定义的第一个界面的后端代码类需要继承两个类
class LoginWindowActions(login.Ui_LoginWindow, QMainWindow):
    def __init__(self):
        super(login.Ui_LoginWindow, self).__init__()
        # 创建界面
        self.setupUi(self)
        # 绑定槽函数`

        #登录键绑定
        self.loginbutton.clicked.connect(self.open_btn_clicked)
        self.loginbutton.clicked.connect(self.close)


    # 核心代码
    # 定义一个按钮的槽函数
    def open_btn_clicked(self):
        """点击相应按钮，跳转到第二个界面"""
        self.Name=self.usernameedit.text() # 全局变量，记录用户名
        self.Pwd=self.passwordedit.text() # 记录用户密码
        if self.Name != "" and self.Pwd != "": # 判断用户名和密码不为空
            # 根据用户名和密码查询数据
            result=service.query("select * from tb_user where userName = %s and userPwd = %s",self.Name,self.Pwd)
            if len(result)>0: # 如果查询结果大于0，说明存在该用户，可以登录
                self.another_window = Logic_main.mainWindowActions() # 创建主窗体对象
                self.another_window.showFullScreen()  # 显示主窗体
               
            else:
                self.usernameedit.setText("") # 清空用户名文本
                self.passwordedit.setText("") # 清空密码文本框
                QMessageBox.warning(None, '警告', '请输入正确的用户名和密码！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入用户名和密码！', QMessageBox.Ok)

        # 实例化第二个界面的后端类，并对第二个界面进行显示
        # 通过派生新类去访问类
        #self.another_window = Logic_main.mainWindowActions()
        #self.another_window.show()


# 主程序入口
if __name__ == '__main__':
    # 这里是界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用再重新定义，只需要调用show()函数即可
    app = QApplication(sys.argv)

    # 实例化
    demo_window = LoginWindowActions()

    # 显示
    demo_window.show()

    sys.exit(app.exec_())
