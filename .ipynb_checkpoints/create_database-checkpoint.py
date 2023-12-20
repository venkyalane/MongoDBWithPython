from connect import connection

def create_database():
    try:
        con = connection()
        #create database
        db = con['FirstDB']
        print("database created")
        return db
    except:
        print("database not created!!!")
