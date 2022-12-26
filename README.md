# hand-tracking
 
 ## Introduction

This is a study project I developed to create a Hand-Tracking in real time program in order to better understand how to implement it in future projects.

Most of this code was done by Murtaza Hassan.

For this code, it was utilized the [MediaPipe](https://google.github.io/mediapipe/) famework. MediaPipe is a framework developed by Google which contains some amazing models that allows to quickly get started with some fundamental AI problems such as Face Detection, Object Detection, Hair Segmentation and much more!

Having said that, the model I'll be working for this project is going to be the [Hand Tracking](https://google.github.io/mediapipe/solutions/hands). Basically, it combines two main modules: the Palm Detection Model and the Hand Landmark Model.

As the name suggests, the **Palm Detection Model** will detect the user's hands and provides a cropped image of the hand. From there, the **Hand Landmark Model** can find 21 different landmarks on this cropped image of the hand (like the image bellow):

![Hand Landmarks](https://mediapipe.dev/images/mobile/hand_landmarks.png)
[Source](https://google.github.io/mediapipe/solutions/hands)



HandTrackingMin.py contains the minimum code that is required to run the Hand Tracking program. This code can (and will!) be changed and improved on future projects.

HandTrackingModule was created because, next time I need to use a HandTracking program inside another project, I won't need to write all of it again! By "just" asking the 21 values of cx and cy