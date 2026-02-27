import cv2 as cv


video_path = "11111.mp4"
cap = cv.VideoCapture(video_path)

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)


while True:
    # Frame Source
    ret, frame = cap.read()
    if not ret:
        print("File wasn't found")
        break

    # Preprocessing
    resized_frame = cv.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
    gray_frame = cv.cvtColor(resized_frame, cv.COLOR_BGR2GRAY)

    # detecting possible face locations
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=7,
    )

    for x, y, w, h in faces:
        x, y, w, h = x * 2, y * 2, w * 2, h * 2
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Visualization
    cv.imshow("Face Detection", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv.destroyAllWindows()
