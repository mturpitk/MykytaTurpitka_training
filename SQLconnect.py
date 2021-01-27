from sqlalchemy import create_engine
import pymysql
import pandas as pd
import Client
pymysql.install_as_MySQLdb()


def collectInfo(id, name) -> Client:
    db[list(clientDB_df.columns)[0]].append(id)
    db[list(clientDB_df.columns)[1]].append(name)
    return db

def writeToDB(dbDict):
    writeQuery = pd.DataFrame(data=dbDict)
    writeQuery.to_sql(name = 'clientDB',con = connection, if_exists = 'append', index = False)


if __name__ == '__main__':

    connection = create_engine("mysql+mysqldb://root:turpitka@localhost/Clients")

    #tableName = input("Please, enter the name of the table: ")
    clientDB_df = pd.read_sql_table('clientDB', connection)

    db = {i: [] for i in list(clientDB_df.columns)}

    writeToDB(collectInfo(int(input("Please, enter client id: ")), input('Please, enter client name: ')))
