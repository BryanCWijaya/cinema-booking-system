from ilkinoapps.ticket import *

class Printer:
    def print_ticket(self, unprinted_ticket):
        name = unprinted_ticket.get_name()
        seat_number = unprinted_ticket.get_seat_number()
        seat_number_ = seat_number.replace(",", "_")
        ticket = open(f"{name}_{seat_number_}.txt", "w+")
        ticket.write("+" + "-" * 50 + "+\n")
        ticket.write("|" + "IL Kino Receipt".center(50) + "|\n")
        ticket.write("+" + "-" * 50 + "+\n")
        ticket.write("|" + " Name         : " + name.ljust(34) + "|\n")
        ticket.write("|" + " Seats Number : " + seat_number.ljust(34) + "|\n")
        if isinstance(unprinted_ticket, SpecialTicket):
            ticket.write("|" + "Please check below your seat to get your gift.".center(50) + "|\n")
        ticket.write("|" + "Please arrive 15 minutes before.".center(50) + "|\n")
        ticket.write("+" + "-" * 50 + "+\n")
        ticket.close()