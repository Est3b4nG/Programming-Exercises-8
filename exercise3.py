"""
Created by (Esteban Gómez) in  ${2022}
"""

class Time:
    """This class find if an interval of hours is in the morning, afternoon,
    evening or night"""


    def __init__( self,initial_hour:int,final_hour:int, initial_minute:int,
                 final_minute:int):
        self.initial_hour = initial_hour
        self.final_hour = final_hour
        self.initial_minute = initial_minute
        self.final_minute = final_minute

        if initial_hour>24 or initial_hour<0:
            self.final_hour=self.initial_hour
            if final_hour<=24 or final_hour<0:
                self.initial_hour=0
                self.final_hour=0
        else:
            self.initial_hour=initial_hour

            if final_hour>=24 or final_hour<0:
                self.final_hour=initial_hour
            else:
                self.final_hour=final_hour

        if initial_minute>60 or initial_minute<0:
            self.initial_minute=0
        else:
            self.initial_minute=initial_minute

        if final_minute>60 or final_minute<0:
            self.final_minute=0
        else:
            self.final_minute=final_minute

        if initial_hour*60 + initial_minute< final_hour*60 + final_minute:
            self.initial_hour=final_hour
            self.final_hour=initial_hour
            self.initial_minute=final_minute
            self.final_minute=initial_minute

        times=["Morning", "afternoon", "evening", "night"]
        morning, afternoon, evening, night= False, False, False, False
        if initial_hour>=6 or final_hour<6:
            morning=True
        if (initial_hour>=6 and initial_hour<=12) or (final_hour>=6 and final_hour<12):
            afternoon=True
        if (initial_hour>=12 and initial_hour<18) or (final_hour<=12 and
                                                      final_hour<18):
            evening=True
        if (initial_hour>=18 and initial_hour<6) or (final_hour>18 and
                                                     final_hour<24):
            night=True

        list_of_values=[morning,afternoon,evening,night]
        remainder= final_hour - initial_hour

        for i in range (1, len(list_of_values)-1):
            if remainder>=6 and remainder<18:
                if list_of_values[i-1]==list_of_values[i+1]:
                    list_of_values[i]=True
            elif remainder>18:
                list_of_values[i]=True
        print("is included in: ")
        for i in range(len(list_of_values)):
            if list_of_values[i]==True:
                print(times[i], end=",")

