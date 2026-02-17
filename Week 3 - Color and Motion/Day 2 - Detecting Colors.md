# Detect a specific color

## What “Detect a Color” Really Means

When we say detect red or detect blue, we mean:<br>
> **Find all pixels which color belongs to a specific range**

* Not objects.
* Not shapes.
* Just **pixels that match a color condition**.

## Why HSV (again, but deeper)

In HSV:
* **Hue** → what color it is (red, blue, green…)
* **Saturation** → how pure the color is
* **Value** → how bright it is

Key idea:<br>
> We mostly care about **Hue**, and we use Saturation + Value to **remove noise** (gray, white, black).

## What “Detecting Red / Blue” Means in Practice

You will:

1. Convert image → HSV
2. Define a **range** for the color
3. Create a **mask**
4. Use the mask to extract or highlight the color
5. (Optionally) find contours of that color

## Hue Is a CIRCLE

Hue is **circular**, not linear.

```python
Red → Yellow → Green → Cyan → Blue → Purple → back to Red
```

In OpenCV:

* Hue range = **0–179**
* Red exists at **both ends** of the range

That’s why red is special
* Low Hue (0–10)
* AND high Hue (170–179)

![Gemini_Generated_Image_ujgkwdujgkwdujgk](https://github.com/user-attachments/assets/3da5fdb1-7f00-41fc-a1ac-43e9cf5bb641)


## Converting an Image to HSV

### Step 1: Convert RGB:
```python
hsv = cv.cvtColor(image_rgb, cv.COLOR_RGB2HSV)
```

* Each pixel is now `[H, S, V]`
* This image looks weird if you display it directly

### Step 2: Split HSV into channels

```python
h, s, v = cv.split(hsv)
```

Now you have:
* `h` → Hue image
* `s` → Saturation image
* `v` → Value image

Each is a **grayscale image**.

### Step 3: Visualize each channel

```python
h, s, v = cv.split(hsv)

images = [h, s, v]
titles = ["Hue", "Saturation", "Value"]

plt.figure(figsize=(12,4))

for i, (img, title)  in enumerate(zip(images, titles)):
    plt.subplot(1, 3, i + 1)
    plt.imshow(img, cmap="gray")
    plt.title(title)
    plt.axis("off")

plt.show()
```

![HBPXAEqacAAzNbB](https://github.com/user-attachments/assets/e93a6045-2434-4cb4-9cfc-5b71f4182f7e)
![ScreenShot Tool -20260216043208](https://github.com/user-attachments/assets/6ce9799d-b4e9-4d52-9ef0-ca93a01c86b2)


**Hue image:**
* Bright areas = pixels of similar color
* Dark areas = different colors
* Not brightness-based

**Saturation image:**
* Bright = strong color
* Dark = gray / white / black

**Value image:**
* Bright = well-lit
* Dark = shadow / dark region

### Step 4: Pick a color range

**General template**
```python
lower_color = np.array([H_min, S_min, V_min])
upper_color = np.array([H_max, S_max, V_max])
```

**Example: 🔵 Blue** 

```python
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])
```

**Meaning:**
* Hue: blue-ish
* Saturation: ignore gray/white
* Value: ignore dark pixels

**Example: 🟢 Green**
```python
lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])
```

**Example: 🔴 Red (special case)**<br>
Red wraps around → **two ranges.**

```python
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([179, 255, 255])
```

### Step 5: Create a mask

**Basic mask (single range)**

```python
mask = cv.inRange(hsv_image, lower_color, upper_color)
```

* Input: HSV image
* Output: binary image (mask)
* White (255) = color detected
* Black (0) = not detected

### Step 6 : Show the mask
```python
plt.imshow(mask_blue, cmap="gray")
plt.title("Blue Mask")
plt.axis("off")
plt.show()
```

This is how you debug color detection.<br>
If the mask looks wrong → HSV ranges are wrong, not your logic.

### Step 7: Apply the mask to the image

**Syntax**
```python
cv.bitwise_and(src1, src2[, dst[, mask]])
```

| Argument | Meaning |
| :--- | :--- |
| **src1** | First input image |
| **src2** | Second input image |
| **mask** | Optional binary mask |


```python
result = cv.bitwise_and(image_rgb, image_rgb, mask=mask)
```

* What this does:<br>
  Keeps only masked pixels
  Everything else becomes black

* Why TWO images? `(image_rgb, image_rgb)`<br>
`bitwise_and` combines *two images* But in color detection, we are **not combining two different images**.<br>
We want to keep pixels from THIS image where the mask is white.<br>
So we pass the **same image twice**.
```python
image_rgb AND image_rgb = image_rgb
```

### Step 8: Display final result
```python
plt.imshow(result)
plt.title("Detected Blue")
plt.axis("off")
plt.show()
```

### Minimal Full Template
```python
hsv = cv.cvtColor(image_rgb, cv.COLOR_RGB2HSV)

lower_color = np.array([H_min, S_min, V_min])
upper_color = np.array([H_max, S_max, V_max])

mask = cv.inRange(hsv, lower_color, upper_color)

result = cv.bitwise_and(image_rgb, image_rgb, mask=mask)
```

### Debug Template
```python
plt.imshow(mask, cmap="gray")
plt.title("Mask")
plt.axis("off")
plt.show()
```


## Mental Model

* Convert → separate color from light
* Split → understand channels
* Mask → turn color into logic
* Apply → see result

## One Rule to Remember

Color range = what you want<br>
Mask = where it exists
