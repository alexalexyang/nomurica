import sqlite3
import psycopg2
# connection = sqlite3.connect("food_crud.sql")


connection = psycopg2.connect("dbname='db_food_crud' "
                              "user='alex' "
                              "host='localhost' "
                              "password='password'")

connection.autocommit = True

c = connection.cursor()

# c.execute("DROP TABLE IF EXISTS movies")
# print("Database dropped")


# Create the Postgres table.
create_table_food = """CREATE TABLE food (
    id SERIAL PRIMARY KEY,
    artists TEXT,
    project_name TEXT,
    production_countries TEXT,
    overview TEXT,
    start_date DATE,
    end_date DATE,
    medium TEXT,
    videos TEXT,
    images TEXT,
    website TEXT,
    facebook TEXT,
    twitter TEXT,
    other_social_media TEXT
    );"""


# # Create the SQLite3 table.
# create_table_food = """CREATE TABLE food (
#     id INTEGER PRIMARY KEY,
#     artists TEXT,
#     project_name TEXT,
#     production_countries TEXT,
#     overview TEXT,
#     start_date DATE,
#     end_date DATE,
#     medium TEXT,
#     videos TEXT,
#     images TEXT,
#     website TEXT,
#     facebook TEXT,
#     twitter TEXT,
#     other_social_media TEXT,
#     );"""

c.execute(create_table_food)

connection.commit()
connection.close()