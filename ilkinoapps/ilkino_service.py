from ilkinoapps.seat import Seat, SpecialSeat
from ilkinoapps.printer import Printer
from ilkinoapps.ticket import Ticket, SpecialTicket
from datetime import datetime
import random


class IlkinoService:
    def __init__(self, gift_list):
        self.left_gift_list = gift_list
        self.right_gift_list = gift_list[:]  # menggunakan slicing untuk mengcopy list
        self.seats = [None] * 36

    def setup(self):
        left_special_seat_number = random.sample(range(0, 35, 2), 5)
        right_special_seat_number = random.sample(range(1, 35, 2), 5)
        for number in range(36):
            if number in left_special_seat_number:
                seat = SpecialSeat(number + 1)
                seat.set_gift(self.left_gift_list.pop())
            elif number in right_special_seat_number:
                seat = SpecialSeat(number + 1)
                seat.set_gift(self.right_gift_list.pop())
            else:
                seat = Seat(number + 1)
            self.seats[number] = seat
        self.ticket_printer = Printer()

    def book(self, seat_number, name):
        seats_number = seat_number.split(",")
        seats_number = list(map(int, seats_number))

        # check exist
        for number in seats_number:
            if not 1 <= number <= 36:
                return -1

        # check availability
        for number in seats_number:
            if self.seats[number - 1].is_booked == True:
                return -2  # Not available

        # if seat(s) exist and available
        is_special_seat = False
        time = datetime.now()
        hour = int(time.strftime("%H"))
        for number in seats_number:
            current_seat = self.seats[number - 1]  # access seat with current number
            current_seat.set_to_booked(name, hour)
            if isinstance(current_seat, SpecialSeat):
                is_special_seat = True
        if is_special_seat:
            unprinted_ticket = SpecialTicket(name, seat_number)
        else:
            unprinted_ticket = Ticket(name, seat_number)
        self.ticket_printer.print_ticket(unprinted_ticket)
        return 0

    def find(self, name):
        booked_numbers = []  # Menggunakan list karena number bisa lebih dari satu
        for num in range(36):
            if self.seats[num].is_booked:
                booked_numbers.append(num)
        numbers = []
        for number in booked_numbers:
            if self.seats[number].book_name == name:
                numbers.append(str(number + 1))
        return numbers

    def get_booked_by_hour(self, hour):
        booked_seats_number = []
        for num in range(36):
            if self.seats[num].is_booked:
                if self.seats[num].get_time() == hour:
                    booked_seats_number.append(num + 1)
        return booked_seats_number

    def get_all_distributed_gifts(self):
        distributed_special_seats = []
        for num in range(36):
            if self.seats[num].is_booked == True and isinstance(self.seats[num], SpecialSeat):
                distributed_special_seats.append((str(num + 1), self.seats[num].gift))
        return distributed_special_seats

    def report(self):
        hourly_booking = {}
        for hour in range(24):
            book = self.get_booked_by_hour(hour)
            if len(book) > 0:
                hourly_booking[hour] = len(book)
        distributed_special_seats = self.get_all_distributed_gifts()
        return hourly_booking, distributed_special_seats
