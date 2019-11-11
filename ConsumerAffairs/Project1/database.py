######################################################################
##              checking database functionality                     ##
##          `   By chanukya Lakamsani  and Alan Lee                 ##`
##          ``                                                      ##
######################################################################

import psycopg2

def select()
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
        finally:
            if(connection):
                cursor.close()
                connection.close()
