from fractions import Fraction
from typing import Callable

def readonly(
    func: Callable
):
    def wrapper(self, *args):
        return lambda *args: func(self, *args)
    return property(wrapper)

class _TimeProperty:
    class __In:
        def __init__(self, seconds_in_property):
            self.__Second= seconds_in_property
            self.__Minute= self.__Second * 60
            self.__Hour  = self.__Minute * 60 
            self.__Day   = self.__Hour * 24
            self.__Week  = self.__Day * 7
            self.__Millisecond= self.__Second / 1000
            self.__Microsecond= self.__Millisecond / 1000
            self.__Nanosecond = self.__Microsecond / 1000
         

        @readonly
        def Nanoseconds(
            self, 
            quantity_of_nanoseconds: float
        )-> float:
            return float(self.__Nanosecond * quantity_of_nanoseconds) 
        
        @readonly
        def Microseconds(
            self,
            quantity_of_microseconds: float
        ):
            return float(self.__Microsecond * quantity_of_microseconds) 

        @readonly
        def Milliseconds(
            self,
            quantity_of_milliseconds: float
        )-> float:
            return float(self.__Millisecond * quantity_of_milliseconds) 
        
        @readonly
        def Seconds(
            self,
            quantity_of_seconds: float
        )-> float:
            return float(self.__Second * quantity_of_seconds) 
        
        @readonly
        def Minutes(
            self,
            quantity_of_minutes: float
        ):
            return float(self.__Minute * quantity_of_minutes)
        
        @readonly
        def Hours(
            self,
            quantity_of_hours: float
        ):
            return float(self.__Hour * quantity_of_hours)

        @readonly
        def Days(
            self,
            quantity_of_days: float
        ):
            return float(self.__Day * quantity_of_days)
        
        @readonly
        def Weeks(
            self,
            quantity_of_weeks: float
        ):
            return float(self.__Week * quantity_of_weeks)
        
    
         
    def __init__(self, seconds_in_property):
        self.In= _TimeProperty.__In(seconds_in_property)

Seconds= _TimeProperty(Fraction(1))

Milliseconds= _TimeProperty(Fraction(10**3))
Microseconds= _TimeProperty(Fraction(10**6))
Nanoseconds = _TimeProperty(Fraction(10**9))

Minutes= _TimeProperty(Fraction(1, Fraction(Seconds.In.Minutes(1))))
Hours  = _TimeProperty(Fraction(1, Fraction(Seconds.In.Hours(1))))
Days   = _TimeProperty(Fraction(1, Fraction(Seconds.In.Days(1))))
Weeks  = _TimeProperty(Fraction(1, Fraction(Seconds.In.Weeks(1))))

