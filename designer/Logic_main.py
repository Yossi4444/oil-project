import sys
import main
import Logic_login
import Logic_Betting
import Logic_curver
import login
import Logic_usermanage
import usermanageUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets


# 业务类需要继承两个类，一个设计的主界面，另一个是QMainWindow
class mainWindowActions(main.Ui_MainWindow, QMainWindow):
    def __init__(self):
        """
         特别注意（最容易出错）：
         1.派生新类访问基类需要super(),同时它的参数是基类文件下的类及“ui_home_window.py中的
           Ui_MainWindow类”
        """

        super(main.Ui_MainWindow, self).__init__()

        self.setupUi(self)
        # 打开生产控制页面
        self.ProductionControlButton.clicked.connect(self.open_coverWin)
        self.ProductionControlButton.clicked.connect(self.close)
        # 打开系统设置
        self.BettingButton.clicked.connect(self.openBetting)
        self.BettingButton.clicked.connect(self.close)
        # 打开用户登录操作
        self.LogoutButton.clicked.connect(self.logout)
        # 打开用户管理页面
        self.UserManage.clicked.connect(self.usermanage)
        self.ExitButton.clicked.connect(self.close)

    def openBetting(self):
        self.Betting_window=Logic_Betting.BettingWindowActions()
        self.Betting_window.showFullScreen()

    def open_coverWin(self):
        self.another_window =Logic_curver.curverWindowActions()
        self.another_window.showFullScreen()
    
    def logout(self): # 用户退出登录框
        return  

    def usermanage(self):
        self.another_window = Logic_usermanage.usermanageWindowActions()
        self.another_window.showFullScreen()
        #
        # # 核心代码
        # # 定义一个按钮的槽函数

            # """点击相应按钮，跳转到第二个界面"""
            # 实例化第二个界面的后端类，并对第二个界面进行显示
            # 通过派生新类去访问类



if __name__ == '__main__':
    # 这里是界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用再重新定义，只需要调用show()函数即可
    app = QApplication(sys.argv)

    # 实例化
    demo_window =mainWindowActions()
    # 显示
    demo_window.show()

    sys.exit(app.exec_())
