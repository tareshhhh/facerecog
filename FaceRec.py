import cv2

#create a casscade classifier obeject

face_cascade = cv2.CascadeClassifier("C:\\Users\\FNU\\PycharmProjects\\ untitled1\\haarcascade_frontalface_default.xml")

#reading the image as it is

img= cv2.imread("C:\\Users\\FNU\\PycharmProjects\\ untitled1\\kug.jpg")




#reading the image asd gray  scale image

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#determinig the coordinates of the fACE

faces = face_cascade.detectMultiScale(gray_img ,scaleFactor=1.02 , minNeighbors=20)

#printiing the type

print(type(faces))

#printing the coordinates of face

print(faces)

#adding rectangular face box around face using for loop

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y), (x+w,x+y), (0,400,0),3)


cv2.imshow("sample",img)

cv2.waitKey(0)

cv2.destroyAllWindows()