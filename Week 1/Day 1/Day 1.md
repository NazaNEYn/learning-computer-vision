# Goal of today :

Load an image → display it → understand its shape
Nothing more. Nothing less.<br>




# What you need to know TODAY (only this)

1. An image = NumPy array
2. Image shape = (height, width, channels)
3. OpenCV reads images in BGR, not RGB (don’t worry too much yet)
4. Pixel values are 0–255


# Verify OpenCV is Available
```python
import cv2
import numpy as np

print(cv2.__version__)
print(np.__version__)
```

# Load the Image
```python
image_path = "/kaggle/input/YOUR_DATASET/YOUR_IMAGE.jpg"

image = cv2.imread(image_path)
```

# Display the Image (Kaggle Way)
Kaggle does NOT support `cv2.imshow()`.<br>
Instead, use `matplotlib`:
