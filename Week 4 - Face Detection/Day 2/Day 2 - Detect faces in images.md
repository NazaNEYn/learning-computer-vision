# Detect faces in images

## What you’ll learn today
* how to prepare an image for face detection
* how `detectMultiScale()` works (conceptually)
* what its parameters mean (without math pain)
* how to draw face boxes correctly
* why detection is never perfect

## The basic face detection pipeline (zoomed out)

Face detection in an image always follows this order:
```python
Load image
   ↓
Convert to grayscale
   ↓
Run face detector
   ↓
Get rectangles
   ↓
Draw rectangles
```

## 1. Load an image
```python
image_path = "face.jpg"
img = cv.imread(image_path)

if img is None:
    raise IOError("Could not load image")
```

## 2. Convert to grayscale
```python
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
```

**Why grayscale?**<br>
Because Haar models look for:<br>
* light vs dark patterns
* contrast relationships

Color information is ignored.

## 3. Load the Haar face model
```python
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    raise IOError("Failed to load Haar cascade")
```

## 4. Detect faces
```python
faces = face_cascade.detectMultiScale(gray)
```

**What this line does**<br>
> “Scan the image at multiple sizes and tell me where faces might be.”

**What faces looks like**<br>
If faces are found:
```
[
  [x, y, w, h],
  [x, y, w, h],
  ...
]
```

If no faces are found:
```python
[]
```
Each rectangle is **one detected face**.

## 5. Draw bounding boxes
```python
for (x, y, w, h) in faces:
    cv.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )
```

This line uses Python unpacking:<br>
`for (x, y, w, h) in faces:`<br>
* faces is not a list of face objects.
* It’s a list (actually a NumPy array) that looks like this:
  
  ```
  [
  [x1, y1, w1, h1],
  [x2, y2, w2, h2],
  [x3, y3, w3, h3]
  ]
  ```
* It means:
  > “For each item in `faces`, take the 4 values inside it and assign them to `x`, `y`, `w`, and `h`.”

You are **not modifying detection** here.<br>
you’re only visualizing the result.

## 6. Display the result
```python
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(rgb)
plt.axis("off")
plt.show()
```
## Full code snippet
```python
import cv
import matplotlib.pyplot as plt

# Load image
img = cv.imread("face.jpg")
if img is None:
    raise IOError("Could not load image")

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Load Haar cascade
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    raise IOError("Failed to load Haar cascade")

# Detect faces
faces = face_cascade.detectMultiScale(gray)

# Draw rectangles
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show result
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.axis("off")
plt.show()
```

## Why detection might fail
* not be detected at all
* be detected multiple times
* be detected on non-faces

Face detection is:<br>
> “best guess,” not “perfect truth”

