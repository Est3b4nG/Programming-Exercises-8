"""
Created by (Esteban Gómez) in  ${2022}
"""

from exercise3 import Time

reps=int(input("How many intervals yoy want to introduce: "))
A=0
while A<reps:
    time1= Time(int(input("Introduce your initial hour: ")),
               int(input("Introduce your final hour: ")),
               int(input("Introduce your initial minute: ")),
               int(input("Introduce your final minute: ")))

    print("\nTime interval: ", "\n Initial time: ", "[", time1.initial_hour,
          ":",
          time1.initial_minute,
          "]", "\nFinal hour: ", "[", time1.final_hour,":",time1.final_minute,"]")
    A += 1
