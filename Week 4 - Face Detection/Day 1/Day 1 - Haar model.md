# Day 1 — What Face Detection Is & Loading a Haar Model


## What face detection actually is

Face detection answers ONE question:<br>
> **“Where are the faces?”**

It does NOT answer:
* who the person is 
* whether two faces are the same 
* emotions, age, gender
That’s **face recognition**, a later topic.

**Output of face detection:** <br>
Unlike everything you’ve done so far:
* ❌ not a binary image
* ❌ not a mask
* ❌ not contours

Face detection outputs **rectangles**:
```
(x, y, w, h)
```

Each rectangle means:<br>
> “I think a face exists here.”<br>
This is **object-level detection**, not pixel-level.

## How face detection is different from what you already know

What you’ve done so far:

| Task | Output |
| :--- | :--- |
| Color detection | Binary mask |
| Motion detection | Binary mask |
| Shape detection | Contours |
| Morphology | Cleaned mask |

You controlled the logic:
* thresholds
* kernels
* contour area

**Face detection**
* Uses a **pre-trained model**
* You do not define rules
* You **ask the model to decide**
 
This is why face detection feels more like a “black box”.<br>

Your job becomes:
* preparing the input correctly
* tuning parameters
* interpreting results
