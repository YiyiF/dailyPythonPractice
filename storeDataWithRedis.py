#! /usr/bin/env python3
from redis import StrictRedis
import random, string, time

beginTime = time.time()
# 连接数据库
redis = StrictRedis(host='localhost', port=6379, db=0, password='test1234')
# 使用pipeline，批量提交——非事务型流水线
# pipe = redis.pipeline(transaction=False)
# 使用pipeline，事务型流水线
pipe = redis.pipeline()

sequence = string.ascii_uppercase + string.digits
discountCodeSet = set()
while len(discountCodeSet) < 200:
    codeCharacter = random.sample(sequence, 6)
    discountCode = ''.join(codeCharacter)
    discountCodeSet.add(discountCode)
    pipe.sadd('discountCode', discountCode)
pipe.execute()
print('Finish in {} secs.' .format(time.time() - beginTime))
# dbValue = redis.smembers('discountCode')
# print(discountCodeSet == dbValue)
