
#import the library opencv

import cv2

#import the image p.s.-image should be in the same folder wherethis program is going to save

img = cv2.imread ("C:\\Users\\FNU\\PycharmProjects\\untitled1\\kanha.JPG",1)

#resizing the image by dividing the old size of the image by 4

resized = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))

###displaying the image

#open a window to show the img
cv2.imshow("legend",resized)

#wait untill the user presses the key
cv2.waitKey(0)

#closes the window
cv2.destroyWindow()
