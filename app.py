from flask import Flask, render_template
import psycopg2
import json

app = Flask(__name__)

''@app.route('/')
def connect():
    ''""" Connect to the PostgreSQL database server """
    localhost = "findmyspot.cmpdtcyalbuc.us-west-2.rds.amazonaws.com"
    dbname = "TeamP"
    username = "TeamP"
    userpsw = "teampteamp"

    try:
        # read connection parameters
        # params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=localhost, database=dbname, user=username, password=userpsw)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('Top 20 spots near Capitol Hill: ')
        cur.execute("SELECT row_to_json(top10spots(17));")

        # display the PostgreSQL database server version
        db_version = cur.fetchone()[0]
        coordz = db_version['geotag'].split("POINT (", 2)[1].split(" ")
        lat = coordz[0]
        long = coordz[1].split(")")[0]
        #return render_template("index.html", name=top20)
        return render_template("Map.html", lat=lat, long=long)
        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    app.run()