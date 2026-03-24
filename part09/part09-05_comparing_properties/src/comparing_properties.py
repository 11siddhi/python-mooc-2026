# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to):
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to):
        this_price = self.price_per_sqm * self.square_metres
        compared_price = compared_to.price_per_sqm * compared_to.square_metres
        return abs(this_price - compared_price)

    def more_expensive(self, compared_to):
        this_price = self.price_per_sqm * self.square_metres
        compared_price = compared_to.price_per_sqm * compared_to.square_metres
        return this_price > compared_price


