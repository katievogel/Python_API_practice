import requests
from pprint import pprint
import base64
from github import Github
import csv
import secrets
import psycopg2

# create connection to db
# conn = psycopg2.connect(database = 'katie_github', user = 'katievogel', host = '::1', port = '5432')
db_config = {
    'database' : 'katie_github', 
    'user' : 'katievogel', 
   ' host' : '::1', 
    'port' : '5432'
}

# query to insert vals to db
SQL = "INSERT INTO katie_github.stargazers (login, name) VALUES (%s, %s)"

# set up github connection with auth token
g = Github(secrets.GITHUB_TOKEN)

# get user
username = 'hyperfiddle'
user = g.get_user(username)

# get repos of user & check request data
repo = g.get_repo('hyperfiddle/electric')

# get name and login and write to db
stargazers = repo.get_stargazers()

def insert_stargazer(login, name):
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cur:
            # star = stargazers[2]
            cur.execute(SQL, (login, name))

def insert_all_stargazers():
    for star in stargazers[:10]:
        insert_stargazer(star.login, star.name)

# get star user name, login from stargazers on repo for csv
# stargazers = repo.get_stargazers()
# def get_stars_info():
#     records = []
#     for star in stargazers:
#         record = {
#             'name': star.name,
#             'login': star.login
#         } 
#         records.append(record)
#     return records


# write star counts to csv
# create fieldnames for header
# writer.writeheader
# create records dict to write to csv
# writer.writerows
# with open('./repo_stars.csv', 'w') as file:
#     fieldnames = ['name', 'login']
#     writer = csv.DictWriter(file, fieldnames)
#     writer.writeheader()
#     records = get_stars_info()
#     writer.writerows(records)




