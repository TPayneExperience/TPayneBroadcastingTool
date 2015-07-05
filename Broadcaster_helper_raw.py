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

class Ui_BroadcastHelper_UI_form(object):
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

