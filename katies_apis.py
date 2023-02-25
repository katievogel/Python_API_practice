import requests
from pprint import pprint
import base64
from github import Github
import csv
import secrets



# set up github connection with auth token
g = Github(secrets.GITHUB_TOKEN)

# get user
username = 'hyperfiddle'
user = g.get_user(username)

# get repos of user & check request data
repo = g.get_repo('hyperfiddle/electric')

# get star user name, login from stargazers on repo
stargazers = repo.get_stargazers()
for star in stargazers[:10]:
    records = {
        'name': star.name, 
        'login': star.login
    }
    print(records)


# write star counts to csv
# create fieldnames for header
# writer.writeheader
# create records dict to write to csv
# writer.writerows


# for repo in user.get_repos():
#     # print(repo)
#     print("Repo name: ", repo.full_name)
#     print("Stars: ", repo.stargazers_count)

# records = {}
# for repo in user.get_repos():
#     records = {
#         'repo_name': repo.full_name,
#         'star_count': repo.stargazers_count
#     }

# with open('./repo_stars.csv', 'w') as file:
#     fieldnames = ['repo_name', 'star_count']
#     writer = csv.DictWriter(file, fieldnames)
#     writer.writeheader()
#     writer.writerows(records)