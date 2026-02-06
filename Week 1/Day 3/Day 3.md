# PART 1 — Coordinates
* When accessing pixels:
  ```
  image[y, x]
  ```
* When drawing shapes:
  ```
  (x, y)
  ```

# PART 2 — Draw a Line
Syntax:
```python
cv2.line(image, pt1, pt2, color, thickness)
```

Example:
```python
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = image_rgb.copy()

cv2.line(
    img,
    (50, 50),
    (300, 50),
    (0, 255, 0)
    3
)

plt.imshow(img_rgb)
plt.axis("off")
```

# Draw a Rectangle

Syntax:
```python
cv2.rectangle(image, pt1, pt2, color, thickness)
```

Example:
```python
cv2.rectangle(
    img,
    (100, 100),
    (300, 300),
    (255, 0, 0)
    2
)
```

Filled rectangle:
```python
cv2.rectangle(img, (100,100), (300,300), (0,0,255), -1)
```
`-1` means fill it.

# Draw a Circle
Syntax:
```python
cv2.circle(image, center, radius, color, thickness)
```

Example:
```python
cv2.circle(
    img,
    (250, 250),
    60,
    (0, 255, 255)
    3
)
```

Filled circle:
```python
cv2.circle(img, (250,250), 60, (0,255,0), -1)
```

# Using proportions with drawing



```python
h, w = image.shape[:2]

cv2.rectangle(
    img,
    (w//4, h//4),
    (3*w//4, 3*h//4),
    (0,255,0),
    2
)
```

This draws a **center box** on *any image size*.

## Why this creates a perfect center:
Because you are starting at $1/4$ and ending at $3/4$, the "gap" on every side of the rectangle is exactly $1/4$ of the image.


| Boundary | Calculation | Position |
| :--- | :--- | :--- |
| Left Gap | 0 to 1/4 | 25% of width |
| Right Gap | 3/4 to w | 25% of width |
| Top Gap | 0 to 1/4 | 25% of height |
| Bottom Gap | 3/4 to h | 25% of height |

**The Math Rule**:<br>
* `w // 4` is the same as saying **"25% of the width."**
* `3 * w // 4` is the same as saying **"75% of the width."**

> (Target Slice $\times$ Dimension) // Total Slices


![Gemini_Generated_Image_kwd2g8kwd2g8kwd2](https://github.com/user-attachments/assets/fb571f7a-31dd-4fac-ab25-666782e7b53f)
![Gemini_Generated_Image_yrolpcyrolpcyrol](https://github.com/user-attachments/assets/4b47f429-5b26-4218-89c9-97971a5d3afa)
![Gemini_Generated_Image_hrru4ghrru4ghrru](https://github.com/user-attachments/assets/4d3879aa-bb02-4bcf-97d9-049fb61fd300)
![Gemini_Generated_Image_2v4xcn2v4xcn2v4x](https://github.com/user-attachments/assets/c3a4ce52-6e69-4c30-b018-b36ae115153d)
