import psycopg2

def insert_data(value):
    try:
       connection = psycopg2.connect(user = "myuser",
                                     password = "new_password",
                                     host = "localhost",
                                     port = "5432",
                                     database = "testdb")
       cursor = connection.cursor()

       postgres_insert_query = """ INSERT INTO search_history (searches) VALUES (%s)"""
       #print(value)
       record_to_insert = (value,)
       #print('step1')

       cursor.execute(postgres_insert_query, record_to_insert)
       connection.commit()
       #count = cursor.rowcount
       #print (count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()


def delete_data_table_all():
    try:
       connection = psycopg2.connect(user = "myuser",
                                     password = "new_password",
                                     host = "localhost",
                                     port = "5432",
                                     database = "testdb")
       cursor = connection.cursor()
       #print('step1')

       cursor.execute("""TRUNCATE search_history """)
       connection.commit()
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
def select():
    try:
        connection = psycopg2.connect(user = "myuser",
                                      password = "new_password",
                                      host = "localhost",
                                      port = "5432",
                                      database = "testdb")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")
        # Print PostgreSQL version
        postgreSQL_select_Query = "select * from search_history"

        cursor.execute(postgreSQL_select_Query)
        #print("Selecting rows from search_history table using cursor.fetchall")
        search_records = cursor.fetchall()

        #print("Print each row and it's columns values")
        return(search_records)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()

#delete_data_table_all()
