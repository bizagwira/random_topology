import sys
from PyQt4 import QtGui
from wsnviewer import WsnViewer
        
if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    wsnView = WsnViewer ()
    wsnView.main()
    sys.exit(app.exec_())