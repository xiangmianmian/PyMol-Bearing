# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Pyqt5 project\testbearing.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Testbearing(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(662, 594)
        Dialog.setMinimumSize(QtCore.QSize(662, 594))
        Dialog.setMaximumSize(QtCore.QSize(662, 594))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 470, 321, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_finish = QtWidgets.QPushButton(Dialog)
        self.pushButton_finish.setGeometry(QtCore.QRect(270, 550, 93, 28))
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 341, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_confirm = QtWidgets.QPushButton(Dialog)
        self.pushButton_confirm.setGeometry(QtCore.QRect(270, 430, 93, 28))
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(180, 500, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 50, 601, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_14.setPalette(palette)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)
        self.lineEdit_bearing_kp = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_kp.setObjectName("lineEdit_bearing_kp")
        self.gridLayout.addWidget(self.lineEdit_bearing_kp, 3, 1, 1, 1)
        self.lineEdit_bearing_mp = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_mp.setObjectName("lineEdit_bearing_mp")
        self.gridLayout.addWidget(self.lineEdit_bearing_mp, 2, 3, 1, 1)
        self.lineEdit_bearing_cr = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_cr.setObjectName("lineEdit_bearing_cr")
        self.gridLayout.addWidget(self.lineEdit_bearing_cr, 5, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_19.setPalette(palette)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_10.setPalette(palette)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)
        self.lineEdit_bearing_cp = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_cp.setObjectName("lineEdit_bearing_cp")
        self.gridLayout.addWidget(self.lineEdit_bearing_cp, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.lineEdit_bearing_kr = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_kr.setObjectName("lineEdit_bearing_kr")
        self.gridLayout.addWidget(self.lineEdit_bearing_kr, 4, 3, 1, 1)
        self.lineEdit_bearing_ms = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_ms.setObjectName("lineEdit_bearing_ms")
        self.gridLayout.addWidget(self.lineEdit_bearing_ms, 1, 1, 1, 1)
        self.lineEdit_bearing_cs = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_cs.setObjectName("lineEdit_bearing_cs")
        self.gridLayout.addWidget(self.lineEdit_bearing_cs, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.lineEdit_bearing_ks = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_ks.setObjectName("lineEdit_bearing_ks")
        self.gridLayout.addWidget(self.lineEdit_bearing_ks, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_bearing_mr = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_mr.setObjectName("lineEdit_bearing_mr")
        self.gridLayout.addWidget(self.lineEdit_bearing_mr, 4, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_17.setPalette(palette)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_12.setPalette(palette)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_8.setPalette(palette)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_20.setPalette(palette)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_22 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_22.setPalette(palette)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 2)
        self.label_41 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_41.setPalette(palette)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 1, 0, 1, 1)
        self.lineEdit_bearing_nb = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_nb.setObjectName("lineEdit_bearing_nb")
        self.gridLayout_2.addWidget(self.lineEdit_bearing_nb, 1, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_43.setPalette(palette)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 1, 2, 1, 1)
        self.lineEdit_bearing_Dp = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_Dp.setObjectName("lineEdit_bearing_Dp")
        self.gridLayout_2.addWidget(self.lineEdit_bearing_Dp, 1, 3, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_45.setPalette(palette)
        self.label_45.setObjectName("label_45")
        self.gridLayout_2.addWidget(self.label_45, 2, 0, 1, 1)
        self.lineEdit_bearing_Db = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_Db.setObjectName("lineEdit_bearing_Db")
        self.gridLayout_2.addWidget(self.lineEdit_bearing_Db, 2, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_47.setPalette(palette)
        self.label_47.setObjectName("label_47")
        self.gridLayout_2.addWidget(self.label_47, 2, 2, 1, 1)
        self.lineEdit_bearing_phi_slip = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_bearing_phi_slip.sizePolicy().hasHeightForWidth())
        self.lineEdit_bearing_phi_slip.setSizePolicy(sizePolicy)
        self.lineEdit_bearing_phi_slip.setObjectName("lineEdit_bearing_phi_slip")
        self.gridLayout_2.addWidget(self.lineEdit_bearing_phi_slip, 2, 3, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_49.setPalette(palette)
        self.label_49.setObjectName("label_49")
        self.gridLayout_2.addWidget(self.label_49, 3, 0, 1, 1)
        self.lineEdit_bearing_mut = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_mut.setObjectName("lineEdit_bearing_mut")
        self.gridLayout_2.addWidget(self.lineEdit_bearing_mut, 3, 1, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_51.setPalette(palette)
        self.label_51.setObjectName("label_51")
        self.gridLayout_2.addWidget(self.label_51, 3, 2, 1, 1)
        self.lineEdit_bearing_kb = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_bearing_kb.sizePolicy().hasHeightForWidth())
        self.lineEdit_bearing_kb.setSizePolicy(sizePolicy)
        self.lineEdit_bearing_kb.setObjectName("lineEdit_bearing_kb")
        self.gridLayout_2.addWidget(self.lineEdit_bearing_kb, 3, 3, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_53.setPalette(palette)
        self.label_53.setObjectName("label_53")
        self.gridLayout_2.addWidget(self.label_53, 4, 0, 1, 1)
        self.lineEdit_bearing_c = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_c.setObjectName("lineEdit_bearing_c")
        self.gridLayout_2.addWidget(self.lineEdit_bearing_c, 4, 1, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_55.setPalette(palette)
        self.label_55.setObjectName("label_55")
        self.gridLayout_2.addWidget(self.label_55, 4, 2, 1, 1)
        self.lineEdit_bearing_alpha = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bearing_alpha.setObjectName("lineEdit_bearing_alpha")
        self.gridLayout_2.addWidget(self.lineEdit_bearing_alpha, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Test Bearing"))
        self.label.setText(_translate("Dialog", "Please choose defect type："))
        self.pushButton_finish.setText(_translate("Dialog", "Finish"))
        self.label_3.setText(_translate("Dialog", "Test Bearing parameters configuration："))
        self.pushButton_confirm.setText(_translate("Dialog", "Confirm"))
        self.comboBox.setItemText(0, _translate("Dialog", "Healthy"))
        self.comboBox.setItemText(1, _translate("Dialog", "RaceWay"))
        self.comboBox.setItemText(2, _translate("Dialog", "Ball"))
        self.label_14.setToolTip(_translate("Dialog", "<html><head/><body><p>Pedestal damping</p><p>Unit: Ns/m</p></body></html>"))
        self.label_14.setText(_translate("Dialog", "cp:"))
        self.lineEdit_bearing_kp.setPlaceholderText(_translate("Dialog", "15100000"))
        self.lineEdit_bearing_mp.setPlaceholderText(_translate("Dialog", "6.638"))
        self.lineEdit_bearing_cr.setPlaceholderText(_translate("Dialog", "9424.8"))
        self.label_19.setToolTip(_translate("Dialog", "<html><head/><body><p>Resonator Mass</p><p>Unit: kg</p></body></html>"))
        self.label_19.setText(_translate("Dialog", "mr:"))
        self.label_10.setToolTip(_translate("Dialog", "<html><head/><body><p>Pedestal Mass</p><p>Unit: kg</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "mp:"))
        self.lineEdit_bearing_cp.setPlaceholderText(_translate("Dialog", "2210.7"))
        self.label_2.setText(_translate("Dialog", "Material parameters:"))
        self.lineEdit_bearing_kr.setPlaceholderText(_translate("Dialog", "8882600000"))
        self.lineEdit_bearing_ms.setPlaceholderText(_translate("Dialog", "3.2638"))
        self.lineEdit_bearing_cs.setPlaceholderText(_translate("Dialog", "1376.8"))
        self.label_6.setToolTip(_translate("Dialog", "<html><head/><body><p>Shaft Stiffness</p><p>Unit:N/m</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "ks:"))
        self.lineEdit_bearing_ks.setPlaceholderText(_translate("Dialog", "74200000"))
        self.label_4.setToolTip(_translate("Dialog", "<html><head/><body><p>Shaft Mass</p><p>Unit: kg</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "ms: "))
        self.lineEdit_bearing_mr.setPlaceholderText(_translate("Dialog", "1"))
        self.label_17.setToolTip(_translate("Dialog", "<html><head/><body><p>Resonator Stiffness</p><p>Unit: N/m</p></body></html>"))
        self.label_17.setText(_translate("Dialog", "kr:"))
        self.label_12.setToolTip(_translate("Dialog", "<html><head/><body><p>Pedestal Stiffness</p><p>Unit: N/m</p></body></html>"))
        self.label_12.setText(_translate("Dialog", "kp:"))
        self.label_8.setToolTip(_translate("Dialog", "<html><head/><body><p>Shaft damping</p><p>Unit: Ns/m</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "cs:"))
        self.label_20.setToolTip(_translate("Dialog", "<html><head/><body><p>Resonator Damping</p><p>Unit: Ns/m</p></body></html>"))
        self.label_20.setText(_translate("Dialog", "cr:"))
        self.label_22.setText(_translate("Dialog", "Design parameters:"))
        self.label_41.setToolTip(_translate("Dialog", "<html><head/><body><p>Ball Number</p></body></html>"))
        self.label_41.setText(_translate("Dialog", "nb:"))
        self.lineEdit_bearing_nb.setPlaceholderText(_translate("Dialog", "9"))
        self.label_43.setToolTip(_translate("Dialog", "<html><head/><body><p>Pitch Diameter</p><p>Unit: m</p></body></html>"))
        self.label_43.setText(_translate("Dialog", "Dp:"))
        self.lineEdit_bearing_Dp.setPlaceholderText(_translate("Dialog", "0.03932"))
        self.label_45.setToolTip(_translate("Dialog", "<html><head/><body><p>Ball Diameter</p><p>Unit: m</p></body></html>"))
        self.label_45.setText(_translate("Dialog", "Db:"))
        self.lineEdit_bearing_Db.setPlaceholderText(_translate("Dialog", "0.00794"))
        self.label_47.setToolTip(_translate("Dialog", "<html><head/><body><p>Ball slip angle</p><p>Unit: rad</p></body></html>"))
        self.label_47.setText(_translate("Dialog", "phi:"))
        self.lineEdit_bearing_phi_slip.setPlaceholderText(_translate("Dialog", "0.01"))
        self.label_49.setToolTip(_translate("Dialog", "<html><head/><body><p>Mutation percetage</p></body></html>"))
        self.label_49.setText(_translate("Dialog", "mut:"))
        self.lineEdit_bearing_mut.setPlaceholderText(_translate("Dialog", "0"))
        self.label_51.setToolTip(_translate("Dialog", "<html><head/><body><p>Ball Stiffness</p><p>Unit: N/m</p></body></html>"))
        self.label_51.setText(_translate("Dialog", "kb:"))
        self.lineEdit_bearing_kb.setPlaceholderText(_translate("Dialog", "18900000000"))
        self.label_53.setToolTip(_translate("Dialog", "<html><head/><body><p>Bearing Clearance</p><p>Unit: m</p></body></html>"))
        self.label_53.setText(_translate("Dialog", "c:"))
        self.lineEdit_bearing_c.setPlaceholderText(_translate("Dialog", "0"))
        self.label_55.setToolTip(_translate("Dialog", "<html><head/><body><p>Contact Angular</p><p>Unit: rad</p></body></html>"))
        self.label_55.setText(_translate("Dialog", "α："))
        self.lineEdit_bearing_alpha.setPlaceholderText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Testbearing()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
