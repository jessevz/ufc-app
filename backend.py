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
    # print(rows)
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
    print(event_json)
    return jsonify(event_json)

if __name__ == '__main__':
    app.run(debug=True)

