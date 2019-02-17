from flask import Flask, request

app = Flask(__name__) #create the Flask app

when = "global"
data = "global"

@app.route("/", methods=['GET', 'POST']) #allow both GET and POST requests
def home():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        when = request.form.get('when')

        if when > 5:
            data = "avaliable"

        return '''
                  <h1>Estimated parking time: {}</h1>
                  <h1>Parking spaces are: {}</h1>'''.format(when, data)

    return '''<form method="POST">
                  Hello!<br>
                  When: <input type="text" name="when"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == "__main__":
    app.run(debug=True)

#http://127.0.0.1:5000/
