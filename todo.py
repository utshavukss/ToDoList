

from PyQt5 import QtCore, QtGui, QtWidgets
import db


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 501, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 470, 501, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 501, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.addToList())
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 240, 41))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clearTheList())
        self.pushButton_3.setGeometry(QtCore.QRect(270, 90, 240, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.saveToDatabase())
        self.pushButton_4.setGeometry(QtCore.QRect(10, 510, 501, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.fetchFromDb()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.pushButton.setText(_translate("MainWindow", "Add to List"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear List"))
        self.pushButton_4.setText(_translate("MainWindow", "Save for Today"))

    def fetchFromDb(self):
        db.cursor.execute("""SELECT * from activities""")
        db.conn.commit()
        records = db.cursor.fetchall()

        for row in records:
            listItem = QtWidgets.QCheckBox(row[0])
            if row[1] == 1: listItem.setChecked(True)
            self.verticalLayout.addWidget(listItem)
        
        self.updateProgress()
    
    def addToList(self):
        text = self.plainTextEdit.toPlainText()
        if text:
            listItem = QtWidgets.QCheckBox(text)
            listItem.stateChanged.connect(self.updateProgress)
            #listItem = QtWidgets.QWidgetItem(listItem)
            self.verticalLayout.addWidget(listItem)
            self.updateProgress()
        
    def clearTheList(self):
        while self.verticalLayout.count():
            layoutItem = self.verticalLayout.takeAt(0)
            layoutItem.widget().deleteLater()
        self.updateProgress()

    def saveToDatabase(self):
        db.cursor.execute("DELETE FROM activities;",)
        db.conn.commit()

        for index in range (self.verticalLayout.count()):
            listItem = self.verticalLayout.itemAt(index)
            listItem = listItem.widget()
            
            if isinstance(listItem, QtWidgets.QCheckBox):
                print("True, now inserting")
                db.cursor.execute("INSERT INTO activities (activity, status) VALUES (:text, :value)", {
                    'text': listItem.text(),
                    'value': 1 if listItem.isChecked() else 0
                })
                db.conn.commit()
            else: print("no instance")
    def updateProgress(self):
        total = self.verticalLayout.count()
        checked = 0
        for i in range (total):
            checkBoxItem = self.verticalLayout.itemAt(i)
            wid = checkBoxItem.widget()
            if isinstance(wid, QtWidgets.QCheckBox) and wid.isChecked():
                checked += 1
        if not checked:
            self.progressBar.setProperty("value", 0)
        else:
            self.progressBar.setProperty("value", checked/total * 100)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
