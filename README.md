# Data Modeling with Postgres
## Introduction

<p>A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.</p>

<p>They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. I created a database schema and ETL pipeline for this analysis. I tested database and ETL pipeline by running queries given by the analytics team from Sparkify and compared results with their expected results.</p>

## Project Description
<p>In this project, I built an ETL pipeline using Python. I defined fact and dimension tables for a star schema for a particular analytic focus, and wrote an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.</p>


## Song Dataset
<p>The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. Here are file paths to two files in this dataset.</p>

song_data/A/B/C/TRABCEI128F424C983.json<br>
song_data/A/A/B/TRAABJL12903CDCF1A.json<br>

<p>And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.<br>
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}</p>

## Log Dataset

<p>The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.
The log files in the dataset are partitioned by year and month. Here are filepaths to two files in this dataset.</p>

log_data/2018/11/2018-11-12-events.json<br>
log_data/2018/11/2018-11-13-events.json<br>

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.
 
<p>To look at the JSON data within log_data files, I created a pandas dataframe to read the data. Remember to first import JSON and pandas libraries.
 
df = pd.read_json(filepath, lines=True)
 
## Schema for Song Play Analysis
 
Using the song and log datasets, I created a star schema optimized for queries on song play analysis. This includes the following tables.
 
## Fact Table
1.	songplays - records in log data associated with song plays i.e. records with page NextSong<br>
•	songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent<br>
## Dimension Tables
2.	users - users in the app<br>
•	user_id, first_name, last_name, gender, level<br>
3.	songs - songs in music database<br>
•	song_id, title, artist_id, year, duration<br>
4.	artists - artists in music database<br>
•	artist_id, name, location, latitude, longitude<br>
5.	time - timestamps of records in songplays broken down into specific units<br>
•	start_time, hour, day, week, month, year, weekday<br>
 
 
The project includes six files:<br>
1.	test.ipynb displays the first few rows of each table to lets you check the database.<br>
2.	create_tables.py drops and creates  tables. <br>
3.	etl.ipynb reads and processes a single file from song_data and log_data and loads the data into tables. This notebook contains detailed instructions on the ETL process for each of the tables.<br>
4.	etl.py reads and processes files from song_data and log_data and loads them into tables.<br>
5.	sql_queries.py contains all sql queries, and is imported into the last three files above.<br>
6.	README.md provides discussion on the project.<br>

### Project Steps
### Create Tables
1.	Write CREATE statements in sql_queries.py to create each table.<br>
2.	Write DROP statements in sql_queries.py to drop each table if it exists.<br>
3.	Run create_tables.py to create database and tables.<br>
4.	Run test.ipynb to confirm the creation of tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.<br>
 
### Build ETL Processes
<p>At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table.</p>
<p>Run test.ipynb to confirm your records were successfully inserted into each table.</p>

### Run Sanity Tests
<p>The cells contain some basic tests that will evaluate the work and catch any silly mistakes. We test column data types, primary key constraints and not-null constraints as well look for on-conflict clauses wherever required. If any of the test cases catches a problem, we will see a warning message printed in Orange that looks like this:
[WARNING] The songplays table does not have a primary key! </p>


