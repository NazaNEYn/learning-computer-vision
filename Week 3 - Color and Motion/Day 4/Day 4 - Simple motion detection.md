# Simple motion detection

## What problem are we solving?

We are **not** asking:
* “What object is this?”
* “What color is this?”

We are asking one simple question:<br>
> **Did something change between two moments in time?**

## What motion means in CV

Motion does not exist in one image.<br>
<br>
Motion only exists when you compare:
```python
Frame at time t
vs
Frame at time t+1
```

So motion detection is really:<br>
> **change over time**


## Why color is ignored

Color is:
* Unstable
* Sensitive to lighting
* Irrelevant for movement

Motion cares about:
* Intensity change

So first step is always:
```python
Frame → Grayscale
```

This removes:
*Color noise
* Channel complexity


## Why blur is necessary

Real cameras are noisy:
* Sensor flicker
* Compression artifacts
* Tiny pixel changes

If you compare frames directly:
* Everything looks like motion


Blur:
* Smooths small changes
* Keeps large changes

So second step:
```python
Grayscale → Blur
```

## The core idea

If something moves:
* its pixels change position
* pixel values change between frames

```python
difference = current_frame − previous_frame 
```

If the difference is big → motion happened.


## What “difference” really means
OpenCV uses:
```python
cv.absdiff(prev_frame, current_frame)
```

This computes:<br>
> “How much did each pixel change?”

* Black (0) → no change
* White (255) → big change

The result is an image of motion intensity.


## Why we store the previous frame

Motion is about **change**, so we need memory.

We store:
```python
previous_frame = current_frame
```
At the end of each loop.

Without this:
* You can’t detect motion
* You only see static images

## Why thresholding comes next

The difference image still contains:
* Small lighting flicker
* Tiny movements
* Camera noise

Thresholding answers:<br>
> “Is this change big enough to care about?”

* Below threshold → ignore (black)
* Above threshold → motion (white)

* White = moving region
* Black = no movement

So thresholding turns motion intensity into a clear decision: moving vs not moving.

## Why contours are used

After thresholding, you have:
* A binary image
* White blobs = moving areas

Contours allow us to:
* Group motion pixels
* Measure motion size
* Draw boxes around motion
* Ignore tiny random movement

## Summary
* **Grayscale** → motion depends on intensity, not color
* **Blur** → removes noise and tiny pixel flickers
* **Frame** comparison → motion = change over time
* **Threshold** → separates motion from no motion
* **Contours** → group motion into meaningful regions we can draw and analyze


## The classic motion detection pipeline

```python
Frame 1
  ↓
Grayscale → Blur
  ↓
Store as previous_frame

Frame 2
  ↓
Grayscale → Blur
  ↓
Absolute difference (Frame2 - Frame1)
  ↓
Threshold
  ↓
Contours (moving regions)
```

Repeat for every frame.



## Why the first frame is special

On the first frame:
* There is no “previous frame”

So we:
* Process it
* Store it
* Skip motion detection

## What simple motion detection can do
* Detect movement
* Draw bounding boxes
* Detect entry / exit
* Count motion events

## What it CANNOT do
* Identify objects
* Track specific people
* Understand intent
* Handle camera movement

This is **frame-difference motion**, not AI.

## Mental model
* Motion = difference between frames
* Big difference = real movement
* Small difference = noise


## Why static camera matters

If the camera moves:
* Entire frame changes
* Everything becomes “motion”

So this method assumes:
* Camera is fixed

---

## Example

```python
import cv2 as cv
import numpy as np

# Open video file
cap = cv.VideoCapture("video.mp4")

# Read first frame
ret, frame = cap.read()
if not ret:
    print("Failed to read video")
    exit()

# Prepare first frame
prev_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
prev_gray = cv.GaussianBlur(prev_gray, (15, 15), 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert current frame to grayscale and blur
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (15, 15), 0)

    # Compute difference
    diff = cv.absdiff(prev_gray, gray)

    # Threshold the difference
    _, motion_mask = cv.threshold(diff, 30, 255, cv.THRESH_BINARY)

    # Find contours (motion regions)
    contours, _ = cv.findContours(
        motion_mask,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE
    )

    # Draw bounding boxes for significant motion
    for cnt in contours:
        if cv.contourArea(cnt) < 800:
            continue

        x, y, w, h = cv.boundingRect(cnt)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # converting to RGB for kaggle notebook
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    plt.imshow(rgb_frame)
    plt.axis("off")

    # Update previous frame
    prev_gray = gray

cap.release()
```
