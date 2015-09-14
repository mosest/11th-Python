#Tara Moses
#Assignment 15.2: Triangle Bonus
#April 7, 2013

import math,turtle,Tkinter

class Triangle():
    def __init__(self,pA,pB,pC):
        self.pA=pA
        self.pB=pB
        self.pC=pC

    def angles(self):
        self.lengths()
        if self.C!=0 and self.A!=0 and self.B!=0:
            a=math.acos((self.C**2+self.B**2-self.A**2)/(2*self.C*self.B))
            self.a=math.degrees(a)
            b=math.acos((self.A**2+self.C**2-self.B**2)/(2*self.C*self.A))
            self.b=math.degrees(b)
            c=math.acos((self.A**2+self.B**2-self.C**2)/(2*self.A*self.B))
            self.c=math.degrees(c)
            return self.a,self.b,self.c
        else:
            return -1

    def lengths(self):
        xa,ya=self.pA
        xb,yb=self.pB
        xc,yc=self.pC
        self.A=math.sqrt((xb-xc)**2+(yb-yc)**2)
        self.B=math.sqrt((xa-xc)**2+(ya-yc)**2)
        self.C=math.sqrt((xb-xa)**2+(yb-ya)**2)
        return self.A,self.B,self.C

    def isRight(self):
        self.lengths()
        if self.angles()!=-1:
            if self.A**2+self.B**2==self.C**2 or self.C**2+self.B**2==self.A**2 or self.A**2+self.C**2==self.B**2:
                return True
            else:
                return False
        else:
            return False

    def draw(self):
        xa,ya=self.pA
        xb,yb=self.pB
        xc,yc=self.pC
        turtle.up()
        turtle.goto(int(xa)*100,int(ya)*100)
        turtle.down()
        turtle.goto(int(xb)*100,int(yb)*100)
        turtle.goto(int(xc)*100,int(yc)*100)
        turtle.goto(int(xa)*100,int(ya)*100)
        turtle.clear()

#program starts hurr

count=0
XA=[]
XB=[]
XC=[]
YA=[]
YB=[]
YC=[]

triangle_file=file("triangles.txt")
for line in triangle_file:
    line=line.strip()
    coordinates=line.split(" ")
    xa,ya,xb,yb,xc,yc=coordinates
    XA.append(int(xa))
    YA.append(int(ya))
    XB.append(int(xb))
    YB.append(int(yb))
    XC.append(int(xc))
    YC.append(int(yc))

for i in range(len(XA)):
    t=Triangle((XA[i],YA[i]),(XB[i],YB[i]),(XC[i],YC[i]))
    if t.isRight():
        count+=1
print "The sum of all",count,"right triangles is:",count*180.0
