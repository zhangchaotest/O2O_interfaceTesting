# #coding=utf-8
# import requests
# a='request={"ChannelName":null,"ChannelCode":"1100000043","SerialNumber":"33402533","OrderStatus":4,"SellerCode":null,"StoreCode":"20000022","PayStatus":0,"RefundReason":null,"FailReason":null,"Content":"{"DiliverymanName":"DiliverymanName","DiliverymanMobile":"13917251653","MailNo":null,"OperateDetail":null,"CompanyName":null}","CancelType":""}'
# changeOrderState = requests.get("http://172.17.7.208:10111/YGPS.O2O.Server.Order.UpdateState", params=a)
# print changeOrderState.content
#
#
# print u'\u5b8b'.encode("utf8")


# # print int(2.00)
# ___________________
# class Switcher(object):
#     def numbers_to_methods_to_strings(self, argument):
#         """Dispatch method"""
#         # prefix the method_name with 'number_' because method names
#         # cannot begin with an integer.
#         method_name = 'number_' + str(argument)+"('1111')"
#         # Get the method from 'self'. Default to a lambda.
#         print method_name
#         method = getattr(self, method_name, lambda: "nothing")
#         print method
#         # Call the method as we return it
#         return method()
#
#     def number_0(self):
#         return "zero"
#
#     def number_1(self,s):
#         print s
#         return "one"
#
#     def number_2(self):
#         return "two"
#
# a=Switcher()
# print a.numbers_to_methods_to_strings("1")
#
# _______________________


import requests

