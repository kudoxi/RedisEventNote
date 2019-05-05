import redis

#建立连接
r = redis.Redis(host='localhost',port=6379,decode_responses=True)
r.set('p3','a3')
#声明一个管道
pipe = r.pipeline(transaction=True)#transaction是否以原子的方式执行

#指令存放
pipe.set('p1','v1')
pipe.set('p2','v2')
pipe.set('p3','v3')
pipe.set('p4','v4')
pipe.set('p5','v5')

print(r.get('p3'))#a3
#执行指令　没有执行，以上p1~p5都不会执行，一直卡在第一条a3
pipe.execute()
print(r.get('p3'))#v3
