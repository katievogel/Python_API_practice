import requests
from pprint import pprint
import base64
from github import Github
import csv
import secrets
import psycopg2

# write to db
def insert_stargazer(login, name):
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO katie_github.stargazers (login, name) VALUES (%s, %s)", 
                (login, name))

def insert_all_stargazers(stargazers):
    for star in stargazers[21:30]:
        insert_stargazer(star.login, star.name)


db_config = {
    'database' : 'katie_github', 
    'user' : 'katievogel', 
    'host' : '::1', 
    'port' : '5432'
}

def main():
    # set up github connection with auth token
    g = Github(secrets.GITHUB_TOKEN)

    # get repos of user & check request data
    repo = g.get_repo('hyperfiddle/electric')
    stargazers = repo.get_stargazers()
    insert_all_stargazers(stargazers)

if __name__ == "__main__": 
    main()

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




