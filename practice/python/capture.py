# -*- coding: utf-8 -*-
from tkinter import *
from datetime import *
import cv2
import sys
import os

#Define the capture device
defaultDevice = 0
apiID = cv2.CAP_ANY

#Create the capture instance
vc = cv2.VideoCapture(defaultDevice + apiID)

#Deal for the device open error
if not vc.isOpened():
	raise DeviceOpenException("Device open is failed")

#get properties
fps = vc.get(cv2.CAP_PROP_FPS)
size = (vc.get(cv2.CAP_PROP_FRAME_WIDTH), vc.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"XVID")

path = "D:\\Videos\\Captures\\"
os.makedirs(path,0o777,True)
fnTime = datetime.now().strftime("%Y%m%d_%H%M%S")

"""
CheckDeal
print(fnTime)
"""
filename = "cap_" + fnTime + ".mp4"

out = cv2.VideoWriter(path + filename,fourcc,30.0,(640,480))

while vc.isOpened():
	#Read images in every frame
	ret, frame = vc.read()

	if ret == True:
		# write the flipped frame
		out.write(frame)

	#Desplay images
	cv2.imshow("capture",frame)
	"""
	CheckMethod
	print(filename,str(round(vc.get(cv2.CAP_PROP_FPS),0)))
	"""

	#Wait a key in every 1msec
	key = cv2.waitKey(1)

	#if ESC key is pushed, the system break though this loop
	if key == 27:
		break

#resources release
vc.release()
out.release()
cv2.destroyAllWindows()
