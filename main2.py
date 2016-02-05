import turtle
import math

# class circle
class Circle:
	def __init__(self,snow,radius,x,y):
		snow.snowmani.up()	#set the initial absolute direction of turtle
		snow.snowmani.sety(y) #set the x and y coordinates of the turtle.These will act as initial points.Could have used goto too here.
		snow.snowmani.setx(x)
		arc_length=1*(math.pi/180)*radius#mathematical stuff.This is basically the arc length corresponding to the said radius.Many lines will be drawn.Which will give the illusion of circle.
		snow.snowmani.down()			#ready to draw a circle.
		snow.snowmani.begin_fill()	#We also have to fill white color
		for i in range(360):		#a circle is a 360 degree figure.
			snow.snowmani.forward(arc_length)	#make the line.This will be a small line.Many lines will be joined giving the illusion of circle.
			snow.snowmani.left(1)		#turn the turtle.
		snow.snowmani.up()#reset the direction
		snow.snowmani.end_fill()	#finish the filling.


class Arm:
	def __init__(self,snow,x,y,length,heading,color="black"):
		snow.snowmani.up()							#Same drill as above
		snow.snowmani.goto(x,y)						# goto the starting point.
		snow.snowmani.color(color)					#set the color of turtle.
		snow.snowmani.setheading(heading)				#set the destination of arm
		snow.snowmani.down()							#set the direction of turtle.
		snow.snowmani.forward(length)					#Go forward.
		snow.snowmani.setheading(heading+20)			
		snow.snowmani.forward(20)
		snow.snowmani.up()
		snow.snowmani.back(20)
		snow.snowmani.down()
		snow.snowmani.setheading(heading-20)
		snow.snowmani.forward(20)
		snow.snowmani.up()
		snow.snowmani.home()
		snow.snowmani.color("black")					#reset the color.


class Face:
	def __init__(self,snow,x,y,color="black",flag=False):
		snow.snowmani.up()
		snow.snowmani.goto(x+10,y)
		snow.snowmani.dot()
		snow.snowmani.goto(x-10,y)
		snow.snowmani.dot()
		snow.snowmani.goto(x,y-10)
		snow.snowmani.dot()
		snow.snowmani.goto(x-15,y-25)
		snow.snowmani.down()
		snow.snowmani.up()
		self.snowmani1=turtle.Turtle()
		self.snowmani1.penup()
		self.snowmani1.goto(x,y)
		self.snowmani1.pendown()
		self.snowmani1.color(color)
		self.snowmani1.fillcolor(color)
		arc_length=1*(math.pi/180)*10
		self.snowmani1.down()
		self.snowmani1.right(90)
		for i in range(180):
			self.snowmani1.forward(arc_length)
			self.snowmani1.left(1)
		if flag:							#if flag is true ,i.e,this is snowwoman than draw girlish lips.
			self.snowmani1.begin_fill()
			i=x+14
			j=y-10
			Circle(self,5,i,j)
			self.snowmani1.end_fill()
		hide(self.snowmani1)


class Button:
	def __init__(self,x,y,radius,color="black"):
		self.snowmani=turtle.Turtle()
		self.x=x
		self.y=y
		self.snowmani.fillcolor(color)
		hide(self.snowmani)
		Circle(self,radius,self.x,self.y)

class Rectangle:
	def __init__(self,x,y,width,height,color="red"):
		self.snowmani=turtle.Turtle()
		self.snowmani.fillcolor(color)
		self.snowmani.color(color)
		hide(self.snowmani)
		self.snowmani.begin_fill()
		self.snowmani.penup() # Pull the pen up
		self.snowmani.goto(x + width / 2, y + height / 2)#again mathematically when you solve the equation you get these formulas to draw the hat.
		self.snowmani.pendown() # Pull the pen down
		self.snowmani.right(90)
		self.snowmani.forward(height)
		self.snowmani.right(90)
		self.snowmani.forward(width)
		self.snowmani.right(90)
		self.snowmani.forward(height)
		self.snowmani.right(90)
		self.snowmani.forward(width)
		self.snowmani.end_fill()

class Triangle:
	def __init__(self,x,y,color="yellow"):
		self.snowmani=turtle.Turtle()
		self.snowmani.fillcolor(color)
		self.snowmani.color(color)
		hide(self.snowmani)
		steps=100				# random steps choosen.
		self.snowmani.begin_fill()
		self.snowmani.penup()
		self.snowmani.goto(x,y)
		self.snowmani.forward(steps)
		self.snowmani.left(120)
		self.snowmani.forward(steps)
		self.snowmani.left(120)
		self.snowmani.forward(steps)
		self.snowmani.left(200)
		self.snowmani.end_fill()

