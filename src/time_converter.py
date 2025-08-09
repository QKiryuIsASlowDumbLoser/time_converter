from fractions import Fraction

class _TimeProperty:
    class __In:
        def __init__(self, seconds_in_property):
            self.__Second= seconds_in_property
            self.__Minute= self.__Second * 60
            self.__Hour  = self.__Minute * 60 
            self.__Day   = self.__Hour * 24
            self.__Week  = self.__Day * 7
         
        def __Seconds(self, quantity_of_seconds: float)-> float:
            return float(self.__Second * quantity_of_seconds) 

        @property
        def Seconds(self):
            return self.__Seconds
        
        def __Minutes(self, quantity_of_minutes: float)-> float:
            return float(self.__Minute * quantity_of_minutes)

        @property
        def Minutes(self):
            return self.__Minutes
        
        def __Hours(self, quantity_of_hours: float)-> float:
            return float(self.__Hour * quantity_of_hours)

        @property
        def Hours(self):
            return self.__Hours
        
        def __Days(self, quantity_of_days: float)-> float:
            return float(self.__Day * quantity_of_days)

        @property
        def Days(self):
            return self.__Days
        
        def __Weeks(self, quantity_of_weeks: float)-> float:
            return float(self.__Week * quantity_of_weeks)

        @property
        def Weeks(self):
            return self.__Weeks
        
    
         
    def __init__(self, seconds_in_property):
        self.In= _TimeProperty.__In(seconds_in_property)

Seconds= _TimeProperty(1)
Minutes= _TimeProperty(Fraction(1, int(Seconds.In.Minutes(1))))
Hours  = _TimeProperty(Fraction(1, int(Seconds.In.Hours(1))))
Days   = _TimeProperty(Fraction(1, int(Seconds.In.Days(1))))
Weeks  = _TimeProperty(Fraction(1, int(Seconds.In.Weeks(1))))

