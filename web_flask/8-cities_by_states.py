#!/usr/bin/python3
# Starts flask web app to serve AirBnB content
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def rem_session(exception):
    """Removes current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states')
def display_html():
    """List all State objects present in DBStorage"""
    return render_template('8-cities_by_states.html',
                           states_list=storage.all('State').values())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
