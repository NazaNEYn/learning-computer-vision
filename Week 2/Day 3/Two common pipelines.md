# Pipeline A — Edge-based (structure)

> **Edges describe SHAPE.**


```python
color → grayscale → blur → edges
```

Used when:

* shape matters
* outlines matter
* object boundaries matter

Examples:
* document detection
* lane detection
* contour finding



# Pipeline B — Region-based (segmentation)

> **Threshold describes AREAS**

```python
color → grayscale → blur → threshold
```

Used when:
*separating object from background
* binary masks
* foreground extraction

Examples:
* text extraction
* coin detection
* simple segmentation

![Gemini_Generated_Image_aw5890aw5890aw58](https://github.com/user-attachments/assets/44620d04-676c-4538-8d51-5e34b4bd15db)

## Think of CV as choosing a path

```python
           ┌─→ blur → edges → contours
color → gray
           └─→ blur → threshold → mask
```

Same start. Different goals.
