import sys
import uisrc.home_page
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
if __name__ == '__main__':
  myapp = QApplication(sys.argv)
  myDlg = QMainWindow()
  myUI = uisrc.home_page.Ui_HomeWindow()
  myUI.setupUi(myDlg)
  myDlg.show()
  sys.exit(myapp.exec_())

