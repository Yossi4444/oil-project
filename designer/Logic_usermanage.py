import sys
import usermanageUi
import Logic_main
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import service

class usermanageWindowActions(usermanageUi.Ui_MainWindow,QMainWindow):
    def __init__(self) :
        super(usermanageUi.Ui_MainWindow,self).__init__()
        self.setupUi(self)

        # 返回主界面操作
        self.home_label.clicked.connect(self.open)
        self.home_label.clicked.connect(self.close)
        ## 进人曲线界面
        self.curve_button.clicked.connect(self.show_curverTab)
        # 进入日志信息
        self.log_button.clicked.connect(self.show_logTab)
        # 进入报警信息
        self.warning_button.clicked.connect(self.showWarningTab)
        self.tabWidget.tabBar().setVisible(False)

    def showWarningTab(self):
        self.tabWidget.setCurrentIndex(2)
    def show_logTab(self):
        self.tabWidget.setCurrentIndex(1)
    def show_curverTab(self):
        self.tabWidget.setCurrentIndex(0)
    # 进入用户管理界面
    def show_useranageTab(self):
        self.tabWidget.setCurrentIndex(4)


    def open(self):
            """点击相应按钮，跳转到第二个界面"""
            # 实例化第二个界面的后端类，并对第二个界面进行显示
            # 通过派生新类去访问类

            #返回主页面
            self.another_window =Logic_main.mainWindowActions()
            self.another_window.show()

if __name__ == '__main__':
    # 这里是界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用再重新定义，只需要调用show()函数即可
    app = QApplication(sys.argv)

    # 实例化
    demo_window =usermanageWindowActions()
    # 显示
    demo_window.show()

    sys.exit(app.exec_())