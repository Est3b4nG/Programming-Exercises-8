"""
Created by (Esteban Gómez) in  ${2022}
"""


class Person:
    def __init__(self, name:str, age:int, dni:int, dniletter: str,
                 weight:float, height:float,gender:str="Male"):
        self.name = name
        self.age = age
        self.dni = dni
        self.dniletter = dniletter
        self.weight = weight
        self.height = height
        self.gender = gender
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if type(name) != str:
            raise TypeError("The name must be an str")
        else:
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if type(age) != int:
            raise TypeError("The name must be a str")
        else:
            self.__age = age

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni: int):
        if type(dni) != int:
            raise TypeError("The dni must be an int")
        str_dni= str(dni)
        list1=[]
        for number in str_dni:
            list1.append(number)
        if len(list1)<1 or len(list1)>8:
            raise ValueError("The dni needs to have between 1 and 8 "
                             "characters")

        else:
            self.__dni = dni

    def dniletter(self,dniletter):
        letras = ["T","R","W","A","G","M","Y","F","P","D","X","B",
              "N","J","Z","S","Q","V","H","L","C","K","E"]
        letter_pos=self.__dni%23
        dniletter= letras[letter_pos]
        self.__dniletter=dniletter


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        if type(weight) != float:
            raise TypeError("The weight must be a float")
        else:
            self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        if type(height) != float:
            raise TypeError("The height must be a float")
        else:
            self.__height = height


    def __str__(self):
        data=("Person Information:\n Name: %s \n Sex:%s\n Age: %i years"
              " old\n DNI: %i %s\n Weight:%f kg\n Height:%f cm\n"%(
            self.name, self.gender, self.age, self.dni,
               self.dniletter,self.weight, self.height))
        return data

programmer= Person("Esteban", 18, 11185364, "*" , 64.3, 180.2)
user=Person(input("Name: "), int(input("Age: ")), int(input("DNI:")),
            str(input("DNI Letter: ")),float(input("Weight: ")),
            float(input("Height: ")),str(input("Gender: ")))
user_exception= Person(str(input("Name: ")), int(input("Age: ")), int(input(
    "DNI:")), str(input("DNI Letter: ")), float(90), float(185))

tuple_final=(programmer.__str__(),user.__str__(),user_exception.__str__())

for i in tuple_final:
    print(i)