from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__) #create the Flask app

when = "global"
day = "global"
data = "global"

def top10spots(time):
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
        cur.execute("SELECT * from top10spots(%s);", (time,))

        # display the PostgreSQL database server version
        db_version = cur.fetchall()
        coords = []
        print(len(db_version))
        for i in range(len(db_version)):
            coordz = db_version[i][4].split("POINT (", 2)[1].split(" ")
            lat = coordz[0]
            long = coordz[1].split(")")[0]
            latlong = [lat, long]
            coords.append(latlong)
        return coords
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def daytimespots(time, day):
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
        cur.execute("SELECT * from daytimespots(%s, %s);", (time, day))

        # display the PostgreSQL database server version
        db_version = cur.fetchall()
        coords = []
        print(len(db_version))
        for i in range(len(db_version)):
            coordz = db_version[i][4].split("POINT (", 2)[1].split(" ")
            lat = coordz[0]
            long = coordz[1].split(")")[0]
            latlong = [lat, long]
            coords.append(latlong)
        return coords
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def closest10spots():
    """ Connect to the PostgreSQL database server """
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
        cur.execute("SELECT * from closespots();")

        # display the PostgreSQL database server version
        db_version = cur.fetchall()
        coords = []
        print(len(db_version))
        for i in range(len(db_version)):
            coordz = db_version[i][4].split("POINT (", 2)[1].split(" ")
            lat = coordz[0]
            long = coordz[1].split(")")[0]
            latlong = [lat, long]
            coords.append(latlong)
        return coords
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@app.route("/", methods=['GET', 'POST']) #allow both GET and POST requests
def home():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        if request.form['button'] == "Show Best Spots":
            when = request.form.get('when')
            day = request.form.get('day')
            coords = daytimespots(when, day)
            return render_template("Map.html", lat1=coords[0][0], long1=coords[0][1],
                               lat2=coords[1][0], long2=coords[1][1], lat3=coords[2][0], long3=coords[2][1],
                               lat4=coords[3][0], long4=coords[3][1], lat5=coords[4][0], long5=coords[4][1],
                               lat6=coords[5][0], long6=coords[5][1], lat7=coords[6][0], long7=coords[6][1],
                               lat8=coords[7][0], long8=coords[7][1], lat9=coords[8][0], long9=coords[8][1],
                               lat10=coords[9][0], long10=coords[9][1])
        elif request.form['button'] == "Show Closest Spots":
            coords = closest10spots()
            return render_template("Map.html", lat1=coords[0][0], long1=coords[0][1],
                                   lat2=coords[1][0], long2=coords[1][1], lat3=coords[2][0], long3=coords[2][1],
                                   lat4=coords[3][0], long4=coords[3][1], lat5=coords[4][0], long5=coords[4][1],
                                   lat6=coords[5][0], long6=coords[5][1], lat7=coords[6][0], long7=coords[6][1],
                                   lat8=coords[7][0], long8=coords[7][1], lat9=coords[8][0], long9=coords[8][1],
                                   lat10=coords[9][0], long10=coords[9][1])
    return render_template("BlankMap.html")

if __name__ == "__main__":
    app.run(debug=True)

#http://127.0.0.1:5000/
