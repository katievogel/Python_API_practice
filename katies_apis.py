import requests
from pprint import pprint
import base64
from github import Github
import csv
import secrets
import psycopg2

# create connection to db
conn = psycopg2.connect(database = 'postgres', user = 'katievogel', host = '::1', port = '5432')

# set up github connection with auth token
g = Github(secrets.GITHUB_TOKEN)

# get user
username = 'hyperfiddle'
user = g.get_user(username)

# get repos of user & check request data
repo = g.get_repo('hyperfiddle/electric')

# get star user name, login from stargazers on repo
stargazers = repo.get_stargazers()
def get_stars_info():
    records = []
    for star in stargazers:
        record = {
            'name': star.name,
            'login': star.login
        } 
        records.append(record)
    return records


# write star counts to csv
# create fieldnames for header
# writer.writeheader
# create records dict to write to csv
# writer.writerows
with open('./repo_stars.csv', 'w') as file:
    fieldnames = ['name', 'login']
    writer = csv.DictWriter(file, fieldnames)
    writer.writeheader()
    records = get_stars_info()
    writer.writerows(records)



