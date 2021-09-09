seats = []
for i in range(1, 101):
    seats.append(i)
class Tickets():
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

    def bookTickets(self):
        a = seats.pop()
        print(f"your seat is booked and seat no. is {a}")

    def cancelTickets(self, seatNum):
        self.seatNum = seatNum
        if seatNum in seats:
            print("Invalid action")
        else:
            seats.append(seatNum)
            print(f"Your ticket with seat No.{seatNum} has been canceled")
            
    def fareInfo(self):
        print(f"The price of ticket is {self.fare}")

    def getInfo(self):
        b = len(seats)
        if b > 0:
            print(f"Seats available in train are {b}")
        else:
            print("No seats are available") 

memo = Tickets("memo", 35)
memo.bookTickets()
memo.cancelTickets(100)
memo.cancelTickets(97)
memo.bookTickets()
memo.fareInfo()
memo.getInfo()
