# DAY 4 — Split Channels, Brightness & Contrast

---

## PART 1 — What are channels REALLY?

**Core truth:**
An RGB image is three grayscale images stacked together.<br>

Shape:
```python
(H, W, 3)
```

Think:

* **Channel 0** → Red intensity
* **Channel 1** → Green intensity
* **Channel 2** → Blue intensity

Each channel:

* Is (H, W)
* Values from 0 → 255

### Why CV cares about channels

Different tasks depend on different channels:

* **Faces** → skin tones (often red)
* **Roads** → brightness
* **Plants** → green channel
* **Medical imaging** → single channels

## PART 2 — Splitting channels
```python
b, g, r = cv2.split(image)
```

Each of these is:
```python
(H, W)
```

```python
plt.imshow(r, cmap='gray')
plt.title("Red Channel")
plt.axis("off")
```

*Even though it’s “red”, display it in grayscale.* <br>

### Visual intuition (IMPORTANT)

* **Bright areas** = strong color presence
* **Bright pixel** = HIGH number `(255, 0, 0)`
 <img width="741" height="445" alt="(255, 0, 0)" src="https://github.com/user-attachments/assets/00e908b6-9018-4d3c-b781-d85c6cb47d2f" />


* **Dark areas** = weak color presence
* **Dark pixel** = LOW number `(100, 0, 0)`
 <img width="744" height="449" alt="(100, 0, 0)" src="https://github.com/user-attachments/assets/c2846f54-f1dd-4860-897b-5ae4eb0f8c63" />


You’re literally seeing how much of that color exists per pixel.

## PART 3 — Re-merging channels

Re-merging channels simply means:

> Putting separate color channels back together to form a color image

```python
merged = cv2.merge([b, g, r])
```

Channels can be:
* reordered
* modified
* removed

### Why channels get split in the first place

You split channels when you want to:

* Look at them individually
* Modify one color
* Remove a color
* Analyze intensity patterns

But after tha:<br>
you usually want a normal color image again.<br>

That’s re-merging.

### How it looks in code (minimal)
```python
b, g, r = cv2.split(image)
merged = cv2.merge([b, g, r])
```
Example:
```python
b, g, r = cv2.split(image)
r = cv2.add(r, 50)
merged = cv2.merge([b, g, r])
```

## PART 4 — Brightness
Brightness = add or subtract pixel values

```python
bright = cv2.add(image, 50)
dark = cv2.subtract(image, 50)
```

## PART 5 — Contrast
Contrast = stretch differences between pixels<br>
Contrast = difference between dark and bright parts

* **High contrast** → dark parts are very dark, bright parts are very bright
* **Low contrast** → everything looks kind of gray and flat

```python
new_pixel = alpha * old_pixel + beta
```

Where:

* `alpha` → contrast (1.0 = same)
* `beta` → brightness

```python
contrast = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
```

Try:
* `alpha = 0.5` → flat image
* `alpha = 2.0` → high contrast


Visual intuition:

* Low contrast → gray, washed out
* High contrast → sharp, punchy

CV loves contrast because:

* edges become clearer
* objects stand out


### Brightness vs Contrast (important distinction)

| Brightness | Contrast |
| :--- | :--- |
| Moves everything up or down | Spreads things apart |
| Makes image lighter/darker | Makes details pop |
| Adds/subtracts values | Multiplies differences |


### Visual mental model

Imagine pixel values on a number line:<br>

**Original**:
```
|----20----60----100----140----|
```

**Increase brightness**:
```
|----70----110----150----190----|
```
Same spacing → same contrast

**Increase contrast**:
```
|--10------60------120------200--|
```
Spacing is bigger → higher contrast

* **High Contrast**
```python
# Alpha > 1: High Contrast
high_contrast = cv.convertScaleAbs(image_rgb, alpha=1.5, beta=0)
```

* **Low Contrast**
```python
# Alpha < 1: Low Contrast
low_contrast = cv.convertScaleAbs(image_rgb, alpha=0.5, beta=0)
```

## PART 6 — Combining brightness & contrast

```python
adjusted = cv2.convertScaleAbs(image, alpha=1.3, beta=30)
```

## PART 7 — Using proportions with channels (advanced intuition)

```python
h, w = image.shape[:2]
img = image.copy()
img[0:h//2] = cv2.add(img[0:h//2], 30)
```

---


### Example of modifying an image

**split → modify → re-merge**<br>

Since `opencv` uses `bgr`, you either have to conver the image to `rgb` before spliting and work with `rgb`, or just work with `rgb` and convert the image when you are done modifying.

```
# 1. converting to rgb first
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# 2. splitting channels
r,g,b = cv.split(image_rgb)

# 3. modifying 
r_contrast = cv.convertScaleAbs(r, alpha=1.2, beta=0)
g_contrast = cv.convertScaleAbs(g, alpha=1.1, beta=0)
b_contrast = cv.convertScaleAbs(b, alpha=.8, beta=0)

# re-marging
merged = cv.merge([r_contrast,g_contrast,b_contrast])

plt.imshow(merged)
plt.axis("off")
```
