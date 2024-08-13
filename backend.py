from flask import Flask, jsonify
from database import SimpleSQLiteDB
from event import Event, Fight
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify(message="The UFC event API")

@app.route('/events')
def get_events():
    db = SimpleSQLiteDB()
    rows = db.retrieve_events()
    events = [Event(*row).to_json() for row in rows]
    return jsonify(events)

@app.route('/past_events')
def get_past_events():
    db = SimpleSQLiteDB()
    rows = db.retrieve_past_events()
    events = [Event(*row).to_json() for row in rows]
    return jsonify(events)

@app.route('/upcoming_events')
def get_upcoming_events():
    db = SimpleSQLiteDB()
    rows = db.retrieve_upcoming_events()
    events = [Event(*row).to_json() for row in rows]
    return jsonify(events)

@app.route('/event/<int:event_id>')
def get_event(event_id):
    db = SimpleSQLiteDB()
    row = db.retrieve_event(event_id)
    event = Event(*row)
    rows = db.retrieve_fights(event_id)
    fights = [Fight(*row) for row in rows]
    event.fights = fights
    event_json = event.to_json()
    return jsonify(event_json)

if __name__ == '__main__':
    app.run(debug=True)

