# Thresholding (Binary Images)

What you'll learn:

* What thresholding is
* Why binary images matter
* How thresholding is different from edges
* When thresholding works well vs fails
* How it fits into the CV pipeline

---

## What is thresholding?

Thresholding means:
> **Turn a grayscale image into black & white based on intensity.**

```python
if pixel_value > threshold:
    white (255)
else:
    black (0)
```


## Why binary images matter in CV

Binary images are powerful because they:

* Remove ambiguity
* Simplify decisions
* Make shapes obvious

**Computers LOVE:**

* Yes / No
* 0 / 1
* Black / White

Thresholding converts vision into logic.



## How thresholding is different from edges

This is important — don’t mix them up.

| Feature | Edges (Canny) | Thresholding |
| :--- | :--- | :--- |
| **Goal** | Finds boundaries | Separates regions |
| **Output** | Outlines | Filled areas |
| **Logic** | Looks at changes | Looks at values |
| **Visual** | White lines | White regions |

Think:

* **Edges** = “Where does it change?”
 **Threshold** = “Which pixels belong?”


![Gemini_Generated_Image_32uf9y32uf9y32uf](https://github.com/user-attachments/assets/0c91c49d-c41a-470b-8029-33a3885f8a80)
![Gemini_Generated_Image_57sqhb57sqhb57sq](https://github.com/user-attachments/assets/99f42aba-4efc-49e1-b6c9-4a0225708173)

## The threshold syntax

**The full thresholding syntax**:

```python
retval, binary = cv2.threshold(
    src,          # input image (grayscale)
    thresh,       # threshold value
    maxval,       # value assigned if condition is met
    type          # thresholding rule
)
```


**The basic thresholding syntax**:

```python
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```

* `gray` = input image
*  `127` = threshold value
*  `255` = value for white
*  `THRESH_BINARY` = rule type

## Threshold value intuition 

* **Low threshold** → more white
* **High threshold** → more black

**Example:**

* **threshold = 50** → almost everything white
* **threshold = 200** → almost everything black

## Common threshold types

* 1. **Binary**:
```python
cv.THRESH_BINARY
```
Above threshold → white

* 2. **Binary Inverse**:
```python
cv.THRESH_BINARY
```
Above threshold → black

* 3.
```python
cv.THRESH_BINARY
```
(will learn this later)

* 4.
```python
cv.THRESH_BINARY
```
(will learn this later)


## Why grayscale is REQUIRED

**Thresholding needs:**

* One value per pixel

**Color images:**

* Have 3 values
* Don’t threshold cleanly

## When thresholding works well

* High contrast images
* Simple lighting
* Clear foreground/background
* Documents, text, silhouettes

**Examples:**

* Scanned papers
* License plates
* Coins on table
* Black objects on white background

## When thresholding FAILS (important)

* Uneven lighting
* Shadows
* Low contrast
* Complex backgrounds

This is why adaptive thresholding exists (next step).



## Where threshold fits conceptually

**Threshold answers a different question:**

* “Is this pixel foreground or background?”

**Edges answer:**

* “Does intensity change here?”

**The Distinction:**

* **Thresholding** is region-based.
* **Edges** are boundary-based.


