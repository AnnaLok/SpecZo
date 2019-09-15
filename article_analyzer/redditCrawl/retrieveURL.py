import os
import sqlite3
from shutil import copy
import json
import threading
from article_analyzer.redditCrawl.redditCrawl import getInstance, filter_domain

data_path = os.getcwd() + "\\history_db"
history_db = os.path.join(data_path, 'History')


def refresh_query():
    # path to user's history database (Chrome)
    copy(os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History", data_path)

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
            instance = getInstance(url[0])
            if instance is not None and filter_domain(instance.domain):
                temp.append(instance.url)

    return unique(temp)


def start():
    #threading.Timer(10.0, start).start()
    f = open(data_path + '\\history.json', 'w+')

    data = refresh_query()
    print(filter_r(data))
    f.write(json.dumps(filter_r(data)))
    print("Written to file successfully")
    f.close()

def retrieve_url():
    try:
        os.mkdir('history_db')
        print("created folder")
    except FileExistsError:
        print("file already exists")

    start()
