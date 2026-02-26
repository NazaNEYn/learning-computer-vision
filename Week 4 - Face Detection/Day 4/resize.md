# `cv.resize()`

`cv.resize` creates **a new image** with a different size.

You can:
* make an image **smaller** → speed
* make an image **bigger** → visualization / detail

It does *not* modify the original image.

# Full syntax

```python
cv.resize(
    src,
    dsize,
    fx=0,
    fy=0,
    interpolation=cv.INTER_LINEAR
)
```

## `srcs`: The unput image

## `dsize`: exact output size (width, height)
```python
cv.resize(frame, (640, 480))
```
This forces the image to become **exactly** that size.

## `fx` and `fy`: scale factors
These are multipliers, not sizes.
```python
fx = scale in x direction
fy = scale in y direction
```
```python
cv.resize(frame, None, fx=0.5, fy=0.5)
```
Means:
* width → 50%
* height → 50%

### `dsize=None`
You must choose **one method**:

* **Method A — exact size**
  ```python
    cv.resize(frame, (640, 480))
  ```

* **Method B — scale factors**
  ```python
    cv.resize(frame, None, fx=0.5, fy=0.5)
  ```
If you use `fx` and `fy`, `dsize` must be `None`.

## `interpolation` — how pixels are calculated

| Interpolation | When to use |
| :--- | :--- |
| `cv.INTER_LINEAR` | Default, general use |
| `cv.INTER_AREA` | Best for shrinking |
| `cv.INTER_CUBIC` | Better quality when enlarging |
| `cv.INTER_NEAREST` | Fast, blocky |


## Best practice for video speed
```python
cv.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
```
