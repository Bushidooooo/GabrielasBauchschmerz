print "Hello World"
im gay
print ("umbenannt")


import redis

host = 'localhost'
redis_port = '6379'
r = redis.Redis(
host = host,
port = redis_port
)



all_keys = r.keys('*')
print(all_keys)




res7 = r.incr("Sensor3")
print(res7)  # 1
res8 = r.incrby("Sensor4", 2)
print(res8)  # 11
 

ligma balls

print("sanderns96")
print("Blendor Test")

print("Feierabend")

