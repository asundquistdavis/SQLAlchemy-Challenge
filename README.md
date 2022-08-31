# SQLAlchemy-Challenge
## Overview
This challenge explores using the sqlalchemy module in python. A sample sqlite database with Hawaii weather data is taken from the [Journal of Atmospheric and Oceanic Technology](https://doi.org/10.1175/JTECH-D-11-00103.1). The database is queried in a jupyter notebook using the [sqlalchemy](https://www.sqlalchemy.org/). The data is then analyzed using [pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) and [matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html). To further explore reading databases, an api website is made which can access various queries from the database. The api is launched using the python [flask](https://flask.palletsprojects.com/en/2.2.x/) library.
## Content
- hawaii.ipynb: Queries data in SQLite database using SQLAlchemy and analyses data using Pandas and Matplotlib.
- app.py: Runs an api server through flask that queries the SQLite database using SQLAlchemy.
- templates
    - index.html: Used to render the api's landing page.
- Resources:
    - hawaii.sqlite: SQLite file that contains the database
    - hawaii_measurements.csv and hawaii_stations.csv: Not actually used in the program but helpful for figuring out what each table in the database contains.