# from insert_many import insert_many
# from insert_one import insert_one

# user_work = input("enter what you do(insert_one/insert_many): ")
# while True:
#     if user_work == 'insert_one':
#         insert_one()
#     else:
#         insert_many()

#     exit = input("do you want to exit?(yes/no): ")
#     if exit == 'yes':
#         break

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

all_databases = client.list_database_names()
print(f'List of all databases: {all_databases}')
for dbs in all_databases[0:2]:
    db = client[dbs]
    print(f'Database name: {dbs}')
    all_collections = db.list_collection_names()
    print(f'List of all collections in {dbs} database: {all_collections}')
    for i in all_collections:
        collection = db[i]
        print(f'Collection name: {i}')
        docs = collection.find()
        for j in docs:
            print(f'This doc from {i} collection in {dbs} database:\n', j)