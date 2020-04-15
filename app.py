import pandas as pd
import datetime 
from datetime import timedelta
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask
from flask import render_template 
from flask import jsonify

#Establish engine
engine = create_engine("sqlite:///Resources/forest_fire.sqlite")
#Establish connection
conn = engine.connect()

#data example
pd.set_option('display.max_columns', None)
df_2015 = pd.read_sql("SELECT * FROM Fires WHERE FIRE_YEAR = 2015", conn)
df_2015['datetime'] = pd.to_datetime(df_2015['DISCOVERY_DATE'])
df_2015['cont_datetime'] = pd.to_datetime(df_2015['CONT_DATE'])

fire_data = {
    "ID" : df_2015['OBJECTID'],
    "fire_name" : df_2015['FIRE_NAME'],
    "year" : df_2015['FIRE_YEAR'],
    "disc_timestamp" : df_2015['DISCOVERY_DATE'],
    "disc_datetime" : df_2015['datetime'],
    "cause" : df_2015['STAT_CAUSE_DESCR'],
    "cont_timestamp" : df_2015['CONT_DATE'],
    "cont_datetime" : df_2015['cont_datetime'],
    "fire_size" : df_2015['FIRE_SIZE'],
    "fire_class" : df_2015['FIRE_SIZE_CLASS'],
    "latitude" : df_2015['LATITUDE'],
    "longitude" : df_2015['LONGITUDE'],
    "state" : df_2015['STATE']
}


app = Flask(__name__)

@app.route("/")
def IndexRoute():
    return render_template("index.html")
    

@app.route("/other")
def OtherRoute():

    webpage = render_template("other.html", title_we_want="example")
    return webpage

@app.route("/fires")
def forest_fires():
    print(fire_data)

    fire_json = fire_data.to_json()
    return (fire_json)
    #fire_data is a dictionary of lists created earlier in the script
if __name__ == '__main__':
    app.run(debug=True)