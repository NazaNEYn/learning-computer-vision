# How OpenCV Opens & Reads a Video

## Goal of today’s lesson

* What a video is in CV terms
* How OpenCV reads video frame by frame
* How each frame is just an image
* Where your existing image-processing pipeline fits

## What OpenCV sees when it opens a video

To humans:
* A video = moving pictures + sound<br> 

To OpenCV:
* ❌ Sound doesn’t exist
* ❌ Motion doesn’t exist 
* ✅ A video = a sequence of images stored in order

So OpenCV treats a video like:
```python
image_0001.jpg
image_0002.jpg
image_0003.jpg
...
```
But stored efficiently in one file.


## Opening a video file
```python
cap = cv.VideoCapture("video.mp4")
```

## Reading frames

```python
ret, frame = cap.read()
```

* `ret` → True / False
* `frame` → the actual image (same format as `cv.imread`)



### What is `frame`?

`frame` = the next image in the video

* Type: NumPy array
* Shape: `(H, W, 3)`
* Same as `cv.imread()`

> A frame is just an image.

### What is `ret`?

`ret` is a **boolean flag**.<br>
> `ret` **tells you whether OpenCV successfully read a frame.**

* `True` → frame was read correctly
* `False` → no frame available

If `ret == False`:
* The video **ended**
* The file **failed to open**
* The frame **couldn’t be decoded**

## The basic video loop
```python
while True:
    ret, frame = cap.read()

    if not ret:
        break
```

## Treat each frame like an image
Inside the loop:
```python
frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
```

From here, you can do anything you already know:
* grayscale
* HSV
* color masks
* contours
* drawing

## Minimal example

```python
cap = cv.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv.imshow("Video", frame)

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
```
