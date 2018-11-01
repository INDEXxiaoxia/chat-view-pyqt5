import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit
,QPushButton,QToolTip,QDesktopWidget,QMessageBox,QAction,qApp)
from PyQt5.QtGui import QIcon,QFont,QPalette,QColor,QBrush,QPixmap
from PyQt5.QtCore import QCoreApplication,QRect,Qt

from mkuchi_chan.mukuchi_pjdr import pjdr_0


class View_login(QWidget):
    def __init__(self):
        super().__init__()
        self.set_palette()
        self.setWindowFlags(Qt.FramelessWindowHint)#取消边框


        self.initUI()
    def initUI(self):
        # 提示字体设置
        QToolTip.setFont(QFont('微软雅黑', 20))
        self.setToolTip('这是<b>注册</b>窗口')
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)

        #提示文本
        x=QLabel(self.setFont(font))#瞎写的
        Lab_ne=QLabel('昵  称:',self)
        Lab_id=QLabel('账  号:',self)
        Lab_pd=QLabel('密  码:',self)
        Lab_pdd=QLabel('再次输入:',self)
        #输入框
        self.Edit_ne=QLineEdit(self)
        self.Edit_id=QLineEdit(self)
        self.Edit_pd=QLineEdit(self)
        self.Edit_pdd = QLineEdit(self)
        self.Edit_pd.setEchoMode(QLineEdit.Password)
        self.Edit_pdd.setEchoMode(QLineEdit.Password)
        #按钮
        btn_ne=QPushButton('注册',self)
        btn_ne.setToolTip('点击这个按钮<b>注册</b>')
        btn_ne.setStyleSheet('background-color:rgba(0,255,255,50)')
        btn_ne.clicked.connect(self.get_texts)
        btn_ne.setFont(font)
        #退出键
        b=QPushButton(self.setFont(font))
        btn_et=QPushButton('EXIT',self)
        btn_et.setToolTip('点击这个按钮<b>退出</b>')
        btn_et.setStyleSheet('background-color:rgba(0, 255,255,50)')
        btn_et.clicked.connect(QCoreApplication.instance().quit)

        #设置绝对定位
        btn_ne.setGeometry(200,240,90,40)
        btn_et.setGeometry(430,0,50,28)
        Lab_ne.move(105,80)
        Lab_id.move(105,120)
        Lab_pd.move(105,160)
        Lab_pdd.move(105,200)
        self.Edit_ne.setGeometry(200,75,200,28)
        self.Edit_id.setGeometry(200, 115, 200, 28)
        self.Edit_pd.setGeometry(200, 155, 200, 28)
        self.Edit_pdd.setGeometry(200, 195, 200, 28)
        #窗口设置
        self.resize(480,320)
        self.center()
        self.setWindowTitle('注册测试')
        self.setWindowIcon(QIcon('AA.png'))
        self.show()##showshow
    def get_texts(self,event):
        user_ne=self.Edit_ne.text()
        user_id=self.Edit_id.text()
        user_pd=self.Edit_pd.text()
        user_pdd=self.Edit_pdd.text()
        if user_ne=='' or user_id=='' or user_pd=='' or user_pdd=='':
            QMessageBox.warning(self, 'o(ﾟДﾟ)っ！', '\n输入项有空(ﾟДﾟ*)ﾉ\n', QMessageBox.Yes)

        elif user_pd!=user_pdd:

            QMessageBox.warning(self, 'o(ﾟДﾟ)っ！', '\n两次输入密码不一致哦(ﾟДﾟ*)ﾉ\n', QMessageBox.Yes)

        else:
            if pjdr_0(user_ne,user_id,user_pd)=='IDOK':

                QMessageBox.information(self, '(ﾉ´▽｀)ﾉ♪', '\n注册成功(＾∀＾)ﾉｼ\n', QMessageBox.Yes)

                #在这写跳转！！



            else:
                QMessageBox.information(self, '(ﾉ´▽｀)ﾉ♪', '\n账号已存在，请重新输入(˘•ω•˘)\n', QMessageBox.Yes)

    def set_palette(self):
        self.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.WindowText, Qt.white)


        # palette.setColor(self.backgroundRole(),QColor(192,253,123,100))#设置背景颜色
        palette.setBrush(self.backgroundRole(),QBrush(QPixmap('bg4.jpg').scaled(480,320)))
        # self.label.width(), self.label.height()
        self.setPalette(palette)
    #------居中显示方法-------------
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #-------退出确认方法--------
    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认窗口',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = View_login()
    sys.exit(app.exec_())








