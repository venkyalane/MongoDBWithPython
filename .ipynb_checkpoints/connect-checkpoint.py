import pymongo

def connection():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print("connection established...")
        return client
    except:
        print("Unable to connect!!!")