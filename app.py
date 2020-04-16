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

# Define the database connection parameters
username = 'postgres'  # Ideally this would come from config.py (or similar)
password = 'password'  # Ideally this would come from config.py (or similar)
database_name = 'forest_fires' # Created in Week 9, Night 1, Exercise 08-Stu_CRUD 
connection_string = f'postgresql://{username}:{password}@localhost:5432/{database_name}'

#Establish engine
engine = create_engine(connection_string)
base = automap_base()
base.prepare(engine, reflect=True)

# Choose the table we wish to use
table = base.classes.fire_table
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Effectively disables page caching

# Here's where we define the various application routes ...
@app.route("/")
def IndexRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''

    webpage = render_template("index.html")
    return webpage


@app.route("/fires")
def forest_fires():
    '''Query dataase'''
    session = Session(engine)
    results = session.query(table.fire_id, table.fire_name, table.fire_size, table.STAT_CAUSE_DESCR ,table.latitude, table.longitude, table.state_code, table.disc_clean_date, table.cont_clean_date, table.Vegitation)
    session.close()
    all_fires = []
    for fire_id, fire_name, fire_size, STAT_CAUSE_DESCR, latitude, longitude, state_code, disc_clean_date, cont_clean_date, Vegitation in results:
        dict = {}
        dict['fire_id'] = fire_id
        dict['fire_name'] = fire_name
        dict['fire_size'] = fire_size
        dict['STAT_CAUSE_DESCR'] = STAT_CAUSE_DESCR
        dict['latitude'] = latitude 
        dict['longitude'] = longitude
        dict['state_code'] = state_code
        dict['disc_clean_date'] = disc_clean_date 
        dict['cont_clean_date'] = cont_clean_date
        dict['Vegitation'] = Vegitation 
        all_fires.append(dict)
    
    return jsonify(all_fires)

if __name__ == '__main__':
    app.run(debug=True)


