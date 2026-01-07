# What you need to know TODAY

* Grayscale = 1 number per pixel
* Resize changes number of pixels
* Crop selects a region of pixels
* All operations are array operations

# 1. Grayscale:

## What is a grayscale image?
Instead of:
```python
[Blue, Green, Red]
```
Grayscale uses:
```python
[Intesity]
```
So shape changes from:
```python
(H, W, 3) → (H, W)
```

Each pixel is:<br>

* 0 → black
* 255 → white

## Why grayscale is huge in CV

Most CV algorithms care about:<br>
* Edges
* Shapes
* Patterns
* Motion

Color often **adds noise**.<br>

That’s why:<br>

* Face detection
* Edge detection
* Feature detection
  
Start with grayscale.

## Convert to grayscale 
```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
```python
print(gray.shape)
print(gray.dtype)
```
Output:
```python
(H, W)
uint8
```

## Display grayscale in Kaggle
```python
plt.imshow(gray, cmap="gray")
plt.axis("off")
```
*Note:* `cmap="gray"` is required — otherwise it looks wrong.

## Pixel values
```python
print(gray[0,0])
```
Output:
```python
128
```

# 2. Resize Images

## What does resizing really mean?

Resizing: <br>
* Changes image dimensions
* Changes number of pixels
* Interpolates values

Example:
```python
640×480 → 320×240
```
Now you have:
* 4× fewer pixels
* Same visual content

## Resize
```python
resized = cv2.resize(image, (300, 300))
```
Order:
```python
(width, height)
```

## Compare shapes
```python
print("Original:", image.shape)
print("Resized:", resized.shape)
```
```python
Original: (700, 961)
Resized: (300, 300)
```

## Why resizing is essential in CV

* ML models expect fixed input size
* Faster computation
* Consistent processing

# 3. Crop Images
Mathematically:
````python
cropped = image[y1:y2, x1:x2]
```
example:
```python
h, w, _ = image.shape

cropped = image[
    h//4 : 3*h//4,
    w//4 : 3*w//4
]
```
This takes the **center region**.

## Cropping is NOT copying
Important concept:

* Cropping uses array slicing
* No pixels are modified
* Just selecting a view
