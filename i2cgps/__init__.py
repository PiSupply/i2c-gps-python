import smbus
import struct
import time
from pprint import pprint
import datetime

i2c_addr = 0x42

class I2CGPS:
    def __init__(self, i2c_address = i2c_addr):
        self.bus = smbus.SMBus(1)
        self.i2c_address = i2c_address
    def get_latitude(self):
        #Return a float of the latitude
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x01, 4)
        latitude = struct.unpack('f',bytes(val))[0];
        time.sleep(0.1)
        return latitude

    def get_longitude(self):
        #Return a float of the longitude
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x02, 4)
        longitude = struct.unpack('f',bytes(val))[0];
        time.sleep(0.01)
        return longitude

    def get_altitude(self):
        #Return a float of the altitude
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x03, 4)
        altitude = struct.unpack('f',bytes(val))[0];
        return altitude

    def get_hdop(self):
        #Return a float of the hdop
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x04, 4)
        hdop = struct.unpack('f',bytes(val))[0];
        return hdop

    def get_speed_kmph(self):
        #Return a float of the kmph
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x05, 4)
        speed_kmph = struct.unpack('f',bytes(val))[0];
        return speed_kmph

    def get_speed_mph(self):
        #Return a float of the mph
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x06, 4)
        speed_mph = struct.unpack('f',bytes(val))[0];
        return speed_mph

    def get_date_time(self):
        #Return a float of the time
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x07, 4)
        gpsTime = str(struct.unpack('f',bytes(val))[0]);
        val = self.bus.read_i2c_block_data(self.i2c_address, 0x08, 4)
        gpsDate = str(struct.unpack('f',bytes(val))[0]);
        gpsDateTime = gpsDate[:-2]+gpsTime[:-2]
        dateTimeObj = datetime.datetime.strptime(gpsDateTime, '%d%m%y%H%M%S%f')
        return dateTimeObj
