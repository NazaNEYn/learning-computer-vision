# HSV

## why RGB starts to fail in Computer Vision  

* RGB is great for **displaying images** to humans.
* But it’s **bad for reasoning** about color.

**Why?**<br>
Because RGB mixes **three different ideas** together:
* color type
* brightness
* lighting conditions

Example:
* red in shadow ≠ red in sunlight
* same object → very different RGB values

To a computer, those look like **different colors**, even though *you* know they’re the same object.

## What HSV actually is (intuitive, not mathy)

HSV separates color into **three independent ideas**:

| Channel | Meaning (human words) |
| :--- | :--- |
| **H – Hue** | What color is it? (red, green, blue…) |
| **S – Saturation** | How strong/pure is the color? |
| **V – Value** | How bright or dark is it? |

Think of it like this:<br>
> **HSV matches how humans describe color**

* “A bright, strongly saturated red”
* “A dark, washed-out blue”

RGB can’t express that cleanly.

## Visual mental model

**RGB thinking:**
“How much red, green, blue light is mixed?”

**HSV thinking:**
“What color is it, how colorful is it, how bright is it?”

## Why HSV is AMAZING for computer vision

HSV lets you:
* ignore brightness changes
* isolate colors reliably
* detect objects by color
* work under different lighting

This is why HSV is used for:
* color segmentation
* tracking objects
* skin detection
* traffic lights
* ball tracking
* motion + color pipelines

## What each HSV channel REALLY does

### Hue (H)
* Represents color type
* Think: color wheel 
* Values wrap around (red → yellow → green → blue → back to red)

In OpenCV:
* Hue range = **0–179** (not 0–360)

### Saturation (S)

* Color intensity
* Low S → grayish
* High S → vivid color

If saturation = 0:<br>
color disappears (becomes gray)

### Value (V)

* Brightness
* Low V → dark
* High V → bright

This is where shadows and lighting mostly live.
