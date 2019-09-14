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

# Filters out all URLs that are not from reddit, and already noted URls

def filter(c_list):
	temp = []
	for url in c_list:
		if "reddit" in url[0]:
			print(url[0])
			temp.add(url[0])

	return temp
	#return list(set(c_list)-set(p_list))

def start():
	threading.Timer(10.0, start).start()
	f = open('C:\\History\\history.json', 'w')

	try:
		data = refresh_query()
		f.write(json.dumps(filter(data)))

		print("Written to file successfully")
		f.close()
	except:
		print("Something went wrong!")
		f.close()

start()














