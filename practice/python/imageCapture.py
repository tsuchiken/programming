# -*- coding: utf-8 -*-
from tkinter import *
from datetime import *
import cv2
import sys
import os
import numpy

#Define capture device
defaultDevice = 0
apiID = cv2.CAP_ANY

#Create the instance
vc = cv2.VideoCapture(defaultDevice + apiID)

#Deal for the device open error
if not vc.isOpened():
	raise DeviceOpenException("Device open is failed")

#Set properties
vc.set(cv2.CAP_PROP_FPS,60)

while vc.isOpened():
	#Read images in every frame
	ret, frame = vc.read()

	#Desplay images
	cv2.imshow("capture",frame)
	"""
	CheckMethod
	print(filename,str(round(vc.get(cv2.CAP_PROP_FPS),0)))
	"""

	#Wait a key in every 1msec
	key = cv2.waitKey(1)

	#if s key is pushed, save the image of this frame
	if key == ord("s"):
		path = "D:\\Pictures\\"
		os.makedirs(path,0o777,True)
		fnTime = datetime.now().strftime("%Y%m%d_%H%M%S")

		"""
		CheckMethod
		print(fnTime)
		"""
		filename = "cap_" + fnTime + ".png"
		cv2.imwrite(path + filename,frame)
	#if ESC key is pushed, the system break though this loop
	elif key == 27:
		break

#resources release
vc.release()
cv2.destroyAllWindows()
