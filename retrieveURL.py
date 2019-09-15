import os
import sqlite3
from shutil import copy
import json
import threading
import redditCrawl


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

def unique(items):
    found = set([])
    keep = []

    for item in items:
        if item not in found:
            found.add(item)
            keep.append(item)

    return keep

# Filters out all URLs that are not from reddit, and already noted URls

def filter_r(list):
	temp = []
	for url in list:
		if "reddit.com/r/" in url[0]:
			instance = redditCrawl.getInstance(url[0])
			if redditCrawl.filter_domain(instance.domain):
				temp.append(instance.url)

	return unique(temp)



def start():
	threading.Timer(10.0, start).start()
	f = open('C:\\History\\history.json', 'w')

	data = refresh_query()
	print(data)
	print(filter_r(data))
	f.write(json.dumps(filter_r(data)))
	print("Written to file successfully")
	f.close()

start()