# Import dependecies to run website and to interact with sql database
from re import M
from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

#  Create engine and automap the Base 
engine = create_engine('sqlite:///Resources/hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

# Declare tables as classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Define context manager to open and close sessions
class Session_call():
    def __init__(self, engine):
        self.engine = engine
        self.session = Session(self.engine)
    def __enter__(self):
        return self.session
    
    def __exit__(self, type, value, traceback):
        self.session.close()

# Create function to turn list of lists into dict
def dlist_2_ldict(dlist, keys):
    ldict = []
    for list in dlist:
        dict = {}
        for key, item in zip(keys, list):
            dict[key] = item
        ldict.append(dict)
    return ldict

# Initiate app
app = Flask(__name__)

# Define routes: index and the five different api calls
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/v1.0/precipitation')
def precipitaion_call():
    with Session_call(engine) as s:
        q = s.query(Measurement.date, Measurement.prcp).filter(Measurement.date>='2016-08-23').order_by(Measurement.date).all()
        return jsonify(dict(q))

@app.route('/api/v1.0/stations')
def stations_call():
    with Session_call(engine) as s:
        q = s.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation, func.count(Measurement.date)).filter(Station.station==Measurement.station).group_by(Measurement.station).all()
    keys = ['station', 'name', 'latitude', 'longitude', 'elevation', 'number of observations']
    return jsonify(dlist_2_ldict(q, keys))

@app.route('/api/v1.0/tobs/<station>')
def tobs_call(station):
    if station == 'all':
        with Session_call(engine) as s:
            q = s.query(Measurement.date, Measurement.tobs, Measurement.station).all()
    else:
        with Session_call(engine) as s:
            q = s.query(Measurement.date, Measurement.tobs, Measurement.station).filter(Station.station==station).all()
    k = ['date','temp observation', 'station']
    return jsonify(dlist_2_ldict(q,k))

@app.route('/api/v1.0/<start>')
def later_than_date_call(start):
    with Session_call(engine) as s:
        q = s.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date>=start).all()
    k = ['min temp', 'max temp', 'average temp']
    return jsonify(dlist_2_ldict(q, k))

@app.route('/api/v1.0/<start>/<end>')
def between_date_Call(start, end):
    with Session_call(engine) as s:
        q = s.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    k = ['min temp', 'max temp', 'average temp']
    return jsonify(dlist_2_ldict(q, k))

if __name__=='__main__':
    app.run(debug=True)