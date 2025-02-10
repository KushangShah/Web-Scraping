# Mon 10 Feb, 2025 [11:44am]
# Web Scraping trending github repositorys

# import library
from bs4 import BeautifulSoup 
import requests
import csv              # for save data in .csv formate

# url
url = "https://github.com/trending/python?since=daily"

# selecting an agent so github don't block us.
headers = {
    "User-Agent": "Mozilla/5.0"
    }

# featch url request
response = requests.get(url, headers = headers)
print(response)

# get html element from the web
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

# selecting the element from the web
repository = soup.find_all('article', class_='Box-row')
# print(repository)

# create an empty list for storing data
data = []

# loop through repository and get repo name, owner name and repo link
for repo in repository:
    repo_name = repo.h2.a.text.strip().replace('\n', '').replace(' ', '')
    # print(repo_name)
    owner, name = repo_name.split('/')              # separating repo name and owner name from repo_name
    # print(owner, name)
    repo_link = "https://github.com/" + repo_name
    # print(repo_link)
    
    # add this in data
    data.append([owner, name, repo_link])
    
# print(data)     # Data is quite a mess

# lets save the data into .csv formate
csv_filename = "Trending_repo.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['repo. Owner', "repo. Name", "repo. URL"])
    writer.writerows(data)              # This will save the file
    