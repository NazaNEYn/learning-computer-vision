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

---

## `scaleFactor` - “How carefully do I look at sizes?”

OpenCV scans the image, then shrinks the image and scans again, then shrinks again and scans again, and so on.<br>


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

**Think of it like zoom steps**<br>
Imagine you’re looking for a face on a photo wall.
* `1.1` → you zoom **very slowly**
* `1.3` → you zoom **in big jumps**

![Gemini_Generated_Image_pwnsuvpwnsuvpwns](https://github.com/user-attachments/assets/1c708dd1-dce4-43b1-8d14-e458af659ec5)


**What changes when the number increases?**

| scaleFactor | What happens |
| :--- | :--- |
| 1.1 | many scans → slow → misses fewer faces |
| 1.2 | fewer scans → faster |
| 1.3 | very few scans → fast → misses small faces |



| scaleFactor | Mechanism | Strategy | Detection Performance | Speed |
| :--- | :--- | :--- | :--- | :--- |
| **1.1** | many small steps | slow climb, careful scanning | catches more face sizes, more faces detected, more stable boxes | slower |
| **1.3** | few big steps | fast jump, skips sizes in between | may miss faces, boxes less stable | faster |


![Gemini_Generated_Image_w8wv93w8wv93w8wv](https://github.com/user-attachments/assets/5f21cb7b-194a-4885-8593-bd326b4a2630)


## The Lock and Key analogy


Think of the detection process as a **Lock and Key** mechanism where the goal is to find a perfect fit.

**1. The Key (The Magnifying Glass)** <br>
In this scenario, the **Key** is your **Fixed-Size Magnifying Glass** (usually $24 \times 24$ pixels). This key is rigid—it cannot grow or shrink. It only knows how to "unlock" a face if that face matches its exact size.<br>

**2. The Lock (The Face in the Image)** <br>
The Lock is the face you are trying to detect. However, since people can be close to the camera or far away, these "locks" appear in all different sizes throughout your photo.

**3. The Problem: A Mismatch** <br>
If a face is very close to the camera, it might be $200 \times 200$ pixels. Your $24 \times 24$ Key is far too small to fit into that giant Lock. Because they don't match, the computer reports: "No face detected." <br>

**4. The Solution: Shrinking the Image (`scaleFactor = 1.1`)** <br>
Since we cannot change the size of the **Key**, we must change the size of the **Lock**.  
* **The First Pass**: The computer tries the key on the original image. It only finds tiny faces far in the distance.
* **The Shrink**: The `scaleFactor` of 1.1 kicks in. It shrinks the entire image by 10%. This makes the "Lock" (the face) smaller, effectively pushing it "further away" from the lens.
* **The Repeat**: It keeps shrinking the image layer by layer. Eventually, that giant face is resized until it hits exactly $24 \times 24$ pixels.
* **The Click**: Finally, the **Lock** fits the **Key** perfectly. **Click**! The magnifying glass recognizes the face and draws a box around it.

<br> 
    
![Gemini_Generated_Image_mdof5wmdof5wmdof](https://github.com/user-attachments/assets/f85858e8-5041-4660-9b2f-634665dbf75a)


**Rule of thumb**
* Start with `1.1`
* Increase if detection is slow
* Decrease only if missing faces


---

## `minNeighbors` - “How sure do I need to be?”

During detection, OpenCV finds many overlapping or very close rectangles.<br>
Each rectangle is like a vote saying “this might be a face.”<br>
If the number of overlapping rectangles is greater than or equal to `minNeighbors`, OpenCV accepts it as a face; otherwise, it rejects it.<br>

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


---

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

![Gemini_Generated_Image_m3r6tdm3r6tdm3r6](https://github.com/user-attachments/assets/f5f7e711-3d22-47ac-a3dd-27441e2daeba)

![Gemini_Generated_Image_ckjzkdckjzkdckjz](https://github.com/user-attachments/assets/e17a7398-9dd5-4d8a-82d6-8d27b0c5a204)


**General rule**<br>
If you detect on a resized image, you must scale the coordinates back before drawing on the original image.


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
