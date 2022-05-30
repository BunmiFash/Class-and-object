class House:
    def __init__(self, type, price,location):
        self.type = type
        self.price = price
        self.location = location

    def gate_present(self,gate):
        self.gate = gate
        print ("This" ,self.type, "located at", self.location, "has", self.gate)
     
    def garden_present(self, garden):
        self.garden = garden
        return ("")

    def pool_present(self,pool):
        self.pool = pool
        return ("")

class Cottage(House):
    def __init__(self, type, price, location):
        super().__init__(type, price, location)


    def gate_present(self,gate):
        self.gate = gate
        print ("This" ,self.type, "located at", self.location, "has no", self.gate)

house1 = House("Duplex", "15 million naira", "Banana Island")
house2 = House("Flats", "10 million naira", "Ikoyi")
house3 = House("Bungalow", "8 million naira", "Lekki")
house4 = House("Boys-Quaters", "5 million naira", "Ajah")

house1.gate_present("big black gate")
house1.pool_present("large pool")
house1.garden_present("beautiful, well taken care of garden")

house2.gate_present("black gate")
house2.pool_present("a small size pool")
house2.garden_present("beautiful, well taken care of garden")

house3.gate_present("big black gate.")
house3.pool_present("no pool")
house3.garden_present("small garden")

house4.gate_present("big black gate.")
house4.pool_present("no pool")
house4.garden_present("no garden")

cot = Cottage("Medium sized, family type cottage", "1 million dollars", "Kentucky")

print(cot.gate_present("big black gate"))