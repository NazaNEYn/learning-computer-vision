# Most common proportions

## Half of the image
```python
h // 2
w // 2
```
Meaning:
> “Cut the image into two equal parts”

## Quarter of the image
```python
h // 4
w // 4
```
Meaning:
> “One fourth from the edge”

## Three quarters
```python
3 * h // 4
3 * w // 4
```
Meaning:
> “Almost the whole image, but leave some margin”

# Ready-to-use cropping patterns

## Center crop (most common)
```python
cropped = image[
    h//4 : 3*h//4,
    w//4 : 3*w//4
]
```
Meaning:
> “Keep the middle 50% of the image”

## Top half
```python
cropped = image[:h//2, :]
```

Meaning:
> “Keep everything above the middle”

## Bottom half
```python
cropped = image[h//2:, :]
```

Meaning:
> “Keep everything below the middle”

## Left half
```python
cropped = image[:, :w//2]
```

## Right half
```python
cropped = image[:, w//2:]
```

## Top-left quarter
```python
cropped = image[:h//2, :w//2]
```

## Bottom-right quarter
```python
cropped = image[h//2:, w//2:]
```

# Using percentages

## Top 10% of image
```python
cropped = image[:int(0.1*h), :]
```

## Center 60%
```python
cropped = image[
    int(0.2*h) : int(0.8*h),
    int(0.2*w) : int(0.8*w)
]
```

You are just saying:
> “Keep between 20% and 80%”

# How to THINK about proportions

**1. Step 1: Decide WHAT you want**
* “Center”
* “Half”
* “Small region”
* “Top part”

**2. Step 2: Translate to simple words**
* Half → divide by 2
* Quarter → divide by 4
* Middle → skip edges

**3. Step 3: Write it using `h` and `w`**<br>
No guessing numbers. Ever.
