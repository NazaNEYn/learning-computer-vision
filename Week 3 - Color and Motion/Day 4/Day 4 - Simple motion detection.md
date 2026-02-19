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

## The core idea

If something moves:
* its pixels change position
* pixel values change between frames

```python
current_frame − previous_frame = difference
```

If the difference is big → motion happened.

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

## Mental model
* Motion = difference between frames
* Big difference = real movement
* Small difference = noise
This is **frame-difference motion**, not AI.
