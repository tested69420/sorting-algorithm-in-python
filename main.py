import turtle
import random
a = []
colors = ["red","orange red","orange","yellow","green","medium sea green","blue","indigo","slate blue","purple"]
for e in range(50):
    a.append(random.randint(1,9))
myTurtles = []
b = str(sorted(a))
c = []
for x in range(len(b)):
    if b[x] != "[" and b[x] != "," and b[x] != "]" and b[x] != " ":
        c.append(b[x])
for i in range(len(a)):
    myTurtles.append(turtle.Turtle())
    myTurtles[i].width(5)
    myTurtles[i].speed(0)
    myTurtles[i].forward(i * 5)
    myTurtles[i].left(90)
    myTurtles[i].color(colors[int(a[i])])
    myTurtles[i].forward(a[i] * 5)
for z in range(len(myTurtles)):
    myTurtles[z].clear()
    myTurtles[z].reset()
myTurtles = []
for y in range(len(a)):
    myTurtles.append(turtle.Turtle())
    myTurtles[y].width(5)
    myTurtles[y].speed(0)
    myTurtles[y].forward(y * 5)
    myTurtles[y].left(90)
    myTurtles[y].color(colors[int(c[y])])
    myTurtles[y].forward(int((1 + int(c[y])) * 5))
turtle.mainloop()