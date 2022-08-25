import pymongo
client=pymongo.MongoClient("mongodb+srv://NimmyBibin:Bibin@cluster0.j67axfs.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)
d={"name":"nimmy","email":"nimmyjoy@gmail.com","surname":"joy"}
db1=client["mongotest"]
coll=db1["test"]
coll.insert_one(d)