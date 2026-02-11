# First: separate TWO DIFFERENT ROLES 
In computer vision, **the same image plays two different roles**:<br>

1. **Processing image** → used for computation
2. **Display image** → used for visualization

They do **not have to be the same image**.

## The rule that fixes everything

> **You process on simplified images.**
> 
> **You draw on images meant for humans.**


# Step-by-step mental model

## 1. Original image (color)

* Purpose: **human-friendly**
* Contains color
* Used for display & drawing
You usually **do NOT process contours on this.**

## 2. Grayscale image

* Purpose: **computation**
* Simplified intensity
* Used for blur, threshold, edges
Humans don’t need to see this most of the time.


## 3. Binary image

* Purpose: **logic**
* White = object
* Black = background
This is purely for the computer.


## 4. Contours (data)
* NOT an image
* Just shape coordinates


