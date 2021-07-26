from turtle import Turtle, Screen

t: Turtle = Turtle()
s: Screen = Screen()

#sideLength: int = int(input('1-150: '))
sideLength: int = s.numinput('input', 'giveme a num: ')

# square circle
#numrep: int = 0
#while numrep <= 36:
for side in range(36):  
  t.forward(sideLength)
  t.right(90)
  t.forward(sideLength)
  t.right(90)
  t.forward(sideLength)
  t.right(90)
  t.forward(sideLength)
  t.right(90)
  t.right(10)
 # numrep =+1

#for side in range(360):