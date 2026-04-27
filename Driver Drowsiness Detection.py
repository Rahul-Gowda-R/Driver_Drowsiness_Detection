import cv2
import time
import winsound
import mediapipe as mp

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)
time.sleep(2)

closed_eyes_frames = 0
yawn_frames = 0
no_face_frames = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1024, 576))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 🚨 Driver not detected logic
    if len(faces) == 0:
        no_face_frames += 1
    else:
        no_face_frames = 0

    if no_face_frames == 30:
        winsound.Beep(1500, 700)

    if no_face_frames > 30:
        cv2.putText(frame, "Driver Not Detected!", (300, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

    # 😮 MediaPipe Yawning Detection (run once per frame)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    yawning = False

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            upper_lip = face_landmarks.landmark[13]
            lower_lip = face_landmarks.landmark[14]

            h_frame, w_frame, _ = frame.shape

            upper_y = int(upper_lip.y * h_frame)
            lower_y = int(lower_lip.y * h_frame)

            mouth_open = abs(lower_y - upper_y)

            cv2.putText(frame, f"Mouth Open: {mouth_open}", (400, 140),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (255, 255, 255), 2)

            if mouth_open > 25:
                yawning = True

    # Stable yawning logic
    if yawning:
        yawn_frames += 1
    else:
        if yawn_frames > 0:
            yawn_frames -= 1   # smooth decay

    if yawn_frames == 15:
        winsound.Beep(1200, 600)

    if yawn_frames > 15:
        cv2.putText(frame, "Yawning!", (400, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

    # 👤 Face + Eye Detection
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # 👀 Eye detection
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 5)

        if len(eyes) == 0:
            closed_eyes_frames += 1
        else:
            closed_eyes_frames = 0

        # 🔊 Sound trigger
        if closed_eyes_frames == 20:
            winsound.Beep(1000, 500)

        # ⚠️ Drowsy alert
        if closed_eyes_frames > 20:
            cv2.putText(frame, "DROWSY!", (400, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 3)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex+ew, ey+eh), (255, 0, 0), 2)

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()