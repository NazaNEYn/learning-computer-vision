# Detect faces in video

## You are learning:

* how image-based face detection behaves over time
* how to run detection frame by frame
* what problems appear only in video
* how to think about speed and stability

# Key mindset shift

**Image detection:** <br>
> “Detect faces once.”

**Video detection:** <br>
> “Detect faces again and again — for every frame.”

## The video face detection pipeline
```python
Open video
↓
Read frame
↓
Convert to grayscale
↓
Detect faces
↓
Draw rectangles
↓
Show frame
↓
Repeat
```

This is almost identical to:
* your motion detection loop
* your color tracking loop

## 1. Open a video file
```python
video_path = "video.mp4"
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    raise IOError("Cannot open video")
```

## 2. Load the Haar face model (once)
Load the model **outside the loop**.

```python
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    raise IOError("Failed to load Haar cascade")
```

Why?
* loading is expensive
* the model does not change per frame

## 3. Frame-by-frame detection loop
```python
while True:
    ret, frame = cap.read()
    if not ret:
        break
```

## 4. Convert frame to grayscale
```python
gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
```

## 5. Detect faces in the frame
```python
faces = face_cascade.detectMultiScale(gray)
```

This runs:
* on every frame
* independently
* with no memory of previous frames

Important:<br>
> The detector does NOT know this is a video.

## 6. Draw bounding boxes
```python
for (x, y, w, h) in faces:
    cv.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )
```
Each frame gets fresh rectangles.

## 7. Display the frame
```python
rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.axis("off")
plt.show()
```

## Full code snippet
```python
import cv
import matplotlib.pyplot as plt

cap = cv.VideoCapture("video.mp4")

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    raise IOError("Failed to load Haar cascade")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    plt.imshow(rgb)
    plt.axis("off")
    plt.show()
    break  # remove this to process entire video

cap.release()
```

## Full code snippet (limiting the frames)
```python
video_path = "/kaggle/input/datasets/nazaninashrafi/face-detection/14737067_1920_1080_60fps.mp4"
cap = cv.VideoCapture(video_path)


face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    raise IOError("Failed to load")

output_frames = []

while len(output_frames) < 8:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame)

    for(x,y,w,h) in faces:
        cv.rectangle(
            frame,
            (x,y),
            (x+w, y+h),
            (0,255,0),
            4
        )

    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    output_frames.append(rgb_frame)

cap.release()

plt.figure(figsize=(15,20))
for i,img  in enumerate(output_frames):
    plt.subplot(4,2,i + 1)
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"Frame: {i + 1}")

plt.show()
```

