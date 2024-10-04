from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)
zone = "US/Eastern"

@app.route('/')
def hello_world():
    return 'Hello worldddd'

@app.route('/time')
def get_current_time():
    return datetime.now(timezone(zone)).strftime('%Y-%m-%d %H:%M:%S')

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