# url = "http://172.17.7.208:8081/OrderManager/CreateTOrder"
#
# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"OrderText\"\r\n\r\n{\"trade_fullinfo_get_response\":{\"trade\":{\"omnichannel_param\":\"orderType:STORE_DELIVER,everStoreAllocated:1,allocationCode:127876895,RDCompanyCode:null,targetCode:123456789,acceptExpirationTime:2017/07/31-15:07:35,subOrderCode:41171611600046272,targetType:STORE,RDTime:2017-07-31 15:07:34,targetStoreOuterId:20000019,orderState:X_SHOP_HANDLED;\",\"step_paid_fee\":null,\"step_trade_status\":null,\"coupon_fee\":0.00,\"paid_coupon_fee\":null,\"seller_nick\":\"天猫超市闪店\",\"pic_path\":null,\"payment\":29.50,\"seller_rate\":null,\"buyer_email\":\" \",\"post_fee\":0.00,\"receiver_name\":\"潘爱华\",\"receiver_state\":\"上海\",\"receiver_address\":\"平凉路街道江浦路157弄101号3楼\",\"receiver_zip\":\"200082\",\"receiver_mobile\":\"13818006101\",\"receiver_phone\":null,\"consign_time\":\"2017-07-31 14:17:30\",\"invoice_kind\":null,\"invoice_name\":null,\"invoice_type\":null,\"receiver_country\":\"\",\"receiver_town\":\"平凉路街道\",\"tid\":41172612680946574,\"num\":null,\"num_iid\":null,\"status\":\"WAIT_BUYER_CONFIRM_GOODS\",\"title\":\"天猫超市闪店\",\"type\":\"fixed\",\"price\":null,\"discount_fee\":0.00,\"has_post_fee\":null,\"total_fee\":44.00,\"created\":\"2017-07-31 14:07:29\",\"pay_time\":\"2017-07-31 14:07:34\",\"modified\":\"2017-07-31 14:17:31\",\"end_time\":null,\"buyer_message\":null,\"buyer_memo\":null,\"buyer_flag\":null,\"seller_memo\":null,\"seller_flag\":0,\"buyer_nick\":\"tb8006101_2012\",\"buyer_area\":\"上海上海电信\",\"has_buyer_message\":null,\"credit_card_fee\":null,\"shipping_type\":\"express\",\"buyer_cod_fee\":null,\"adjust_fee\":0.00,\"trade_from\":\"WAP,WAP\",\"alipay_warn_msg\":null,\"alipay_no\":\"2017073121001001330227018741\",\"buyer_alipay_no\":\"13818006101\",\"alipay_id\":\"2088702839178332\",\"buyer_rate\":null,\"receiver_city\":\"上海市\",\"receiver_district\":\"杨浦区\",\"orders\":{\"order\":[{\"divide_order_fee\":null,\"part_mjz_discount\":null,\"item_meal_name\":null,\"pic_path\":\"https://img.alicdn.com/bao/uploaded/i4/TB1MF9PSXXXXXbdXVXXXXXXXXXX_!!0-item_pic.jpg\",\"seller_nick\":null,\"buyer_nick\":null,\"refund_status\":\"NO_REFUND\",\"outer_iid\":\"1286608\",\"snapshot_url\":\"m:41171611600046272_1\",\"snapshot\":null,\"timeout_action_time\":null,\"buyer_rate\":false,\"seller_rate\":false,\"seller_type\":null,\"cid\":50050732,\"oid\":41171411613446363,\"status\":\"WAIT_BUYER_CONFIRM_GOODS\",\"title\":\"山东栖霞精品红富士2个果径80-85mm\",\"price\":8.80,\"num_iid\":1234566803401,\"item_meal_id\":null,\"sku_id\":null,\"num\":5,\"outer_sku_id\":null,\"order_from\":\"WAP,WAP\",\"total_fee\":29.50,\"payment\":29.50,\"discount_fee\":14.50,\"adjust_fee\":0.00,\"modified\":null,\"sku_properties_name\":null,\"refund_id\":null,\"is_oversold\":null,\"is_service_order\":null,\"end_time\":null,\"consign_time\":\"2017-07-31 14:17:30\",\"shipping_type\":null,\"bind_oid\":null,\"logistics_company\":\"点我达\",\"invoice_no\":\"104232941\",\"is_daixiao\":null,\"store_code\":\"170211163\",\"is_www\":null}]},\"promotion_details\":{\"promotion_detail\":[{\"id\":\"41171611600046272\",\"promotion_name\":\"火热促销\",\"discount_fee\":14.50,\"gift_item_name\":null,\"gift_item_id\":null,\"gift_item_num\":null,\"promotion_desc\":\"火热促销:省14.50元\",\"promotion_id\":\"Tmall$commonItemPromotion-3928745088_21092935128\"}]}}},\"error_response\":null}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'cache-control': "no-cache",
#     'postman-token': "8e951a52-c670-5c22-d833-379d7328e528"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
#________________________________
# class testA:
#     def __init__(self, list):
#         self.list = list
#
#     def a(self,bbb):
#         print bbb
#         return self.list.pop()
#
# li=["zhangjing","zhangwei"]
# test= testA(li)
# print getattr(test,"a")("12321312")
# # aa={"State":true,"ResultCode":0,"ErrorMessage":null,"ResultObj":{"IsSuccess":true,"ReturnCode":null,"ReturnMsg":"订单编号：33325674未变更状态信息失败，现状态为6，状态日志记录为WAIT_BUYER_CONFIRM_GOODS（5）"}}
# _____________________________________________________________________
# import requests
#
# url = "http://172.17.14.102:8080/O2O/submitorder"
#
# payload = "{\"StoreCode\": \"20000022\", \"CommodityCodes\": [{\"CommodityCode\":\"1289396\",\"Stock\":2 }],   \"NickName\":\"\"}"
# headers = {
#     'content-type': "application/json",
#     'cache-control': "no-cache",
#     'postman-token': "ae98bedd-2ad1-905d-562a-7117db5799ef"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
#
# __________________________________________________________________________________________________________________________________________________
#

# from opention import createOrder
# from opention import orderUpdateState
# from Base import sqlServerDatabase
# MSSQL = sqlServerDatabase.MSSQL
#
#
# commodityDict = {
#     "9000070219":5,
# }
# data=createOrder.createTestOrder(commodityDict=commodityDict).TMSDorder()
# print data
# print data["data"]["tid"]
# ms = MSSQL(host="172.17.7.202",user="ygtest",pwd="ygtest",db="YGPS_O2O")
# resList = ms.ExecQuery("SELECT SerialNumber FROM dbo.Fct_Order WHERE PartnerOrderCode='" + "" + "';")
# print resList


# r=orderUpdateState.changeOrderState("33431221","9")
# r=orderUpdateState.changeOrderState("33431221","10")
# r=orderUpdateState.changeOrderState("33431221","4")

print u'\u4ee5'.encode("utf-8")