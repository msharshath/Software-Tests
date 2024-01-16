# Importing necessary modules from the pyleap library
from pyleap import *

# Setting the size of the window
window.set_size(600, 600)

# Creating graphical elements for the windmill project
bg = Rectangle(0, 0, 600, 600, 'black')  # Background rectangle
#txt = Text("Windmill project in pyleap", 130, 540, 20, "black")  # Text element
body = Rectangle(285, 160, 10, 200, 'gray')  # Body of the windmill
mid = Circle(292, 372, 20, 'red')  # Circle representing the midpoint of the windmill

# Handles of the windmill
handle1 = Triangle(293, 374, 392, 460, 403, 440, 'purple')
handle1.rotation = 0
handle1.set_anchor(292, 372)

handle2 = Triangle(293, 374, 392, 460, 403, 440, 'orange')
handle2.rotation = 90
handle2.set_anchor(292, 372)

handle3 = Triangle(293, 374, 392, 460, 403, 440, 'blue')
handle3.rotation = 180
handle3.set_anchor(292, 372)

handle4 = Triangle(293, 374, 392, 460, 403, 440, 'yellow')
handle4.rotation = 270
handle4.set_anchor(292, 372)

# Path to the file containing windmill rotation speed
speed_file_path = 'C:/Users/z004tu0x/Desktop/IT_Group/2. Graphical_Wind_Turbine/speed.txt'

# Function to read windmill rotation speed from the file
def read_speed():
    try:
        with open(speed_file_path, 'r') as file:
            speed_str = file.readline().strip()
            if speed_str:
                speed = int(speed_str)
                if 1 <= speed <= 10:
                    return speed
                else:
                    print('Please make sure to enter the Speed limit  between 1 - Low and 10 - High')
                    exit()
                
            else:
                print("Error: Empty line or non-integer value in the file.")
                return None
    except Exception as e:
        print(f"Error reading speed from file: {e}")
        return None

# Function to draw the windmill and update rotation based on speed
def windmill(dt):
    bg.draw()
    #txt.draw()
    body.draw()
    mid.draw()
    handle1.draw()
    handle2.draw()
    handle3.draw()
    handle4.draw()

    speed = read_speed()

    if speed is not None:
        # Update handle rotation based on speed
        handle1.rotation += -speed
        handle2.rotation += -speed
        handle3.rotation += -speed
        handle4.rotation += -speed

# Repeating the windmill function to create animation
repeat(windmill)

# Running the pyleap application
run()