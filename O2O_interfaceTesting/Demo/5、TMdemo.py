#coding=utf-8
from opention import createOrder
from opention import orderUpdateState
from Base import sqlServerDatabase
import time
MSSQL = sqlServerDatabase.MSSQL
# 准备测试数据
commodityDict = {
    "554781483658":5,
}
data=createOrder.createTestOrder(commodityDict=commodityDict).TMSDorder()
print data
partnerOrderCode = data["data"]["tid"]
print partnerOrderCode
time.sleep(3)
ms = MSSQL(host="172.17.7.181", user="ygtest", pwd="ygtest", db="YGPS_O2O")
sql = "SELECT SerialNumber FROM dbo.Fct_Order WHERE PartnerOrderCode='" + partnerOrderCode + "';"
SerialNumber = str(ms.ExecQuery(sql)[0][0])
print ms.ExecQuery(sql)
print SerialNumber



print 9,orderUpdateState.changeOrderState(SerialNumber,"9")
print 10,orderUpdateState.changeOrderState(SerialNumber,"10")
print 11,orderUpdateState.changeOrderState(SerialNumber,"4")
print 12,orderUpdateState.changeOrderState(SerialNumber,"5")
print 13,orderUpdateState.changeOrderState(SerialNumber,"6")