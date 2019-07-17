import meraDb
db = meraDb.load("shivi.db")
print db.setData("name","shivani")
print db.getData("name")