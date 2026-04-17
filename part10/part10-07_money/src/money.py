# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, __euros: int, __cents: int):
        self.__euros = __euros
        self.__cents = __cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __gt__(self, another):
        if self.__euros > another.__euros:
            return True
        elif self.__euros == another.__euros and self.__cents > another.__cents:
            return True
        return False
    
    def __lt__(self, another):
        if self.__euros < another.__euros:
            return True
        elif self.__euros == another.__euros and self.__cents < another.__cents:
            return True
        return False
    
    def __ne__(self, another):
        # return not self.__eq__(another)
        return self.__euros != another.__euros or self.__cents != another.__cents

    def __add__(self, another):
        s = self.__euros + (self.__cents/100)
        a = another.__euros + (another.__cents/100)
        # ans = round((s + a), 1)
        ans = s + a
        euro = int(ans)
        # cent = int((ans - euro)*100)
        cent = int(round((ans - euro), 2) * 100)
        return Money(euro, cent)
    
    def __sub__(self, another):
        s = self.__euros + (self.__cents/100)
        a = another.__euros + (another.__cents/100)
        ans = s - a
        if ans < 0:
            raise ValueError("a negative result is not allowed") 
        euro = int(ans)
        cent = int(round((ans - euro), 2) * 100)
        return Money(euro,cent)

if __name__ == "__main__":
    e1 = Money(15, 95)
    e2 = Money(15, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1