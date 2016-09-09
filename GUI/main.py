import APM
import sys
from PyQt4 import QtGui

if __name__ == '__main__':
    _app_ = QtGui.QApplication(sys.argv)
    _window_ = QtGui.QMainWindow()
    _myapp_ = APM.APMUi()
    _myapp_.setupUi(_window_)
    _window_.show()
    _app_.exec_()
