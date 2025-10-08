class Calendar() :
    def __init__(self) :
        self.day = 1
        self.month = 1
        self.year = 1970
    
    
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
                
    def next_year(self) :
        self.year += 1
        
        if self.day == 29 and self.month == 2 :
            self.month = 3
            self.day = 1
            
    
    def get_year(self) -> int : return self.year
    def get_month(self) -> int : return self.month
    def get_day(self) -> int : return self.day