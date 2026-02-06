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
