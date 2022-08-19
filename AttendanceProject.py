def DetectFace():
    runFull = True
    while runFull:
        # global i
        import cv2
        import numpy as np 
        import face_recognition
        import os
        import pyttsx3
        # from chat import speak
        # import time

        path = 'ImagesAttendance'
        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        print(classNames)

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # resized = cv2.resize(img, (600, 600))
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        encodeListKnown = findEncodings(images)
        print('Encoding Completed')
        speak('Encoding Completed')

        cap = cv2.VideoCapture(0)

        i = 0
        runCam = True
        while runCam:
            i = i + 1
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print("done till here")
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex]
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(img, (x1, y1), (x2, y2),(0, 255 ,0), 2)
                    cv2.rectangle(img, (x1, y2-35), (x2, y2),(0, 255 ,0), cv2.FILLED)
                    cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


            a = 'continue'
            cv2.imshow('Webcam', img)
            k=cv2.waitKey(1)
            if k%256==27:
                print("close")
                print(i)
                runCam = False
                runFull = False
            
            if i == 1500:
                speak(f' {i} rounds is over,,, should i continue the webcam')
                print(f' {i} rounds is over,,, should i continue the webcam')
                run20 = input("continue? ")
                if run20 == "no":
                    a = 'stop'
                    runCam = False
                    runFull = False
                else:
                    i=0
                    continue

            if a=='stop':
                runCam = False
                runFull = False

        cap.release()
        cv2.destroyAllWindows()