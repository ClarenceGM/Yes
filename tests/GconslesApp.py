import sqlite3 as sl
from flask import Flask, request, render_template

app = Flask(__name__)


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


@app.route('/')
def index():
    return render_template('GameConsole.html', game_consoles=None, output="")


@app.route('/lookup')
def lookup():
    conn = sl.connect('GConsoles.db')

    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Game
                        (Name TEXT, Brand TEXT, Year INTEGER, Sold INTEGER)''')

    GameConsole = [
        Game('NES', 'Nintendo', 1983, 69000000),
        Game('SNES', 'Nintendo', 1990, 49000000),
        Game('Nintendo 64', 'Nintendo', 1996, 32000000),
        Game('GameCube', 'Nintendo', 2001, 21000000),
        Game('Wii', 'Nintendo', 2006, 100000000),
        Game('Wii U', 'Nintendo', 2012, 13000000),
    ]

    with conn:
        for console in GameConsole:
            conn.execute('''INSERT INTO Game
                            (Name, Brand, Year, Sold)
                            VALUES (?,?,?,?)''',
                         (console.getName(), console.getBrand(), console.getYear(), console.getSold()))

    game_name = request.args.get('lookup_name')

    if game_name:
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT Name, Brand, Year FROM Game WHERE Name = ?", (game_name,))
            GameConsole = cur.fetchall()
    else:
        GameConsole = []

    return render_template('GameConsole.html', game_consoles=GameConsole)


if __name__ == '__main__':
    app.run()
