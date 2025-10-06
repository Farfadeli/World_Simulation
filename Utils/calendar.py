class Calendar() :
    def __init__(self) :
        self.day = 01
        self.month = 01
        self.year = 0
    
    
    def is_leap_year(self) :
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)
    
    def next_day(self) : 
        self.day += 1
        if (self.month in [1,3,5,7,8,10] and self.day > 31) or (self.month in [4,6,9,11] and self.day > 30) or (self.month == 2 and self.is_leap_year() and self.day > 29) or (self.month == 2 and self.is_leap_year() == False and self.day > 28):
            self.day = 1
            self.month += 1
        else :
            if self.day > 31 :
                self.day = 1
                self.month = 1
                self.year += 1