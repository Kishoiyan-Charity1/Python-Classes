class Circle:
    def __init__(self,r):
        self.r= r
    
    def area(self):
        A= 3.14*(self.r * self.r)
        return A

    def circumference(self):
        C=(self.r * 3.14)*2
        return C


class Square:
    def __init__(self,a):
        self.a= a
        
    def square_area(self):
        A= self.a * self.a
        return A

    def square_perimeter(self):
        P= (self.a)*4


    
class Rectangle:
    def __init__(self,l,w):
        self.w= w
        self.l= l

    def rectangle_area(self):
        A= self.w * self.l
        return A

    def rectangle_perimeter(self):
        P= 2 * (self.l + self.w) 
        return P


class Sphere:
    def __init__(self,r):
        self.r= r

    def surfacearea(self):
        A= 4/3 * (3.142(self.r * self.r * self.r))
        return A

    
    


        


