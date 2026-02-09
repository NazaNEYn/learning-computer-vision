# Day 2, Week 2 — Canny Edge Detection

**What you'll learn:**
* What an edge actually is (for a computer)
* Why grayscale + blur come before edges
* What Canny does (conceptually, not math-heavy)
* What the two thresholds mean
* How to tune Canny without guessing

---

### First: What is an “edge”?

An edge is a place where pixel intensity changes sharply.<br>
<br>

Examples:
* Object boundaries
* Corners
* Text strokes
* Shape outlines

Computers don’t see objects — they see **intensity change**.
<br>
<br>

![Gemini_Generated_Image_2an2tl2an2tl2an2](https://github.com/user-attachments/assets/34529a10-c092-4b06-a6f3-3ee9b21413fb)


### Visual intuition

Imagine pixel values along a line:
```python
10  11  12  200  202  203
```
That jump (12 → 200) is an **edge**.

### Why edges matter in CV
Edges are:
* stable across lighting changes
* shape-defining
* compact representations of objects

---

## PART 1 — Why blur FIRST (important)

Noise = tiny intensity jumps
Canny = “find sharp jumps”

![Gemini_Generated_Image_yzux0pyzux0pyzux](https://github.com/user-attachments/assets/47a7d2c2-f4c1-4cc9-90e3-e4c0020e7e10)


If you skip blur:
* noise becomes edges
* output becomes messy

So the classic pipeline:
```python
gray → blur → edges
```

<br>

![Gemini_Generated_Image_5p9wwx5p9wwx5p9w](https://github.com/user-attachments/assets/d3687570-a471-4f6e-a9c5-504fcad898bc)


## PART 2 — Canny in practice

```python
edges = cv2.Canny(gray_blur, 50, 150)
```

```python
edges = cv2.Canny(img input, thresholds_1, thresholds_2)
```

* Lower threshold = weak edges
* Upper threshold = strong edges

Canny logic (simplified):
* Strong edges → keep
* Weak edges near strong → keep
* Weak edges alone → discard

### Threshold intuition

| Values | Result |
| :--- | :--- |
| low (10, 30) | many edges, noisy |
| medium (50, 150) | balanced |
| high (100, 250) | few edges, clean |

No “correct” values — only useful ones.


## PART 3 — Full pipeline

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)

plt.imshow(edges, cmap="gray")
plt.title("Canny Edges")
plt.axis("off")
```

## PART 4 — How to read an edge image

* White = edge detected
* Black = no edge

Good edge image:

* clean outlines
* minimal speckles
* important shapes preserved

Bad edge image:

* snow-like noise
* broken contours
* missing object boundaries
