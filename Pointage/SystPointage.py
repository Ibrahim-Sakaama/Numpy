import pymongo

myclient= pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#DB creation
mydb = myclient["systPointage"]
#listing DBs
print(myclient.list_database_names())

dblist = myclient.list_database_names()
# if "systPointage" in dblist:
#     print("the database exists.")
# else:
#     print("the database does not exists.")
#mycol = mydb["user"]