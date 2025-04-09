import lcm, time, random
from cerberus_lcm import IA

lc = lcm.LCM()

msg = IA()

while True:
    rand = random.uniform(0,1)
    msg.id = 1
    msg.speed = 1.0 + rand
 
    lc.publish("IA", msg.encode())

    time.sleep(0.1)