import cv2
import numpy as np
import math
import os

# Lists to store the points
topLeft=[]
bottomRight=[]

def drawBoxandSave(action, x, y, flags, userdata):
  # Referencing global variables 
  global topLeft, bottomRight, source, dummy
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
    topLeft=(x,y)
    source = dummy.copy()
  # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:
    bottomRight = (x,y)
    color = (0,0,0)
    cv2.rectangle(source, topLeft, bottomRight, color, 1) 
    cv2.imshow("Window",source)

    lowerY = topLeft[0]
    upperY = bottomRight[0]
    lowerX = topLeft[1]
    upperX = bottomRight[1]
   
    cv2.imwrite("output.jpg", source[lowerX+1:upperX-1,lowerY+1:upperY-1,:])

print("Enter filepath: ")
filepath = input()
while not os.path.isfile(filepath):
  print("Invalid file!")
  filepath = input()
  pass
source = cv2.imread(filepath,1)

# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawBoxandSave)
k = 0
# loop until escape character is pressed
while k!=27 :
  
  cv2.imshow("Window", source)
  cv2.putText(source,'Click top left corner & drag, ESC to exit' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX, 
              0.7,(255,255,255), 2 );
  k = cv2.waitKey(20) & 0xFF
cv2.destroyAllWindows()
