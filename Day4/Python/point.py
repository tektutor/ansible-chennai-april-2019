#!/usr/bin/python

class Point:
    
   def __init__(self):
       self.x = 0
       self.y = 0 

   def setValues (self,value1,value2):
       self.x = value1
       self.y = value2

   def getX(self):
       return self.x

   def getY(self):
       return self.y

   def printValues(self):
       print ( '###################')
       print ( 'X = ', self.getX() )
       print ( 'Y = ', self.getY() )
       print ( '###################')

point1 = Point()
point1.setValues ( 10, 20 )
point1.printValues()

point2 = Point()
point2.setValues ( 100, 200 )
point2.printValues()

point1.printValues()
