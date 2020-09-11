#!/usr/bin/env python3
"""PI SUPPLY GPS TEST
"""

from time import sleep
from i2cgps import I2CGPS

gps = I2CGPS()


# Most of the setup should happen only once...
print('Setup')

while True:
    print("Latitude: ", gps.get_latitude())
    print("Longitude: ", gps.get_longitude())
    print("Altitude: ", gps.get_altitude())
    print("HDOP: ", gps.get_hdop())
    print("Speed KMPH: ", gps.get_speed_kmph())
    print("Speed MPH: ", gps.get_speed_mph())
    print("Date Time Obj: ", gps.get_date_time())
    sleep(1)



lora.close()
