from flask import Flask, request, render_template
import psycopg2
import json

app = Flask(__name__) #create the Flask app

when = "global"
data = "global"

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
        print('Top 10 spots near Capitol Hill: ')
        cur.execute("SELECT row_to_json(top10spots(17));")

        # display the PostgreSQL database server version
        db_version = cur.fetchone()[0]
        coordz = db_version['geotag'].split("POINT (", 2)[1].split(" ")
        lat = coordz[0]
        long = coordz[1].split(")")[0]
        coords = [lat, long]
        # return render_template("index.html", name=top20)
        return coords
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



@app.route("/", methods=['GET', 'POST']) #allow both GET and POST requests
def home():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        when = request.form.get('when')

        data = "avaliable"

        coords = connect()

        return render_template("Map.html", lat=coords[0], long=coords[1])

        ''''''''''
                  <h1>Estimated parking time: {}</h1>
                  <h1>Parking spaces are: {}</h1>.format(when, coords)'''

    return '''<form method="POST">
                  Hello!<br>
                  When: <input type="text" name="when"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == "__main__":
    app.run(debug=True)

#http://127.0.0.1:5000/
