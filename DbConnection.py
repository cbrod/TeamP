#!/usr/bin/python
import psycopg2
import json
#from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    localhost = "findmyspot.cmpdtcyalbuc.us-west-2.rds.amazonaws.com"
    dbname = "TeamP"
    username = "TeamP"
    userpsw = "teampteamp"
    
    try:
        # read connection parameters
        #params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=localhost,database=dbname, user=username, password=userpsw)
 
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('Top 20 spots near Capitol Hill: ')
        cur.execute("SELECT row_to_json(top20spots(17)) FROM top20spots(17);")
 
        # display the PostgreSQL database server version
        db_version = cur.fetchall()
        print(json.dumps(db_version))
       
        cur.close()
        
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()