#!/usr/bin/env python3
import os
old_dir = os.getcwd()
os.chdir('/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-LVDS-1/intel_backlight')

while True:
	try:
		with open("brightness", 'r') as f:
			old_value = f.read()
			print('Current brightness is {}'.format(old_value))

		value = int(input('Put your new value here : '))
		if value < 50 or value > 1000:
			f.close()
			print('\n\tSetting done!!!')
			break
		with open('brightness', 'w') as f:
			f.write(str(value))
	except:
		print('\n\tSetting done!!!')
		break

os.chdir(old_dir)
