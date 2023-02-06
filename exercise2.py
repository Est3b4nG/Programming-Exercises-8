"""
Created by (Esteban Gómez) in  ${2022}
"""
class Rectangle:
    def __init__(self, base:float, height:float, square:bool):
        self.base = base
        self.height=height
        self.square=square

    def __str__(self):
        if self.square==True:
            square_v= ("You have a square of base and height of %f x %f"%(
                self.base,self.height))
        else:
            square_v = ("You have a rectangle of base and height of %f x %f"
                        % (
                self.base, self.height))
        return square_v

    def __eq__(self, other):
        if True:
            return "They are equal"

    def area(self):
        self.__area=self.__base * self.__height
        return self.__area

    def perimeter(self):
        self.__perimeter= 2 * self.__base + 2 * self.__height
        return self.__perimeter

    def biggest_side(self):
        if self.__height>self.base:
            self.__biggest_side=self.__height
        elif self.__height<self.base:
            self.__biggest_side=self.__base
        else:
            self.__biggest_side="It is a square"
        return self.__biggest_side

    def convert_to_square(self):
        if self.__biggest_side==self.__height:
            self.__base=self.__height
            return True
        else:
            return False

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self,base):
        if type(base) != int or base<=0:
            self.__base== 1
        else:
            self.__base= base

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        if type(height)!= float or height<=0:
            raise  TypeError("The height must be a positive non-zero float")
        else:
            self.__height= height

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self,square):
        if self.base == self.height:
            self.__square=True
        else:
            self.__square== False

