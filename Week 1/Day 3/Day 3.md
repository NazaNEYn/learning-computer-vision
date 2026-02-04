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
![Gemini_Generated_Image_kwd2g8kwd2g8kwd2](https://github.com/user-attachments/assets/fb571f7a-31dd-4fac-ab25-666782e7b53f)

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
