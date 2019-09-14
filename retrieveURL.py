import os
import sqlite3
from shutil import copy
import json
import threading


data_path = "C:\\History"
history_db = os.path.join(data_path, 'History')
prev = []


def refresh_query():
	# path to user's history database (Chrome)
	copy(os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History", "C:\History")

	# querying the db
	c = sqlite3.connect(history_db)
	cursor = c.cursor()
	select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
	cursor.execute(select_statement)
	results = cursor.fetchall()

	return results[-20:]

def filter(prev:list , curr: list):
	return list(set(curr)-set(prev))

def start():
	threading.Timer(10.0, start).start()
	f = open('C:\\History\\history.json', 'w')

	try:
		data = refresh_query()
		f.write(json.dumps(filter(prev,data)))
		prev = data
		print("Written to file successfully")
		f.close()
	except:
		print("Something went wrong!")
		f.close()

start()














