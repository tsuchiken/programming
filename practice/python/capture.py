# -*- coding: utf-8 -*-
import tkinter
import cv2

#Define capture device
defaultDevice = 0
apiID = cv2.CAP_ANY

#Create the instance
vc = cv2.VideoCapture(defaultDevice + apiID)

#Deal for the device open error
if not vc.isOpened():
	raise DeviceOpenException("Device open is failed")
	
vc.set(cv2.CAP_PROP_FPS,60)
while True:
	#Read images in every frame
	ret, frame = vc.read()

	#Desplay images
	cv2.imshow("test",frame)
	filename = "test"+str(cv2.CAP_PROP_FRAME_COUNT)+".png"
	print(filename,str(round(vc.get(cv2.CAP_PROP_FPS),0)))

	#Wait a key in every 1msec
	key = cv2.waitKey(1)

	#if s key is pushed, save the image of this frame
	if key == ord("s"):
		cv2.imwrite("D:\\Pictures\\test.png",frame)
	#if ESC key is pushed, break though this loop
	elif key == 27:
		break

#resources release
vc.release()
cv2.destroyAllWindows()
