# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APM.ui'
#
# Created: Sat Sep 10 01:26:53 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class APMUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 781, 571))
        self.tabWidget.setMinimumSize(QtCore.QSize(127, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self._username_ = QtGui.QLineEdit(self.tab1)
        self._username_.setGeometry(QtCore.QRect(160, 120, 151, 31))
        self._username_.setObjectName(_fromUtf8("_username_"))
        self._password_ = QtGui.QLineEdit(self.tab1)
        self._password_.setGeometry(QtCore.QRect(160, 180, 151, 31))
        self._password_.setObjectName(_fromUtf8("_password_"))
        self.label = QtGui.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(90, 130, 61, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(90, 180, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._login_ = QtGui.QPushButton(self.tab1)
        self._login_.setGeometry(QtCore.QRect(90, 260, 91, 31))
        self._login_.setObjectName(_fromUtf8("_login_"))
        self._logout_ = QtGui.QPushButton(self.tab1)
        self._logout_.setGeometry(QtCore.QRect(220, 260, 91, 31))
        self._logout_.setObjectName(_fromUtf8("_logout_"))
        self._accountlist_ = QtGui.QListWidget(self.tab1)
        self._accountlist_.setGeometry(QtCore.QRect(430, 120, 181, 101))
        self._accountlist_.setObjectName(_fromUtf8("_accountlist_"))
        self.label_15 = QtGui.QLabel(self.tab1)
        self.label_15.setGeometry(QtCore.QRect(420, 80, 81, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self._rememberpw_ = QtGui.QRadioButton(self.tab1)
        self._rememberpw_.setGeometry(QtCore.QRect(100, 230, 89, 16))
        self._rememberpw_.setObjectName(_fromUtf8("_rememberpw_"))
        self._autologin_ = QtGui.QRadioButton(self.tab1)
        self._autologin_.setGeometry(QtCore.QRect(220, 230, 89, 16))
        self._autologin_.setObjectName(_fromUtf8("_autologin_"))
        self._deleteaccount_ = QtGui.QPushButton(self.tab1)
        self._deleteaccount_.setGeometry(QtCore.QRect(330, 180, 75, 23))
        self._deleteaccount_.setObjectName(_fromUtf8("_deleteaccount_"))
        self._addaccount_ = QtGui.QPushButton(self.tab1)
        self._addaccount_.setGeometry(QtCore.QRect(330, 130, 75, 23))
        self._addaccount_.setObjectName(_fromUtf8("_addaccount_"))
        self._multipleaccount_ = QtGui.QPushButton(self.tab1)
        self._multipleaccount_.setGeometry(QtCore.QRect(470, 250, 101, 31))
        self._multipleaccount_.setObjectName(_fromUtf8("_multipleaccount_"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.groupBox = QtGui.QGroupBox(self.tab2)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 731, 401))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self._urlBox_ = QtGui.QComboBox(self.groupBox)
        self._urlBox_.setGeometry(QtCore.QRect(80, 50, 281, 21))
        self._urlBox_.setObjectName(_fromUtf8("_urlBox_"))
        self._url_ = QtGui.QLineEdit(self.groupBox)
        self._url_.setGeometry(QtCore.QRect(80, 50, 231, 21))
        self._url_.setObjectName(_fromUtf8("_url_"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 351, 201))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self._postname_ = QtGui.QLineEdit(self.groupBox_2)
        self._postname_.setGeometry(QtCore.QRect(80, 50, 231, 20))
        self._postname_.setObjectName(_fromUtf8("_postname_"))
        self._postcontent_ = QtGui.QPlainTextEdit(self.groupBox_2)
        self._postcontent_.setGeometry(QtCore.QRect(80, 100, 231, 61))
        self._postcontent_.setObjectName(_fromUtf8("_postcontent_"))
        self._ifautopost_ = QtGui.QRadioButton(self.groupBox_2)
        self._ifautopost_.setGeometry(QtCore.QRect(130, 20, 89, 16))
        self._ifautopost_.setObjectName(_fromUtf8("_ifautopost_"))
        self._deleteurl_ = QtGui.QPushButton(self.groupBox)
        self._deleteurl_.setGeometry(QtCore.QRect(520, 150, 75, 23))
        self._deleteurl_.setObjectName(_fromUtf8("_deleteurl_"))
        self._urllist_ = QtGui.QListWidget(self.groupBox)
        self._urllist_.setGeometry(QtCore.QRect(440, 30, 261, 111))
        self._urllist_.setObjectName(_fromUtf8("_urllist_"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(380, 50, 71, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 190, 341, 201))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 81, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 100, 91, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self._titleelement_ = QtGui.QLineEdit(self.groupBox_4)
        self._titleelement_.setGeometry(QtCore.QRect(120, 20, 171, 20))
        self._titleelement_.setObjectName(_fromUtf8("_titleelement_"))
        self._contextelement_ = QtGui.QLineEdit(self.groupBox_4)
        self._contextelement_.setGeometry(QtCore.QRect(120, 60, 171, 20))
        self._contextelement_.setObjectName(_fromUtf8("_contextelement_"))
        self._requesturl__ = QtGui.QLineEdit(self.groupBox_4)
        self._requesturl__.setGeometry(QtCore.QRect(120, 100, 171, 20))
        self._requesturl__.setObjectName(_fromUtf8("_requesturl__"))
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(10, 130, 91, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self._captchapicelement_ = QtGui.QLineEdit(self.groupBox_4)
        self._captchapicelement_.setGeometry(QtCore.QRect(120, 130, 171, 20))
        self._captchapicelement_.setObjectName(_fromUtf8("_captchapicelement_"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(10, 170, 91, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self._captchainputelement_ = QtGui.QLineEdit(self.groupBox_4)
        self._captchainputelement_.setGeometry(QtCore.QRect(120, 170, 171, 20))
        self._captchainputelement_.setObjectName(_fromUtf8("_captchainputelement_"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 101, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self._needpostnumber_ = QtGui.QSpinBox(self.groupBox)
        self._needpostnumber_.setGeometry(QtCore.QRect(140, 90, 71, 21))
        self._needpostnumber_.setObjectName(_fromUtf8("_needpostnumber_"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self._minpostinterval_ = QtGui.QSpinBox(self.groupBox)
        self._minpostinterval_.setGeometry(QtCore.QRect(140, 140, 71, 22))
        self._minpostinterval_.setObjectName(_fromUtf8("_minpostinterval_"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(230, 140, 21, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self._maxpostinterval_ = QtGui.QSpinBox(self.groupBox)
        self._maxpostinterval_.setGeometry(QtCore.QRect(260, 140, 81, 22))
        self._maxpostinterval_.setObjectName(_fromUtf8("_maxpostinterval_"))
        self._startpost_ = QtGui.QPushButton(self.tab2)
        self._startpost_.setGeometry(QtCore.QRect(140, 420, 75, 23))
        self._startpost_.setObjectName(_fromUtf8("_startpost_"))
        self._endpost_ = QtGui.QPushButton(self.tab2)
        self._endpost_.setEnabled(False)
        self._endpost_.setGeometry(QtCore.QRect(500, 420, 75, 23))
        self._endpost_.setObjectName(_fromUtf8("_endpost_"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 450, 731, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(40, 30, 61, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self._postednumber_ = QtGui.QLineEdit(self.groupBox_3)
        self._postednumber_.setEnabled(False)
        self._postednumber_.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self._postednumber_.setObjectName(_fromUtf8("_postednumber_"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(320, 30, 54, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self._remainpostnumber_ = QtGui.QLineEdit(self.groupBox_3)
        self._remainpostnumber_.setEnabled(False)
        self._remainpostnumber_.setGeometry(QtCore.QRect(420, 30, 113, 20))
        self._remainpostnumber_.setObjectName(_fromUtf8("_remainpostnumber_"))
        self._stoppost_ = QtGui.QPushButton(self.tab2)
        self._stoppost_.setEnabled(False)
        self._stoppost_.setGeometry(QtCore.QRect(260, 420, 75, 23))
        self._stoppost_.setObjectName(_fromUtf8("_stoppost_"))
        self._continuepost_ = QtGui.QPushButton(self.tab2)
        self._continuepost_.setEnabled(False)
        self._continuepost_.setGeometry(QtCore.QRect(380, 420, 75, 23))
        self._continuepost_.setObjectName(_fromUtf8("_continuepost_"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.tabWidget.addTab(self.tab3, _fromUtf8(""))
        self.tab4 = QtGui.QWidget()
        self.tab4.setObjectName(_fromUtf8("tab4"))
        self.tabWidget.addTab(self.tab4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)


        #这是手动添加的部分
        self._timer_ = QtCore.QTimer()
        self._timer_.timeout.connect(self.timecallfunc)
        self._timer_.start(100)

        # 绑定鼠标事件
        self._login_.clicked.connect(self.login)
        self._logout_.clicked.connect(self.logout)
        self._addaccount_.clicked.connect(self.addaccount)
        self._deleteaccount_.clicked.connect(self.deleteaccount)
        self._multipleaccount_.clicked.connect(self.multipleaccount)
        self._deleteurl_.clicked.connect(self.deleteurl)
        self._startpost_.clicked.connect(self.startpost)
        self._stoppost_.clicked.connect(self.stoppost)
        self._continuepost_.clicked.connect(self.continuepost)
        self._endpost_.clicked.connect(self.endpost)

        self._password_.setEchoMode(QtGui.QLineEdit.Password)
        self.init()

        self._urlBox_.activated[str].connect(self.changeurl)
        self._urllist_.activated.connect(self.changeurl1)
        self._ifautopost_.clicked.connect(self.autopost)
        #添加结束

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "用户名：", None))
        self.label_2.setText(_translate("MainWindow", "密码：", None))
        self._login_.setText(_translate("MainWindow", "登录", None))
        self._logout_.setText(_translate("MainWindow", "注销", None))
        self.label_15.setText(_translate("MainWindow", "多账号管理", None))
        self._rememberpw_.setText(_translate("MainWindow", "记住密码", None))
        self._autologin_.setText(_translate("MainWindow", "自动登录", None))
        self._deleteaccount_.setText(_translate("MainWindow", "删除账号", None))
        self._addaccount_.setText(_translate("MainWindow", "加入账号", None))
        self._multipleaccount_.setText(_translate("MainWindow", "多账号发帖", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "账号信息", None))
        self.groupBox.setTitle(_translate("MainWindow", "发帖参数设置", None))
        self.label_3.setText(_translate("MainWindow", "网址：", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "发帖内容", None))
        self.label_4.setText(_translate("MainWindow", "贴名：", None))
        self.label_5.setText(_translate("MainWindow", "帖子内容：", None))
        self._ifautopost_.setText(_translate("MainWindow", "自动生成", None))
        self._deleteurl_.setText(_translate("MainWindow", "删除网址", None))
        self.label_11.setText(_translate("MainWindow", "常用网址", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "页面元素设置", None))
        self.label_12.setText(_translate("MainWindow", "标题输入元素：", None))
        self.label_13.setText(_translate("MainWindow", "内容输入元素：", None))
        self.label_14.setText(_translate("MainWindow", "提交请求的url:", None))
        self.label_16.setText(_translate("MainWindow", "验证码图片元素：", None))
        self.label_17.setText(_translate("MainWindow", "验证码输入元素：", None))
        self.label_6.setText(_translate("MainWindow", "发帖数量：", None))
        self.label_7.setText(_translate("MainWindow", "发帖间隔时间(秒)：", None))
        self.label_8.setText(_translate("MainWindow", "至", None))
        self._startpost_.setText(_translate("MainWindow", "开始发帖", None))
        self._endpost_.setText(_translate("MainWindow", "停止发帖", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "程序运行情况", None))
        self.label_9.setText(_translate("MainWindow", "已发帖数：", None))
        self.label_10.setText(_translate("MainWindow", "剩余贴数：", None))
        self._stoppost_.setText(_translate("MainWindow", "暂停发帖", None))
        self._continuepost_.setText(_translate("MainWindow", "继续发帖", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "自动发贴", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "自动回帖", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("MainWindow", "信息统计", None))

    #增加的函数
    def addaccount(self):
        if self._username_.text() == "" or self._password_.text() == "":
            return
        self.addaccounttrue(self._username_.text(), self._password_.text())
        self._accountlist_.addItem(self._username_.text())

    def deleteaccount(self):
        if self._accountlist_.currentItem() == None:
            return
        self.deleteaccounttrue(self._accountlist_.currentItem().text())
        self._accountlist_.takeItem(self._accountlist_.currentRow())

    def deleteurl(self):
        if self._urllist_.currentItem() == None:
            return
        self.deleteurltrue(self._urllist_.currentItem().text())
        self._urllist_.takeItem(self._urllist_.currentRow())

    def startpost(self):
        self._urlBox_.addItem(self._url_.text())
        self.startposttrue()
        self.groupBox.setDisabled(True)
        self._startpost_.setDisabled(True)
        self._stoppost_.setEnabled(True)
        self._continuepost_.setDisabled(True)
        self._endpost_.setEnabled(True)

    def stoppost(self):
        self.stopposttrue()
        self._startpost_.setDisabled(True)
        self._stoppost_.setDisabled(True)
        self._continuepost_.setEnabled(True)
        self._endpost_.setEnabled(True)

    def continuepost(self):
        self.continueposttrue()
        self._startpost_.setDisabled(True)
        self._stoppost_.setEnabled(True)
        self._continuepost_.setDisabled(True)
        self._endpost_.setEnabled(True)

    def endpost(self):
        self.endposttrue()
        self.groupBox.setEnabled(True)
        self._startpost_.setEnabled(True)
        self._stoppost_.setDisabled(True)
        self._continuepost_.setDisabled(True)
        self._endpost_.setDisabled(True)

    # 选择网址
    def changeurl(self, index):
        self._url_.setText(self._urlBox_.currentText())

    def changeurl1(self):
        self._url_.setText(self._urllist_.currentItem().text())

    def getusername(self):
        return self._username_.text()

    def getpassword(self):
        return self._password_.text()

    def geturl(self):
        return self._url_.text()

    def autopost(self):
        if self._ifautopost_.isChecked():
            self._postname_.setDisabled(True)
            self._postcontent_.setDisabled(True)
        else:
            self._postname_.setEnabled(True)
            self._postcontent_.setEnabled(True)

    def ifautopost(self):
        if self._ifautopost_.isChecked():
            return True
        else:
            return False

    def ifrememberpw(self):
        if self._rememberpw_.isChecked():
            return True
        else:
            return False

    def ifautologin(self):
        if self._autologin_.isChecked():
            return True
        else:
            return False

    def getpostname(self):
        return self._postname_.text()

    def getpostcontext(self):
        return self._postcontent_.toPlainText()

    def needpostnumber(self):
        return self._needpostnumber_.text()

    def minpostinterval(self):
        return self._minpostinterval_.text()

    def maxpostinterval(self):
        return self._maxpostinterval_.text()

    def gettitleelement(self):
        return self._titleelement_.text()

    def getcontextelement(self):
        return self._contextelement_.text()

    def getrequesturl(self):
        return self._requesturl__.text()

    def getcaptchapicelement(self):
        return self._captchapicelement_.text()

    def getcaptchainputelement(self):
        return self._captchainputelement_.text()

    # 时间回调用函数
    def timecallfunc(self):
        pass

    def init(self):
        pass

    def login(self):
        username = self.getusername()
        password = self.getpassword()
        pass

    def logout(self):
        username = self.getusername()
        password = self.getpassword()
        pass

    def setusername(self, username):
        self._username_.setText(username)

    def setpassword(self, password):
        self._password_.setText(password)

    def setaccountlist(self, accountlist):
        self._accountlist_.clear()
        self._accountlist_.addItems(accountlist)

    def seturllist(self, urllist):
        self._urllist_.clear()
        self._urllist_.addItems(urllist)

    def addaccounttrue(self, username, password):
        pass

    def deleteaccounttrue(self, username):
        pass

    def deleteurltrue(self, url):
        pass

    def startposttrue(self):
        pass

    def stopposttrue(self):
        pass

    def continueposttrue(self):
        pass

    def endposttrue(self):
        pass

    def multipleaccount(self):
        pass