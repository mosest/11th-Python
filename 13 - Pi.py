#Tara Moses
#Assignment 13: Pi
#March 15, 2013

import turtle,random

turtle.tracer(100)
total=0
inside=0

print "Hold on, I'm drawing 3000 points."

while total<3000:
  x=(random.random()*100.0)-50
  y=(random.random()*100.0)-50
  turtle.up()
  turtle.goto(x,y)
  turtle.down()
  if turtle.distance(0,0)<=50.0:
    turtle.pencolor("blue")
    inside+=1.0
  else:
    turtle.pencolor("orange")
  turtle.dot()
  total+=1.0

first_pi=4.0*(inside/total)
print "Dots method: pi~",first_pi,"\n"

print "Here, lemme try something else."
second_pi=0
for i in xrange(1000):
  if i%2!=0:
    if (i%4)==1:
      second_pi+=(4.0/i)
    else:
      second_pi-=(4.0/i)

print "Leibniz series: pi~",second_pi,"\n"

avg_pi=(first_pi+second_pi)/2.0

print "Average of these two estimations:",avg_pi

real_pi=3.14159265358
percent_error=abs(real_pi-avg_pi)/(real_pi)*100

print "Using",real_pi,"as pi, this experiment was",100-percent_error,"% accurate."
