class Game:
    def __init__(self, Name, Brand, Year,Sold):
        self.Name = Name
        self.Brand = Brand
        self.Year = Year
        self.Sold = Sold

    def getName(self):
        return self.Name
    def getBrand(self):
        return self.Brand
    def getYear(self):
        return self.Year
    def getSold(self):
        return self.Sold