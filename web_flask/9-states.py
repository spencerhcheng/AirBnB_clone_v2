#!/usr/bin/python3
# Starts a flask web app to serve AirBnB content
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def rem_session(exception):
    """Removes current SQLAlchemy Session"""
    storage.close()


@app.route('/states')
def display_states():
    """Lists all State objects present in DBStorage"""
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def display_state_by_id(id):
    """Displays State object attributes using id"""
    states = storage.all("State")
    if states is not None:
        state_id = states['id']
        return render_template('9-states.html', state_id=state_id)
    else:
        return "Not found!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
