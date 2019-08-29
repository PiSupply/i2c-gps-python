import smbus
import struct
from time import sleep
from pprint import pprint

i2c_addr = 0x42

class I2CGPS:
    def __init__(self, i2c_address = i2c_addr):
        self.bus = smbus.SMBus(1)
        self.i2c_address = i2c_address
    def get_latitude(self):
        #Return a float of the latitude
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x01, 4)
        latitude = struct.unpack('f',bytes(val))[0];
        return latitude

    def get_longitude(self):
        #Return a float of the longitude
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x02, 4)
        longitude = struct.unpack('f',bytes(val))[0];
        return longitude

    def get_altitude(self):
        #Return a float of the altitude
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x03, 4)
        altitude = struct.unpack('f',bytes(val))[0];
        return altitude
