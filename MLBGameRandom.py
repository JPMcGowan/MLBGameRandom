import random
import webbrowser
import time
import xlrd

#loc = ("C:\Users\jm50016\Downloads\MLBRandomGame.py")
#wb = xlrd.open_workbook(loc)
#sheet = wb.sheet_by_index(0)

#Random team
teamArray = ("Diamondbacks", "Braves", "Orioles", "Red Sox", "Cubs", "White Sox", "Reds", "Guardians", "Rockies", "Tigers", 
             "Astros", "Royals", "Angels", "Dodgers", "Marlins", "Brewers", "Twins", "Mets", "Yankees", "A's",
             "Phillies", "Pirates", "Padres", "Giants", "Mariners", "Rays", "Rangers", "Blue Jays", "Nationals")
             
teamArrayAbbrev = ("ARI", "ATL", "BAL", "BOS", "CHN", "CHA", "CIN", "CLE", "COL", "DET", 
                   "HOU", "KCR", "LAA", "LAN", "MIA", "MIL", "MIN", "NYN", "NYA", "OAK",
                   "PHI", "PIT", "SDN", "SFN", "SEA", "TBA", "TEX", "TOR", "WSH")
             
teamNum = random.randint(1,30) - 1
team = teamArray[teamNum]
teamAbbrev = teamArrayAbbrev[teamNum]

#Random month
monthArray = ("March", "April", "May", "June", "July", "August", "September")
monthNum = random.randint(3, 9) - 3
month = monthArray[monthNum]
monthNum = monthNum + 3

#Random day
if monthNum == 3 or 5 or 7 or 8:
    day = random.randint(1, 31)
if monthNum == 4 or 6 or 9:
    day = random.randint(1, 30)

#Random year
year = random.randint(2009, 2019)

#Making sure random game can exist
if year == 2009 or 2010 or 2015 or 2016 or 2017:
    if monthNum == 3:
        month = "April"
if year == 2009 or 2015:
    if monthNum == 4:
        if day < 5:
            day = random.randint(5, 30)
if year == 2010:
    if monthNum == 4:
        if day < 4:
            day = random.randint(4, 30)
if year == 2011 or 2013:
    if monthNum == 3:
        day = 31
if year == 2012 or 2019:
    if monthNum == 3:
        day = random.randint(28, 31)
if year == 2014:
    if monthNum == 3:
        day = random.randint(22, 31)
if year == 2016:
    if monthNum == 4:
        day = random.randint(3, 30)
if year == 2017:
    if monthNum == 4:
        day = random.randint(2, 30)
if year == 2018:
    if monthNum == 3:
        day = random.randint(29, 31)

print("TEAM: %s" % (team))
print("DAY: %s %s, %s" % (month, day, year))

gameURL = "https://www.youtube.com/results?search_query=%s+%s+%s+%s" % (teamAbbrev, month, day, year)
time.sleep(3)
webbrowser.open(gameURL)
