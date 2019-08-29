#!/usr/bin/env python3
"""RAK811 GPS Demo
"""

from time import sleep

from rak811 import Mode, Rak811
from cayennelpp import LppFrame
from i2cgps import I2CGPS

gps = I2CGPS()



lora = Rak811()

# Most of the setup should happen only once...
print('Setup')
lora.hard_reset()
lora.mode = Mode.LoRaWan
lora.band = 'EU868'
lora.set_config(dev_addr="",
                apps_key="",
                nwks_key="")


print('Joining')
lora.join_abp()
# Note that DR is different from SF and depends on the region
# See: https://docs.exploratory.engineering/lora/dr_sf/
# Set Data Rate to 5 which is SF7/125kHz for EU868
lora.dr = 5



while True:
    frame = LppFrame()
    print("addgps")
    frame.add_gps(1,gps.get_latitude(),gps.get_longitude(),gps.get_altitude())
    lora.send(bytes(frame.bytes()))
    sleep(10)
    print("loop")



lora.close()

