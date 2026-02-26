# Improve accuracy & speed

## What Day 4 is about
* reduce false positives
* reduce flickering
* speed up detection
* understand *why* tuning works
We’ll do this by controlling **how the detector searches**.

## The most important function today
```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)
```

### `scaleFactor` (how the image is scanned)

**Problem it solves**<br>

Faces can appear:<br>
* A face close to the camera → big
* A face far away → small

But the Haar detector:
* has a fixed-size face template
* can’t magically detect all sizes at once

So OpenCV:
* resizes the image many times
* checks each size for faces

**What `scaleFactor` means**<br>
> How much smaller the image becomes at each step.
<br>

Example:
```
1.1 → very fine search → slower → more accurate
1.3 → coarse search → faster → less accurate
```

**Think of it like zooming**

* `scaleFactor` = 1.05 → slow, careful zoom
* `scaleFactor` = 1.1 → normal zoom
* `scaleFactor` = 1.3 → aggressive zoom


![Gemini_Generated_Image_pwnsuvpwnsuvpwns](https://github.com/user-attachments/assets/1c708dd1-dce4-43b1-8d14-e458af659ec5)


**Rule of thumb**
* Start with `1.1`
* Increase if detection is slow
* Decrease only if missing faces

### `minNeighbors` (how strict the detector is)

**Problem it solves**<br>

Sometimes the detector sees:
* shadows
* patterns
* background textures

and thinks they’re faces.

**What `minNeighbors` means**<br>
> How many overlapping detections are required to confirm a face.

Think:
* low value → “be optimistic”
* high value → “be confident”

**Typical values**
```
3 → many detections, many false positives
5 → balanced (recommended)
8 → very strict, fewer detections
```

![Gemini_Generated_Image_tusorztusorztuso](https://github.com/user-attachments/assets/32d3dd02-dbc1-46a4-9ecd-244d74f436f3)

## Resize frames to improve speed

**Why this works**<br>

Face detection cost grows with:
* image width
* image height

Smaller image → much faster detection

**Resize before detection**
```python
small_frame = cv.resize(frame, None, fx=0.5, fy=0.5)
gray_small = cv.cvtColor(small_frame, cv.COLOR_BGR2GRAY)
```

**Detect on the small image:**
```python
faces = face_cascade.detectMultiScale(
    gray_small,
    scaleFactor=1.1,
    minNeighbors=5
)
```

**Scale boxes back up**
```python
for (x, y, w, h) in faces:
    x = int(x * 2)
    y = int(y * 2)
    w = int(w * 2)
    h = int(h * 2)

    cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
```
This trick alone can make detection **2–4× faster**.


## Full code snippet for vscode
```python
import cv2 as cv

cap = cv.VideoCapture("video.mp4")

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for speed
    small = cv.resize(frame, None, fx=0.5, fy=0.5)
    gray = cv.cvtColor(small, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60)
    )

    for (x, y, w, h) in faces:
        x, y, w, h = x*2, y*2, w*2, h*2
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv.imshow("Face Detection", frame)
    if cv.waitKey(20) == 27:
        break

cap.release()
cv.destroyAllWindows()
```
