#coding=utf-8
import sys

import requests

reload(sys)
sys.setdefaultencoding( "utf-8" )

import time
from Base import sqlServerDatabase
MSSQL = sqlServerDatabase.MSSQL
def orderSql(sql):
    try:
        ms = MSSQL(host="172.17.7.181", user="ygtest", pwd="ygtest", db="YGPS_O2O")
        resList = ms.ExecQuery(sql)
    except:
        return {"code":"101","msg":u"数据库连接或查询失败"}
    if len(resList) == 1:
        data = {"code":"1","msg":u"查询到的该订单的数据量为一条","data": resList}
    elif len(resList) == 0:
        data = {"code":"0","msg":u"没有查询到该订单的信息"}
    else:
        data = {"code":"2","msg":u"查询到的该订单的数据量有多条","data": resList}
    return data

class createTestOrder:
    def __init__(self, commodityDict):
        self.commodityDict = commodityDict

    def DDorder(self, storeCode='20000022'):
        headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "15800b29-8890-386b-9287-e8b760beced2"
        }
        # querystring = r'"{\n    \"StoreCode\": \"20000022\",\n    \"CommodityCodes\": [{\n    \t\"CommodityCode\":\"1289396\",\n    \t\"Stock\":stockNub\n    \t}],\n    \"NickName\":\"张超\"\n\t\n}"'
        strContent=r'{"CommodityCode":"1289396","Stock":stockNub},'
        nunContent=''
        for commodity, stock in self.commodityDict.items():
            strContent = strContent.replace("1289396", commodity)
            strContent = strContent.replace("stockNub", str(stock))
            nunContent = nunContent + strContent
        querystring = '{"StoreCode": "20000022","CommodityCodes": [' + nunContent[0:-1] + '],"NickName":"张超"}'
        querystring = querystring.replace("20000022", storeCode)
        import json
        querystring = json.dumps(eval(querystring)) # 将字符串转换成字典，然后将字典转换成json
        response = requests.post(url="http://172.17.14.102:8080/O2O/submitorder", data=querystring, headers=headers)
        return response.content


    def TMSDorder(self, storeCode='20000070', isPayment="1"):
        '''
        :param storeCode:
        :param isPayment:
        :return:
        '''
        strTime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        tid ='152'+ strTime
        oid =strTime
        #TODO  没有校验Tid的唯一性，需要后续补上
        sql="SELECT OutStoreId FROM dbo.Rel_ChannelStore WHERE StoreCode='"+ storeCode +"' AND ChannelCode='9000000009';"
        if str(orderSql(sql)["code"])!="1":
            return {"code":"112","msg":u"渠道店铺表的数据不唯一，无法进行订单新增","data": orderSql(sql)}
        strContent = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"OrderText\"\r\n\r\n{\"trade_fullinfo_get_response\":{\"trade\":{\"omnichannel_param\":\"orderType:STORE_DELIVER,everStoreAllocated:1,allocationCode:127876895,RDCompanyCode:null,targetCode:123456789,acceptExpirationTime:2017/07/31-15:07:35,subOrderCode:41171611600046272,targetType:STORE,RDTime:2017-07-31 15:07:34,targetStoreOuterId:20000019,orderState:X_SHOP_HANDLED;\",\"step_paid_fee\":null,\"step_trade_status\":null,\"coupon_fee\":0.00,\"paid_coupon_fee\":null,\"seller_nick\":\"天猫超市闪店\",\"pic_path\":null,\"payment\":29.50,\"seller_rate\":null,\"buyer_email\":\" \",\"post_fee\":0.00,\"receiver_name\":\"潘爱华\",\"receiver_state\":\"上海\",\"receiver_address\":\"平凉路街道江浦路157弄101号3楼\",\"receiver_zip\":\"200082\",\"receiver_mobile\":\"13818006101\",\"receiver_phone\":null,\"consign_time\":\"2017-07-31 14:17:30\",\"invoice_kind\":null,\"invoice_name\":null,\"invoice_type\":null,\"receiver_country\":\"\",\"receiver_town\":\"平凉路街道\",\"tid\":tidNumber,\"num\":null,\"num_iid\":null,\"status\":\"WAIT_BUYER_CONFIRM_GOODS\",\"title\":\"天猫超市闪店\",\"type\":\"fixed\",\"price\":null,\"discount_fee\":0.00,\"has_post_fee\":null,\"total_fee\":44.00,\"created\":\"2017-07-31 14:07:29\",\"pay_time\":\"2017-07-31 14:07:34\",\"modified\":\"2017-07-31 14:17:31\",\"end_time\":null,\"buyer_message\":null,\"buyer_memo\":null,\"buyer_flag\":null,\"seller_memo\":null,\"seller_flag\":0,\"buyer_nick\":\"tb8006101_2012\",\"buyer_area\":\"上海上海电信\",\"has_buyer_message\":null,\"credit_card_fee\":null,\"shipping_type\":\"express\",\"buyer_cod_fee\":null,\"adjust_fee\":0.00,\"trade_from\":\"WAP,WAP\",\"alipay_warn_msg\":null,\"alipay_no\":\"2017073121001001330227018741\",\"buyer_alipay_no\":\"13818006101\",\"alipay_id\":\"2088702839178332\",\"buyer_rate\":null,\"receiver_city\":\"上海市\",\"receiver_district\":\"杨浦区\",\"orders\":{\"order\":[{\"divide_order_fee\":null,\"part_mjz_discount\":null,\"item_meal_name\":null,\"pic_path\":\"https://img.alicdn.com/bao/uploaded/i4/TB1MF9PSXXXXXbdXVXXXXXXXXXX_!!0-item_pic.jpg\",\"seller_nick\":null,\"buyer_nick\":null,\"refund_status\":\"NO_REFUND\",\"outer_iid\":\"1286608\",\"snapshot_url\":\"m:41171611600046272_1\",\"snapshot\":null,\"timeout_action_time\":null,\"buyer_rate\":false,\"seller_rate\":false,\"seller_type\":null,\"cid\":50050732,\"oid\":oidNumber,\"status\":\"WAIT_BUYER_CONFIRM_GOODS\",\"title\":\"山东栖霞精品红富士2个果径80-85mm\",\"price\":8.80,\"num_iid\":TMcommodity,\"item_meal_id\":null,\"sku_id\":null,\"num\":commodityNumber,\"outer_sku_id\":null,\"order_from\":\"WAP,WAP\",\"total_fee\":29.50,\"payment\":29.50,\"discount_fee\":14.50,\"adjust_fee\":0.00,\"modified\":null,\"sku_properties_name\":null,\"refund_id\":null,\"is_oversold\":null,\"is_service_order\":null,\"end_time\":null,\"consign_time\":\"2017-07-31 14:17:30\",\"shipping_type\":null,\"bind_oid\":null,\"logistics_company\":\"点我达\",\"invoice_no\":\"104232941\",\"is_daixiao\":null,\"store_code\":\"170211163\",\"is_www\":null}]},\"promotion_details\":{\"promotion_detail\":[{\"id\":\"41171611600046272\",\"promotion_name\":\"火热促销\",\"discount_fee\":14.50,\"gift_item_name\":null,\"gift_item_id\":null,\"gift_item_num\":null,\"promotion_desc\":\"火热促销:省14.50元\",\"promotion_id\":\"Tmall$commonItemPromotion-3928745088_21092935128\"}]}}},\"error_response\":null}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        strContent = strContent.replace("tidNumber", tid)
        strContent = strContent.replace("oidNumber", oid)
        for commodity, stock in self.commodityDict.items():
            strContent = strContent.replace("TMcommodity", commodity)
            #TODO 由于天猫闪店的订单会涉及订单金额问题，故不能修改商品数量，写死为5
            strContent = strContent.replace("commodityNumber", '5')
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "db5a036c-1e1a-4141-d980-d1ebd399d591"
            }
        response = requests.post("http://172.17.7.208:8081/OrderManager/CreateTOrderV2", data=strContent, headers=headers)
        if "天猫闪店创建订单成功" in str(response.content):
            info={"code":"10","msg":str(response.content)+"订单未支付tid为："+ str(tid)+",oid为："+str(oid),"data":{"oid":oid,"tid":tid}}
            if str(isPayment) == "1":
                payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Tid\"\r\n\r\n15220171017205304\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Oid\"\r\n\r\n20171017205304\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
                payload = payload.replace("15220171017205304", str(tid))
                payload = payload.replace("20171017205304", str(oid))
                headers = {
                    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                    'cache-control': "no-cache",
                    'postman-token': "171677de-1830-d1d1-d9b4-d78ab00e6653"
                    }
                payResponse = requests.post("http://172.17.7.208:8081/OrderManager/PayByTid", data=payload, headers=headers)
                if "已执行" in payResponse:
                    info={"code":"11","msg":str(response.content)+"订单已支付tid为："+ str(tid)+",oid为："+str(oid),"data":{"oid":oid,"tid":tid}}
                else:
                    info={"code":"100","msg":str(response.content)+"订单支付失败tid为："+ str(tid)+",oid为："+str(oid),"data":{"oid":oid,"tid":tid}}
        else:
            info = {"code":120,"msg":str(response.content),"data":""}
        return info


if __name__ == "__main__":
    commodityDict = {
        "554781483658": 5,
    }
    print createTestOrder(commodityDict=commodityDict).TMSDorder()["msg"]
