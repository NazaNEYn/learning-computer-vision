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
