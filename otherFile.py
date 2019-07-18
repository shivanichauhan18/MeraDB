import meraDb
db = meraDb.load('ektha.db')
db.setData('key1', 'value1')
db.getData('key1')
db.setData('key2', 'value2')
db.getData('key2')