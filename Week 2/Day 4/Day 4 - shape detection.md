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

**what `x, y, w, h` mean**:
```python
(x, y)  → top-left corner of the box
w       → width  (how far to the right)
h       → height (how far down)
```

So the rectangle goes from:
```python
(x, y) → (x + w, y + h)
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

![Gemini_Generated_Image_49hk4449hk4449hk](https://github.com/user-attachments/assets/037b18be-5c6c-4fbf-8348-98f0b59acc62)


**Why it matters**:
* Locate objects
* Crop them
* Draw boxes
* Measure proportions


### Example

* **Draw one contour/object**

```python
image_path = "/kaggle/input/datasets/nazaninashrafi/img-testt/2224564.jpg"
image = cv.imread(image_path)
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

gray = cv.cvtColor(image_rgb, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (9,9), 0)

_, binary = cv.threshold(blur, 127, 255, cv.THRESH_BINARY_INV)

contours, _ = cv.findContours(
    binary,
    cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_SIMPLE
)

output = image_rgb.copy()


cnt = contours[5]  # take one object

x, y, w, h = cv.boundingRect(cnt)
print(x, y, w, h)

cv.rectangle(output,
             (x,y),
             (x+w, y+h),
             (0,255,0),
             2
            )

plt.imshow(output)
```

<img width="617" height="309" alt="image" src="https://github.com/user-attachments/assets/d519f590-226b-49b0-8cb9-9324e1ce6c01" />

<br>

* **Draw a bounding box**

```python
for cnt in contours:
    area = cv.contourArea(cnt)
    if area < 500:
        continue

    # FIX: Use 'cnt', not 'contours'
    x, y, w, h = cv.boundingRect(cnt) 
    
    cv.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )
```

```python
image_path = "/kaggle/input/datasets/nazaninashrafi/img-testt/2224564.jpg"
image = cv.imread(image_path)
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

gray = cv.cvtColor(image_rgb, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (9,9), 0)

_, binary = cv.threshold(blur, 127, 255, cv.THRESH_BINARY_INV)

contours, _ = cv.findContours(
    binary,
    cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_SIMPLE
)

output = image_rgb.copy()


for cnt in contours:
    area = cv.contourArea(cnt)
    if area < 500:
        continue

    x, y, w, h = cv.boundingRect(cnt)
    
    cv.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        4
    )

plt.imshow(output)
```
<img width="720" height="352" alt="image" src="https://github.com/user-attachments/assets/1d7d0053-ff76-4943-8095-4738800ef2f0" />


## `arcLength()`

**What it does**:
Measures **how long the contour edge is.**<br>
<br>
Think of it as:
Walking around the shape’s outline with a measuring tape.

**Syntax**:
```python
perimeter = cv2.arcLength(contour, True)
```
`True` → shape is closed

**What you get**:
A single number (length in pixels)

**Mental image**:

| Shape | Perimeter |
| :--- | :--- |
| **Small square** | Short |
| **Big circle** | Long |
| **Star** | Very long |


**Why it matters**:
* Used to scale other operations
* Makes algorithms size-independent

### Example:
```python
for cnt in contours:
    perimeter = cv.arcLength(cnt, True)
    print(f"Object perimeter: {perimeter:.2f}")
```


## `approxPolyDP()`

**What it does**:
Simplifies a contour into fewer points.<br>
<br>

It turns:
* hundreds of tiny points → a **clean polygon**

**Syntax**:
```python
approx = cv2.approxPolyDP(
    contour,
    epsilon,
    True
)
```
Where:
```python
epsilon = 0.04 * perimeter
```

```python
epsilon = 0.01 * perimeter   # very detailed
epsilon = 0.04 * perimeter   # common
epsilon = 0.1  * perimeter   # very rough
```

**What you get**:
* A simplified contour
* Fewer points
* Each point ≈ **a corner**

**Mental image**:

| Shape | Points |
| :--- | :--- |
| **Triangle** | 3 |
| **Rectangle** | 4 |
| **Circle** | Many |

**Why it matters**:
* Count corners
* Identify shapes
* Reduce noise


### Example:
```python
# approx = cv.approxPolyPD(cnt, epsilone,True)
# epsilon = 0.04 x perimeter
# perimeter = cv.arcLength(cnt, True)

for cnt in contours:

    perimeter = cv.arcLength(cnt, True)
    epsilon = 0.04 * perimeter
    approx = cv.approxPolyDP(cnt, epsilon,True)

    print("Number of points:", len(approx))
```
Result:
```python
# Number of points: 5
# Number of points: 4
# Number of points: 6
# Number of points: 7
# Number of points: 4
```

```python
for cnt in contours:
    area = cv.contourArea(cnt)
    if area < 500:
        continue

    # 1. Calculate the perimeter (arc length)
    perimeter = cv.arcLength(cnt, True)

    # 2. Approximate the shape
    epsilon = 0.02 * perimeter
    approx = cv.approxPolyDP(cnt, epsilon, True)

    # 3. Draw the approximated contour
    # We use [approx] because drawContours needs a LIST of shapes
    cv.drawContours(output, [approx], -1, (0, 255, 0), 4)
```

## How They Connect

| Function | Role |
| :--- | :--- |
| **`findContours()`** | Find objects |
| **`contourArea()`** | Filter objects |
| **`arcLength()`** | Measure shape |
| **`approxPolyDP()`** | Understand shape |
| **`boundingRect()`** | Locate & draw |

## Summary

| Tool | Question it answers |
| :--- | :--- |
| **findContours** | What objects exist? |
| **contourArea** | Is this object important? |
| **boundingRect** | Where is it? |
| **arcLength** | How complex/large is it? |
| **approxPolyDP** | What shape is it? |
