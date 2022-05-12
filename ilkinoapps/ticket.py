class Ticket:
    def __init__(self, name, seat_number):
        self.name = name
        self.seat_number = seat_number

    def get_name(self):
        return self.name

    def get_seat_number(self):
        return self.seat_number

class SpecialTicket(Ticket):
    def __init__(self, name, seat_number):
        super(SpecialTicket, self).__init__(name, seat_number)