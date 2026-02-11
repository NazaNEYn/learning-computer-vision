# What object boundaries are clear?

Clear object boundaries are:

* Outlines between foreground and background
* Borders where intensity changes a lot
* Silhouettes of objects

**Examples:**

* Edge of a face against background
* Outline of a car
* Border of a building against sky
* Text strokes

## Rule of thumb

If you can trace the object with a pencil, that’s a clear boundary.

**These edges:**

* Are thick
* Continuous
* Survive threshold changes

---


# What is noise?

Noise is **NOT** random-looking pixels only.

**Noise is:**

Any edge detected that does not correspond to a meaningful object boundary.

**Examples:**

* Grainy speckles
* Fabric texture
* Skin pores
* Grass blades (often)
* Compression artifacts

**Noise edges:**

* Appear and disappear quickly
* Break apart
* Look “snowy”

---


# What details are unnecessary?

Unnecessary details are:

* Tiny texture patterns
* Surface roughness
* Repeated micro-edges

**Examples:**

* Wrinkles on skin (for face detection)
* Wood grain
* Grass texture
* Wall cracks (unless your task is crack detection)

## Key idea

Details are unnecessary if removing them does **NOT** change object shape.

---

# What does blur remove first?

Blur removes:

* Noise
* Fine texture
* Thin edges
* Small objects

**And removes big edges last.**

So blur acts like:

> “Small → gone first
>
> Large → survive longer”

This is why over-blur kills everything.

---


# What kind of edges survive all settings?

**Edges that survive:**

* Are large-scale
* Have high contrast
* Separate major regions

**Examples:**

* Object silhouettes
* Horizon lines
* Door frames
* Road boundaries

**These edges:**

* Stay visible across blur sizes
* Survive high thresholds
* Are structurally important

**Think of them as:**
Structural edges

---


# When do edges become useless?

Edges become useless when:

* Noise dominates real structure
* Edges are broken and fragmented
* Important shapes disappear
* Everything looks equally “edgy”

**This happens when:**

* Thresholds are too low
* Blur is skipped
* Image quality is poor

**Useless edge image feels like:**
“I see white everywhere, but nothing meaningful.”

---

# The big picture (this ties everything together)

| Concept | Meaning |
| :--- | :--- |
| **Clear edges** | Shape & structure |
| **Noise** | Meaningless detail |
| **Blur** | Noise control |
| **Thresholds** | Strictness |
| **Good edges** | Stable & interpretable |
| **Bad edges** | Chaotic & noisy |

---

**Good edge detection reveals structure; bad edge detection reveals texture and noise.**
