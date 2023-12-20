from create_database import create_database

def create_collection():
    try:
        #create collection/table
        cd = create_database()
        collection = cd['MyFirstCollection']
        print("collection created...")
        return collection
    except:
        print("collection not created!!!")