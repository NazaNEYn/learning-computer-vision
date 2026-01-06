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
`plt.imshow()` *expects* the array in RGB and that's why we need to convert the image.

# 4. Print Image Shape (Core Concept)
```python
print("Image shape:", image.shape)
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
