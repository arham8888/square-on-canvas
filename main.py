import turtle
turtle.Screen().bgcolor("orange")
sc=turtle.Screen()
sc.setup(300,400)
turtle.title("Welcome to window")
#turtle object creation
window=turtle.Turtle()
for i in range(4):
 window.right (90)
 window.forward (100) 
turtle.mainloop()