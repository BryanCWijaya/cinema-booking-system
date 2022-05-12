class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False

    def set_to_booked(self, name, time):
        self.is_booked = True
        # book name dan book time tidak didefinisikan di init karena nilainya baru ada ketika di booking
        self.book_name = name
        self.book_time = time

    def get_time(self):
        return self.book_time

    def __str__(self):
        if self.is_booked == False:
            return str(self.seat_number)
        else:
            return "X"


class SpecialSeat(Seat):
    def __init__(self, seat_number):
        super(SpecialSeat, self).__init__(seat_number)
        self.gift = None

    def set_gift(self, gift):
        self.gift = gift

    def __str__(self): # method overriding
        if self.is_booked == False:
            return str(self.seat_number)
        else:
            return "G"
