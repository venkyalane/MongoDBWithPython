from insert_many import insert_many
from insert_one import insert_one

user_work = input("enter what you do(insert_one/insert_many): ")
while True:
    if user_work == 'insert_one':
        insert_one()
    else:
        insert_many()

    exit = input("do you want to exit?(yes/no): ")
    if exit == 'yes':
        break
