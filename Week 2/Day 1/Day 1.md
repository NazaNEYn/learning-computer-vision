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
