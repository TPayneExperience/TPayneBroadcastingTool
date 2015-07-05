

beginningLines = '''
#!/usr/bin/env python

import os, sys, time, shutil
from os.path import join, isfile
from os import listdir
'''

constructorCode = '''
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

        self.fileLoc = 'D:\\Captures\\Stream_Recordings'
        self.lastFileCheck = [f for f in listdir(self.fileLoc) if isfile(join(self.fileLoc, f))]

        '''

finalLines = '''
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
'''

# =============================================
# =============================================
sourceFile = open('Broadcaster_helper_raw.py', 'r')
lines = sourceFile.read()
sourceFile.close()

parts = lines.split('class Ui_BroadcastHelper_UI_form(object):')


f = open('Broadcaster_helper_MAIN.py', 'w')
f.write(beginningLines)
f.write(parts[0])
f.write(constructorCode)
f.write(parts[1])
f.write(finalLines)
f.close()