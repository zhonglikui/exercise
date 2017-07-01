import redis
code_list=['2NdmkA01ufdiqX6L0000','8AM5FHfqTFbe3yfL0001','CCQluAx9Qo4cj4QL0002', 'PCTG5NcZWOFutNkL0003','AWFUTvRnj6WTU7uL0004',
            '2RVxpHAsIc2VuNdL0005','YqZumDemBG0SrZNL0006','11ElKwxL8EJwFg1L0007','0oDxpGAP6mwMmCJL0008','Rk5SishGKEXWNQDL0009',
            'D4YEzZxTrVPEAPHL0010','0B8Y2C7caZoa62PL0011','2LFM4looS9JsCzDL0012','UCnABhIeozdyMRDL0013','YjX6p89Zsqs9UNwL0014',
            'y3k1jEdULjFIxc7L0015','bR0JeiV9Ub9vowyL0016','dHORI0CoyUKaiHSL0017','XwQdQLqTabYGxSGL0018','4rsvCsycfq7me19L0019']

r=redis.StrictRedis(host='localhost',port=6379,db=0)
for code in code_list:
    r.sadd('code',code)
r.save()
print('一共存储了%d条数据'% r.scard('code'))
#暂时空缺