# Morphology

## The problem morphology solves

After this line:
```python
orange_mask = cv.inRange(hsv, lower_orange, upper_orange)
```

You get a binary image:
* white (255) → “this pixel looks orange”
* black (0) → “this pixel doesn’t”

But real life is messy.<br>

Typical problems:
* tiny white dots (noise)
* holes inside the object
* broken shapes
* jagged edges

Your computer sees **many small blobs** instead of **one clean object**. <br>

Morphology fixes *the shape of the mask*.

## What morphology actually does (simple mental model)

* Morphology **edits shapes** in a black-and-white image
* using a **small sliding window**.

It does NOT:
* detect color
* detect edges
* detect objects

It only answers:
* “Which white pixels should stay?”
* “Which white pixels should disappear?”

## The kernel

```python
kernel = np.ones((5, 5), np.uint8)
```


## Morphology operations

### OPEN — remove small noise

```python
clean = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
```

**OPEN = erosion → dilation**

* **Erosion**: The "Shrinker"
In plain English, Erosion erodes away the boundaries of foreground objects (usually the white pixels).
* **Dilation**: The "Expander
Dilation is the exact opposite. It adds pixels to the boundaries of objects in an image.

What it does:
* removes tiny white dots
* keeps large shapes

Think:<br>
> “Delete small garbage”<br>

**Before OPEN**:
```
..#...#..
.###.###.
..#...#..
```

**After OPEN**:
```
.........
.###.###.
.........
```


Use OPEN when:
* you see random speckles
* contours flicker
* small false detections appear

### CLOSE — fill holes and connect shapes

```python
clean = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
```

**CLOSE = dilation → erosion**

* **Erosion**: The "Shrinker"
In plain English, Erosion erodes away the boundaries of foreground objects (usually the white pixels).
* **Dilation**: The "Expander
Dilation is the exact opposite. It adds pixels to the boundaries of objects in an image.


What it does:

* fills holes inside objects
* connects broken regions

Think:<br>
> “Repair the object”<br>

**Before CLOSE**:
```
.####.
.##..#
.####.
```

**After CLOSE**:
```
.#####.
.#####.
.#####.
```

Use CLOSE when:
* objects look broken
* bounding boxes jump around
* shapes are incomplete
