#! /usr/bin/env python3
import random, string, pymysql

sequence = string.ascii_uppercase + string.digits

discountCodeList = []
while len(discountCodeList) < 200:
    codeCharacter = random.sample(sequence, 6)
    discountCode = ''.join(codeCharacter)
    if discountCode not in discountCodeList:
        discountCodeList.append(discountCode)
print(discountCodeList)

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='mysql1234',
                             charset='utf8')
# 获取游标
cursor = connection.cursor()

# 创建数据库
db_sql = "CREATE DATABASE IF NOT EXISTS test DEFAULT CHARSET utf8 COLLATE utf8_general_ci"
cursor.execute(db_sql)

# 使用创建的数据库
cursor.execute('USE test')

# 创建数据表
effect_row = cursor.execute('''
CREATE TABLE IF NOT EXISTS `discountCode` (
  `code` varchar(32) NOT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
''')

# 插入数据
# effect_row = cursor.execute('INSERT INTO `discountCode` (`code`) VALUES (%s)', discountCodeList)

sql = 'INSERT INTO `discountCode` (`code`) VALUES (%s)'
cursor.executemany(sql, discountCodeList)
connection.commit()

connection.close()
