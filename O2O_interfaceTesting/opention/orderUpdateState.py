#coding=utf-8

import requests

from Base import sqlServerDatabase
MSSQL = sqlServerDatabase.MSSQL
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


# 查询订单的渠道和店铺编码
def orderSql(sql):
    try:
        ms = MSSQL(host="172.17.7.181", user="ygtest", pwd="ygtest", db="YGPS_O2O")
        resList = ms.ExecQuery(sql)
    except:
        data = {"code":"101","msg":u"数据库连接或查询失败"}
        return data
    if len(resList) == 1:
        data = {"code":"1","msg":u"查询到的该订单的数据量为一条","data": resList}
    elif len(resList) == 0:
        data = {"code":"0","msg":u"没有查询到该订单的信息"}
    else:
        data = {"code":"2","msg":u"查询到的该订单的数据量有多条","data": resList}
    return data

class orderState:
    def __init__(self, SerialNumber):
        self.SerialNumber = SerialNumber


    def toOrderState(self, argument):
        '''
        调度方法，我也看不懂
        '''
        """Dispatch method"""
        # prefix the method_name with 'number_' because method names
        # cannot begin with an integer.
        method_name = 'orderState' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "nothing")
        # Call the method as we return it
        return method()

    # 订单状态变更为4
    def orderState4(self):
        '''将订单状态变更为配送中'''
        querystring = r'request={"ChannelName":null,"ChannelCode":"1100000043","SerialNumber":"57877150","OrderState":4,"SellerCode":null,"StoreCode":"20000022","PayStatus":0,"RefundReason":null,"FailReason":null,"Content":"{\"DiliverymanName\":\"DiliverymanName\",\"DiliverymanMobile\":\"13917251653\",\"MailNo\":null,\"OperateDetail\":null,\"CompanyName\":null}","CancelType":""}'
        sql ="SELECT ChannelCode,StoreCode FROM dbo.Fct_Order	WHERE SerialNumber = '" + self.SerialNumber + "';"
        order = orderSql(sql)
        querystring = querystring.replace("57877150",self.SerialNumber)
        querystring = querystring.replace("1100000043",order["data"][0][0])
        querystring = querystring.replace("20000022",order["data"][0][1])
        return querystring


    # 订单状态变更为5
    def orderState5(self):
        '''将订单状态变更为已送达'''
        querystring = r'request={"ChannelName":null,"ChannelCode":"1100000043","SerialNumber":"57877150","OrderState":5,"SellerCode":null,"StoreCode":"20000022","PayStatus":0,"RefundReason":null,"FailReason":null,"Content":null,"CancelType":""}'
        sql = "SELECT ChannelCode,StoreCode FROM dbo.Fct_Order	WHERE SerialNumber='"+ self.SerialNumber +"';"
        order= orderSql(sql)
        querystring = querystring.replace("57877150",self.SerialNumber)
        querystring = querystring.replace("1100000043",order["data"][0][0])
        querystring = querystring.replace("20000022",order["data"][0][1])
        return querystring

    def orderState6(self):
        '''将订单状态变更为已完成'''
        querystring = r'request={"ChannelName":null,"ChannelCode":"1100000043","SerialNumber":"57877150","OrderStatus":6,"SellerCode":null,"StoreCode":"20000022","PayStatus":2,"RefundReason":null,"FailReason":null,"Content":null,"CancelType":null}'
        sql = "SELECT ChannelCode,StoreCode FROM dbo.Fct_Order	WHERE SerialNumber='"+ self.SerialNumber +"';"
        order= orderSql(sql)
        querystring = querystring.replace("57877150",self.SerialNumber)
        querystring = querystring.replace("1100000043",order["data"][0][0])
        querystring = querystring.replace("20000022",order["data"][0][1])
        return querystring

    def orderState7(self):
        '''将订单状态变更为已完成'''
        querystring = r'request={"ChannelName":null,"ChannelCode":"1100000043","SerialNumber":"57877150","OrderStatus":7,"SellerCode":null,"StoreCode":"20000022","PayStatus":2,"RefundReason":null,"FailReason":null,"Content":null,"CancelType":null}'
        sql = "SELECT ChannelCode,StoreCode FROM dbo.Fct_Order	WHERE SerialNumber='"+ self.SerialNumber +"';"
        order= orderSql(sql)
        querystring = querystring.replace("57877150",self.SerialNumber)
        querystring = querystring.replace("1100000043",order["data"][0][0])
        querystring = querystring.replace("20000022",order["data"][0][1])
        return querystring

    # 订单状态变更为9
    def orderState9(self):
        '''将订单状态变更为复核完成'''

        sql = "SELECT OutItemCode,CommodityCode,CommodityName,Amount FROM dbo.Rel_OrderDetail WHERE OrderId=(SELECT OrderId FROM dbo.Fct_Order WHERE SerialNumber='"+ self.SerialNumber +"');"
        strContent = r'{\"MainCommodityCode\":\"1303731\",\"CommodityCode\":\"1303750\",\"CommodityName\":\"commodityName\",\"OrderCommodityQty\":OrderCommodityQtyNum,\"ActualQty\":ActualQtyNum },'
        nunContent =''

        for order_each in orderSql(sql)["data"]:
            strContent = strContent.replace("1303731",str(order_each[0]))
            strContent = strContent.replace("1303750",str(order_each[1]))
            strContent = strContent.replace("commodityName",str(order_each[2]))
            print
            strContent = strContent.replace("OrderCommodityQtyNum" ,str(order_each[3]).split(".")[0])
            strContent = strContent.replace("ActualQtyNum",(str(order_each[3])).split(".")[0])
            nunContent = nunContent + strContent
        querystring = r'request={"ChannelName":null,"ChannelCode":"1100000043","SerialNumber":"57877150","OrderState":9,"SellerCode":null,"StoreCode":20000022,"PayStatus":0,"RefundReason":null,"FailReason":null,"Content":"['+ strContent +']","CancelType":""}'
        sql = "SELECT ChannelCode,StoreCode FROM dbo.Fct_Order	WHERE SerialNumber='"+ self.SerialNumber +"';"
        order = orderSql(sql)
        querystring = querystring.replace("57877150",self.SerialNumber)
        querystring = querystring.replace("1100000043",order["data"][0][0])
        querystring = querystring.replace("20000022",order["data"][0][1])

        return querystring

    def orderState10(self):
        '''将订单状态变更为配送中'''
        querystring = r'request={"ChannelName":"null","ChannelCode":null,"SerialNumber":"57877150","OrderState":10,"SellerCode":null,"StoreCode":"20000022","PayStatus":2,"RefundReason":null,"FailReason":null,"Content":null,"CancelType":null}'
        sql = "SELECT ChannelCode,StoreCode FROM dbo.Fct_Order	WHERE SerialNumber='"+ self.SerialNumber +"';"
        order= orderSql(sql)
        querystring = querystring.replace("57877150",self.SerialNumber)
        querystring = querystring.replace("1100000043",order["data"][0][0])
        querystring = querystring.replace("20000022",order["data"][0][1])
        return querystring




def changeOrderState(serialNumber, State):
    """
    :param serialNumber: 需要更改的订单流水号
    :param State: 需要变更的订单状态
    :return:
    """
    data = orderState(serialNumber).toOrderState(State).encode("UTF-8")
    print data
    if str(State) != "6":
        r = requests.get("http://172.17.7.208:10111/YGPS.O2O.Server.Order.UpdateState", params=data)
    else:
        r = requests.get("http://172.17.7.208:10111/YGPS.O2O.Server.Order.UpdateStatus", params=data)
    #TODO 增加对结果的校验
    return r


if __name__ == "__main__":
    print changeOrderState("33758375","9").content


