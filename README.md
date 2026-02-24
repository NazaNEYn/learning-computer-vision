# Folder Structre
```
CV_Roadmap/
 └── Week1/
      └── Day1/
```

---

## A few notes about kaggle notebook:
I use kaggle notebook for my learning journey. So my codes are based on how kaggle works.<br>

* Make sure to import `matplotlib.pyplot`
```python
import matplotlib.pyplot as plt
```

Beacsue you need it to show the result:
```python
plt.imshow(image_rgb)
plt.axis("off")
plt.show()
```

* `openCV` reads images in `BGR` but kaggle reads them in `RGB`.<br>
So make sure you convert the images to `RGB`:
```python
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
```
