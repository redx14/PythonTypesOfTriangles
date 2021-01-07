#Andrey Ilkiv Assignment 3 Problem 1 10/05/2020 section 01

#-----------------------------------------------------
#This part of the code asks the user to input 6 numbers 1 for each corisponding location
#of a point on a triangle
point1x = float(input('Enter Point #1 - x position: '))

point1y = float(input('Enter Point #1 - y position: '))

point2x = float(input('Enter Point #2 - x position: '))

point2y = float(input('Enter Point #2 - y position: '))

point3x = float(input('Enter Point #3 - x position: '))

point3y = float(input('Enter Point #3 - y position: '))
#-----------------------------------------------------

#Prints heading with empty lines for formatting
print('' , 'The length of each side of your test shape is: ' , '' , sep='\n')

#-----------------------------------------------------
#Calculates and rounds up (2 decimal spots) the distance between each point for each of the 3 sides of a triangle
#using the distance formula sqrt((x1-x2)^2 + (y1-y2)^2)
Side1 = format(((point1x - point2x)**2 + (point1y - point2y)**2)**0.5, '.2f')

Side2 = format(((point2x - point3x)**2 + (point2y - point3y)**2)**0.5, '.2f')

Side3 = format(((point3x - point1x)**2 + (point3y - point1y)**2)**0.5, '.2f')
#-----------------------------------------------------

#-----------------------------------------------------
#Prints out the lengths of each side for the user

print('Side 1: ' , Side1)
print('Side 2: ' , Side3)
print('Side 3: ' , Side2)

#-----------------------------------------------------

#-----------------------------------------------------
#Checks if the triangle is a real triangle by making sure that the lengths of any 2 sides
#is = or > than the length of the third side
#After this check is complete the program checks if the triangle is an
#isosceles, equilateral, or scalene triangle
#equilater means all sides are the same we do this by confirming side1 = both sides 2 and 3 which in turn means side2 = side3 and side1 etc.
#If it is not a real triangle then program prints this is not a valid triangle
if (Side1 + Side2 > Side3 and Side2 + Side3 > Side1 and Side3 + Side1 > Side2):
    print('' , 'This is a valid triangle!' , sep='\n')
    if (Side1 == Side2 and Side1 == Side3):
        print('This is an equilateral triangle')
    if (Side1 != Side2 and Side1 != Side3):
        print('This is a Scalene triangle')
    if ((Side1 == Side2 and Side1 != Side3 and Side2 != Side3) or (Side2 == Side3 and Side2 != Side1 and Side3 != Side1) or (Side3 == Side1 and Side3 != Side2 and Side1 != Side2)):
        print('This is an Isosceles triangle')
else:
    print('' , 'This is not a valid triangle' , '' , sep='\n')
#-----------------------------------------------------
