# Computer Vision Operations — What Problem Each Solves

| Step | What problem exists WITHOUT it | What problem it solves | What the computer “sees” after |
| :--- | :--- | :--- | :--- |
| **Color (RGB/BGR)** | Image is rich but confusing | Keeps human-meaningful info | Color + intensity |
| **Grayscale** | Too many channels (R,G,B) | Simplifies data to intensity | Light vs dark only |
| **Blur** | Noise & tiny details | Removes noise, smooths image | Clean intensity regions |
| **Edges** | Shapes are unclear | Finds boundaries & structure | Object outlines |
| **Thresholding** | Foreground & background mixed | Separates regions (binary) | Black & white mask |


## Operation Summary

| Operation | Think of it as… | Primary use |
| :--- | :--- | :--- |
| **Color** | Raw photo | Visualization, human meaning |
| **Grayscale** | Light meter | Structure analysis |
| **Blur** | Noise filter | Stability & robustness |
| **Edges** | Shape detector | Contours & boundaries |
| **Threshold** | Yes / No decision | Segmentation |

---

# Operation Pairings

| Pair | Relationship |
| :--- | :--- |
| **Grayscale → Blur** | Blur works best on intensity |
| **Blur → Edges** | Reduces false edges |
| **Blur → Threshold** | Cleaner regions |
| **Edges vs Threshold** | Lines vs areas |
| **Color vs Everything** | Mostly optional for classic CV |


---

# When you use WHAT (quick guide)

| Goal | Use |
| :--- | :--- |
| Find object shape | Edges |
| Extract object region | Threshold |
| Reduce noise | Blur |
| Simplify processing | Grayscale |
| Human interpretation | Color |

---
