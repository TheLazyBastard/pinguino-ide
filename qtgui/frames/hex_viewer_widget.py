# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/Documentos/python/dev/developing/pinguino/pinguino-ide/qtgui/frames/hex_viewer_widget.ui'
#
# Created: Sun Sep 14 22:40:38 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_HexViewer(object):
    def setupUi(self, HexViewer):
        HexViewer.setObjectName("HexViewer")
        HexViewer.resize(722, 390)
        self.centralwidget = QtGui.QWidget(HexViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_view = QtGui.QComboBox(self.centralwidget)
        self.comboBox_view.setMinimumSize(QtCore.QSize(141, 0))
        self.comboBox_view.setObjectName("comboBox_view")
        self.comboBox_view.addItem("")
        self.comboBox_view.setItemText(0, "HEX (FF)")
        self.comboBox_view.addItem("")
        self.comboBox_view.setItemText(1, "HEX (0xFF)")
        self.comboBox_view.addItem("")
        self.comboBox_view.setItemText(2, "DEC")
        self.horizontalLayout.addWidget(self.comboBox_view)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tableWidget_viewer = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_viewer.setAlternatingRowColors(True)
        self.tableWidget_viewer.setObjectName("tableWidget_viewer")
        self.tableWidget_viewer.setColumnCount(24)
        self.tableWidget_viewer.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(0, item)
        self.tableWidget_viewer.horizontalHeaderItem(0).setText("00")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(1, item)
        self.tableWidget_viewer.horizontalHeaderItem(1).setText("01")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(2, item)
        self.tableWidget_viewer.horizontalHeaderItem(2).setText("02")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(3, item)
        self.tableWidget_viewer.horizontalHeaderItem(3).setText("03")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(4, item)
        self.tableWidget_viewer.horizontalHeaderItem(4).setText("04")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(5, item)
        self.tableWidget_viewer.horizontalHeaderItem(5).setText("05")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(6, item)
        self.tableWidget_viewer.horizontalHeaderItem(6).setText("06")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(7, item)
        self.tableWidget_viewer.horizontalHeaderItem(7).setText("07")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(8, item)
        self.tableWidget_viewer.horizontalHeaderItem(8).setText("08")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(9, item)
        self.tableWidget_viewer.horizontalHeaderItem(9).setText("09")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(10, item)
        self.tableWidget_viewer.horizontalHeaderItem(10).setText("0A")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(11, item)
        self.tableWidget_viewer.horizontalHeaderItem(11).setText("0B")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(12, item)
        self.tableWidget_viewer.horizontalHeaderItem(12).setText("0C")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(13, item)
        self.tableWidget_viewer.horizontalHeaderItem(13).setText("0D")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(14, item)
        self.tableWidget_viewer.horizontalHeaderItem(14).setText("0E")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(15, item)
        self.tableWidget_viewer.horizontalHeaderItem(15).setText("0F")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(16, item)
        self.tableWidget_viewer.horizontalHeaderItem(16).setText("10")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(17, item)
        self.tableWidget_viewer.horizontalHeaderItem(17).setText("11")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(18, item)
        self.tableWidget_viewer.horizontalHeaderItem(18).setText("12")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(19, item)
        self.tableWidget_viewer.horizontalHeaderItem(19).setText("13")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(20, item)
        self.tableWidget_viewer.horizontalHeaderItem(20).setText("14")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(21, item)
        self.tableWidget_viewer.horizontalHeaderItem(21).setText("15")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(22, item)
        self.tableWidget_viewer.horizontalHeaderItem(22).setText("16")
        item = QtGui.QTableWidgetItem()
        self.tableWidget_viewer.setHorizontalHeaderItem(23, item)
        self.tableWidget_viewer.horizontalHeaderItem(23).setText("17")
        self.tableWidget_viewer.horizontalHeader().setDefaultSectionSize(37)
        self.gridLayout.addWidget(self.tableWidget_viewer, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_close = QtGui.QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.pushButton_save_changes = QtGui.QPushButton(self.centralwidget)
        self.pushButton_save_changes.setEnabled(False)
        self.pushButton_save_changes.setObjectName("pushButton_save_changes")
        self.horizontalLayout_2.addWidget(self.pushButton_save_changes)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        HexViewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(HexViewer)
        QtCore.QMetaObject.connectSlotsByName(HexViewer)

    def retranslateUi(self, HexViewer):
        HexViewer.setWindowTitle(QtGui.QApplication.translate("HexViewer", "Hex Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("HexViewer", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save_changes.setText(QtGui.QApplication.translate("HexViewer", "Save changes as...", None, QtGui.QApplication.UnicodeUTF8))

