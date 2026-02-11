# The mental model (before code)

| Step | What you have |
| :--- | :--- |
| **Load image** | Photo |
| **Threshold** | Black & white mask |
| **findContours** | Shape data |
| **drawContours** | Visualization |

**Contours are NOT images**.<br>
They are **data extracted from an image**.

 # line-by-line example:

* 1. load an image
```python
image_path = "YOUR_IMAGE_PATH"
image = cv.imread(image_path)
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
```

* 2. convert to grayscale
```python
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
```

* 3. Threshold the image
```python
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
```

* 4. Find contours
```python
contours, hierarchy = cv.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

`contours` = List of shapes (data)<br>
`hierarchy` = Metadata (ignore for now)<br>

* 5. Copy the image before drawing

**Note**:
Draw on the **COLOR image**, not the binary one.<br>
We create a copy so we don't ruin the original variable

```python
img = image_rgb.copy()
```

* 6. Draw contours
```python
cv.drawContours(
    img,
    contours,
    -1,            # draw all contours
    (0, 255, 0),   # green
    2              # thickness
)
```

* 7. Display the result
```python
plt.imshow(img)
plt.axis("off")
```

**Full code snippet**:
```python
# 1. load an image
image_path = "/kaggle/input/datasets/nazaninashrafi/img-testt/111.jpg"
image = cv.imread(image_path)
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# 2. convert to grayscale
gray = cv.cvtColor(image_rgb, cv.COLOR_BGR2GRAY)

# 3. Threshold the image
_, binary = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

# 4. Find contours
contours, hierarchy = cv.findContours(
    binary,
    cv.RETR_EXTERNAL,
    
    cv.CHAIN_APPROX_SIMPLE
)

# 5. Copy the image before drawing
img = image_rgb.copy()

# 6. Draw contours
cv.drawContours(
    img,
    contours,
    -1,            # draw all contours
    (0, 255, 0),   # green
    2              # thickness
)

# 7. Display the result
plt.imshow(img)
plt.axis("off")
```


## How to think about it

`findContours()`:
> “Convert image → shape data”

`drawContours()`:
> “Convert shape data → pixels for humans”

They are two halves of the same operation:
* extract
* visualize
