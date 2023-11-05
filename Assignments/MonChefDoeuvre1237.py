# MonChefDoeuvre1237.py
#
# Description: Using turtle,create a drawing inspired from the work of a
# known painter (artist) using the Python Turtle module and its built-in
# functions. You must create and use at least one turtle from this module
# to create your drawing.
#
# Author: M. Vivan Prasad
#
# Name of Artist: Claude Monet
# Name of Chef D’oeuvre: Impression Sunrise
# Note to Instructor: I would like to keep this to myself, thanks!
# I am not the best at art, but I tried my best!
#
# Date Created: Thursday October 19th, 2023
# Last Updated: Wednesday October 25th, 2023

import turtle as tt

#Sets up the screen size (fixed to the painting)
screen = tt.Screen()
screen.setup(1200,931)
tt.colormode(255) #Set color to RGB tuple (255,255,255)

# Draws a rectangle with a length, width, line color and fill color
# at a particular starting point at (x,y)
def rectangle(x, y, length, width, 
              line_color, fill_color="",line_width=5,tilt=0):
    teleportTo(x,y)
    set_pen(line_color,line_width)
    if fill_color != "":
        tt.fillcolor(fill_color)
        tt.begin_fill()
    tt.setheading(tilt)
    for i in range(2):
        tt.forward(length)
        tt.right(90)
        tt.forward(width)
        tt.right(90)
    tt.setheading(0)  
        
    if fill_color != "":
        tt.end_fill()  
    return

#Uses the rectangle function, but since a square has the same side lengths
#
def square(side_length, color, fill_color="",line_width=5):
    #It just uses it for both the length and width parameters
    rectangle(side_length,side_length,color,fill_color,line_width)
    return

def polygon(x,y,radius,sides=0,
            line_color="",fill_color="",line_width=5,length=360):
    teleportTo(x,y)
    set_pen(line_color,line_width)

    if fill_color != "":
        tt.fillcolor(fill_color)
        tt.begin_fill()
    
    if sides == 0:
        #If a circle
        tt.circle(radius,extent=length)
    else:
        tt.circle(radius,extent=length,steps=sides)
    
    if fill_color != "":
        tt.end_fill()
    tt.setheading(0) 
    return


def circle(x,y,radius,line_color="",fill_color="",line_width=5,length=360):
    #Using the tt.circle() function, it can also draw polygons
    #A circle is a polygon with 0 sides
    polygon(x,y,radius,0,line_color,fill_color,line_width,length)
    return

# Lifts the pen up and goes to the x,y coordinate
# Makes life much easier with making shapes where needed ^-^
def teleportTo(x,y):
    tt.penup()
    tt.goto(x,y)
    return

#Sets the pen width and color
def set_pen(pen_color,pen_width=5):
    tt.pencolor = pen_color
    tt.pensize = pen_width
    tt.pendown()
    return

#These are all the stages of drawing in order
#It makes it easier to see the components and their origin!
def sky():
    rectangle(-600,460,1200,280,"",Color.skylight_orange,5,0)
    fog()
    circle(130,155,20,"",Color.scarlet_orange)
    circle(105,355,50,"",Color.pale_brown,10,315)
    circle(355,400,20,"",Color.pale_brown,10,315)
    circle(-200,300,40,"",Color.skylight_orange,0,235)
    circle(300,300,30,"",Color.skylight_orange,0,235)
    circle(-500,280,10,"",Color.skylight_orange,0,225)
    return

def fog():
    rectangle(-600,275,1200,280,"",Color.foggy_blue,5,0.2)
    return

def ripples():
    #Sun Reflection
    rectangle(130,-40,50,8,"",Color.sky_red,5,1)
    rectangle(142,-68,50,8,"",Color.scarlet_orange,5,-1)
    rectangle(150,-80,50,8,"",Color.sky_red,5,1)
    rectangle(136,-122,50,8,"",Color.sky_red,5,-1)
    rectangle(156,-152,50,8,"",Color.scarlet_orange,5,1)
    rectangle(106,-212,50,8,"",Color.sky_red,5,-1)
    rectangle(160,-246,50,8,"",Color.scarlet_orange,5,1)
    rectangle(100,-266,50,8,"",Color.scarlet_orange,5,1)
    rectangle(150,-276,50,8,"",Color.scarlet_orange,5,-1)
    #Main Boat Reflection
    rectangle(-350,-102,80,12,"",Color.muddy_green,5,-1)
    return

def water():
    rectangle(-600,0,1200,450,"",Color.warm_water,5,0.2)
    ships()
    ripples()
    return

def ships():
    tt.setheading(270)
    #Main Boat
    circle(-300,-185,200,"",Color.dark_water,10,180)
    circle(-30,-225,30,"",Color.muddy_green,10,160)
    rectangle(-75,-205,105,32,"",Color.muddy_green,10,2)
    rectangle(-85,-195,105,22,"",Color.muddy_green,10,0)
    rectangle(-30,-200,20,70,"",Color.muddy_green,0,180)

    rectangle(-500,100,10,102,"",Color.sky_blue,10,0)

    #Foggy Harbor
    rectangle(-400,-20,300,20,"",Color.foggy_blue,0,0)
    rectangle(-500,-80,500,20,"",Color.warm_water,0,0)
    rectangle(-280,-110,200,20,"",Color.warm_water,0,1)
    polygon(-308,8,90,1,"",Color.foggy_blue,0,180)
    polygon(-300,50,40,4,"",Color.sky_blue,0,180)
    polygon(-210,50,80,2,"",Color.sky_blue,0,180)
    polygon(-148,28,80,2,"",Color.foggy_cyan,0,180)
    polygon(-138,8,90,1,"",Color.foggy_blue,0,180)
    rectangle(-180,0,105,22,"",Color.foggy_blue,10,0)
    
    rectangle(20,50,350,80,"",Color.foggy_blue)
    rectangle(200,50,350,90,"",Color.muddy_green,0,0.1)
    rectangle(400,100,50,200,"",Color.foggy_cyan,0,)
    return

# I have been learning about classes!
# I made a Color class, in which different color 
# variables have been assigned the RGB values.
# That way, it does not clutter the code with all 
# the colors used for Mon Chef D'oeuvre!
class Color:
    pale_brown = (161, 128, 107)
    scarlet_orange = (207, 102, 83) #For the sun and its reflection!
    skylight_orange = (159, 121, 88) #For the sunrise sky
    foggy_blue = (125, 139, 139) #For the ships in the fog!
    foggy_cyan = (93, 119, 116)
    muddy_green = (26, 65, 57) #For the boats
    
    sky_blue = (138, 170, 174)
    sky_red = (251, 197, 189)
    #Colors for the water
    dark_water = (92, 94, 81)
    warm_water = (139, 146, 134)
    cool_water = (126, 140, 132)
    
# For making things VERY FAST
tt.speed("fastest")

#Main Process of the works
sky()
water()
# Fin
tt.penup()
tt.exitonclick()