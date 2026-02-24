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
