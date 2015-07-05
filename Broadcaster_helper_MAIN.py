
#!/usr/bin/env python

import os, sys, time, shutil
from os.path import join, isfile
from os import listdir
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Broadcaster_helper.ui'
#
# Created: Sat Jun 27 13:57:50 2015
#      by: PyQt4 UI code generator 4.11.3
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


class BroadcastHelper_UI_form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        size = self.size()
        self.setGeometry(1970,960, size.width(), size.height())
        self.clearTime()

        self.preshow = True
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        
        self.updateClock()
        self.clockTimer = QtCore.QTimer(self)
        self.clockTimer.timeout.connect(self.updateClock)
        self.clockTimer.start(1000)

        self.startTime = None
        self.endTime = None
        self.broadcasting = False
        self.timerDeleted = False

        self.fileLoc = 'D:\Captures\Stream_Recordings'
        self.lastFileCheck = [f for f in listdir(self.fileLoc) if isfile(join(self.fileLoc, f))]

        
    def setupUi(self, BroadcastHelper_UI_form):
        BroadcastHelper_UI_form.setObjectName(_fromUtf8("BroadcastHelper_UI_form"))
        BroadcastHelper_UI_form.setWindowModality(QtCore.Qt.NonModal)
        BroadcastHelper_UI_form.resize(217, 241)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(75, 4, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 208, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 4, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 208, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 208, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 208, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        BroadcastHelper_UI_form.setPalette(palette)
        self.verticalLayout_2 = QtGui.QVBoxLayout(BroadcastHelper_UI_form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.timer_text = QtGui.QLabel(BroadcastHelper_UI_form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Damn Noisy Kids"))
        font.setPointSize(48)
        self.timer_text.setFont(font)
        self.timer_text.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_text.setObjectName(_fromUtf8("timer_text"))
        self.verticalLayout.addWidget(self.timer_text)
        self.temp_horizontalLayout = QtGui.QHBoxLayout()
        self.temp_horizontalLayout.setObjectName(_fromUtf8("temp_horizontalLayout"))
        self.timer_timeEdit = QtGui.QTimeEdit(BroadcastHelper_UI_form)
        self.timer_timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_timeEdit.setTime(QtCore.QTime(0, 5, 0))
        self.timer_timeEdit.setCurrentSection(QtGui.QDateTimeEdit.MinuteSection)
        self.timer_timeEdit.setObjectName(_fromUtf8("timer_timeEdit"))
        self.temp_horizontalLayout.addWidget(self.timer_timeEdit)
        self.timer_btn = QtGui.QPushButton(BroadcastHelper_UI_form)
        self.timer_btn.setObjectName(_fromUtf8("timer_btn"))
        self.temp_horizontalLayout.addWidget(self.timer_btn)
        self.verticalLayout.addLayout(self.temp_horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.name_lineEdit = QtGui.QLineEdit(BroadcastHelper_UI_form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.verticalLayout.addWidget(self.name_lineEdit)
        self.broadcast_btn = QtGui.QPushButton(BroadcastHelper_UI_form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gadugi"))
        font.setPointSize(16)
        self.broadcast_btn.setFont(font)
        self.broadcast_btn.setObjectName(_fromUtf8("broadcast_btn"))
        self.verticalLayout.addWidget(self.broadcast_btn)
        self.clock_text = QtGui.QLabel(BroadcastHelper_UI_form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Kozuka Gothic Pro M"))
        font.setPointSize(24)
        self.clock_text.setFont(font)
        self.clock_text.setAlignment(QtCore.Qt.AlignCenter)
        self.clock_text.setObjectName(_fromUtf8("clock_text"))
        self.verticalLayout.addWidget(self.clock_text)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(BroadcastHelper_UI_form)
        QtCore.QMetaObject.connectSlotsByName(BroadcastHelper_UI_form)

    def retranslateUi(self, BroadcastHelper_UI_form):
        BroadcastHelper_UI_form.setWindowTitle(_translate("BroadcastHelper_UI_form", "TPayne\'s Broadcast Helper!!", None))
        self.timer_text.setText(_translate("BroadcastHelper_UI_form", "--:--", None))
        self.timer_timeEdit.setDisplayFormat(_translate("BroadcastHelper_UI_form", "mm:ss", None))
        self.timer_btn.setText(_translate("BroadcastHelper_UI_form", "START Timer", None))
        self.name_lineEdit.setText(_translate("BroadcastHelper_UI_form", "Show Name", None))
        self.broadcast_btn.setText(_translate("BroadcastHelper_UI_form", "START Broadcast", None))
        self.clock_text.setText(_translate("BroadcastHelper_UI_form", "12:31", None))


    @QtCore.pyqtSignature("on_broadcast_btn_clicked()")
    def broadcastBtn(self):
        self.deleteTimerWidget()
        if not self.broadcasting:
            self.broadcasting = True
            self.startBroadcast()
            self.broadcast_btn.setText(_translate("BroadcastHelper_UI_form", "STOP Broadcast", None))
        else:
            self.broadcasting = False
            self.endBroadcast()
            self.broadcast_btn.setText(_translate("BroadcastHelper_UI_form", "START Broadcast", None))

    def startBroadcast(self):
        self.moveOldFiles()
        self.timer.start(1000)

    def endBroadcast(self):
        print ("SUPER HAM!")
        self.timer.stop()
        self.startTime = None
        self.endTime = None
        self.clearTime()
        self.renameFinalFiles()

    @QtCore.pyqtSignature("on_timer_btn_clicked()")
    def startPreshowTimer(self):
        t = self.timer_timeEdit.time()
        self.startTimer(t.minute()*60 + t.second())
        self.timer.start(1000)

    def deleteTimerWidget(self):
        if not self.timerDeleted:
            self.timerDeleted = True
            self.temp_horizontalLayout.setParent(None)
            self.timer_btn.setParent(None)
            self.timer_timeEdit.setParent(None)
            self.resize(203,203)

    ## =============================================

    def moveOldFiles(self):
        files = [f for f in listdir(self.fileLoc) if isfile(join(self.fileLoc, f))]
        print files
        dest = join(self.fileLoc, 'old')
        for f in files:
            shutil.move(join(self.fileLoc, f), join(dest, f))
        print 'moving OLD files...'

    def renameFinalFiles(self):
        files = [f for f in listdir(self.fileLoc) if isfile(join(self.fileLoc, f))]
        files.sort()
        showName = str(self.name_lineEdit.text()).replace(' ', '_')
        showName = showName.replace('-', '~').replace(':', '~')
        for f in range(len(files)):
            if '_Part_' not in files[f]:
                newName = showName + "_Part_%02d.mp4" % (f+1)
                os.rename(join(self.fileLoc, files[f]), join(self.fileLoc, newName))

    def startTimer(self, amountOfTime = 30*60):
        self.startTime = time.time()
        self.endTime = time.time() + amountOfTime
        print ("TIME STARTED!")

    def clearTime(self):
        self.timer_text.setText(_translate("BroadcastHelper_UI_form", '--:--', None))

    def update(self):
        if (self.startTime == None) or (self.endTime < time.time()):
            files = [f for f in listdir(self.fileLoc) if isfile(join(self.fileLoc, f))]
            if (files != self.lastFileCheck):
                self.startTimer()
                self.lastFileCheck = files
        else:
            self.timer_text.setText(_translate("BroadcastHelper_UI_form", self.calcCurrentTime(), None))

    def updateClock(self):
        t = time.localtime()
        p = 'am'
        hour = t.tm_hour
        if hour >= 12:
            p = 'pm'
            if hour > 12:
                hour -= 12
        curTime = '%d:%02d %s' %(hour, t.tm_min, p)
        self.clock_text.setText(_translate("BroadcastHelper_UI_form", curTime, None))


    def calcCurrentTime(self):
        curTime = self.endTime - time.time()
        minutes = curTime/60
        seconds = curTime % 60
        return "%02d:%02d" % (minutes, seconds)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = BroadcastHelper_UI_form()
    ex.show()
    sys.exit(app.exec_())
