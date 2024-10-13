"""
This module allows for the creation of a pixel art drawing using a turtle object.
The functions below implement basic drawing capabilities, where each pixel can be colored based on a character input.
Each function is developed incrementally as part of the project.

Functions:
1. get_color(character)
2. draw_color_pixel(color_string, turta)
3. draw_pixel(color_character, turta)
4. draw_line_from_string(color_string, turta)
5. draw_shape_from_string(turta)
"""
import turtle as t





#get_color function alligns or allocates each number to the requestion color as mentioned in activit 1 doc
def get_color(character):
    if character == "0":
        return "black"
    elif character == "1":
        return "white"
    elif character == "2":
        return "red"
    elif character == "3":
        return "yellow"
    elif character == "4":
        return "orange"
    elif character == "5":
        return "green"
    elif character == "6":
        return "yellowgreen"
    elif character == "7":
        return "sienna"
    elif character == "8":
        return "tan"
    elif character == "9":
        return "grey"
    elif character == "A":
        return "darkgrey"
    else:
        return None #this will return none if theres no valid input for example X also 


#draw_color_pixel function sets the color of the turtle and draws the pixel of size 30 and moves the turtle to the next position 
def draw_color_pixel(color_string, t):
    t.pendown()
    t.fillcolor(color_string)  #set the turtle color
    t.pencolor("black")
    t.begin_fill()
    for _ in range(4):  #draw a square (pixel)
        t.forward(30)  #each side of the pixel is 30 units
        t.right(90)
    t.end_fill()
    t.penup()
    t.forward(30)#move turtle to the next position
  

#draw_pixel function draws a single pixel based on the character given using get_color function to convert the character to a color and the draw_color_pixel function to draw the actual pixel
def draw_pixel(color_character, t):
    color_string = get_color(color_character)
    if color_string:
        draw_color_pixel(color_string, t)
    else:
        print(f"Invalid color code: {color_character}")

#draw_line_from_string function draws a row of pixels suing the input given by user and each character has a preassignemed color so if its invalid and not pre assigneed it shows up an error
def draw_line_from_string(color_string, t):
    for character in color_string:
        if get_color(character) is None:  #stop if an invalid color is found
            print(f"Invalid character: {character}")
            return False
        draw_pixel(character, t)
    return True

#draw_shape_from_string function keeps asking the user t continue and if they want to stop they can do enter or if invalid inout then also stop and this function also helps move turle move to the next line to start the next row
def draw_shape_from_string(t):
    while True:
        color_string = input("Enter a string of color codes (or press Enter to stop): ")
        if not color_string:  #stop if the string is empty
            break
        if not draw_line_from_string(color_string, t):
            print("Drawing stopped due to invalid input.")
            break
        t.screensize(3000, 3000)
        t.penup()  #move the turtle to the next line
        t.setpos(t.xcor() - len(color_string) * 30, t.ycor() - 30)
        t.pendown()

def clear_screen():
    print("\n" * 100)

#we use the main funtion to add all the funtions under one and then we only have to call it once 


if __name__ == "_main_":
    main()
#here we call the main functin and only that because the function itself has everything in it 
if __name__ == "__main__":
    main()