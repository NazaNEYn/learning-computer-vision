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

