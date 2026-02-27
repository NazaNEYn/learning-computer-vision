# How to think about this projcet like a CV engineer designing a system

---

# How CV Engineers Actually Think
A CV engineer does **not** start with:<br>
> “Which OpenCV functions do I use?”
<br>

They start with:<br>
> “What problem am I solving, and what am I not trying to solve?”

## 1. Define the Problem (Very Precisely)

Bad definition:<br>
> “Detect faces in a video.”

<br>

Engineering definition:<br>
> “For each frame in a video, find where faces are, count them, and show the result on the screen.”

This definition is important because it sets limits.<br>

It means:
* We work frame by frame
* We estimate, not guarantee
* We only visualize results

It also means we are **not**:
* Identifying people
* Tracking faces over time
* Trying to be perfect

## 2. Write Down Assumptions

Engineers simplify the world by making assumptions.<br>

**Input assumptions**
* The video is already recorded
* Faces mostly look forward
* Video quality is decent
* Lighting is okay

**System assumptions**
* The app should run fast enough to watch
* Some mistakes are okay
* Missing a face sometimes is okay

**Output assumptions**
* Boxes are enough
* Face count is per frame, not over time

## 3. Break the System Into Parts

Don’t think in code. Think in **modules**.<br>
Each part has one job.<br>

**A. Frame Source**<br>

Job:
* Give the next image from the video

What can go wrong:
* Video ends
* Frame can’t be read
* Reading is slow

**B. Preprocessing**<br>

Job:
* Prepare the image for detection

Decisions:
* Convert to grayscale
* Resize or not
* Trade accuracy for speed

What can go wrong:
* Wrong image format
* Bad resizing
* Coordinates don’t match

**C. Detector**<br>

Job:
* Find possible face locations

Important idea:
* The detector does not understand faces
* It only checks many small windows

What can go wrong:
* False positives
* Missed faces
* Sensitivity to size

**D. Interpretation**<br>

Job:
* Turn detections into useful info

In this project:
* Face count = number of boxes

Later projects might:
* Track faces
* Filter detections
* Add confidence

**E. Visualization**<br>

Job:
* Show results to a human

Important rule:
* Drawing must not affect detection

What can go wrong:
* Wrong box positions
* Wrong text
* Debugging the wrong part

## 3. Think in Data Flow
Engineers think about how data changes as it moves.<br>
