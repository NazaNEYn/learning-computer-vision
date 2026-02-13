# Shape Detection

## Goal:
Look at an image, find shapes, decide what they are, and draw boxes around them.


## Mental Model

**A computer does NOT “see” circles or rectangles.**

It does this instead:

1. Finds white blobs (contours)
2. Measures each blob
3. Asks simple questions:
   * How big is it?
   * How big is it?
   * Is it wide or tall?
   * How smooth is it?
  
From those answers → **decision**



## Tools You Need (Small Set)

You only need 5 things:

| Tool | Purpose |
| :--- | :--- |
| **`cv2.findContours()`** | Find objects |
| **`cv2.contourArea()`** | Ignore tiny junk |
| **`cv2.boundingRect()`** | Draw a box |
| **`cv2.approxPolyDP()`** | Count corners |
| **`cv2.arcLength()`** | Shape perimeter |



## The Full Pipeline
```python
Color image                ← humans
   ↓
Grayscale                  ← remove color distraction
   ↓
Blur                        ← remove noise
   ↓
Threshold OR Edges          ← separate objects
   ↓
Contours                    ← shapes as data
   ↓
Analyze contour geometry    ← numbers
   ↓
Decide shape                ← logic
   ↓
Draw result on color image  ← humans again
```

### 1. `cv2.findContours()`

**What it does**:<br>
Finds **object outlines** in a **binary image**.

**Syntax**:
```python
contours, hierarchy = cv2.findContours(
    binary_image,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

**What you get**:
* `contours` → a list of contours
* each contour → an array of `(x, y)` points
* `hierarchy` → parent/child info (ignored for now)

**Mental Imaage**:
```
███████     █████
█     █     █   █
███████     █████
```

→ Two contours (two shapes)<br>

**Important rules**:
* Works on binary images
* Doesn’t draw anything
* Just gives you **data**

### 2. `cv2.contourArea()`

**What it does**:<br>
Tells you **how big a contour** is (in pixels).

**Syntax**:
```python
area = cv2.contourArea(contour)
```

**What you get**
* A single number
* Roughly = number of pixels inside shape


Example:
```python
for cnt in contours:
    area = cv.contourArea(cnt)
    print(f"contour Area: {area}")
```

Result:
```python
# 185.5
# 39192.5
# 657.0
# 111.0
```

*Note:* `contours` is a list contours. So in order to get the areas, we need to loop through the list.


**Mental image**:

| Shape | Area |
| :--- | :--- |
| **Tiny dot** | 20 |
| **Coin** | 5,000 |
| **Box** | 30,000 |


**Why it matters**:
* Remove noise
* Ignore tiny junk
* Focus on real objects

```python
if area < 500:
    continue
```

Example:
```python
for cnt in contours:
    area = cv.contourArea(cnt)
    if area < 500:
        continue
    print(f"Keeping object with area: {area}")
```

Result:
```python
length: 34
# Keeping object with area: 9086.5
# Keeping object with area: 39192.5
# Keeping object with area: 657.0
# Keeping object with area: 42689.5
# Keeping object with area: 618.5
# Keeping object with area: 62139.0
```

## `cv2.boundingRect()`

**What it does**:
`boundingRect()` is the easiest way to put a "box" around an object.<br>
It takes a contour (that complex list of points) and simplifies it into a simple, straight rectangle

**Syntax**:

```python
x, y, w, h = cv2.boundingRect(contour)
```

**Mental image**:
```python
   +--------+
   |  ◯     |
   |        |
   +--------+
```

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/58a566ee-733f-4bab-ad04-d318c44b59ab" />
<br>

Bounding box doesn’t care about shape — just size & position.<br>

![Gemini_Generated_Image_h1vofph1vofph1vo](https://github.com/user-attachments/assets/032162c3-e5cc-42de-8e68-b84576787ae6)



**Why it matters**:
* Locate objects
* Crop them
* Draw boxes
* Measure proportions


