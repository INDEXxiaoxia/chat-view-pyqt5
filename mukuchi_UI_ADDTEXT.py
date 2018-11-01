from PyQt5.QtGui import QIcon,QFont,QPalette,QColor,QBrush,QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication,QRect,Qt
import sys
import time
class MukuchiChatDemo(QWidget):
    def __init__(self,parent=None):
        super(MukuchiChatDemo, self).__init__(parent)
        self.set_palette()
        # self.setWindowFlags(Qt.FramelessWindowHint)#取消边框
        self.initUI()

    def initUI(self):

        # 提示字体设置
        QToolTip.setFont(QFont('微软雅黑', 20))
        self.setToolTip('这是<b>聊天</b>窗口')
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        Lab_ne=QLabel('智能机器人大白正为您服务',self)
        #创建多行文本框
        self.textBR=QTextBrowser(self)
        self.textBR.setToolTip('这是<b>信息页面</b>')
        self.textBR.setHtml("""<body  background='bg000.jpg'>""")


        # self.textBR.moveCursor()
        self.textEdit=QTextEdit("来聊天吧",self)

        #创建两个按钮
        setbtn=QPushButton(self.setFont(font))
        self.btnPress1=QPushButton('发 送',self)
        self.btnPress1.setToolTip('点击这个按钮<b>发送</b>')
        self.btnPress1.setStyleSheet('background-color:rgba(0, 255,255,200)')
        # self.btnPress2=QPushButton('清 空',self)
        # self.btnPress2.setToolTip('点击这个按钮<b>清空</b>')
        # self.btnPress2.setStyleSheet('background-color:rgba(0, 255,255,200)')
        #图片显示   32823
        pix = QPixmap('这大概是个大白.png')
        lb1 = QLabel(self)
        lb1.setToolTip('你好<b>我是大白！</b>')
        lb1.setGeometry(465, 30, 280, 401)
        lb1.setPixmap(pix)
        pix0 = QPixmap('临时广告位.jpg')
        lb2 = QLabel(self)
        lb2.setToolTip('<b>广告位招租</b>')
        lb2.setGeometry(476, 440, 430, 122)
        lb2.setPixmap(pix0)
        #退出键
        b=QPushButton(self.setFont(font))
        btn_et=QPushButton('EXIT',self)
        btn_et.setToolTip('点击这个按钮<b>退出</b>')
        btn_et.setStyleSheet('background-color:rgba(70,130,180,220)')
        btn_et.clicked.connect(QCoreApplication.instance().quit)
        #设置位置
        self.textBR.setGeometry(10,30,450,400)#聊天显示框
        self.textEdit.setGeometry(10,440,450,90)#输入框
        # self.btnPress2.setGeometry(340,535,121,30)#清空
        self.btnPress1.setGeometry(340,535,121,30)#发送
        btn_et.setGeometry(200,535,121,30)#退出按钮
        Lab_ne.setGeometry(20,2,300,30)#上端字符
        #将按钮的点击信号与相关的槽函数进行绑定，点击即触发
        self.btnPress1.clicked.connect(self.btnPress1_clicked)
        # self.btnPress2.clicked.connect(self.btnPress2_clicked)#清空按钮
        #窗口设置
        self.setWindowIcon(QIcon('AA.png'))
        self.setWindowTitle('聊天界面')
        self.setFixedSize(750,570)
        self.center()
    def btnPress1_clicked(self):
        msg0=self.textEdit.toPlainText()#接收文本框中的信息
        msg1="[用户]"
        msgtime=time.ctime()
        msg1_ch="<font color='red' size='4'>"+msg1+"</font>"#处理名字
        msgtime_ch="<font color='blue' size='2'>"+msgtime+"</font>"#处理时间
        msg0_ch="<font color='MidnightBlue' size='4' style='background-color:Cyan;'>"+msg0+"</font>"#处理信息
        msg_final="<hr> "+msg1_ch+msgtime_ch+"<br>"+msg0_ch
        self.textBR.insertHtml(msg_final)#发送到显示框
        self.textEdit.clear()#清空输入框

        self.Alice_Glass(msg0)
#---------------------------------------

    def Alice_Glass(self,msgABC):
        msg0=RecvMsg(msgABC)#接收到的信息
        msg1="[智能机器人]"
        msgtime=time.ctime()
        msg1_ch="<font color='red' size='4'>"+msg1+"</font>"#处理机器人的名字
        msgtime_ch="<font color='blue' size='2'>"+msgtime+"</font>"#处理时间
        msg0_ch="<font color='MidnightBlue' size='4' >"+msg0+"</font>"#处理机器人的信息

        msg_final="<hr>"+msg1_ch+msgtime_ch+"<br>"+msg0_ch

        self.textBR.insertHtml(msg_final)#发送到显示框
        cursor=self.textBR.textCursor()
        pos=len(self.textBR.toPlainText())
        cursor.setPosition(pos-1)
        self.textBR.ensureCursorVisible()
        self.textBR.setTextCursor(cursor)
        self.textEdit.clear()#清空输入框
    def btnPress2_clicked(self):
        self.textBR.clear()

    def center(self):
        # ------居中显示方法-------------
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def set_palette(self):
        #------------设置背景----------------------
        self.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.WindowText, Qt.white)
        # palette.setColor(self.backgroundRole(),QColor(192,253,123,100))#设置背景颜色
        palette.setBrush(self.backgroundRole(),QBrush(QPixmap('bg4.jpg').scaled(400,600)))
        # self.label.width(), self.label.height()
        self.setPalette(palette)
    def keyPressEvent(self, e):
        if str(e.key()) =='16777220' or e.key() == Qt.Key_Enter: #Qt.Key_Enter:
            self.btnPress1_clicked()

def RecvMsg(msg):
    #-------回复信息------
    if "吃" in msg:
        return "没钱了，不吃了"
    if "睡" in msg:
        return "睡觉吧，晚安"
    if len(msg)>5:
        return "太长了，看不懂！(ﾟДﾟ*)ﾉ"
    else:
        return '你在说什么呢¿<hr><img src="bq1.jpg">'

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MukuchiChatDemo()
    win.show()
    sys.exit(app.exec_())

