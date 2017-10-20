#coding=utf-8
import requests
import re

def requestShow(r):
    print 1, r.url  # 输出一个url http://www.baidu.com/
    print 2, r.content  # 输出内容
    print 3, r.elapsed  # 输出时间
    print 4, r.cookies
    print 5, r.encoding
    print 6, r.headers

# from Base import sqlServerDatabase
# sqlCheck = sqlServerDatabase.MSSQL()

payload = "{\n    \"StoreCode\": \"20000022\",\n    \"CommodityCodes\": [{\n    \t\"CommodityCode\":\"1289396\",\n    \t\"Stock\":2\n    \t}],\n    \"NickName\":\"张超\"\n\t\n}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "6db129e9-34f5-3b88-f73d-2d3f3c6fcfbf"
    }

createOrderObject = requests.post("http://172.17.14.102:8080/O2O/submitorder",data=payload,headers=headers)
requestShow(createOrderObject)


pattern=r'("message":"(\d{8})",)'
SerialNumber=re.search(pattern,createOrderObject.content).group(2)

# headers = {
#     'cache-control': "no-cache",
#     'postman-token': "4e987189-4927-0d20-5fd2-d0794517b76e"
#     }
#
'''
            //4使用Content的报文   {\"DiliverymanName\":\"zhangsan\",\"DiliverymanMobile\":\"12312311\"}
            //9使用Content的报文   [{\"MainCommodityCode\":\"\",\"CommodityCode\":\"7160637\",\"CommodityName\":\"美威包心三文鱼丸300g（FG）\",\"OrderCommodityQty\":\"2\",\"ActualQty\":\"1\"}]
            10,5 同4
'''
querystring = '	{"ChannelName":"钉钉"","ChannelCode":"1100000043","SerialNumber":"33386638","OrderStatus":4,"SellerCode":"2100000003","StoreCode":null,"PayStatus":0,"RefundReason":null,"FailReason":null,"Content":null,"CancelType":null}'
querystring=querystring.replace("33386638",SerialNumber)
changeOrderState = requests.get("http://172.17.7.208:10111/YGPS.O2O.Server.Order.UpdateState",headers=headers, params=querystring)
requestShow(changeOrderState)
# 钉钉下单


# data_TMSD={"trade_fullinfo_get_response":{"trade":{"omnichannel_param":"orderType:STORE_DELIVER,everStoreAllocated:1,allocationCode:127876895,RDCompanyCode:None,targetCode:123456789,acceptExpirationTime:2017/07/31-15:07:35,subOrderCode:41171611600046272,targetType:STORE,RDTime:2017-07-31 15:07:34,targetStoreOuterId:20000019,orderState:X_SHOP_HANDLED;","step_paid_fee":None,"step_trade_status":None,"coupon_fee":0.00,"paid_coupon_fee":None,"seller_nick":"天猫超市闪店","pic_path":None,"payment":29.50,"seller_rate":None,"buyer_email":" ","post_fee":0.00,"receiver_name":"潘爱华","receiver_state":"上海","receiver_address":"平凉路街道江浦路157弄101号3楼","receiver_zip":"200082","receiver_mobile":"13818006101","receiver_phone":None,"consign_time":"2017-07-31 14:17:30","invoice_kind":None,"invoice_name":None,"invoice_type":None,"receiver_country":"","receiver_town":"平凉路街道","tid":41171612630246574,"num":None,"num_iid":None,"status":"WAIT_BUYER_CONFIRM_GOODS","title":"天猫超市闪店","type":"fixed","price":None,"discount_fee":0.00,"has_post_fee":None,"total_fee":44.00,"created":"2017-07-31 14:07:29","pay_time":"2017-07-31 14:07:34","modified":"2017-07-31 14:17:31","end_time":None,"buyer_message":None,"buyer_memo":None,"buyer_flag":None,"seller_memo":None,"seller_flag":0,"buyer_nick":"tb8006101_2012","buyer_area":"上海上海电信","has_buyer_message":None,"credit_card_fee":None,"shipping_type":"express","buyer_cod_fee":None,"adjust_fee":0.00,"trade_from":"WAP,WAP","alipay_warn_msg":None,"alipay_no":"2017073121001001330227018741","buyer_alipay_no":"13818006101","alipay_id":"2088702839178332","buyer_rate":None,"receiver_city":"上海市","receiver_district":"杨浦区","orders":{"order":[{"divide_order_fee":None,"part_mjz_discount":None,"item_meal_name":None,"pic_path":"https://img.alicdn.com/bao/uploaded/i4/TB1MF9PSXXXXXbdXVXXXXXXXXXX_!!0-item_pic.jpg","seller_nick":None,"buyer_nick":None,"refund_status":"NO_REFUND","outer_iid":"1286608","snapshot_url":"m:41171611600046272_1","snapshot":None,"timeout_action_time":None,"buyer_rate":False,"seller_rate":False,"seller_type":None,"cid":50050732,"oid":41171411613446363,"status":"WAIT_BUYER_CONFIRM_GOODS","title":"山东栖霞精品红富士2个果径80-85mm","price":8.80,"num_iid":1234566803401,"item_meal_id":None,"sku_id":None,"num":5,"outer_sku_id":None,"order_from":"WAP,WAP","total_fee":29.50,"payment":29.50,"discount_fee":14.50,"adjust_fee":0.00,"modified":None,"sku_properties_name":None,"refund_id":None,"is_oversold":None,"is_service_order":None,"end_time":None,"consign_time":"2017-07-31 14:17:30","shipping_type":None,"bind_oid":None,"logistics_company":"点我达","invoice_no":"104232941","is_daixiao":None,"store_code":"170211163","is_www":None}]},"promotion_details":{"promotion_detail":[{"id":"41171611600046272","promotion_name":"火热促销","discount_fee":14.50,"gift_item_name":None,"gift_item_id":None,"gift_item_num":None,"promotion_desc":"火热促销:省14.50元","promotion_id":"Tmall$commonItemPromotion-3928745088_21092935128"}]}}},"error_response":None}
#
# r = requests.post("http://172.17.7.208:8081/OrderManager/CreateTOrder",json=data_TMSD)
# requestShow(r)