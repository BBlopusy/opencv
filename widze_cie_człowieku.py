"""
Wykrywa twarze z obrazu pozyskiwanego z kamery
z użyciem klasyfikatorów kaskadowych Haara.
"""
import cv2 as cv
import pyttsx3 as tts
import time



# Określa ścieżki do klasyfikatorów kaskadowych Haara biblioteki OpenCV.
path = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data'
face_cascade = cv.CascadeClassifier(path + '\haarcascade_frontalface_alt.xml')

cap = cv.VideoCapture()



_, frame = cap.read()
face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.2,
                                               minNeighbors=4) 
for (x, y, w, h) in face_rects:
    print('wykryłem twarz')
    


frame = cv.VideoCapture() 

engine=tts.init()
engine.setProperty('rate', 147)
engine.say('witaj człowieku')
engine.runAndWait() 
time.sleep(1)
# Określa ścieżki do klasyfikatorów kaskadowych Haara biblioteki OpenCV.
path = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data'
face_cascade = cv.CascadeClassifier(path + '\haarcascade_frontalface_alt.xml')

cap = cv.VideoCapture(0)

while True:
    # Przechwytuje kolejne ramki.
    _, frame = cap.read()
    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.2,
                                               minNeighbors=4)    

    for (x, y, w, h) in face_rects:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    # Wyświetla wynikową ramkę.
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Koniec przechwytywania obrazu wideo.
cap.release()
cv.destroyAllWindows()
