"""
Created by (Esteban Gómez) in  ${2022}
"""
import random
from exercise2 import Rectangle

list_rectangle=[]
list_area=[]
list_perimeter=[]
list_biggestside=[]

number_elements=random.randint(10,1000)
for i in range(number_elements):
    rectangle=Rectangle(random.randint(1,10),random.randint(1,10),True)
    list_rectangle.append(rectangle)
    list_area.append(rectangle.area())
    list_perimeter.append(rectangle.perimeter())

for elem in list_rectangle:
    if i.square==True:
        print(i)
    else:
        if i.area()==max(list_area):
            print(i)
        elif i.permieter()==max(list_perimeter):
            print(i)
        elif i.biggest_side()==max(list_biggestside):
            print(i)