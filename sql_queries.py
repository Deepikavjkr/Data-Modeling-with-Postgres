# DROP TABLES

songplay_table_drop = "DROP table  IF EXISTS songplays"
user_table_drop = "DROP table  IF EXISTS users"
song_table_drop = "DROP table  IF EXISTS songs"
artist_table_drop = "DROP table  IF EXISTS artists"
time_table_drop = "DROP table  IF EXISTS time"

# CREATE TABLES


songplay_table_create = ("""create table if not exists 
    songplays
    (
        songplay_id SERIAL NOT NULL PRIMARY KEY,
        start_time varchar NOT NULL, 
        user_id int NOT NULL ,
        song_id varchar ,
        artist_id varchar,
        level varchar,
        session_id int NOT NULL,
        location varchar,
        user_agent varchar 
    )
""")


user_table_create = ("""create table if not exists 
    users
    (
        user_id int NOT NULL PRIMARY KEY, 
        first_name varchar, 
        last_name varchar, 
        gender varchar,
        level varchar
    )
""")

song_table_create = ("""create table if not exists 
    songs
    (
        song_id varchar NOT NULL PRIMARY KEY,
        title varchar,
        artist_id varchar NOT NULL, 
        year int,
        duration float
    )
""")


artist_table_create = ("""create table if not exists 
    artists
    (
        artist_id varchar NOT NULL PRIMARY KEY, 
        name varchar, 
        location varchar, 
        latitude float, 
        longitude float
    )
""")

time_table_create = ("""create table if not exists 
    time
    (
        start_time varchar PRIMARY KEY, 
        hour int, 
        day int,
        week int, 
        month int, 
        year int,
        weekday int
    )
""")
# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO 
    songplays
    (
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING
""")

user_table_insert = ("""INSERT INTO 
    users
    (
        user_id,
        first_name,
        last_name,
        gender,
        level
    )
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (user_id)
    DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
                     INSERT INTO songs (
                         song_id,
                         title,
                         artist_id,
                         year,
                         duration)
                      VALUES (%s, %s, %s, %s, %s)
                      ON CONFLICT (song_id) DO NOTHING;
                      """)


artist_table_insert = ("""
    INSERT INTO 
    artists
    (
        artist_id, 
        name, 
        location, 
        latitude, 
        longitude
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO 
    time
    (
        start_time,
        hour,
        day,
        week,
        month,
        year,
        weekday
    )
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id FROM songs as s
    LEFT JOIN artists as a 
    ON a.artist_id = s.artist_id
    WHERE title = %s and duration=%s and name = %s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]