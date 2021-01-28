from sqlalchemy import create_engine
import pymysql
import pandas as pd
#import Client
pymysql.install_as_MySQLdb()


def collectInfo(id, name):
    db[list(clientDB_df.columns)[0]].append(id)
    db[list(clientDB_df.columns)[1]].append(name)
    return db

def writeToDB(dbDict):
    writeQuery = pd.DataFrame(data=dbDict)
    writeQuery.to_sql(name = 'clientDB', con = connection, if_exists = 'append', index = False)


def nameInput():
    return input('Please, enter client name: ')

def idInput():
    return int(input('Please, enter client id: '))


if __name__ == '__main__':

    status = input("Hello! Hit 'Return' to proceed. To display the table enter r. To exit: enter 'e'.")
    if status != 'e':
        connection = create_engine("mysql+mysqldb://root:turpitka@localhost/Clients")
        if status == 'r':
            clientDB_df = pd.read_sql_table('clientDB', connection)
            print(clientDB_df)
        else:
            clientDB_df = pd.read_sql_table('clientDB', connection)
            db = {i: [] for i in list(clientDB_df.columns)}
            write_count = 0

    while status != 'e' and status != 'r':
        writeToDB(collectInfo(idInput(), nameInput()))
        write_count += 1
        status = input("Hit 'Return' to make another entry. To exit: enter 'e'.")
        print("Session Details:\nwrites: " + str(write_count))
