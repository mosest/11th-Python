#Tara Moses
#Assignment 15.1: Triangle
#March 29, 2013

import math,turtle,Tkinter

class Triangle():
    def __init__(self,pA,pB,pC):
        self.pA=pA
        self.pB=pB
        self.pC=pC
        self.areatotal=self.area()
        
    def draw(self):
        turtle.up()
        turtle.goto(self.pA)
        turtle.down()
        turtle.goto(self.pB)
        turtle.goto(self.pC)
        turtle.goto(self.pA)
        
    def lengths(self):
        xa,ya=self.pA
        xb,yb=self.pB
        xc,yc=self.pC
        self.A=math.sqrt((xb-xc)**2+(yb-yc)**2)
        self.B=math.sqrt((xa-xc)**2+(ya-yc)**2)
        self.C=math.sqrt((xb-xa)**2+(yb-ya)**2)
        return self.A,self.B,self.C
    
    def area(self):
        s=(sum(self.lengths()))/2.0
        triangle_area=math.sqrt(s*(s-self.A)*(s-self.B)*(s-self.C))
        return triangle_area
    
    def perimeter(self):
        return sum(self.lengths())
    
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

    def isRight(self):
        if self.angles()!=-1:
            if self.a==90 or self.b==90 or self.c==90:
                return True
            else:
                return False
        else:
            return False

    def isIsosceles(self):
        if self.angles()!=-1:
            if self.A==self.B or self.A==self.C or self.B==self.C:
                return True
            else:
                return False

    def isEquilateral(self):
        if self.angles()!=-1:
            if self.A==self.B==self.C:
                return True
            else:
                return False

    def isPointInside(self,point):
        self.lengths()
        xa,ya=self.pA
        xb,yb=self.pB
        xc,yc=self.pC
        x_new,y_new=point
        
        length_anew=math.sqrt((xa-x_new)**2+(ya-y_new)**2)
        length_bnew=math.sqrt((xb-x_new)**2+(yb-y_new)**2)
        length_cnew=math.sqrt((xc-x_new)**2+(yc-y_new)**2)

        s_abnew=(self.C+length_anew+length_bnew)/2.0
        s_bcnew=(self.A+length_bnew+length_cnew)/2.0
        s_acnew=(self.B+length_cnew+length_anew)/2.0
        
        area_abnew=math.sqrt(s_abnew*(s_abnew-self.C)*(s_abnew-length_anew)*(s_abnew-length_bnew))
        area_bcnew=math.sqrt(s_bcnew*(s_bcnew-self.A)*(s_bcnew-length_bnew)*(s_bcnew-length_cnew))
        area_acnew=math.sqrt(s_acnew*(s_acnew-self.B)*(s_acnew-length_cnew)*(s_acnew-length_anew))
        small_areas=area_abnew+area_bcnew+area_acnew
        
        if self.areatotal-0.00001 <= small_areas <= self.areatotal+0.00001:
            return True
        else:
            return False

t=Triangle((0,0),(0,30),(40,0))
t.perimeter()
t.angles()
t.lengths()
t.isRight()
t.isIsosceles()
t.isEquilateral()
