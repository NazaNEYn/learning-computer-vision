# `cv.normalize()`

## what it is and why it exists

### The problem it solves

Images from videos **do not have consistent brightness**.<br>

Even in the same tunnel:
* Camera auto-exposure changes
* Entering/exiting the tunnel changes intensity
* Some frames are darker, some brighter

If you use **fixed thresholds**, those changes break detection.<br> 

So we ask:<br>
> “Can I force every frame to use the full brightness range?” <br>

That is exactly what **normalization** does.

### What normalization actually means
Think of grayscale pixel values as numbers:
* Dark image might live in range: `20 → 110`
* Bright image might live in range: `80 → 240`

Normalization **stretches or compresses** values so that:
```python
minimum value  → 0
maximum value  → 255
everything else → scaled in between
```

So both images now use the **same intensity range**.<br>

Important:
You are **not making the image brighter**
You are **redistributing contrast**

### Visual intuition
Imagine this grayscale row:
```python
[ 40, 50, 60, 70, 80 ]
```
Min = 40 <br>
Max = 80 <br>

After normalization:
```python
[ 0, 64, 128, 191, 255 ]
```

Same structure.<br>
Much stronger contrast.<br>

That’s why normalization is great for dark tunnels.


### How `cv.normalize` works
Syntax:
```python
cv.normalize(src, dst, alpha, beta, norm_type)
```

What each part means:

* `src` → input image
* `dst` → output image (often `None`)
* `alpha` → new minimum value
* `beta` → new maximum value
* `norm_type` → how to normalize
  
The most common one:
```python
cv.NORM_MINMAX
```
Which means:<br>
> “Map min → alpha, max → beta”

-----------------------------------------------------------------------
![Gemini_Generated_Image_dwb5jzdwb5jzdwb5](https://github.com/user-attachments/assets/db15c121-f4af-4662-a80b-8d57a5dfbd98)
![Gemini_Generated_Image_gj4dafgj4dafgj4d](https://github.com/user-attachments/assets/40655825-9662-4193-8cdf-84b6e6a94010)

