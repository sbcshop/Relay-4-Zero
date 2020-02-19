import pizero_4relay as pirelay
from time import sleep

r1 = pirelay.relay("R1")
r2 = pirelay.relay("R2")
r3 = pirelay.relay("R3")
r4 = pirelay.relay("R4")


r1.on()
sleep(2)
r1.off()
sleep(2)

r2.on()
sleep(2)
r2.off()
sleep(2)

r3.on()
sleep(2)
r3.off()
sleep(2)

r4.on()
sleep(2)
r4.off()
sleep(2)
