# Contours and shape detection

## What are contours
A contour is:
* a list of points
* that trace the boundary of a connected white region

Not an image.<br>
Not pixels.<br>
Not edges.<br>
<br>

**Contours are geometry.**

If thresholding gives you:
* **regions** (filled areas)

Contours give you:
* **outlines of those regions**

Think:
* Threshold = “this area belongs to the object”
* Contours = “this is the shape of the object”

### Visual intuition

Imagine this binary image:
```python
⬛⬛⬛⬛⬛⬛
⬛⬜⬜⬜⬛⬛
⬛⬜⬜⬜⬛⬛
⬛⬛⬛⬛⬛⬛
```

* Threshold → one white blob
* Contours → draws a line around it


## Where contours fit in the pipeline

* **Most common (beginner & stable)**:
```python
color → grayscale → blur → threshold → contours
```

* **Alternative (shape-focused)**:
```python
color → grayscale → blur → edges → contours
```

## `findContours()`
```python
contours, hierarchy = cv2.findContours(
    binary_image,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

### 1. Retrieval mode `(cv2.RETR_EXTERNAL)`:

This answers:
> “Which contours do you want?”

`RETR_EXTERNAL`:
* only outer boundaries
* ignores holes

Example:
* letter “O” → only outer circle
* donut → only outside edge

### 2. Approximation method `(CHAIN_APPROX_SIMPLE)`

This answers:
> “How many points should describe the contour?”

Without approximation:
* every pixel on the edge = a point
* huge memory usage

With `CHAIN_APPROX_SIMPLE`:
* straight lines are compressed
* corners are preserved

Same shape, fewer points.
