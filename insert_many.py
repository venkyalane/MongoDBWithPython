from create_collection import create_collection

def insert_many():
    try:
        # insert many record/documents in collection
        cc = create_collection()
        insertThis = [
            {'name':'Savita', 'location':'Mumbai', 'marks': 75},
            {'name':'Amit', 'location':'Delhi', 'marks': 80},
            {'name':'Sumit', 'location':'Hydrabad', 'marks': 90},
            {'name':'Pawan', 'location':'Surat', 'marks': 95},
        ]
        cc.insert_many(insertThis)
        print("documents inserted...")
    except:
        print("documents not inserted...")