from ilkinoapps.ilkino_service import *
from datetime import datetime
import os  # untuk delete file karena ini hanya test


def test_book_unbooked_seat():
    gifts = ['apel', 'jeruk', 'nanas', 'pisang', 'anggur']
    service = IlkinoService(gifts)
    service.setup()
    seat_number = "1"
    name = 'Bryan'
    booked_seat = service.seats[0] # 0 karena python mulai dari 0

    assert booked_seat.is_booked == False
    service.book(seat_number, name)
    assert booked_seat.is_booked == True

    os.remove("Bryan_1.txt")


def test_book_unknown_seat():
    gifts = ['apel', 'jeruk', 'nanas', 'pisang', 'anggur']
    service = IlkinoService(gifts)
    service.setup()
    seat_number = "100"
    name = 'Bryan'
    status = service.book(seat_number, name)
    assert status == -1


def test_book_booked_seat():
    gifts = ['apel', 'jeruk', 'nanas', 'pisang', 'anggur']
    service = IlkinoService(gifts)
    service.setup()
    seat_number = "10"
    name = 'Bryan'
    service.book(seat_number, name)
    status = service.book(seat_number, name)
    assert status == -2


def test_book_seat_with_gift():
    gifts = ['apel', 'jeruk', 'nanas', 'pisang', 'anggur', 'stroberi']
    service = IlkinoService(gifts)
    service.setup()
    seat_number = 10
    index = seat_number - 1  # karena python mulai dari 0
    name = 'Bryan'
    seat = SpecialSeat(seat_number)
    seat.set_gift(gifts[0])
    service.seats[index] = seat
    status = service.book(str(seat_number), name)
    assert status == 0
    assert service.seats[index].gift == "apel"

    os.remove("Bryan_10.txt")


def test_get_booked_by_hour():
    gifts = ['apel', 'jeruk', 'nanas', 'pisang', 'anggur']
    service = IlkinoService(gifts)
    service.setup()
    seat_number = "10,12,13"
    name = 'Bryan'
    service.book(seat_number, name)
    hour = int(datetime.now().strftime("%H"))
    book = service.get_booked_by_hour(hour)

    expected = [10, 12, 13]
    assert book == expected

    os.remove("Bryan_10_12_13.txt")


def test_get_all_distributed_gifts():
    gifts = ['jeruk', 'nanas', 'pisang', 'anggur', 'stroberi']
    service = IlkinoService(gifts)
    service.setup()
    seat_number_1, seat_number_2 = 10, 15
    index_1, index_2 = seat_number_1 - 1, seat_number_2 - 1  # karena python mulai dari 0
    new_gift = ['apel', 'melon']
    seat_1, seat_2 = SpecialSeat(seat_number_1), SpecialSeat(seat_number_2)
    seat_1.set_gift(new_gift[0]);
    seat_2.set_gift(new_gift[1])
    service.seats[index_1] = seat_1;
    service.seats[index_2] = seat_2
    service.book("10,15", "Bryan")
    distributed_gift = service.get_all_distributed_gifts()

    expected_1 = '10', 'apel'
    expected_2 = '15', 'melon'
    assert distributed_gift[0] == expected_1
    assert distributed_gift[1] == expected_2

    os.remove("Bryan_10_15.txt")


def test_serch_booked_name():
    gifts = ['apel', 'jeruk', 'nanas', 'pisang', 'anggur']
    service = IlkinoService(gifts)
    service.setup()
    seat_number = "1,6,10"
    name = 'Bryan'
    service.book(seat_number, name)  # string karena dari input

    booked = service.find("Bryan")
    expected = ["1", "6", "10"]
    assert booked == expected

    os.remove("Bryan_1_6_10.txt")


def test_search_unbooked_name():
    gifts = ['apel', 'jeruk', 'nanas', 'pisang', 'anggur']
    service = IlkinoService(gifts)
    service.setup()
    seat_number = "1,6,10"
    name = 'Bryan'
    service.book(seat_number, name)  # string karena dari input

    booked = service.find("Ryan")
    expected = []
    assert booked == expected

    os.remove("Bryan_1_6_10.txt")


def test_gift_randomly_assigned_left():
    gifts = ['jeruk', 'nanas', 'pisang', 'anggur', 'stroberi']
    service = IlkinoService(gifts)
    service.setup()
    left_special_seat_1 = []
    for i in range(0, 35, 2):
        if isinstance(service.seats[i], SpecialSeat):
            left_special_seat_1.append(i)

    gifts = ['jeruk', 'nanas', 'pisang', 'anggur', 'stroberi']
    service = IlkinoService(gifts)
    service.setup()
    left_special_seat_2 = []
    for i in range(0, 35, 2):
        if isinstance(service.seats[i], SpecialSeat):
            left_special_seat_2.append(i)

    assert left_special_seat_1 != left_special_seat_2


def test_gift_randomly_assigned_right():
    gifts = ['jeruk', 'nanas', 'pisang', 'anggur', 'stroberi']
    service = IlkinoService(gifts)
    service.setup()
    right_special_seat_1 = []
    for i in range(1, 35, 2):
        if isinstance(service.seats[i], SpecialSeat):
            right_special_seat_1.append(i)

    gifts = ['jeruk', 'nanas', 'pisang', 'anggur', 'stroberi']
    service = IlkinoService(gifts)
    service.setup()
    right_special_seat_2 = []
    for i in range(1, 35, 2):
        if isinstance(service.seats[i], SpecialSeat):
            right_special_seat_2.append(i)

    assert right_special_seat_1 != right_special_seat_2


def test_five_gift_assigned_right():
    gifts = ['jeruk', 'nanas', 'pisang', 'anggur', 'stroberi']
    service = IlkinoService(gifts)
    service.setup()
    right_special_seat_1 = []
    for i in range(1, 35, 2):
        if isinstance(service.seats[i], SpecialSeat):
            right_special_seat_1.append(i)

    assert len(right_special_seat_1) == 5


def test_ticket_is_printed():
    gifts = ['apel', 'jeruk', 'nanas', 'pisang', 'anggur']
    service = IlkinoService(gifts)
    service.setup()
    seat_number = "10,12,13"
    name = 'Bryan'

    assert os.path.isfile("Bryan_10_12_13.txt") == False
    service.book(seat_number, name)
    assert os.path.isfile("Bryan_10_12_13.txt") == True

    os.remove("Bryan_10_12_13.txt")
