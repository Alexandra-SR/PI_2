import face_recognition
import os
import cv2
import numpy as np
import glob
import time


def runTest():
    flag = False
    # To capture a video, you need to create a VideoCapture object (#0-the default one)
    video_cap = cv2.VideoCapture(0)

    known_face_encodings = []
    known_face_names = []
    known_dir = 'known'

    for file in os.listdir(known_dir):
        img = face_recognition.load_image_file(known_dir + '/' + file)
        img_enc = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(img_enc)
        known_face_names.append(file.split('.')[0])

    # Initialize some variables
    face_locations = []
    face_encodings = []
    process_this_frame = True

    while True:
        # Capture frame-by-frame (a single frame)
        ret, frame = video_cap.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            best_matches = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match = np.min(face_distances)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)
                best_matches.append(best_match)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name, best_match in zip(face_locations, face_names, best_matches):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            if best_match <= 0.5:
                # Draw a box around the face
                cv2.rectangle(frame, (left, top),
                              (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35),
                              (right, bottom), (0, 255, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name + str(np.round(best_match, 3)),
                            (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            else:
                name = "Unknown"
            # Draw a box around the face
                cv2.rectangle(frame, (left, top),
                              (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35),
                              (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name + str(np.round(best_match, 3)),
                            (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('PI2 - Face recognition', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            flag = True
            break

    # Release handle to the webcam
    video_cap.release()
    cv2.destroyAllWindows()
    return flag


def testPictureSignUp():
    flag = False
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            flag = True
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "image_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    return flag


def login(username):
    # primero colocar el username de usario
    if os.path.isdir("known_users/" + username):
        print("The username exists")
        video_cap = cv2.VideoCapture(0)
        known_face_encodings = []
        known_face_names = []
        known_dir = "known_users/" + username
        for file in os.listdir(known_dir):
            # print(len(os.listdir(known_dir)))
            img = face_recognition.load_image_file(known_dir + '/' + file)
            img_enc = face_recognition.face_encodings(img)
            if len(img_enc) > 0:
                img_enc = img_enc[0]
                known_face_encodings.append(img_enc)
                known_face_names.append(file.split('.')[0])
                print('done')
            else:
                print("empty")
        # Initialize some variables
        face_locations = []
        face_encodings = []
        process_this_frame = True
        probar = 0
        start = time.time()
        end = start
        print("out")
        while (probar == 0 and end - start < 10):

            # Capture frame-by-frame (a single frame)
            ret, frame = video_cap.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(
                    rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)

                face_names = []
                best_matches = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(
                        known_face_encodings, face_encoding)
                    name = "Unknown"

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(
                        known_face_encodings, face_encoding)
                    best_match = np.min(face_distances)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)
                    best_matches.append(best_match)

            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom, left), name, best_match in zip(face_locations, face_names, best_matches):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                if best_match <= 0.5:
                    # Draw a box around the face
                    cv2.rectangle(frame, (left, top),
                                  (right, bottom), (0, 255, 0), 2)

                # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35),
                                  (right, bottom), (0, 255, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name + str(np.round(best_match, 3)),
                                (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    print('detected')
                    time.sleep(2)
                    probar = best_match
                    video_cap.release()
                    cv2.destroyAllWindows()
                    return (True, True)
                    # break  #cerrar ciclo pero tambien deberia haber una mayor comprobacion del reconocimiento

                else:
                    name = "Unknown"
                 # Draw a box around the face
                    cv2.rectangle(frame, (left, top),
                                  (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35),
                                  (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name + str(np.round(best_match, 3)),
                                (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                # break
            # break no sale la camara

            # Display the resulting image
            cv2.imshow('PI2 - Face recognition', frame)
            end = time.time()
            print(end - start)
            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_cap.release()
        cv2.destroyAllWindows()
        return (True, False)
    else:
        return (False, False)


def signup(username):
    try:
        os.makedirs("known_users/" + username)
        print("Directory ", username,  " Created ")
        # To capture a video, you need to create a VideoCapture object (#0-the default one)
        video_cap = cv2.VideoCapture(0)

        face_classif = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        s = 0
        q = 0

        while True and s < 20:
            ret, frame = video_cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_classif.detectMultiScale(gray, 1.3, 5)

            q = s

            # Put rectangle in face
            for(x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                rostro = frame
                s = s+1
                if s > 10:
                    cv2.imwrite('known_users/'+username+'/'+username+'_{}.jpg'.format(len(glob.glob(
                        'known_users/'+username+'/'+'*.jpg'))), rostro)  # falta quitarle el texto en la foto
                    print("Face saved")
                print(s)

            if q == s:
                s = 0

            # Display the resulting image
            cv2.imshow('PI2 - Face detection', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if len(glob.glob('known_users/'+username+'/'+'*.jpg')) > 10:
                for f in glob.glob('known_users/'+username+'/'+'*.jpg'):
                    os.remove(f)
                s = 0

        # Release handle to the webcam
        video_cap.release()
        cv2.destroyAllWindows()
        print("REGISTRO COMPLETADO CON EXITO! ")
        return True

    except FileExistsError:
        print("Directory ", username,  " already exists")
        return False