class Hair:
	def __init__(self,x,y):
		self.snowmani=turtle.Turtle()
		self.snowmani.pensize(2)
		self.snowmani.fillcolor("red")
		self.snowmani.color("red")
		hide(self.snowmani)
		self.snowmani.penup()
		self.snowmani.goto(x-30,y-5)
		self.snowmani.pendown()
		self.snowmani.right(100)
		self.snowmani.forward(40)
		self.snowmani.penup()
		self.snowmani.goto(x-25,y-5)
		self.snowmani.pendown()
		self.snowmani.left(10)
		self.snowmani.forward(30)
		self.snowmani.penup()
		self.snowmani.goto(x+25,y-5)
		self.snowmani.pendown()
		# self.snowmani.left(100)
		self.snowmani.forward(40)
		self.snowmani.penup()
		self.snowmani.goto(x+30,y-5)
		self.snowmani.pendown()
		self.snowmani.left(10)
		self.snowmani.forward(30)

# class Snowman
class Snowperson:
	def __init__(self,x,y,color="white"):
		self.start_x=x
		self.start_y=y
		self.snowmani=turtle.Turtle()
		self.snowmani.fillcolor(color)
		self.snowmani.speed(0)
		hide(self.snowmani)

	def draw(self):
		Circle(self,40,self.start_x,self.start_y)			#head
		Face(self,self.start_x,self.start_y+50)
		# Hair(self.start_x,self.start_y+80)
		Circle(self,70,self.start_x,self.start_y-140)		#upper torso
		Circle(self,100,self.start_x,self.start_y-340)		#lower torso
		Arm(self,self.start_x-70,self.start_y-70,50,160)	#left arm
		Arm(self,self.start_x+70,self.start_y-70,50,20)		#right arm	
		Button(self.start_x,self.start_y-30,10) 			#topmost button
		Button(self.start_x,self.start_y-60,10) 			#second button
		Button(self.start_x,self.start_y-170,10)			#first button
		Button(self.start_x,self.start_y-280,10)			#second button

	def __str__(self):
		return "this is snowperson"


class Snowman:
	def __init__(self,x,y,color="white"):
		self.start_x=x
		self.start_y=y
		self.snowmani=turtle.Turtle()
		self.snowmani.fillcolor(color)
		hide(self.snowmani)

	def draw(self):
		Circle(self,40,self.start_x,self.start_y)			#head
		Rectangle(self.start_x,self.start_y+80,100,5)		#hat below
		Rectangle(self.start_x,self.start_y+130,60,100)		#hat above
		Circle(self,70,self.start_x,self.start_y-140)		#upper torso
		Circle(self,100,self.start_x,self.start_y-340)		#lower torso
		Arm(self,self.start_x-70,self.start_y-70,50,160,"red")	#left arm
		Arm(self,self.start_x+70,self.start_y-70,50,20,"red")		#right arm
		Face(self,self.start_x,self.start_y+50)				#face
		Button(self.start_x,self.start_y-30,10,"grey") 			#topmost button
		Button(self.start_x,self.start_y-60,10,"grey") 			#second button
		Button(self.start_x,self.start_y-170,10,"grey")			#first button
		Button(self.start_x,self.start_y-280,10,"grey")			#second button		

	def __str__(self):
		return "this is snowman"


class Snowwoman:
	def __init__(self,x,y,color="white"):
		self.start_x=x
		self.start_y=y
		self.snowmani=turtle.Turtle()
		self.snowmani.fillcolor(color)
		hide(self.snowmani)

	def draw(self):
		Circle(self,40,self.start_x,self.start_y)			#head
		Circle(self,70,self.start_x,self.start_y-140)		#upper torso
		Circle(self,100,self.start_x,self.start_y-340)		#lower torso
		Arm(self,self.start_x-70,self.start_y-70,50,160,"red")	#left arm
		Arm(self,self.start_x+70,self.start_y-70,50,20,"red")		#right arm
		Face(self,self.start_x,self.start_y+50,"red",True)				#face
		Button(self.start_x,self.start_y-30,10,"yellow") 			#topmost button
		Button(self.start_x,self.start_y-60,10,"purple") 			#second button
		Button(self.start_x,self.start_y-170,10,"yellow")			#first button
		Button(self.start_x,self.start_y-280,10,"purple")			#second button		
		Triangle(self.start_x-50,self.start_y+75)
		Hair(self.start_x,self.start_y+80)

	def __str__(self):
		return "this is snowwomen"


class Screen():
	"""
	This is to manipulate the screen object.
	"""
	def __init__(self):
		self.screen=turtle.Screen()

	def wait(self):
		self.screen.exitonclick()

	def putitle(self,string):
		"""
		What to write when the drawing part of the program is completed.
		"""
		self.screen.title(string)

def hide(turtle):
	turtle.hideturtle()

if __name__=="__main__":
	snowperson=Snowperson(-500,100)
	snowperson.draw()
	snowman=Snowman(-100,100)
	snowman.draw()
	snowwoman=Snowwoman(300,100)
	snowwoman.draw()
	screen=Screen()
	screen.putitle("Three snowpeople")
	screen.wait()