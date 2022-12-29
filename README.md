# Hand Tracking wih OpenCV and MediaPipe
 
![Hand Tracking Gif](./images/handtracking.gif)

## Introduction

This is a study project I developed to create a real time Hand-Tracking program to better understand how to implement it in future projects.

Most of this code was taken as reference from this [informative video](https://www.youtube.com/watch?v=01sAkU_NvOY) created by [Murtaza Hassan](https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A).

## Development 

For this code, it was utilized the [MediaPipe](https://google.github.io/mediapipe/) framework. MediaPipe is a framework developed by Google which contains some amazing models that allows us to quickly get started with some fundamental AI problems such as Face Detection, Object Detection, Hair Segmentation and much more!

Having said that, the model I'll be working with for this project is going to be the [Hand Tracking](https://google.github.io/mediapipe/solutions/hands). Basically, it combines two main modules: the Palm Detection Model and the Hand Landmark Model.

As the name suggests, the **Palm Detection Model** will detect the user's hands and provides a cropped image of the hand. From there, the **Hand Landmark Model** can find up to 21 different landmarks on this cropped image of the hand (like the image bellow):

![Hand Landmarks](https://mediapipe.dev/images/mobile/hand_landmarks.png)
[Source](https://google.github.io/mediapipe/solutions/hands)


<mark>HandTrackingMin.py</mark> contains the minimum code that is required to run the Hand Tracking program. This code can (and will!) be changed and improved on future projects.

<mark>HandTrackingModule</mark> was created because, next time I need to use a HandTracking program inside another project, I won't need to write all of it again! By "just" asking the 21 values of cx and cy and importing **HandTrackingModule** on the project, it is possible to make use of the algorithm (just like I did at <mark>HandTrackingWithModule.py</mark>):


```
import HandTrackingModule as htm

detector = htm.handDetector()

img = detector.findHands(img)
landmarksList = detector.findPositions(img)

```

## Next Steps

As next steps, I pretend to implement this "simple" handtrack project in other more complex personal projects like:

- [x] [Finger Counter](https://github.com/lucasmirachi/finger-counter)
![Finger Counter](https://github.com/lucasmirachi/finger-counter/blob/main/finger_counter.gif?raw=true)
- [x] [Gesture Control of the system's volume](https://github.com/lucasmirachi/gesture-volume-control)
![Gesture Volume Control](https://github.com/lucasmirachi/gesture-volume-control/blob/main/images/gesturevolumecontrol.gif)
- [ ] Gesture Control of the mouse
