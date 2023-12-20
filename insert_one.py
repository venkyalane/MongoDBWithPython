from create_collection import create_collection

def insert_one():
    try:
        # insert one record/document in collection
        cc = create_collection()
        dictionary = {'name':'Test', 'location':'Test', 'marks': 100}
        cc.insert_one(dictionary)
        print("document inserted...")
    except:
        print("document not inserted...")
