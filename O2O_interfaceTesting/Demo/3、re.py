#coding=utf-8
import re
#获取8位数字的订单号
querystring = '{"code":200,"msg":"success","data":{"message":"33402540","state":"true","errorMessage":null,"success":"true","resultCode":"0"}}'
pattern=r'("message":"(\d{8})",)'
print re.search(pattern,querystring).group(2)