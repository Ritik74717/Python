class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getstatus(self):
        print(f"Train name = {self.name}")
        print(f"Seats Available = {self.seats}")

    def getfair(self):
        print(f" Fair = RS.{self.fare}")

    def book(self):
        if(self.seats):
            print(f"Your ticket has been booked Your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Seats are full")

Intercity = Train("Intercity",300,90)
Intercity.getstatus()
Intercity.getfair()
Intercity.book()

Intercity.getstatus()

        
