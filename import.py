#!/usr/bin/python3
import sqlite3
import csv

conn = sqlite3.connect('recipes.db')
c = conn.cursor()

# Recreate table
c.execute('DROP TABLE IF EXISTS recipes;')
c.execute('CREATE TABLE recipes (id integer primary key autoincrement, name text, ingredients text, memo text)')

# Load data from csv and insert into database
with open('output.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvReader:
        c.execute('INSERT INTO recipes VALUES (null,?,?,?)', (row[0], row[1], row[2]))

conn.commit()
conn.close()
