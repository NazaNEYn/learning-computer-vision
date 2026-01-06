# Goal of today :

Load an image → display it → understand its shape
Nothing more. Nothing less.<br>




# What you need to know TODAY (only this)

1. An image = NumPy array
2. Image shape = (height, width, channels)
3. OpenCV reads images in BGR, not RGB (don’t worry too much yet)
4. Pixel values are 0–255


# 1. Verify OpenCV is Available
```python
import cv2
import numpy as np

print(cv2.__version__)
print(np.__version__)
```

# 2. Load the Image
```python
image_path = "/kaggle/input/YOUR_DATASET/YOUR_IMAGE.jpg"

image = cv2.imread(image_path)
```

# 3. Display the Image (Kaggle Way)
Kaggle does NOT support `cv2.imshow()`.<br>
Instead, use `matplotlib`:
```python
import matplotlib.pyplot as plt

# Convert BGR → RGB for correct colors
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis("off")
```
`cv2.imread()`loads the data into an array with BGR.<br>
`plt.imshow()` *expects* the array in RGB and that's why we need to convert the image.<br>
<br>

You convert **only** when:<br>
* Using matplotlib.pyplot.imshow()
* Using libraries that expect RGB

You do **NOT** convert when:<br>
* Using OpenCV functions
* Doing CV processing
* Using `cv2.imshow()` (desktop)
* Applying filters, edges, detection, etc.

In real CV pipelines:<br>
| You usually stay in BGR.

# 4. Print Image Shape (Core Concept)
```python
print("Image shape:", image_rgb.shape)
```

Output:
```python
Image shape: (480, 640, 3)
```
```
Height = 480 pixels
Width  = 640 pixels
Channels = 3 (color)
```

# 5. Explore Pixel Values

what is a pixel?
A pixel is NOT a color dot.<br>
It's a small list of numbers.<br>

For a color image:
```python
Pixel = [Blue, Green, Red]   (in OpenCV)
```

Each number:<br>

* is an intensity
* ranges from 0 to 255
* bigger number = stronger color

Top-left pixel:
```python
print(image[0, 0])
```

Output:
```python
[14 14 12]
```

What does [0,0] mean?<br>

* First `0` → row (height / y)
* Second `0` → column (width / x)

So:
```python
image[row, column]
```


Center pixel:
```python
h, w, c = image.shape
print("Center pixel:", image[h//2, w//2])
```

`//` means integer division — required for array indexing.

This means:<br>

* Go halfway down the image
* Go halfway across the image
* Print the color value for the pixel there

# 6. Modify Pixels

**Change a single pixel**:
```python
image[0,0] = [0, 0, 255]  # red (BGR)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis("off")
```
this just changes a pixel and that is not something that can be seen with eyes. That's why we change it by blocks/regions.

**Draw a square**:
```python
image[0:100, 0:100] = [255, 0, 0]  # blue square

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis("off")
```

# 7. Check Data Type
```python
print(image.dtype)
```

Output:
```python
uint8
```
Meaning: pixel values are `0–255`.

