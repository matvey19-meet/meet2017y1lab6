#________________________________
def up():                      #|
    global direction           #|
    direction = UP             #|
    print("You pressed up!")   #|
                               #|    
def down():                    #|
    global direction           #|
    direction = DOWN           #|
    print("You pressed down!") #|
                               #|
def left():                    #|
    global direction           #| 
    direction = LEFT           #| 
    print("You pressed left!") #|
                               #|
def right():                   #| 
    global direction           #|  
    direction = RIGHT          #|
    print("You pressed right!")#|
#___________________________________________________________________________________



import turtle

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"



UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()





turtle.mainloop()
