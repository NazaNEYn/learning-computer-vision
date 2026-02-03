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

---

## How to THINK in Proportions (No Memorization)

### First: drop the word “math” for a moment
Proportions are not formulas. They are **relationships**.

You already use proportions every day:
* half a pizza
* middle of a road
* edge of a screen

You don’t calculate those — you feel them. We want to do the same with images.



## Start with the IMAGE, not numbers

When you want to crop, ask only one question:

**Which part of the image do I want?**

Examples:
* “The center”
* “The top part”
* “Most of the image”
* “A small region”

Do not think about numbers yet.



## Translate words → relative positions (this is the key skill)

Instead of numbers, think in relative locations:

| Human thought | CV thought |
| :--- | :--- |
| top | near 0 |
| bottom | near h |
| left | near 0 |
| right | near w |
| middle | between |

So when you say: **“I want the center”**, your brain should say: **“Not near 0, not near h — somewhere between”**.

That’s proportion thinking.




## Proportions are just “start” and “end”

Cropping always asks two questions:
1. **Where do I start?**
2. **Where do I stop?**

### For height (Y direction):
* Start somewhere below the top
* Stop somewhere before the bottom

### For width (X direction):
* Start somewhere after the left
* Stop somewhere before the right

That’s it.




## Now bring in VERY simple math (only when needed)

Let’s say: **“I want the middle part vertically”**

Middle means:
* Not at the very top
* Not at the very bottom

A simple way to describe that is:
* Start after 25%
* End before 75%

**Why 25 and 75?**
* Because they’re easy
* Because they leave margins on both sides
* No deeper reason.



## Why h // 4 feels magical (but isn’t)

```
h // 4
```
Means: **“A bit down from the top”**

```
3 * h // 4
```

Means: **“A bit before the bottom”**

You’re not solving anything — you’re placing boundaries.




## Thinking visually (THIS is how you stop memorizing)

When you see:

`image[y1:y2, x1:x2]`

Don’t think “math”. Think:

```text
|----|=========|----|
     ↑         ↑
   start     end
```
You are drawing a box inside the image.
