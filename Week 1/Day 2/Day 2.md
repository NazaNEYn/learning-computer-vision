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

## What cropping REALLY is
Cropping means:<br>
> Selecting a rectangular region from an image

You are NOT:

* Changing pixel values
* Editing colors
* Creating new data

You ARE:
* Choosing which pixels to keep

## Images are grids

```python
image.shape = (H, W, C)
```

Think of an image as a grid:

* Rows → top to bottom (y)
* Columns → left to right (x)

So:
```python
image[y, x]
```
*Note:* This is the opposite of math graphs.

## Cropping = NumPy slicing
```python
cropped = image[y1:y2, x1:x2]
```

Meaning:

* Rows from y1 to y2 | `(y = y2 - y1)`
* Columns from x1 to x2 | `(x = x2 - x1)`

Channels stay the same automatically.

Example:
```python
image.shape = (400, 600, 3)
```

```python
cropped = image[100:300, 200:400]
```

This gives:
```python
cropped.shape = (200, 200, 3)

# y = 300 - 100 = 200
# x = 400 - 200 = 200
```
## How to think about cropping correctly

Think like this:

> “From which row to which row?”
> “From which column to which column?”

Not:

> “x and y coordinates”

## Center crop

```python
h, w, _ = image.shape

y1 = h // 4
y2 = 3 * h // 4

x1 = w // 4
x2 = 3 * w // 4

cropped = image[y1:y2, x1:x2]
```
You don’t guess numbers, you use *proportions*.<br>
> `_` means: “I don’t care about this value right now.”
> `//` is integer division (floor division). It rounds down to the nearest integer/float floor.

## What proportions mean

A proportion is:
> “A fraction of
>

Examples:
* 1/4 of height
* 1/2 of width
* 10% of image

Instead of saying:
> “Crop from pixel 120”

You say:
> “Crop from 25% down the image”
