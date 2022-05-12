class IlkinoGui:
    def __init__(self, service):
        self.service = service

    def run(self):
        while True:
            choice = self.menu_utama()
            if choice == 1:
                self.option1()
            elif choice == 2:
                self.option2()
            elif choice == 3:
                self.option3()
            elif choice == 4:
                print("4. Exit")
                break
            else:
                print("Option not available")

    def menu_utama(self):
        seats = self.service.seats
        print("\n")
        print("+" + "-" * 34 + "+")
        print("|" + "IL Kino".center(34) + "|")
        print("|" + "Nansenstrasse 22,".center(34) + "|")
        print("|" + "12047 Berlin".center(34) + "|")
        print("+" + "-" * 34 + "+")
        print()
        print("+" + "-" * 34 + "+")
        print("|", "SCREEN".center(32), "|")
        print("+" + "-" * 34 + "+")
        print()
        print("+----+----+----+    +----+----+----+")
        for row in range(6):
            print(f"|{str(seats[row * 6]).center(4)}|{str(seats[row * 6 + 2]).center(4)}|{str(seats[row * 6 + 4]).center(4)}|    |{str(seats[row * 6 + 1]).center(4)}|{str(seats[row * 6 + 3]).center(4)}|{str(seats[row * 6 + 5]).center(4)}|")
            print("+----+----+----+    +----+----+----+")
        print()
        print("1. Seat Booking")
        print("2. Find by name")
        print("3. Report")
        print("4. Exit")

        try:
            choice = int(input("Enter your choise 1-4?: "))
        except:
            return  -1
        if choice in [1, 2, 3, 4]:
            return choice
        else:
            return -1

#=================================================================================================================================================================================================================

    def option1(self):
        print("1. Seat Booking")
        seat_number = input("Enter Seat number: ")
        name = input("Enter name: ")
        is_success = self.seat_booking(seat_number, name)
        while not is_success:  # looping sampai menemukan kursi yang belum dibooking
            is_success = self.book_other_seat(name) # memberi argumen nama karena yang memesan lagi adalah orang yang sama

    def seat_booking(self, seat_number, name):
        is_booked = self.service.book(seat_number, name)
        if is_booked == -1:
            print(f"Seat number {seat_number.replace(',', ' or ')} does not exist")
            return False
        elif is_booked == -2:
            print(f"Seat number {seat_number.replace(',', ' or ')} already booked")
            return False
        else:
            print(f"Seat {seat_number} is booked by {name}")
            print(f"Receipt {name}_{seat_number.replace(',', '_')}.txt is printed. Don't loose your ticket.")
            return True # Aman

    def book_other_seat(self, name):
        loop = True
        while loop:
            check = input("Select another seat? [y/n]: ").lower()
            if check not in ("y", "n"):
                print("Pilihan tidak tersedia")
            else:
                loop = False
        if check == "n":
            return True
        else:
            seat_number = input("Enter Seat number: ")
            is_success = self.seat_booking(seat_number, name)
            return is_success

#=================================================================================================================================================================================================================

    def option2(self):
        print("2. Find by Name")
        name = input("Name: ")
        numbers = self.service.find(name)
        if numbers == []:
            print("Name not found")
        else:
            print(f"{name} booked seat number {','.join(numbers)}")

#=================================================================================================================================================================================================================

    def option3(self):
        hourly_booking, special_seat_numbers = self.service.report()
        print("+" + "-" * 34 + "+")
        print("|", "Hour".ljust(12), "Number of booking".ljust(19), "|")
        for hour in hourly_booking:
            print("|", f"{hour}:00".ljust(12), str(hourly_booking[hour]).center(19), "|")
        print("|" + " " * 34 + "|")
        print("|", "All distributed SeatNumber-GIft:".ljust(32), "|")
        for number, gift in special_seat_numbers:
            print(f"| {number} - {gift}".ljust(34), "|")
        print("+" + "-" * 34 + "+")
