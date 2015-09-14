#Tara Moses
#Assignment 17: Fractions
#April 22, 2013

class Fraction:
    def __init__(self,n,d):
        self.n=n
        self.d=d

    def reduce(self):
        if self.n>=self.d:
            a=self.n
            b=self.d
        else:
            b=self.n
            a=self.d
        gcd=b
        while True:
            if a%b!=0:
                a=a%b
            else:
                gcd=b
                break
            if b%a!=0:
                b=b%a
            else:
                gcd=a
                break
        f4=Fraction(self.n/gcd,self.d/gcd)
        if self.d/gcd==1:
            return self.n/gcd
        else:
            return f4

    def __add__(self,f2):
        n1=self.n
        d1=self.d
        n2=f2.n
        d2=f2.d
        f3=Fraction(n1*d2+n2*d1,d1*d2)
        return f3.reduce()

    def __sub__(self,f2):
        n1=self.n
        d1=self.d
        n2=f2.n
        d2=f2.d
        f3=Fraction(n1*d2-n2*d1,d1*d2)
        return f3.reduce()

    def __mul__(self,f2):
        n1=self.n
        d1=self.d
        n2=f2.n
        d2=f2.d
        f3=Fraction(n1*n2,d1*d2)
        return f3.reduce()

    def __div__(self,f2):
        n1=self.n
        d1=self.d
        n2=f2.n
        d2=f2.d
        f3=Fraction(n1/d1,n2/d2)
        return f3.reduce()

    def __str__(self):
        return str(self.n)+"/"+str(self.d)

#program starts here
while True:
    input_statement=raw_input("Input an expression with fractions and spaces (e.g. 3/4 + 1/2): ")
    first_fraction,operator,second_fraction=input_statement.split(" ")

    first_slash=first_fraction.find("/")
    second_slash=second_fraction.find("/")

    n1=int(first_fraction[:first_slash])
    d1=int(first_fraction[first_slash+1:])
    n2=int(second_fraction[:second_slash])
    d2=int(second_fraction[second_slash+1:])

    f1=Fraction(n1,d1)
    f2=Fraction(n2,d2)
    f3=0

    if operator=="+":
        f3=f1+f2
        print f1,"+",f2,"=",f3
    elif operator=="-":
        f3=f1-f2
        print f1,"-",f2,"=",f3
    elif operator=="*":
        f3=f1*f2
        print f1,"*",f2,"=",f3
    elif operator=="/":
        f3=f1/f2
        print f1,"/",f2,"=",f3
    else:
        print "What?"

    again=raw_input("Would you like to calculate something else? (y/n): ")
    if again=="y" or again=="Y":
        pass
    else:
        break
