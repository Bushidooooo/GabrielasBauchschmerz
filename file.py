print ("Hallo Mergim")
im gay
print ("Bonne Nuit")
print ("Merci")
print ("umbenannt")
print ("Schmerz")
import redis
host = 'localhost'
redis_port = '6379'
r = redis.Redis(
host = host,
port = redis_port
)

all_keys = r.keys('*')
print(all_keys)
print("Ich habe 6 Tage frei")
res7 = r.incr("Sensor3")
print(res7)  # 1
res8 = r.incrby("Sensor4", 2)
print(res8)  # 11
 ligma balls

print("sanderns96")
print("Blendor Test")

print("Feierabend")

