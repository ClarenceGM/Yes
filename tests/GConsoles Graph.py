import matplotlib.pyplot as plt

# Game console data
class Game:
    def __init__(self, Name, Brand, Year, Sold):
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



game_console_data = [
    Game('NES', 'Nintendo', 1983, 69000000),
    Game('SNES', 'Nintendo', 1990, 49000000),
    Game('Nintendo 64', 'Nintendo', 1996, 32000000),
    Game('GameCube', 'Nintendo', 2001, 21000000),
    Game('Wii', 'Nintendo', 2006, 100000000),
    Game('Wii U', 'Nintendo', 2012, 13000000)
]

# Extract console names and units sold
console_names = [game.getName() for game in game_console_data]
units_sold = [game.getSold() for game in game_console_data]

# Create a bar graph
plt.bar(console_names, units_sold)
plt.xlabel('Game Console')
plt.ylabel('Units Sold')
plt.title('Units Sold for Each Game Console')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Display the graph
plt.show()
