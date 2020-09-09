import cv2, time, pandas
from datetime import datetime
first_frame = None

status_list = [None,None]
times = []
df = pandas.DataFrame(columns=['Start','End'])

#creating a VideoCapyure obj to record video using webcam

video = cv2.VideoCapture(0)

while True:



    check , frame  = video.read()

#status at the beginign of the recording is 0 as the obj is not visible
    status = 0
#converting the frame into grayscale+
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#convertung grascale into gaussian blur
    gray = cv2.GaussianBlur(gray,(21,21),0)

#this is used to store the first frame or image of the  video

    if first_frame is None:
        first_frame = gray
        continue

#calculate the difeerenece between the fisrt frame and other frames
    delta_frame = cv2.absdiff(first_frame,gray)
#provids a threhold value such that it will covert the diff value less than 30 to black, if the diff id greater than 30 it will convert it to white pixles
    thresh_delta = cv2.threshold(delta_frame,144,300,cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta,None,iterations = 0)
#defin the contour area, basically borders
    (cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in cnts:
# removes noises and shadows, basically does not detect the obj less than 1000 pixels
        if cv2.contourArea(contour)<10000:
             continue
#change in the status since the obj has been moved
        status=1
#creates a rect box
        (x ,y ,w ,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame ,(x , y),(x+w , y+h),(0,300,0),3)

# for every frame we are going to append the list of the status

    status_list.append(status)

#second last status list value

    status_list = status_list[-2:]

#record the datetime in a list when change occurs

    if status_list [-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    print(status_list)
    print(times)

    for i in range(1,len(times),2):
        df=df.append({"Start":times[i],"Ends": times[i+1]},ignore_index = True)

    df.to_csv("Times.csv")

    cv2.imshow('frame', frame)
    cv2.imshow('Capturing', gray)
    cv2.imshow('delta', delta_frame)
    cv2.imshow('thresh', thresh_delta)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


