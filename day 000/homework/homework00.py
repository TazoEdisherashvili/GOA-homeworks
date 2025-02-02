from turtle import*

penup()
goto(0, -100)
pendown()

#we draw house

#we draw square

width(10)
color("green")
forward(200)    
left(90)      
forward(200)     
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square

#drawing a door

forward(70)
left(90)
color("cyan")
forward(120)    
right(90)
forward(60)
right(90)
forward(120)
  
#end of door

#drawing a roof

penup()
goto(200, 100)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of roof

#we draw windows

penup()
goto(20, 30)
pendown()

color("blue")
begin_fill()
left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)  
forward(40)
end_fill()

#end of window

#we draw window

penup()
goto(140, 30)
pendown()

color("yellow")
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

#end of window


exitonclick()