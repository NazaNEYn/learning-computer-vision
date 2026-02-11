# Contours and shape detection

## What are contours
A contour is a curve that traces the boundary of an object.<br>
<br>

If thresholding gives you:
* **regions** (filled areas)

Contours give you:
* **outlines of those regions**

Think:
* Threshold = “this area belongs to the object”
* Contours = “this is the shape of the object”

### Visual intuition

Imagine a black silhouette on white paper:
* Threshold → fills the silhouette
* Contours → draws a line around it

That line is the contour.

## Where contours fit in the pipeline

* **Most common (beginner & stable)**:
```python
color → grayscale → blur → threshold → contours
```

* **Alternative (shape-focused)**:
```python
color → grayscale → blur → edges → contours
```
