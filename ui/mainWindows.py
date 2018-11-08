# -*- coding:utf-8 -*-
import sys
import os
import subprocess
from qss import uiQss
sys.path.append(r'C:\cgteamwork\bin\lib\pyside')
from PySide import QtGui as QtWidgets
from PySide import QtCore
from PySide import QtGui
QtCore.QCoreApplication.addLibraryPath(os.path.join(os.path.dirname(QtCore.__file__), "plugins"))
import mouseDragEvent
MAYABATCHPATH = 'D:/Autodesk Maya/Maya2017/bin/mayabatch.exe'
class MainView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.setWindowTitle('Export AnimationCurves')
        self._mainUI()
        
    def _mainUI(self):
        resultLButton = QtGui.QPushButton(u'确定')
        self.listWidget = mouseDragEvent.My_ListWidget(self)
        self.listWidget.setDragEnabled(True)
        
        Hlayout2 = QtGui.QHBoxLayout()
        Hlayout2.addStretch(0)
        Hlayout2.addWidget(resultLButton)

        VLayout = QtGui.QVBoxLayout()
        VLayout.addWidget(self.listWidget)
        VLayout.addLayout(Hlayout2)

        self.setLayout(VLayout)

        resultLButton.clicked.connect(self.Run)

    def Run(self):
        maFileList = []
        currentPath = os.path.dirname(__file__)       
        publishPath = '%s/exportCurves.py'%currentPath
        melFile = '%s/exportCurves.mel'%currentPath
        count = self.listWidget.count()
        for ii in xrange(count):
            maFileList.append(self.listWidget.item(ii).text())
        for ii in maFileList:
            cmd = '"{mayaBatchPath}" -script "{melFile}" "{publishPath}" "{maPath}" "{currentFolder}"'.format(
                mayaBatchPath = MAYABATCHPATH,
                melFile = melFile,
                publishPath = publishPath,
                maPath = ii,
                currentFolder = os.path.dirname(ii),
                )
            subprocess.check_call(cmd, shell=True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainView()
    ex.setStyleSheet(uiQss)
    ex.show()
    sys.exit(app.exec_())
