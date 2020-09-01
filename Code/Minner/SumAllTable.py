'''

分页显示数据

limit n,m

limit 10,20


'''

import sys
import re
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *




class DataGridAll(QWidget):
    def createTableAndInit(self):
        # 添加数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # 设置数据库名称
        self.db.setDatabaseName('./db/Test1database.db')
        # 判断是否打开
        if not self.db.open():
            return False

        # 声明数据库查询对象
        self.query = QSqlQuery()
        # 创建表
        self.query.exec("create table SegResult(recordNumber int primary key, CameraID vchar, CameraSite vchar,FrameTime datatime ,XL float, L floatl,M float, S float)")

        return True

    def __init__(self):
        super().__init__()
        self.setWindowTitle("分页查询例子")
        self.resize(750, 300)
        self.createTableAndInit()

        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecrodCount = 0
        # 每页显示记录数
        self.PageRecordCount = 10

        self.initUI()

    def initUI(self):
        # 创建窗口
        self.createWindow()
        # 设置表格
        self.setTableView()

        # 信号槽连接
        self.prevButton.clicked.connect(self.onPrevButtonClick)
        self.nextButton.clicked.connect(self.onNextButtonClick)
        self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick)

    def closeEvent(self, event):
        # 关闭数据库
        self.db.close()

    # 创建窗口
    def createWindow(self):
        # 操作布局
        operatorLayout = QHBoxLayout()
        self.prevButton = QPushButton("前一页")
        self.nextButton = QPushButton("后一页")
        self.switchPageButton = QPushButton("Go")
        self.switchPageLineEdit = QLineEdit()
        self.switchPageLineEdit.setFixedWidth(40)

        switchPage = QLabel("转到第")
        page = QLabel("页")
        operatorLayout.addWidget(self.prevButton)
        operatorLayout.addWidget(self.nextButton)
        operatorLayout.addWidget(switchPage)
        operatorLayout.addWidget(self.switchPageLineEdit)
        operatorLayout.addWidget(page)
        operatorLayout.addWidget(self.switchPageButton)
        operatorLayout.addWidget(QSplitter())

        # 状态布局
        statusLayout = QHBoxLayout()
        self.totalPageLabel = QLabel()
        self.totalPageLabel.setFixedWidth(70)
        self.currentPageLabel = QLabel()
        self.currentPageLabel.setFixedWidth(70)

        self.totalRecordLabel = QLabel()
        self.totalRecordLabel.setFixedWidth(70)

        statusLayout.addWidget(self.totalPageLabel)
        statusLayout.addWidget(self.currentPageLabel)
        statusLayout.addWidget(QSplitter())
        statusLayout.addWidget(self.totalRecordLabel)

        # 设置表格属性
        self.tableView = QTableView()
        # 表格宽度的自适应调整
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setStyleSheet(
            "QHeaderView::section{ background:#005E96;color:white;border: 1px solid rgb(144, 144, 144);}"
            " QTableView{color:white;}")
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        # 创建界面
        mainLayout = QVBoxLayout(self);
        mainLayout.addWidget(self.tableView);
        mainLayout.addLayout(statusLayout);
        mainLayout.addLayout(operatorLayout);
        self.setLayout(mainLayout)


    # 设置表格
    def setTableView(self):

        # 声明查询模型
        self.queryModel = QSqlQueryModel(self)
        self.queryModel.setQuery(self.query)
        # 设置当前页
        self.currentPage = 1;
        # 得到总记录数
        self.totalRecrodCount = self.getTotalRecordCount()
        # 得到总页数
        self.totalPage = self.getPageCount()
        # 刷新状态
        self.updateStatus()
        # 设置总页数文本
        self.setTotalPageLabel()
        # 设置总记录数
        self.setTotalRecordLabel()

        # 记录查询
        self.recordQuery(0)
        # 设置模型
        self.tableView.setModel(self.queryModel)

        print('totalRecrodCount=' + str(self.totalRecrodCount))
        print('totalPage=' + str(self.totalPage))

        # 设置表格表头
        self.queryModel.setHeaderData(0, Qt.Horizontal, "编号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "摄像ID")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "摄像机点位")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "图片帧时间")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "20+(%)")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "10+(%)")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "5+(%)")
        self.queryModel.setHeaderData(7, Qt.Horizontal, "2+(%)")

        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 100)
        self.tableView.setColumnWidth(2, 100)
        self.tableView.setColumnWidth(3, 200)
        self.tableView.setColumnWidth(4, 70)
        self.tableView.setColumnWidth(5, 70)
        self.tableView.setColumnWidth(6, 70)
        self.tableView.setColumnWidth(7, 70)

    # 得到记录数
    def getTotalRecordCount(self):
        self.queryModel.setQuery("select * from SegResult")
        rowCount = self.queryModel.rowCount()
        print('rowCount=' + str(rowCount))
        return rowCount

    # 得到页数
    def getPageCount(self):
        if self.totalRecrodCount % self.PageRecordCount == 0:
            return (self.totalRecrodCount / self.PageRecordCount)
        else:
            return (int(self.totalRecrodCount / self.PageRecordCount) + 1)

    # 记录查询
    def recordQuery(self, limitIndex):
        szQuery = ("select * from SegResult limit %d,%d" % (limitIndex, self.PageRecordCount))
        print('query sql=' + szQuery)
        self.queryModel.setQuery(szQuery)

    # 刷新状态
    def updateStatus(self):
        szCurrentText = ("当前第%d页" % self.currentPage)
        self.currentPageLabel.setText(szCurrentText)

        # 设置按钮是否可用
        self.prevButton.setEnabled(True)
        self.nextButton.setEnabled(True)
        if self.currentPage == 1:
            self.prevButton.setEnabled(False)
        if self.currentPage >= self.totalPage:
            self.nextButton.setEnabled(False)


    # 设置总数页文本
    def setTotalPageLabel(self):
        szPageCountText = ("总共%d页" % self.totalPage)
        self.totalPageLabel.setText(szPageCountText)

    # 设置总记录数
    def setTotalRecordLabel(self):
        szTotalRecordText = ("共%d条" % self.totalRecrodCount)
        print('*** setTotalRecordLabel szTotalRecordText=' + szTotalRecordText)
        self.totalRecordLabel.setText(szTotalRecordText)

    # 前一页按钮按下
    def onPrevButtonClick(self):
        print('*** onPrevButtonClick ');
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage -= 1
        self.updateStatus()

    # 后一页按钮按下
    def onNextButtonClick(self):
        print('*** onNextButtonClick ');
        limitIndex = self.currentPage * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    # 转到页按钮按下
    def onSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.switchPageLineEdit.text()


        # 得到页数
        pageIndex = int(szText)
        # 判断是否有指定页
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面,请重新输入")
            return

        # 得到查询起始行号
        limitIndex = (pageIndex - 1) * self.PageRecordCount

        # 记录查询
        self.recordQuery(limitIndex);
        # 设置当前页
        self.currentPage = pageIndex
        # 刷新状态
        self.updateStatus();


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    example = DataGridAll()
    # 显示窗口
    example.show()
    sys.exit(app.exec_())
