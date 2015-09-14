#Tara Moses
#Assignment 14: Bob the Ball
#March 25, 2013

class Ball:
  def __init__(self):
    self.psi=50
    self.isPopped=False

  def pop(self):
    if self.isPopped==True:
      print "Dorothy is already popped!"
    else:
      self.isPopped=True
      self.psi=0
      print "Dorothy is popped! psssssh..."

  def patch(self):
    if self.isPopped==False:
      print "PROGRAMMER uses PATCH! It's not very effective..."
    else:
      self.isPopped=False
      print "Dorothy is patched up."

  def inflate(self):
    if not self.isPopped:
      if self.psi<50:
        self.psi+=5
        print "Now inflated, Dorothy is now at",self.psi,"psi."
      else:
        print "Dorothy has exploded! WHAT HAVE YOU DONE"
        self.isPopped=True
        self.psi=0
      if self.psi==50:
        print "Any more and she'll explode!"
    else:
      print "Dorothy can't be inflated until you patch her up."

  def deflate(self):
    if self.isPopped==False and self.psi>0:
      self.psi-=5
      print "Now deflated, Dorothy is now at",self.psi,"psi."
    else:
      print "Dorothy is already deflated!"

  def bounce(self):
    if self.isPopped or self.psi==0:
      print "Dorothy can't bounce with no air! Try inflating her."
    else:
      print "Dorothy bounced",self.psi/10.0,"feet high!"
      self.psi-=5
      print "Her psi dropped to "+str(self.psi)+"."

Dorothy = Ball()

print "This is Dorothy the Ball. Dorothy will love you unconditionally! Have fun!\n"
print "1. Pop her"
print "2. Patch her up"
print "3. Inflate her"
print "4. Deflate her"
print "5. Bounce her"
print "6. Do nothing"
print "7. I'm done playing\n"

while True:
  option=raw_input("Dorothy asks, \"What do you want to do?\" Enter a number (1-7): ")
  option=int(option)
  if option==1:
    Dorothy.pop()
  elif option==2:
    Dorothy.patch()
  elif option==3:
    Dorothy.inflate()
  elif option==4:
    Dorothy.deflate()
  elif option==5:
    Dorothy.bounce()
  elif option==6:
    print "Nothing happened."
  elif option==7:
    print "Dorothy says, \"It was fun! Bye!\""
    break
  else:
    print "I didn't understand that. One more time?"
  
