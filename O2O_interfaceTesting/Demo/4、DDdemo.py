#coding=utf-8
from opention import createOrder
from opention import orderUpdateState
import re

# 准备测试数据
commodityDict = {
    "1289396":5,
}
data=createOrder.createTestOrder(commodityDict=commodityDict).DDorder()
print data
pattern=r'("message":"(\d{8})",)'
serialNumber = str(re.search(pattern,data).group(2))

print orderUpdateState.changeOrderState(serialNumber,"9")
print orderUpdateState.changeOrderState(serialNumber,"10")
print orderUpdateState.changeOrderState(serialNumber,"4")
print orderUpdateState.changeOrderState(serialNumber,"5")
print orderUpdateState.changeOrderState(serialNumber,"6")