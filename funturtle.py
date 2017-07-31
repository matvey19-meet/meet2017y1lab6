import turtle

turtle.color("green")
turtle.shape('blank')

square = turtle.clone()
square.shape('square')


triangle=turtle.clone()
triangle.shape('triangle')


triangle.goto(0,0)
triangle.goto(100,0)
triangle.goto(100,100)
triangle.goto(0,100)
triangle.goto(0,0)
square.goto(300,300)
square.stamp()
square.goto(100,100)




turtle.mainloop()
