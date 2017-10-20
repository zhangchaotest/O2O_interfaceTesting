#coding=utf-8
from Base import sqlServerDatabase

MSSQL = sqlServerDatabase.MSSQL


def main():

'''
ExecQuery:执行查询语句
ExecNonQuery：执行非查询语句

## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")
'''
    ms = MSSQL(host="172.17.7.202",user="ygtest",pwd="ygtest",db="YGOP_RTYG")
    resList = ms.ExecQuery("SELECT StockId FROM dbo.Mob_Fct_StockInfo")
    for (id) in resList:
        print str(id).decode("utf8")
if __name__ == '__main__':
    main()