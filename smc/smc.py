
from __future__ import division, print_function
import serial
import time

# https://forum.pololu.com/t/multiple-18v7-motor-controllers-over-usb/6251/2
# mc = SMC('/dev/tty', 115200)
# mc.init()
# mc.speed(1000)
# mc.stop()


class SMC(object):
	def __init__(self, port, baudrate):
		self.ser = serial.Serial()
		self.ser.port = port
		self.ser.baudrate = baudrate

	def __del__(self):
		self.stop()
		self.close()

	def stop(self):
		# stop
		pass

	def write(self, command):
		# not sure if this function is useful
		self.ser.write(command)
		# self.ser.flush()

	def init(self):
		"""Opens serial port and puts SMC into xxx mode"""
		self.ser.open()
		self.write(chr(0x83))

	def speed(self, speed):
		if speed > 0:
			channelByte = chr(0x85)
		else:
			speed = -speed
			channelByte = chr(0x86)

		cmd = tuple(channelByte, chr(speed & 0x1F), chr((speed >> 5) & 0x7F))
		self.write(cmd)

	def close(self):
		if self.ser.isOpen():
			self.ser.close()
