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
img = image.copy()

cv2.line(
    img,
    (50, 50),
    (300, 50),
    (0, 255, 0),  # green
    3
)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis("off")
```
