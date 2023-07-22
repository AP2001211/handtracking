# Handtracking
This was basically a project I worked on to get some experience with mediapipe, and openCV. 

HandTrackingMin.py
It uses Mediapipe's built-in solution for hand tracking instead of a custom hand-tracking module. 
It also draws circles on the detected landmarks (fingers) and connects them with lines to represent the hand shape. 

handTrackingModule.py
It is using Python with the OpenCV and Mediapipe libraries to perform real-time hand tracking from a video stream. 
It detects hands in the video, identifies landmarks on the seen hands, and calculates the frames per second (FPS) of the video stream.

VolumeHandControl.py
This code uses the handTrackingModule (probably a custom module) along with OpenCV and NumPy to perform hand tracking on a video stream 
from the webcam. It detects the distance between the tips of the thumb and the index finger and uses that distance to control the system 
volume. The code calculates the volume level using interpolation and adjusts the system volume accordingly using the Osascript module.

**NOTE**
Regarding the use of osascript, it is a macOS-specific command-line tool used to execute AppleScript commands. This means the code as it is 
will work on macOS, but not on Windows. If you want to control the system volume on Windows, you will need to use a different approach that 
is compatible with the Windows operating system.
for WINDOWS: use pycaw code and explanation of how to use pycaw:
https://github.com/AndreMiras/pycaw

htGame.py
This code is using Python with the OpenCV and Mediapipe libraries to perform real-time hand tracking from a video stream. It detects hands 
in the video, identifies landmarks on the seen hands, and calculates the frames per second (FPS) of the video stream.
