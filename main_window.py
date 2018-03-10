# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 587)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalSlider_cam_y = QtWidgets.QSlider(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_cam_y.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_cam_y.setSizePolicy(sizePolicy)
        self.horizontalSlider_cam_y.setSizeIncrement(QtCore.QSize(0, 100))
        self.horizontalSlider_cam_y.setBaseSize(QtCore.QSize(0, 100))
        self.horizontalSlider_cam_y.setStyleSheet("Slider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 50px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 50px;\n"
"height: 50px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.horizontalSlider_cam_y.setMaximum(4000)
        self.horizontalSlider_cam_y.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_cam_y.setInvertedAppearance(False)
        self.horizontalSlider_cam_y.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_cam_y.setObjectName("horizontalSlider_cam_y")
        self.verticalLayout_4.addWidget(self.horizontalSlider_cam_y)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(793, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.spinBox_cam_y = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_cam_y.sizePolicy().hasHeightForWidth())
        self.spinBox_cam_y.setSizePolicy(sizePolicy)
        self.spinBox_cam_y.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        self.spinBox_cam_y.setFont(font)
        self.spinBox_cam_y.setObjectName("spinBox_cam_y")
        self.horizontalLayout.addWidget(self.spinBox_cam_y)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalSlider_cam_level_rear_x_low = QtWidgets.QSlider(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_cam_level_rear_x_low.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_cam_level_rear_x_low.setSizePolicy(sizePolicy)
        self.horizontalSlider_cam_level_rear_x_low.setSizeIncrement(QtCore.QSize(0, 100))
        self.horizontalSlider_cam_level_rear_x_low.setBaseSize(QtCore.QSize(0, 100))
        self.horizontalSlider_cam_level_rear_x_low.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 2px solid #999999;\n"
"height: 40px;\n"
"border-radius: 2px;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 12px;\n"
"border-bottom-left-radius: 0px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 18px;\n"
" background-image: url(:/slider-knob.png)\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: yellow;\n"
"foreground: red;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"background: green;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-left-radius: 9px;\n"
"border-bottom-left-radius: 9px;\n"
"}")
        self.horizontalSlider_cam_level_rear_x_low.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_cam_level_rear_x_low.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_cam_level_rear_x_low.setObjectName("horizontalSlider_cam_level_rear_x_low")
        self.verticalLayout.addWidget(self.horizontalSlider_cam_level_rear_x_low)
        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(793, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.spinBox_cam_level_rear_x_low = QtWidgets.QSpinBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_cam_level_rear_x_low.sizePolicy().hasHeightForWidth())
        self.spinBox_cam_level_rear_x_low.setSizePolicy(sizePolicy)
        self.spinBox_cam_level_rear_x_low.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        self.spinBox_cam_level_rear_x_low.setFont(font)
        self.spinBox_cam_level_rear_x_low.setObjectName("spinBox_cam_level_rear_x_low")
        self.horizontalLayout_2.addWidget(self.spinBox_cam_level_rear_x_low)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalSlider_cam_level_rear_x_high = QtWidgets.QSlider(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_cam_level_rear_x_high.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_cam_level_rear_x_high.setSizePolicy(sizePolicy)
        self.horizontalSlider_cam_level_rear_x_high.setSizeIncrement(QtCore.QSize(0, 100))
        self.horizontalSlider_cam_level_rear_x_high.setBaseSize(QtCore.QSize(0, 100))
        self.horizontalSlider_cam_level_rear_x_high.setStyleSheet("QSlider::groove:vertical {\n"
"    background: red;\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 4px; right: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: pink;\n"
"}")
        self.horizontalSlider_cam_level_rear_x_high.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_cam_level_rear_x_high.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_cam_level_rear_x_high.setObjectName("horizontalSlider_cam_level_rear_x_high")
        self.verticalLayout_5.addWidget(self.horizontalSlider_cam_level_rear_x_high)
        self.widget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.spinBox_cam_level_rear_x_high = QtWidgets.QSpinBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_cam_level_rear_x_high.sizePolicy().hasHeightForWidth())
        self.spinBox_cam_level_rear_x_high.setSizePolicy(sizePolicy)
        self.spinBox_cam_level_rear_x_high.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.spinBox_cam_level_rear_x_high.setFont(font)
        self.spinBox_cam_level_rear_x_high.setObjectName("spinBox_cam_level_rear_x_high")
        self.horizontalLayout_3.addWidget(self.spinBox_cam_level_rear_x_high)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 402, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider_cam_level_rear_x_high.valueChanged['int'].connect(self.spinBox_cam_level_rear_x_high.setValue)
        self.horizontalSlider_cam_level_rear_x_low.valueChanged['int'].connect(self.spinBox_cam_level_rear_x_low.setValue)
        self.horizontalSlider_cam_y.valueChanged['int'].connect(self.spinBox_cam_y.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Camera Position"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Rear Y"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Rear X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

