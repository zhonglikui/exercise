import pymysql

code_list=['2NdmkA01ufdiqX6L0000','8AM5FHfqTFbe3yfL0001','CCQluAx9Qo4cj4QL0002', 'PCTG5NcZWOFutNkL0003','AWFUTvRnj6WTU7uL0004',
            '2RVxpHAsIc2VuNdL0005','YqZumDemBG0SrZNL0006','11ElKwxL8EJwFg1L0007','0oDxpGAP6mwMmCJL0008','Rk5SishGKEXWNQDL0009',
            'D4YEzZxTrVPEAPHL0010','0B8Y2C7caZoa62PL0011','2LFM4looS9JsCzDL0012','UCnABhIeozdyMRDL0013','YjX6p89Zsqs9UNwL0014',
            'y3k1jEdULjFIxc7L0015','bR0JeiV9Ub9vowyL0016','dHORI0CoyUKaiHSL0017','XwQdQLqTabYGxSGL0018','4rsvCsycfq7me19L0019']
conn=pymysql.connect(host='localhost',port=3306,user='root',password='Zlk$$123456',charset='utf8mb4')
try:
    with conn.cursor() as cursor:
            db="CREATE DATABASE IF NOT EXISTS db_code"
            cursor.execute(db)
            use="USE db_code"
            cursor.execute(use)
            create="CREATE TABLE IF NOT EXISTS promo_code(id int(8) NOT NULL AUTO_INCREMENT,code varchar(64) COLLATE utf8_bin NOT NULL, PRIMARY KEY (id))"
            cursor.execute(create)
            conn.commit()
            for code in code_list:
                sql = "INSERT INTO `promo_code` (`code`) VALUES (%s)"
                cursor.execute(sql, (code))
            conn.commit()
except Exception as e:
    print("fail:%s" % e)
finally:
    conn.close()
