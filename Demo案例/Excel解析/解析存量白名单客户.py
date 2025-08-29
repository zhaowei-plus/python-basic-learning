import math
import pymysql
import pandas as pd
from datetime import datetime

db_config = {
    "host": "127.0.0.1",
    "user": "",
    "password": "",
    "db": "test",
    "charset": "utf8mb4"
}

file_path = './测试文件.csv'

def readExcel(file_path):
    df = pd.read_csv(file_path)
    return df.values

def isNone(value):
    if pd.isna(value):
        return ''
    return value

def writeToHTImportClientTable(data):
    try:
        connection = pymysql.connect(**db_config)
        # 创建游标(查询数据返回元组格式)
        with connection.cursor() as cursor:
            # sql语句
            sql = 'insert into dayu_high_threat_important_client(appid,uin,customer_name,remark) values(%s,%s,%s,%s)'
            # 数据
            tuple_records = []
            for record in data[0:]:
                customer_name       = isNone(record[1])
                appid               = isNone(record[2])
                uin                 = isNone(record[3])
                remark              = isNone(record[4])
                print('customer_name: ' + customer_name)
                if customer_name == '':
                    print('Complete')
                    continue

                tuple_record = tuple([
                    appid,
                    uin,
                    customer_name,
                    remark
                ])
                cursor.execute(sql, tuple_record)
                tuple_records.insert(len(tuple_records), tuple_record)

            # 批量倒入数据
            # cursor.executemany(sql, tuple_records)
            # 提交事务
            connection.commit()
            # 关闭游标
            cursor.close()

    except pymysql.MySQLError as e:
        print(e)

    finally:
        # 关闭数据库连接
        connection.close()

result = readExcel(file_path)
writeToHTImportClientTable(result)




