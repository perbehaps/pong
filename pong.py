import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 1024, height = 778)
wn.tracer(0)


# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-462,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(462,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx  = 0.2
ball.dy = 0.2


# Pen
pen = turtle.Turtle()
pen.speed(0) # animation speed not the movement speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,350)
pen.write("Player A: 0 Player B: 0",align="center", font=("Courier",24,"normal"))
pen.goto(0,349)
pen.write("__________________________________________________________________________________________________________________________________________________________________________",align="center")


# Function
def paddle_a_up():
   y = paddle_a.ycor()
   y += 20
   paddle_a.sety(y)

def paddle_a_down():
   y = paddle_a.ycor()
   y -= 20
   paddle_a.sety(y)

def paddle_b_up():
   y = paddle_b.ycor()
   y += 20
   paddle_b.sety(y)

def paddle_b_down():
   y = paddle_b.ycor()
   y -= 20
   paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") #user presses W , call the function
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# main game loop
def tick():
   wn.ontimer(tick, 10)

   global score_a
   global score_b

   #Move the ball
   ball.setx(ball.xcor() + ball.dx)
   ball.sety(ball.ycor() + ball.dy)

   #Border checking
   if ball.ycor() > 344:
      ball.sety(344)
      ball.dy *= -1
   if ball.ycor() < -374:
      ball.sety(-374)
      ball.dy *= -1
   if paddle_a.ycor() > 299:
      paddle_a.sety(299)
   if paddle_a.ycor() < -339:
      paddle_a.sety(-339)
   if paddle_b.ycor() > 299:
      paddle_b.sety(299)
   if paddle_b.ycor() < -339:
      paddle_b.sety(-339)

   # left and right borders
   if ball.xcor() > 502:
      ball.goto(0,0)
      ball.dx *= -1
      score_a +=1
      pen.clear()
      pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center", font=("Courier",24,"normal"))
      pen.write("__________________________________________________________________________________________________________________________________________________________________________",align="center")

   if ball.xcor() < -502:
      ball.goto(0,0)
      ball.dx *= -1
      score_b +=1
      pen.clear()
      pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center", font=("Courier",24,"normal"))
      pen.write("__________________________________________________________________________________________________________________________________________________________________________",align="center")

   #paddle and ball collisions
   if (ball.xcor() > 442 and ball.xcor() < 462) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
      ball.setx(442)
      ball.dx *= -1

   if (ball.xcor() < -442 and ball.xcor() > -462) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
      ball.setx(-442)
      ball.dx *= -1
   wn.update()

if __name__ == "__main__":
    tick()
    wn.mainloop()
