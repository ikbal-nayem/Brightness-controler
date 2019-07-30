#!/usr/bin/env python3
import os
import datetime, time
import keyboard

brightness_dir = '/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight'

class Brightness:

	def change(self, light):
		try:
		    if light > 50 and light < 1000:
		        with open(os.path.join(brightness_dir, 'brightness'), 'w') as f:
		            f.write(str(light))
		        with open('last_brightness', 'w') as f:
		            f.write(str(light))
		except:
			print('Error found!')

	def up(self):
		with open('last_brightness', 'r') as f:
			light = int(f.read())
			light += 100
			self.change(light)

	def down(self):
		with open('last_brightness', 'r') as f:
			light = int(f.read())
			light -= 100
			self.change(light)

	def startUp(self):
		light = ''
		try:
		    with open('last_brightness', 'r') as f:
		        light = int(f.read())
		except:
		    with open('last_brightness', 'w') as f:
		        light = 800
		        f.write(str(light))
		self.change(light)


if __name__=='__main__':
	control = Brightness()
	control.startUp()
	keyboard.add_hotkey('ctrl+right', control.up, suppress=False, timeout=1, trigger_on_release=False)
	keyboard.add_hotkey('ctrl+left', control.down, suppress=False, timeout=1, trigger_on_release=False)

	while True:
		time.sleep(0.1)
