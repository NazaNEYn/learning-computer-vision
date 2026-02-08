# Gaussian Blur & Why Noise Matters

## Day 6 Goal

* By the end of today, you should:
* Understand what noise is
* Understand why CV hates noise
* Know what Gaussian blur does
* Be able to apply blur and see its effect
* Know when to blur and when not to

---

## Big picture first (VERY IMPORTANT)
> **Computer vision algorithms don’t see objects.
They see pixel changes.**

* Noise = unwanted pixel changes
* Blur = controlled smoothing

## PART 1 — What is noise?

**Noise = random pixel variation that shouldn’t be there**

Examples:

* Grainy dots in dark photos
* Sensor artifacts
* Compression artifacts
* Tiny texture that isn’t important

To humans:<br>
“Meh, I can ignore that”<br>
<br>

To computers:<br>
“OMG EVERYTHING IS AN EDGE”<br>

### Visual intuition

Imagine a straight line:
```
████████████
```

With noise:
```
█ ███ █ ███ █
```

Your eyes ignore the gaps.<br>
Edge detectors will NOT.

## PART 2 — Why noise is BAD for CV

Noise causes:

* False edges
* Broken contours
* Too many detected features
* Unstable results

So before detecting:
* edges
* corners
* objects

We **clean the image**.<br>
That’s preprocessing.

## PART 3 — What Gaussian Blur really is
Forget math. Here’s the idea:
> **Gaussian blur replaces each pixel with an average of its neighbors**

* Small details → smoothed out
* Large shapes → stay

This removes noise but keeps structure.

## Why “Gaussian”?

Because the averaging gives:

* more weight to nearby pixels
* less weight to far ones



kernel:
![Gemini_Generated_Image_1ac99p1ac99p1ac9](https://github.com/user-attachments/assets/0aedaadf-d685-4f14-b05b-c4927f9fc380)


<br> <br>

<img width="500" height="298" alt="0_YO8XSDvUu-wxgXl7" src="https://github.com/user-attachments/assets/bc0dd9ae-195e-437e-9941-3070ae7458ee" />
<br>

image credit: [https://muneebsa.medium.com/deep-learning-101-lesson-20-convolution-kernels-40641dda695d](https://muneebsa.medium.com/deep-learning-101-lesson-20-convolution-kernels-40641dda695d)
