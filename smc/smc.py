
from __future__ import division, print_function
import serial
import time

# https://forum.pololu.com/t/multiple-18v7-motor-controllers-over-usb/6251/2
# mc = SMC('/dev/tty', 115200)
# mc.init()
# mc.speed(1000)
# mc.stop()


class SMC(object):
    """
    This class allows control of a Pololu simple motor controller using binary
    mode with CRC disabled and a fixed baudrate. You must use their software to
    enable that.
    """
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Constructor
        """
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.timeout = timeout

    def __del__(self):
        """
        Destructor
        """
        self.stop()
        self.close()

    def stop(self):
        """
        You must re-init() again after calling this method
        """
        self.write((0xe0,))

    def write(self, command):
        # not sure if this function is useful
        pkt = bytes(bytearray(command))
        self.ser.write(pkt)
        # self.ser.flush()

    def init(self):
        """Opens serial port and puts SMC into binary mode"""
        if not self.ser.is_open:
            self.ser.open()
        self.write((0x83,))

    def speed(self, speed):
        """
        Set speed between -3200 and 3200. If you send a speed greater (or smaller)
        than this, it will be truncated to this range.
        """
        if speed > 0:
            if speed > 3200:
                speed = 3200
            channelByte = 0x85
        else:
            if speed < -3200:
                speed = 3200
            else:
                speed = -speed
            channelByte = 0x86

        cmd = tuple([channelByte, speed & 0x1F, (speed >> 5) & 0x7F])
        self.write(cmd)

    def speed7b(self, speed):
        """
        Set speed using the 7 bit command. Speed has a range of -127 to 127. If
        you send a speed greater or smaller than this range, the speed will be
        truncated.
        """
        if speed > 0:
            if speed > 127:
                speed = 127
            channelByte = 0x89
        else:
            if speed < -127:
                speed = 127
            else:
                speed = -speed
            channelByte = 0x8a

        cmd = tuple([channelByte, speed])
        self.write(cmd)

    def mbreak(self, level=32):
        """
        Breaks the motor. The level of force is between 0 (coast) and 32 (max).
        """
        if level < 0:
            level = 0
        elif level > 32:
            level = 32
        self.write((0x92, level,))

    def getFirmware(self):
        """
        Return the id and firmware
        """
        self.write((0xc2,))
        idlow, idhi, fwminor, fwmajor = self.ser.read(4)
        ID = (idhi << 8) + idlow
        fw = (fwmajor << 8) + fwminor
        return (ID, fw)

    def close(self):
        """
        Close serial port
        """
        if self.ser.is_open:
            self.ser.close()
