import requests
from pprint import pprint
import base64
from github import Github
import csv
import secrets
import psycopg2
import tweepy


g = None
# write to db
# it is cleaner to write a function to do one thing and call that function in another to do multiple
# also ensure consistent functionality instead of trying to redo the same function each time
def insert_stargazer(login, name, email):
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO katie_github.stargazers (login, name, email) VALUES (%s, %s, %s)", 
                (login, name, email))
            print(f"Inserting {login}, {name}, {email}")

def insert_all_stargazers(stargazers):
    for star in stargazers:
        insert_stargazer(star.login, star.name, find_user_email(star.login))

def users_first_push_event(user):
    public_events = user.get_public_events()
    for event in public_events:
        if event.type != 'PushEvent':
            continue
        else:
            return event

def push_event_to_email(event):
    try:
        return event.payload['commits'][0]['author']['email']
    except:
        return None

def find_user_email(user_instance):
    e = users_first_push_event(g.get_user(user_instance))
    if e:
        return push_event_to_email(e)

def get_stargazer_email(stargazers):
    return [find_user_email(user_instance.login) for user_instance in stargazers]
        
db_config = {
    'database' : 'katie_github', 
    'user' : 'katievogel', 
    'host' : '::1', 
    'port' : '5432'
}

def main():
    # set up github connection with auth token
    global g # dirty hack, makes the below a global variable when it's run. not typical.
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




