import turtle as t
import pixart

def draw_row(column, row, colors):
    '''Function to draw a row of pixels based on a string input'''
    for i in colors:
        pixart.move(column, row)
        # Conditions to select color based on input. Would've used dictionaries but we didn't learn them yet, so i can't use it :(
        if i == "0":
            pixart.pixel("black")
        elif i == "1":
            pixart.pixel("white")
        elif i == "2":
            pixart.pixel("red")
        elif i == "3":
            pixart.pixel("yellow")
        elif i == "4":
            pixart.pixel("orange")
        elif i == "5":
            pixart.pixel("green")
        elif i == "6":
            pixart.pixel("yellowgreen")
        elif i == "7":
            pixart.pixel("sienna")
        elif i == "8":
            pixart.pixel("tan")
        elif i == "9":
            pixart.pixel("gray")
        elif i in "Aa":
            pixart.pixel("darkgray")
        else:
            return False
        column += 1
    return True

def main():
    pixart.initialize()
    column = 0
    row = 0
    while True:
        colors = input("Enter a row of colors: ")
        if not draw_row(column, row, colors):
            raise Exception("Invalid color entered! Choose from '0123456789A'")
        if colors == "":
            print("Drawing complete! You can view it in the turtle window.")
            break
        row += 1
    t.exitonclick()

if __name__ == "__main__":
    main()