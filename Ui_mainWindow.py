# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/junxing.yang/Dropbox/dev/py-presto/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainSplitter = QtWidgets.QSplitter(self.centralwidget)
        self.mainSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.mainSplitter.setObjectName("mainSplitter")
        self.leftSplitter = QtWidgets.QSplitter(self.mainSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftSplitter.sizePolicy().hasHeightForWidth())
        self.leftSplitter.setSizePolicy(sizePolicy)
        self.leftSplitter.setOrientation(QtCore.Qt.Vertical)
        self.leftSplitter.setObjectName("leftSplitter")
        self.tablesWidget = QtWidgets.QTreeWidget(self.leftSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablesWidget.sizePolicy().hasHeightForWidth())
        self.tablesWidget.setSizePolicy(sizePolicy)
        self.tablesWidget.setMinimumSize(QtCore.QSize(250, 100))
        self.tablesWidget.setMaximumSize(QtCore.QSize(800, 800))
        self.tablesWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tablesWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed)
        self.tablesWidget.setIndentation(15)
        self.tablesWidget.setColumnCount(1)
        self.tablesWidget.setObjectName("tablesWidget")
        self.tablesWidget.header().setVisible(True)
        self.schemaView = QtWidgets.QTreeWidget(self.leftSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schemaView.sizePolicy().hasHeightForWidth())
        self.schemaView.setSizePolicy(sizePolicy)
        self.schemaView.setMinimumSize(QtCore.QSize(250, 300))
        self.schemaView.setMaximumSize(QtCore.QSize(800, 16777215))
        self.schemaView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.schemaView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked)
        self.schemaView.setIndentation(15)
        self.schemaView.setObjectName("schemaView")
        self.layoutWidget = QtWidgets.QWidget(self.mainSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.dataLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.dataLayout.setContentsMargins(0, 0, 0, 0)
        self.dataLayout.setObjectName("dataLayout")
        self.connWidget = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connWidget.sizePolicy().hasHeightForWidth())
        self.connWidget.setSizePolicy(sizePolicy)
        self.connWidget.setMinimumSize(QtCore.QSize(0, 40))
        self.connWidget.setObjectName("connWidget")
        self.connWidgetLayout = QtWidgets.QHBoxLayout(self.connWidget)
        self.connWidgetLayout.setContentsMargins(-1, 0, -1, 0)
        self.connWidgetLayout.setObjectName("connWidgetLayout")
        self.urlLabel = QtWidgets.QLabel(self.connWidget)
        self.urlLabel.setObjectName("urlLabel")
        self.connWidgetLayout.addWidget(self.urlLabel)
        self.urlEdit = QtWidgets.QLineEdit(self.connWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlEdit.sizePolicy().hasHeightForWidth())
        self.urlEdit.setSizePolicy(sizePolicy)
        self.urlEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.urlEdit.setText("")
        self.urlEdit.setObjectName("urlEdit")
        self.connWidgetLayout.addWidget(self.urlEdit)
        self.userLabel = QtWidgets.QLabel(self.connWidget)
        self.userLabel.setObjectName("userLabel")
        self.connWidgetLayout.addWidget(self.userLabel)
        self.userEdit = QtWidgets.QLineEdit(self.connWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userEdit.sizePolicy().hasHeightForWidth())
        self.userEdit.setSizePolicy(sizePolicy)
        self.userEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.userEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.userEdit.setText("")
        self.userEdit.setObjectName("userEdit")
        self.connWidgetLayout.addWidget(self.userEdit)
        self.tunnelButton = QtWidgets.QPushButton(self.connWidget)
        self.tunnelButton.setCheckable(True)
        self.tunnelButton.setObjectName("tunnelButton")
        self.connWidgetLayout.addWidget(self.tunnelButton)
        self.connButtonBox = QtWidgets.QDialogButtonBox(self.connWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connButtonBox.sizePolicy().hasHeightForWidth())
        self.connButtonBox.setSizePolicy(sizePolicy)
        self.connButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.connButtonBox.setObjectName("connButtonBox")
        self.connWidgetLayout.addWidget(self.connButtonBox)
        self.dataLayout.addWidget(self.connWidget)
        self.tunnelWidget = QtWidgets.QWidget(self.layoutWidget)
        self.tunnelWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.tunnelWidget.setStyleSheet("#tunnelWidget {background-color: lightgray}")
        self.tunnelWidget.setObjectName("tunnelWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tunnelWidget)
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serverLabel = QtWidgets.QLabel(self.tunnelWidget)
        self.serverLabel.setObjectName("serverLabel")
        self.horizontalLayout.addWidget(self.serverLabel)
        self.serverEdit = QtWidgets.QLineEdit(self.tunnelWidget)
        self.serverEdit.setText("")
        self.serverEdit.setObjectName("serverEdit")
        self.horizontalLayout.addWidget(self.serverEdit)
        self.gatewayLabel = QtWidgets.QLabel(self.tunnelWidget)
        self.gatewayLabel.setObjectName("gatewayLabel")
        self.horizontalLayout.addWidget(self.gatewayLabel)
        self.gatewayEdit = QtWidgets.QLineEdit(self.tunnelWidget)
        self.gatewayEdit.setText("")
        self.gatewayEdit.setObjectName("gatewayEdit")
        self.horizontalLayout.addWidget(self.gatewayEdit)
        self.tunnelUserLabel = QtWidgets.QLabel(self.tunnelWidget)
        self.tunnelUserLabel.setObjectName("tunnelUserLabel")
        self.horizontalLayout.addWidget(self.tunnelUserLabel)
        self.tunnelUserEdit = QtWidgets.QLineEdit(self.tunnelWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tunnelUserEdit.sizePolicy().hasHeightForWidth())
        self.tunnelUserEdit.setSizePolicy(sizePolicy)
        self.tunnelUserEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.tunnelUserEdit.setText("")
        self.tunnelUserEdit.setObjectName("tunnelUserEdit")
        self.horizontalLayout.addWidget(self.tunnelUserEdit)
        self.keyComboBox = QtWidgets.QComboBox(self.tunnelWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyComboBox.sizePolicy().hasHeightForWidth())
        self.keyComboBox.setSizePolicy(sizePolicy)
        self.keyComboBox.setMinimumSize(QtCore.QSize(110, 0))
        self.keyComboBox.setMaximumSize(QtCore.QSize(110, 16777215))
        self.keyComboBox.setObjectName("keyComboBox")
        self.keyComboBox.addItem("")
        self.keyComboBox.addItem("")
        self.horizontalLayout.addWidget(self.keyComboBox)
        self.pwdLineEdit = QtWidgets.QLineEdit(self.tunnelWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwdLineEdit.sizePolicy().hasHeightForWidth())
        self.pwdLineEdit.setSizePolicy(sizePolicy)
        self.pwdLineEdit.setMinimumSize(QtCore.QSize(188, 22))
        self.pwdLineEdit.setMaximumSize(QtCore.QSize(188, 16777215))
        self.pwdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdLineEdit.setObjectName("pwdLineEdit")
        self.horizontalLayout.addWidget(self.pwdLineEdit)
        self.keyFileButton = QtWidgets.QPushButton(self.tunnelWidget)
        self.keyFileButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyFileButton.sizePolicy().hasHeightForWidth())
        self.keyFileButton.setSizePolicy(sizePolicy)
        self.keyFileButton.setMinimumSize(QtCore.QSize(200, 0))
        self.keyFileButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.keyFileButton.setObjectName("keyFileButton")
        self.horizontalLayout.addWidget(self.keyFileButton)
        self.clearButton = QtWidgets.QPushButton(self.tunnelWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.dataLayout.addWidget(self.tunnelWidget)
        self.sqlEdit = TextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqlEdit.sizePolicy().hasHeightForWidth())
        self.sqlEdit.setSizePolicy(sizePolicy)
        self.sqlEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.sqlEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.sqlEdit.setObjectName("sqlEdit")
        self.dataLayout.addWidget(self.sqlEdit)
        self.sqlWidget = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqlWidget.sizePolicy().hasHeightForWidth())
        self.sqlWidget.setSizePolicy(sizePolicy)
        self.sqlWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.sqlWidget.setObjectName("sqlWidget")
        self.sqlWidgetLayout = QtWidgets.QHBoxLayout(self.sqlWidget)
        self.sqlWidgetLayout.setObjectName("sqlWidgetLayout")
        self.runButtonBox = QtWidgets.QDialogButtonBox(self.sqlWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButtonBox.sizePolicy().hasHeightForWidth())
        self.runButtonBox.setSizePolicy(sizePolicy)
        self.runButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.runButtonBox.setObjectName("runButtonBox")
        self.sqlWidgetLayout.addWidget(self.runButtonBox)
        self.dataLayout.addWidget(self.sqlWidget)
        self.dataWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.dataWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dataWidget.setAlternatingRowColors(True)
        self.dataWidget.setObjectName("dataWidget")
        self.dataWidget.setColumnCount(0)
        self.dataWidget.setRowCount(0)
        self.dataLayout.addWidget(self.dataWidget)
        self.horizontalLayout_2.addWidget(self.mainSplitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PiePresto"))
        self.tablesWidget.headerItem().setText(0, _translate("MainWindow", "DBs/Tables"))
        self.schemaView.headerItem().setText(0, _translate("MainWindow", "Field"))
        self.schemaView.headerItem().setText(1, _translate("MainWindow", "Type"))
        self.urlLabel.setText(_translate("MainWindow", "Url:"))
        self.userLabel.setText(_translate("MainWindow", "Presto User:"))
        self.tunnelButton.setText(_translate("MainWindow", "Tunnel"))
        self.serverLabel.setText(_translate("MainWindow", "PrestoServer:"))
        self.gatewayLabel.setText(_translate("MainWindow", "Gateway:"))
        self.tunnelUserLabel.setText(_translate("MainWindow", "User:"))
        self.keyComboBox.setCurrentText(_translate("MainWindow", "KeyFile"))
        self.keyComboBox.setItemText(0, _translate("MainWindow", "KeyFile"))
        self.keyComboBox.setItemText(1, _translate("MainWindow", "Password"))
        self.pwdLineEdit.setPlaceholderText(_translate("MainWindow", "Enter Password..."))
        self.keyFileButton.setText(_translate("MainWindow", "Choose Key File..."))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.sqlEdit.setPlaceholderText(_translate("MainWindow", "Write your Presto SQL"))
        self.dataWidget.setSortingEnabled(True)


from textedit import TextEdit
