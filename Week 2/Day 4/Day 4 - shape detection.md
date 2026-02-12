# Shape Detection

## Goal:
Look at an image, find shapes, decide what they are, and draw boxes around them.


## Mental Model

**A computer does NOT “see” circles or rectangles.**

It does this instead:

1. Finds white blobs (contours)
2. Measures each blob
3. Asks simple questions:
   * How big is it?
   * How big is it?
   * Is it wide or tall?
   * How smooth is it?
  
From those answers → **decision**


## The Full Pipeline
```python
Color image                ← humans
   ↓
Grayscale                  ← remove color distraction
   ↓
Blur                        ← remove noise
   ↓
Threshold OR Edges          ← separate objects
   ↓
Contours                    ← shapes as data
   ↓
Analyze contour geometry    ← numbers
   ↓
Decide shape                ← logic
   ↓
Draw result on color image  ← humans again
```

