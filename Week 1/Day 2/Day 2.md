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
