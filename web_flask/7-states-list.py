#!/usr/bin/python3
# Starts flask web app to serve AirBnB content
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontent
def rem_session(exc):
    """
    Removes current SQLAlchemy Session
    """
    storage.close()

@app.route('/states_list')
def states_hbnb():
    """
    returns all states in db
    """
    return render_template('7-states_list.html', states=storage.all('State').values())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000') 
