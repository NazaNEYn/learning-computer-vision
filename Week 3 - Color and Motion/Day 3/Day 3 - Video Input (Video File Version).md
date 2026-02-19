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

It:
* Opens the file
* Prepares a decoder
* Sets an internal pointer to **frame 0**

Think of it like opening a book:
* You don’t read all pages at once
* You open it and prepare to read page by page

### Why we don’t load the whole video at once

Videos can be:
* Thousands of frames
* Huge in memory
* Too slow to load entirely

So OpenCV:
* Reads one frame at a time
* Only when you ask for it

This is why `read()` exists.

## Reading frames

```python
ret, frame = cap.read()
```
This line does **three things internally**:

**Step A: Decode next frame**<br>
<br>
OpenCV asks:<br>
> “Is there another frame after the current one?”


**Step B: Try to read it**:<br>

* If yes → decode it into an image
* If no → stop

**Step C — Return results**:

* `ret` → success or failure
* `frame` → the image (if successful)

### What is `frame`?

`frame` = the next image in the video

* Type: NumPy array
* Shape: `(H, W, 3)`
* Color format : BGR (not RGB)
* Same as `cv.imread()`

> A frame is just an image.

### What is `ret`?

`ret` stands for **“return status”**.<br>
<br>
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

**Means**:<br>
> “Give me frames until there are no more.”

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

## Releasing the video
```python
cap.release()
```

This:
* Closes the file
* Frees memory
* Releases decoder resources

Always do this.

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
