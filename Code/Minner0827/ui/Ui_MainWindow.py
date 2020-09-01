# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# from ResultTableView import DataGrid
# from VideoDisplay import Display
# from Camera import Camera
# from Video1 import *
# from Video4 import *
# from InfoWindow import Info_Dialog
# from SumDialog import Sum_Dialog
import cv2
import sip

from ResultTableView import DataGrid
from ui.InfoWindow import Info_Dialog
from ui.Video1 import Ui_VideoWidget1
from ui.Video4 import Ui_VideoWidget4
from utils.video.Camera import Camera
from utils.video.VideoDisplay import Display


class Ui_MainWindow(QtCore.QObject):
    addedSignalLocation = QtCore.pyqtSignal(Camera)
    CameraDict = dict()
    deviceUrlDict=dict()
    cameraViewDict = dict()
    CheckedNumber = 0
    cameraNum = 0
    MaxShowCamera = 1
    player = Display()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 960)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../icon/1x/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(" QWidget{\n"
"    background:#333333;\n"
"  }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(" QWidget{\n"
"    background:#333333;\n"
"  }")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1260, 720))
        self.tabWidget.setMaximumSize(QtCore.QSize(1659, 948))
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"background-color:#666666;\n"
"}\n"
"QTabWidget::pane{\n"
"\n"
"border-top: 1px solid;\n"
"\n"
"border-color: #333333;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"min-width:100px;\n"
"\n"
"min-height:30px;\n"
"\n"
"color: white;\n"
"background:#666666;\n"
"\n"
"border: 0px solid;\n"
"\n"
" \n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"\n"
"min-width:100px;\n"
"\n"
"min-height:30px;\n"
"\n"
"color: white;\n"
"background:#009DE2;\n"
"\n"
"border: 0px solid;\n"
"\n"
"border-bottom: 2px solid;\n"
"\n"
"}\n"
"QTabBar::close-button {\n"
"\n"
"image: url(../../icon/1x/closeN.png)\n"
"\n"
"}\n"
"QTabBar::close-button:hover {\n"
"\n"
"image: url(../../icon/1x/closeC.png)\n"
"\n"
"}")
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.HomeTab = QtWidgets.QWidget()
        self.HomeTab.setEnabled(True)
        self.HomeTab.setStyleSheet("QTabBar::tab {\n"
" image: url(../../icon/1x/home.png)\n"
"}\n"
"")
        self.HomeTab.setObjectName("HomeTab")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../icon/1x/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.HomeTab, icon1, "")
        self.tabWidget.tabBar().setTabButton(0, QtWidgets.QTabBar.RightSide, None)
        self.realtimeVideoTab = QtWidgets.QWidget()
        self.realtimeVideoTab.setObjectName("realtimeVideoTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.realtimeVideoTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.realtimeWidget = QtWidgets.QWidget(self.realtimeVideoTab)
        self.realtimeWidget.setStyleSheet(" QWidget{\n"
"    background:#333333;\n"
"  }")
        self.realtimeWidget.setObjectName("realtimeWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.realtimeWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.bottomRightWidget = QtWidgets.QWidget(self.realtimeWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.bottomRightWidget.sizePolicy().hasHeightForWidth())
        self.bottomRightWidget.setSizePolicy(sizePolicy)
        self.bottomRightWidget.setStyleSheet(" QWidget{\n"
"    background:#555555;\n"
"  }\n"
"")
        self.bottomRightWidget.setObjectName("bottomRightWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottomRightWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dataGrid=DataGrid()
        self.dataGrid.tableView.doubleClicked.connect(self.showDetailDialog)
        self.player.FiniSignal().connect(self.dataGrid.ShowTable)
        self.verticalLayout_2.addWidget(self.dataGrid)
        self.widget_sum = QtWidgets.QWidget(self.bottomRightWidget)
        self.widget_sum.setMinimumSize(QtCore.QSize(100, 40))
        self.widget_sum.setObjectName("widget_sum")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_sum)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(1154, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sumButton = QtWidgets.QPushButton(self.widget_sum)
        self.sumButton.setStyleSheet("QPushButton{\n"
"           border:none;\n"
"          background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 rgb(96,157,200),stop:1 rgb(0,94,150));\n"
"          font-size:15px;\n"
"            color:white;\n"
"            width:120px;\n"
"            height:40px;\n"
"            text-align:center;\n"
"            border-radius:5px;\n"
"        }\n"
"QPushButton:hover{\n"
"            color:#0caaff\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 88, 138)\n"
"}\n"
"QPushButton:disabled{\n"
"color:rgb(172, 172, 172);\n"
"background-color:rgb(93, 93, 93)\n"
"}")
        self.sumButton.setObjectName("sumButton")
        self.sumButton.clicked.connect(self.showSumDialog)
        self.horizontalLayout.addWidget(self.sumButton)
        self.verticalLayout_2.addWidget(self.widget_sum)
        self.gridLayout.addWidget(self.bottomRightWidget, 1, 1, 1, 1)
        self.widget_video = QtWidgets.QWidget(self.realtimeWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_video.sizePolicy().hasHeightForWidth())
        self.widget_video.setSizePolicy(sizePolicy)
        self.widget_video.setStyleSheet("")
        self.widget_video.setObjectName("widget_video")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_video)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_videoAreaTitle = QtWidgets.QLabel(self.widget_video)
        self.label_videoAreaTitle.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_videoAreaTitle.setStyleSheet(" QLabel{\n"
"    border:none;\n"
"    font-size:16px;\n"
"    font-weight:400;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #777777,stop:1 #000000);\n"
"    color:white;\n"
"  }")
        self.label_videoAreaTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_videoAreaTitle.setObjectName("label_videoAreaTitle")
        self.verticalLayout_3.addWidget(self.label_videoAreaTitle)
        self.widget_videoArea = QtWidgets.QWidget(self.widget_video)
        self.widget_videoArea.setStyleSheet(" QWidget{\n"
"    background:#000000;\n"
"  }\n"
"")
        self.widget_videoArea.setObjectName("widget_videoArea")
        self.verticalLayout_3.addWidget(self.widget_videoArea)
        self.widget_controlGroup = QtWidgets.QWidget(self.widget_video)
        self.widget_controlGroup.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_controlGroup.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_controlGroup.setStyleSheet(" QWidget{\n"
"    background:#555555;\n"
"  }\n"
"")
        self.widget_controlGroup.setObjectName("widget_controlGroup")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_controlGroup)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(0, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.radioButton = QtWidgets.QRadioButton(self.widget_controlGroup)
        self.radioButton.setMinimumSize(QtCore.QSize(40, 30))
        self.radioButton.setStyleSheet("QRadioButton::indicator{\n"
"    width: 40px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(../../icon/1x/one40.png);}\n"
"QRadioButton::indicator::checked {\n"
"    image: url(../../icon/1x/one40C.png);}")
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.changeVideoNumberSlot1)
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_controlGroup)
        self.radioButton_2.setMinimumSize(QtCore.QSize(40, 30))
        self.radioButton_2.setStyleSheet("QRadioButton::indicator{\n"
"    width: 40px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(../../icon/1x/two40.png);}\n"
"QRadioButton::indicator::checked {\n"
"    image: url(../../icon/1x/two40C.png);}")
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget_controlGroup)
        self.radioButton_3.setMinimumSize(QtCore.QSize(40, 30))
        self.radioButton_3.setStyleSheet("QRadioButton::indicator{\n"
"    width: 40px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(../../icon/1x/four40.png);}\n"
"QRadioButton::indicator::checked {\n"
"    image: url(../../icon/1x/four40C.png);}")
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton.toggled.connect(self.changeVideoNumberSlot4)
        self.horizontalLayout_4.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget_controlGroup)
        self.radioButton_4.setMinimumSize(QtCore.QSize(40, 30))
        self.radioButton_4.setStyleSheet("QRadioButton::indicator{\n"
"    width: 40px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(../../icon/1x/six40.png);}\n"
"QRadioButton::indicator::checked {\n"
"    image: url(../../icon/1x/six40C.png);}")
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_4.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget_controlGroup)
        self.radioButton_5.setMinimumSize(QtCore.QSize(40, 30))
        self.radioButton_5.setStyleSheet("QRadioButton::indicator{\n"
"    width: 40px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(../../icon/1x/nine40.png);}\n"
"QRadioButton::indicator::checked {\n"
"    image: url(../../icon/1x/nine40C.png);}")
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_4.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget_controlGroup)
        self.radioButton_6.setMinimumSize(QtCore.QSize(40, 30))
        self.radioButton_6.setStyleSheet("QRadioButton::indicator{\n"
"    width: 40px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(../../icon/1x/sixteen40.png);}\n"
"QRadioButton::indicator::checked {\n"
"    image: url(../../icon/1x/sixteen40C.png);}")
        self.radioButton_6.setText("")
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_4.addWidget(self.radioButton_6)
        self.verticalLayout_3.addWidget(self.widget_controlGroup)
        self.gridLayout.addWidget(self.widget_video, 0, 1, 1, 1)
        self.widget_Left = QtWidgets.QWidget(self.realtimeWidget)
        self.widget_Left.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_Left.setStyleSheet(" QWidget{\n"
"    background:#555555;\n"
"  }")
        self.widget_Left.setObjectName("widget_Left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_Left)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_camTree = QtWidgets.QLabel(self.widget_Left)
        self.label_camTree.setMinimumSize(QtCore.QSize(0, 30))
        self.label_camTree.setStyleSheet(" QLabel{\n"
"    border:none;\n"
"    font-size:16px;\n"
"    font-weight:400;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #777777,stop:1 #000000);\n"
"    color:white;\n"
"  }")
        self.label_camTree.setAlignment(QtCore.Qt.AlignCenter)
        self.label_camTree.setObjectName("label_camTree")
        self.verticalLayout.addWidget(self.label_camTree)
        self.widget_search = QtWidgets.QWidget(self.widget_Left)
        self.widget_search.setObjectName("widget_search")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_search)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchContext = QtWidgets.QLineEdit(self.widget_search)
        self.searchContext.setMinimumSize(QtCore.QSize(0, 30))
        self.searchContext.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    color:white;\n"
