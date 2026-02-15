# When to Use Which?

| Aspect | Hue (HSV) | Grayscale |
| :--- | :--- | :--- |
| **What it represents** | Color identity | Brightness / intensity |
| **Value meaning** | “What color is this?” | “How bright is this pixel?” |
| **Sensitive to lighting** | Mostly resistant | Very sensitive |
| **Keeps color info** | Yes | No |
| **Removes color** | No | Yes |
| **Best for** | Color-based tasks | Shape, structure, edges |
| **Human intuition** | Color wheel (red, green, blue…) | Light <-> dark |
| **Range (OpenCV)** | 0–179 (circular) | 0–255 (linear) |

# Use-Case Comparison

## Grayscale — Use it when:

| Situation | Why |
| :--- | :--- |
| **Edge detection** | Edges depend on intensity changes |
| **Contours** | Shape comes from contrast, not color |
| **Thresholding** | Binary decisions need brightness |
| **Noise reduction** | Color often adds noise |
| **Preprocessing** | Simplifies the image |

**Mental model:**<br>
“I don’t care what color it is — just where things are.”

## Hue — Use it when:

| Situation | Why |
| :--- | :--- |
| **Color detection** | Hue isolates color |
| **Tracking objects by color** | Hue stays stable across lighting |
| **Removing background colors** | Background often differs in Hue |
| **Traffic lights, balls, clothes** | Color matters more than shape |

**Mental model:**<br>
“I care what color it is, not how bright it is.”

# Why They Are NOT Alternatives

* Hue and Grayscale solve different problems.

## Typical pipelines

**Shape detection:**
```python
Color → Grayscale → Blur → Edges / Threshold → Contours
```

**Color detection:**
```python
Color → HSV → Hue mask → (optional) contours
```

---

**Grayscale is for structure. Hue is for identity.**
* One does NOT replace the other.
