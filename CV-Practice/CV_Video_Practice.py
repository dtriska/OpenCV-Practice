import cv2
import datetime

# first bit of work with video

cap = cv2.VideoCapture('FallGuys.mp4')


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        datet = str(datetime.datetime.now()) # gets updated date and time and binds to datet which is a string of the date/time
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts video capture to gray
        font = cv2.FONT_HERSHEY_SIMPLEX # assigns a font to the font variable
        cv2.putText(gray, datet, (10, 50), font, 1, (0, 255, 0), 5, cv2.LINE_AA) # puts text, datet, on the gray capture in the top left corner with our font
        cv2.imshow('frame', gray) # display frame

        if cv2.waitKey(1) & 0XFF == ord('q'): # if q is pressed 
            cv2.destroyAllWindows() # destroys all windows
            break