"    background:#444444;\n"
"}")
        self.searchContext.setObjectName("searchContext")
        self.horizontalLayout_3.addWidget(self.searchContext)
        self.searchButton = QtWidgets.QToolButton(self.widget_search)
        self.searchButton.setMinimumSize(QtCore.QSize(30, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../icon/1x/search16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon2)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_3.addWidget(self.searchButton)
        self.verticalLayout.addWidget(self.widget_search)
        self.camTreeWidget = QtWidgets.QTreeWidget(self.widget_Left)
        self.camTreeWidget.setStyleSheet("QTreeView::item:hover{background-color:#888888}\n"
"\n"
"QTreeView::item:selected{background-color:#005E96}\n"
"")
        self.camTreeWidget.setRootIsDecorated(True)
        self.camTreeWidget.setObjectName("camTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.camTreeWidget)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../icon/1x/rootfold16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_1.setForeground(0, brush)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../icon/1x/fold16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon4)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_1.setForeground(0, brush)
        item_1.setIcon(0, icon4)
        self.camTreeWidget.header().setVisible(False)
        self.camTreeWidget.header().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.camTreeWidget)
        self.gridLayout.addWidget(self.widget_Left, 0, 0, 2, 1)
        self.gridLayout_2.addWidget(self.realtimeWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.realtimeVideoTab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        for i in self.widget_videoArea.children():
                print(i.objectName())
                i.deleteLater()
        print("1")
        self.video1 = Ui_VideoWidget1()
        self.video4 = Ui_VideoWidget4()
        self.video1.setupUi(self.widget_videoArea)
        self.addedSignalLocation.connect(self.addCameraOnline)
        self.currentVideo=self.video1
        self.player.init(self.widget_videoArea.findChild(QtWidgets.QWidget).findChildren(QtWidgets.QLabel))
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.radioButton_2.setDisabled(True)
        self.radioButton_3.setDisabled(True)
        self.radioButton_4.setDisabled(True)
        self.radioButton_5.setDisabled(True)
        self.radioButton_6.setDisabled(True)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def closeEvent(self, event):
        self.player.CloseAll()
        event.accept()

    def addCameraOnline(self,camera):
        onlineCameras = self.camTreeWidget.topLevelItem(0).child(0)
        newChildCamera = QtWidgets.QTreeWidgetItem(onlineCameras)
        newChildCamera.setText(0,camera.GetLocation())
        newChildCamera.setCheckState(0, QtCore.Qt.Unchecked)

    def addCameraOffline(self,camera):
        offlineCameras = self.camTreeWidget.topLevelItem(0).child(1)
        newChildCamera = QtWidgets.QTreeWidgetItem(offlineCameras)
        newChildCamera.setText(0,camera.GetLocation())

    def handleChanged(self, item, column):
        # 当check状态改变时得到他的状态。
        if item.checkState(column) == QtCore.Qt.Checked:
            self.CheckedNumber = self.GetTreeCheckedNumber()
            if not self.CheckedNumber < self.MaxShowCamera:
                self.SetTreeUnCheckable()
            self.player.Open(self.GetCameraById(self.GetCameraIdByLocation(item.text(0))),
                             self.GetCameraIdByLocation(item.text(0)))
        elif item.checkState(column) == QtCore.Qt.Unchecked:
            if not self.CheckedNumber < self.MaxShowCamera:
                self.CheckedNumber = self.GetTreeCheckedNumber()
                if not self.CheckedNumber < self.MaxShowCamera:
                    item.setData(0,QtCore.Qt.CheckStateRole,QtCore.QVariant())
                else :
                    self.SetTreeCheckable()
            ID = self.player.GetLabelIndexByID(self.GetCameraIdByLocation(item.text(0)))
            if not ID==-1:
                self.player.Close(ID)
    def GetTreeCheckedNumber(self):
        onlineCameras = self.camTreeWidget.topLevelItem(0).child(0)
        number = 0
        for index in range(onlineCameras.childCount()) :
            if onlineCameras.child(index).checkState(0)== QtCore.Qt.Checked :
                    number+=1
        return number

    def SetTreeUnCheckable(self):
        onlineCameras = self.camTreeWidget.topLevelItem(0).child(0)
        for index in range(onlineCameras.childCount()) :
            if onlineCameras.child(index).checkState(0)== QtCore.Qt.Unchecked:
                onlineCameras.child(index).setData(0,QtCore.Qt.CheckStateRole,QtCore.QVariant())

    def SetTreeCheckable(self):
        onlineCameras = self.camTreeWidget.topLevelItem(0).child(0)
        for index in range(onlineCameras.childCount()) :
            if not onlineCameras.child(index).checkState(0)== QtCore.Qt.Checked:
                onlineCameras.child(index).setCheckState(0, QtCore.Qt.Unchecked)

    def InitTreeItem(self):
        onlineCameras = self.camTreeWidget.topLevelItem(0).child(0)
        for index in range(onlineCameras.childCount()):
            onlineCameras.child(index).setCheckState(0, QtCore.Qt.Unchecked)

    def changeVideoNumberSlot1(self):
            if self.radioButton.isChecked():
                self.InitTreeItem()
                for i in self.widget_videoArea.children():
                        print(i.objectName())
                        i.deleteLater()
                        sip.delete(i)
                self.video1.setupUi(self.widget_videoArea)
                self.currentVideo = self.video1
                self.widget_videoArea.update()
                # self.horizontalLayout_10.addWidget(self.video1)
                self.player.init(self.widget_videoArea.findChild(QtWidgets.QWidget).findChildren(QtWidgets.QLabel))
                self.MaxShowCamera=1
                print("aha")

    def changeVideoNumberSlot4(self):
            if self.radioButton_3.isChecked():
                self.InitTreeItem()
                for i in self.widget_videoArea.children():
                        print(i.objectName())
                        i.deleteLater()
                        sip.delete(i)
                self.video4.setupUi(self.widget_videoArea)
                self.currentVideo = self.video4
                self.widget_videoArea.update()
                # self.horizontalLayout_10.addWidget(self.video4)
                # self.horizontalLayout_10
                self.player.init(self.widget_videoArea.findChild(QtWidgets.QWidget).findChildren(QtWidgets.QLabel))
                self.MaxShowCamera = 4

    def GetCurrentView(self):
        if self.MaxShowCamera==1:
             return self.video1
        elif self.MaxShowCamera==4:
             return self.video4

    def AddCamera(self, camera):
            self.CameraDict[str(len(self.CameraDict.keys()))] = camera
            self.addedSignalLocation.emit(camera)

    def GetCameraById(self, id):
            return self.CameraDict[id]

    def GetCameraIdByLocation(self, location):
            for k, v in self.CameraDict.items():
                    if v.GetLocation() == location:
                            return k;
    def showDialog(self):
        self.dialog = QtWidgets.QDialog()
        self.infordialog = Info_Dialog()
        self.infordialog.setupUi(self.dialog)
        self.infordialog.prev_Button.clicked.connect(self.PrevDetailDialog)
        self.infordialog.next_Button.clicked.connect(self.NextDetailDialog)
        self.SetDialog()
        self.dialog.show()

    def SetDialog(self):
        self.data = self.dataGrid.getRowData(self.row)
        self.infordialog.retranslateUi(self.dialog,self.data)
        if self.row <= 0:
            self.infordialog.SetPrevButtonDisable(True)
        else:
            self.infordialog.SetPrevButtonDisable(False)

        if self.row >= self.dataGrid.totalRecrodCount-1:
            self.infordialog.SetNextButtonDisable(True)
        else:
            self.infordialog.SetNextButtonDisable(False)

    def showDetailDialog(self,index):
        self.row=index.row()
        print(str(self.row)+"rownumber")
        self.showDialog()

    def PrevDetailDialog(self):
        self.row=self.row-1
        print(str(self.row)+"rownumber")
        self.SetDialog()
        self.dialog.update()

    def NextDetailDialog(self):
        self.row=self.row+1
        print(str(self.row)+"rownumber")
        self.SetDialog()

    def showSumDialog(self):
        self.sdialog=QtWidgets.QDialog()
        self.sumdialog=Sum_Dialog()
        self.sumdialog.setupUi(self.sdialog)
        self.sdialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "矿石视觉分析平台"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HomeTab), _translate("MainWindow", "首页"))
        self.sumButton.setText(_translate("MainWindow", "结果统计"))
        self.label_videoAreaTitle.setText(_translate("MainWindow", "视频播放"))
        self.label_camTree.setText(_translate("MainWindow", "设备列表"))
        self.searchContext.setPlaceholderText(_translate("MainWindow", "请输入查询名称"))
        self.searchButton.setText(_translate("MainWindow", "0"))
        self.camTreeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        __sortingEnabled = self.camTreeWidget.isSortingEnabled()
        self.camTreeWidget.setSortingEnabled(False)
        self.camTreeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "监控设备"))
        self.camTreeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "在线"))
        self.camTreeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "离线"))
        self.camTreeWidget.itemChanged.connect(self.handleChanged)
        self.camTreeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.realtimeVideoTab), _translate("MainWindow", "实时视频"))


