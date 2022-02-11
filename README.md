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
