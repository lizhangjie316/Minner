from PyQt5.QtSql import *
import time
def test():
    db = QSqlDatabase.addDatabase('QSQLITE')
    # 设置数据库名称
    db.setDatabaseName('./db/Test2database.db')
    # 判断是否打开
    if not db.open():
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
    return True

if __name__ =="__main__":
    test()