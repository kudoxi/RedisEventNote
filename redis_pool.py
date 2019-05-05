import redis

#声明连接池
pool = redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)

#建立连接
r = redis.Redis(connection_pool=pool)
r2 = redis.Redis(connection_pool=pool)

#执行操作
r.set('apple','a')
print(r.get('apple'))
r2.set('banana','b')
print(r.get('banana'))

#打印客户端信息
print(r.client_list())
print(r.client_list())
