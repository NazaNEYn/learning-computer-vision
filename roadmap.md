# Computer Vision Roadmap for myself


## Table of Contents: 8-Week Computer Vision Starter Plan

1.  [WEEK 1: Images Are Data](#week-1)
2.  [WEEK 2: Image Processing Basics](#week-2)
3.  [WEEK 3: Color & Motion](#week-3)
4.  [WEEK 4: Face Detection (Classic CV)](#week-4)
5.  [WEEK 5: Intro to Machine Learning](#week-5)
6.  [WEEK 6: Deep Learning Foundations](#week-6)
7.  [WEEK 7: Object Detection](#week-7)
8.  [WEEK 8: Portfolio Project](#week-8)
9.  [Rules and Schedule](#rules-and-schedule)

----------

# 8-Week Computer Vision Starter Plan (3 hrs/day)

This plan is designed for beginners to gain confidence and practical skills in Computer Vision (CV) with a focus on consistency over speed.

## Schedule assumption

* ⏱️ ~3 hours/day
* 📅 5 days/week (take weekends off or use them lightly)
* 🎯 Goal: confidence + real CV projects, not mastery

---

## DAILY STRUCTURE (same every day)

| Time Slot | Activity | Focus |
| :--- | :--- | :--- |
| **Hour 1** | Learn | Short video / article, Take minimal notes |
| **Hour 2** | Code | Follow examples, Modify them |
| **Hour 3** | Build | Small task or mini-project, Break things on purpose |

> This structure prevents overwhelm.

---

<a id="week-1"></a>
## WEEK 1: Images Are Data 🖼️

**Goal**
Understand what images actually are and get comfortable with OpenCV.

| Learn | Tools |
| :--- | :--- |
| Pixels & image arrays | Python |
| RGB vs grayscale  | OpenCV (cv2) |
| Loading & displaying images | NumPy |

| Daily plan | Task |
| :--- | :--- |
| **Day 1** | Install OpenCV. Load & display an image. Print image shape. |
| **Day 2** | Convert to grayscale. Resize & crop images. |
| **Day 3** | Draw lines, circles, rectangles on images. |
| **Day 4** | Split RGB channels. Change brightness & contrast. |
| **Day 5** | 🎯 **Mini Project: Image Playground** Load any image. Apply 3 transformations. Display before & after. |

> ✅ **Result:** Images stop feeling “mystical”

---

<a id="week-2"></a>
## WEEK 2: Image Processing Basics 🔧

**Goal**
Learn how computers find edges, shapes, and colors.

| Learn |
| :--- |
| Blurring |
| Edge detection  |
| Thresholding |
| Contours |

| Daily plan | Task |
| :--- | :--- |
| **Day 1** | Gaussian blur. Why noise matters. |
| **Day 2** | Canny edge detection. |
| **Day 3** | Thresholding (binary images). |
| **Day 4** | Contours & shape detection. |
| **Day 5** | 🎯 **Mini Project: Shape Detector** Detect circles & rectangles in an image. Draw bounding boxes. |

> ✅ **Result:** You’re “seeing” like a computer

---

<a id="week-3"></a>
## WEEK 3: Color & Motion 🎨🎥

**Goal**
Work with color spaces and detect movement.

| Learn |
| :--- |
| HSV color space  |
| Webcam frames |
| Frame differencing |

| Daily plan | Task |
| :--- | :--- |
| **Day 1** | RGB vs HSV. Convert images to HSV. |
| **Day 2** | Detect a specific color (red/blue). |
| **Day 3** | Read webcam video. Display real-time frames. |
| **Day 4** | Simple motion detection. |
| **Day 5** | 🎯 **Mini Project: Color Tracking App** Track a colored object using webcam. |

> ✅ **Result:** Real-time CV feels exciting

---

<a id="week-4"></a>
## WEEK 4: Face Detection (Classic CV) 😄

**Goal**
Build something impressive without deep learning yet.

| Learn |
| :--- |
| Haar cascades |
| Face detection basics  |

| Daily plan | Task |
| :--- | :--- |
| **Day 1** | What face detection is. Load Haar model. |
| **Day 2** | Detect faces in images. |
| **Day 3** | Detect faces in webcam video. |
| **Day 4** | Improve accuracy & speed. |
| **Day 5** | 🎯 **Mini Project: Face Detection App** Draw boxes around faces. Show face count. |

> ✅ **Result:** Confidence boost 💪

---

<a id="week-5"></a>
## WEEK 5: Intro to Machine Learning 🤖

**Goal**
Understand why deep learning exists.

| Learn | Tools |
| :--- | :--- |
| What a model is | `scikit-learn` |
| Training vs inference | |
| Classification concept  | |

| Daily plan | Task |
| :--- | :--- |
| **Day 1** | ML basics (no math heavy). |
| **Day 2** | Train a simple image classifier. |
| **Day 3** | Test & evaluate predictions. |
| **Day 4** | Improve results (resize, normalize). |
| **Day 5** | 🎯 **Mini Project: Digit Recognizer** Recognize handwritten digits (MNIST). |

> ✅ **Result:** ML stops being scary

---

<a id="week-6"></a>
## WEEK 6: Deep Learning Foundations 🧠🔥

**Goal**
Understand CNNs intuitively.

| Learn | Tool |
| :--- | :--- |
| What CNNs do (conceptually)  | PyTorch |
| Pre-trained models | |
| Transfer learning | |

| Daily plan | Task |
| :--- | :--- |
| **Day 1** | PyTorch basics. Tensors. |
| **Day 2** | Load a pre-trained CNN. |
| **Day 3** | Classify images using a CNN. |
| **Day 4** | Fine-tune a model. |
| **Day 5** | 🎯 **Mini Project: Image Classifier** Classify everyday objects. |

> ✅ **Result:** You’re officially doing DL

---


<a id="week-7"></a>
## WEEK 7: Object Detection 🚗📦

**Goal**
Detect multiple objects in images/videos.

| Learn |
| :--- |
| Object detection vs classification |
| YOLO intuition  |

| Daily plan | Task |
| :--- | :--- |
| **Day 1** | Load YOLO model. |
| **Day 2** | Detect objects in images. |
| **Day 3** | Detect objects in video. |
| **Day 4** | Improve confidence thresholds. |
| **Day 5** | 🎯 **Mini Project: Real-Time Object Detector** Webcam object detection. |

---

<a id="week-8"></a>
## WEEK 8: Portfolio Project 🏗️

**Goal**
Build ONE project you’re proud of.

| Choose ONE |
| :--- |
| Face mask detector |
| Gesture recognition |
| Smart surveillance system |
| Object counter |

| Daily plan | Task |
| :--- | :--- |
| **Days 1–4** | Build |
| **Day 5** | Polish & document |

---

## VERY IMPORTANT RULES ⚠️

* ❌ Don’t try to understand everything
* ❌ Don’t compare yourself to YouTubers
* ❌ Don’t add new topics early
* ✔ Build ugly things
* ✔ Break code
* ✔ Be curious

---

## Final reassurance

If you follow even 70% of this plan, you’ll:
* Truly understand what CV is
* Know if you want it as a career
* Have real projects to show

