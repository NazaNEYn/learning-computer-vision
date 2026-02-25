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
