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




class DataGrid(QWidget):
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
        self.query.exec("create table SegResultImage(recordNumber int primary key, ImagePath vchar)")

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

    def closeEvent(self, event):
        # 关闭数据库
        self.db.close()

    # 创建窗口
    def createWindow(self):
        # 操作布局
        operatorLayout = QHBoxLayout()



        # 状态布局
        statusLayout = QHBoxLayout()

        self.totalRecordLabel = QLabel()
        self.totalRecordLabel.setFixedWidth(70)

        statusLayout.addWidget(QSplitter())
        statusLayout.addWidget(self.totalRecordLabel)

        # 设置表格属性
        self.tableView = QTableView()
        # 表格宽度的自适应调整
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setStyleSheet(
            "QHeaderView::section{ background:#005E96;color:white;border: 1px solid rgb(144, 144, 144);}"
            " QTableView{color:white;}")
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)


        # 创建界面

        self.mainLayout = QVBoxLayout(self);
        self.mainLayout.addLayout(operatorLayout);
        self.mainLayout.addWidget(self.tableView);
        self.mainLayout.addLayout(statusLayout);
        self.setLayout(self.mainLayout)

    # 设置表格
    def setTableView(self):

        # 声明查询模型
        self.queryModel = QSqlQueryModel()
        self.queryModel.setQuery(self.query)
        self.queryModelImage=QSqlQueryModel(self)
        self.queryModelImage.setQuery(self.query)
        # 得到总记录数
        self.totalRecrodCount = self.getTotalRecordCount()

        # 刷新状态
        self.updateStatus()

        # 设置总记录数
        self.setTotalRecordLabel()

        # 记录查询
        self.recordQuery(self.totalRecrodCount-self.PageRecordCount)
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
        self.tableView.setColumnWidth(0, 140)
        self.tableView.setColumnWidth(1, 140)
        self.tableView.setColumnWidth(2, 140)
        self.tableView.setColumnWidth(3, 300)
        self.tableView.setColumnWidth(4, 120)
        self.tableView.setColumnWidth(5, 120)
        self.tableView.setColumnWidth(6, 120)
        self.tableView.setColumnWidth(7, 120)
        self.tableView.selectRow(self.totalRecrodCount-1)
    # 得到记录数

    def ShowTable(self):
        self.createTableAndInit()
        self.queryModel = QSqlQueryModel(self)
        self.queryModelImage=QSqlQueryModel(self)
        self.queryModel.setQuery(self.query)
        self.queryModelImage.setQuery(self.query)
        self.totalRecrodCount = self.getTotalRecordCount()

        # 刷新状态
        self.updateStatus()

        # 设置总记录数
        self.setTotalRecordLabel()

        self.tableView.setModel(self.queryModel)
        self.queryModel.setHeaderData(0, Qt.Horizontal, "编号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "摄像ID")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "摄像机点位")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "图片帧时间")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "20+(%)")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "10+(%)")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "5+(%)")
        self.queryModel.setHeaderData(7, Qt.Horizontal, "2+(%)")
        self.tableView.setColumnWidth(0, 140)
        self.tableView.setColumnWidth(1, 140)
        self.tableView.setColumnWidth(2, 140)
        self.tableView.setColumnWidth(3, 300)
        self.tableView.setColumnWidth(4, 120)
        self.tableView.setColumnWidth(5, 120)
        self.tableView.setColumnWidth(6, 120)
        self.tableView.setColumnWidth(7, 120)
        # 记录查询
        self.recordQuery(self.totalRecrodCount - self.PageRecordCount)
        self.tableView.selectRow(self.totalRecrodCount-1)


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
            return (self.totalRecrodCount / self.PageRecordCount + 1)

    # 记录查询
    def recordQuery(self, limitIndex):
        szQuery = ("select * from SegResult limit %d,%d" % (limitIndex, self.PageRecordCount))
        szQueryImage=("select * from SegResultImage limit %d,%d" % (limitIndex, self.PageRecordCount))
        print('query sql=' + szQuery)
        print('query sql=' + szQueryImage)
        self.queryModel.setQuery(szQuery)
        self.queryModelImage.setQuery(szQueryImage)

    # 刷新状态
    def updateStatus(self):
        self.tableView.scrollToBottom()

    # 设置总记录数
    def setTotalRecordLabel(self):
        szTotalRecordText = ("共%d条" % self.totalRecrodCount)
        print('*** setTotalRecordLabel szTotalRecordText=' + szTotalRecordText)
        self.totalRecordLabel.setText(szTotalRecordText)

    def getRowData(self,row):
        data=list()
        for i in range(self.queryModel.columnCount()):
            data.append(self.queryModel.data(self.queryModel.index(row,i)))
            print(data[i])
        data.append(self.queryModelImage.data(self.queryModelImage.index(row,1)))
        return data
import time
def test():
    db1 = QSqlDatabase.addDatabase('QSQLITE')
    # 设置数据库名称
    db1.setDatabaseName('./db/Test2database.db')
    # 判断是否打开
    if not db1.open():
        return False

    # 声明数据库查询对象
    query = QSqlQuery()
    query.exec(
        "create table SegResult(recordNumber int primary key, CameraID vchar, CameraSite vchar,FrameTime datatime ,XL float, L floatl,M float, S float)")
    query.exec("create table SegResultImage(recordNumber int primary key, ImagePath vchar)")
    query.exec("select * from SegResult")
    model=QSqlQueryModel()
    model.setQuery(query)
    recordCount=model.rowCount()+1
    query.exec("insert into SegResult values(%d,%s,%s,%s,%s,%s,%s,%s)" %(1,'\'0\'','\'出矿口1\'','\'2020-06-27 20:57:23\'',10.5,4.5,10.3,10.4))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    query.exec("insert into SegResultImage values(%d,%s)" %(1,"\'results/0.jpg\'"))
    db1.close()
    return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    example = DataGrid()
    # 显示窗口

    example.show()
    test()
    time.sleep(3)
    example.ShowTable()
    sys.exit(app.exec_())
