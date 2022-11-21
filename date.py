class Date:
    def __init__(self, date, month, year):
        self.__date = date
        self.__month = month
        self.__year = year
    
    def __str__(self):
        return f"{self.__date}:{self.__month}:{self.__year}"
