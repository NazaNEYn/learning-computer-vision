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
* **Dark areas** = weak color presence

You’re literally seeing how much of that color exists per pixel.
