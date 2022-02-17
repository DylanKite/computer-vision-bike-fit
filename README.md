# computer-vision-bike-fit
Using opencv to determine a better bike fit

## Joints to track
when using this software stickers have to be placed on the body in order to track body position while the user is riding 
they have to be placed in the following locations:
- first knuckle of pinky toe
- ankle bone 
- side of knee 
- hip bone
- shoulder 
- elbow 
- wrist

## optimal angles: 
using *** the following angles are desireable to target: 

## software tools:
This program is developed using the following tools:
-Python 3.10
-OpenCV
-numpy

## getting colour values:
In order to get the colour values for the joints a single frame will be converted to hsv
and when you hover the mouse over the pixel you need to get the value from it will display it
as an rgb value as well as the x,y coordinate for it,

b = h
g = s
r = v

it should sit in the middle of the range of the upper and lower limits for the colour detection
and should be tight enough to not get false positives but not too tight that it falls outside
the range

need to find a way to automate this maybe?

each joint is a specific colour far enough away from a different colour that it isnt an issue?

##Class Descriptions
This section will describe the classes invoved with this project and how they will be inhearated

#class joint
This class will be used to contain the data associated with the joints
It will have the following members:
Member Variables:
- associated_colour: this will be used when spitting the image to determine the joint
- coordinates: This will be the coordinates for the detected circle. This will be public
- hsv_image: This will be the stored HSV image that will be used for circle detection
Public Member Functions:
- constrtructor: will be passed the name of the joint and it will set the colour to be opened
- update_coordinate: This function will be called to get the new coordinates for the joint. It will return 1 if successful and 0 if failure
Private Members:
- open_stream: This function will be called by the constructor to open the image file - will return an int 1 = pass 0 = fail
- get_frame: this function will be used to get the latest frame from the stream and will be calld by update_coordinate
- split_colour: This function will be called after get_frame by update_coordinate and will be used to split the new frame based on the colour associated with this class.
- detect_circle
