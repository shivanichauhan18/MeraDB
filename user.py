import meraDb
import json
db = meraDb.load("shivi.db")
print db.setData("name","shivani")
print db.setData("clg","sant-singaji")
print db.setData("village","piplda")
print db.getData("name")

file = open("shivi.db")
load_data=json.load(file)
db.getAll(load_data)
db.rem("village")
print db.existsKey("name")
db.totalKeys(load_data)
db.delDb(load_data)
db.randomInsertKeys("the quick brown fox jumps over the lazy dog")
