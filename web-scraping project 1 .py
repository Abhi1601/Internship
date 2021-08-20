#!/usr/bin/env python
# coding: utf-8
# Q1. Write a python proogram to display all the header tags from 'en.wikipedia.org/wiki/Main_page'.
# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs= BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1','h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')

Q2. write a python program to display IMDB's Top rated 100 movies data(i.e. Name, IMDB rating, year of release).
# In[3]:


import pandas as pd
import numpy as np
import requests


# In[4]:


url = "https://www.imdb.com/list/ls091520106/"
page2 = requests.get(url)

#see page content
soup2 = BeautifulSoup(page2.content)

# top Movies name
name = soup2.find_all("h3", class_="lister-item-header")
# get text from movie name web elements
movies_name = [] #empty list
for i in name:
    for j in i.find_all("a"):
        movies_name.append(j.text)


# Year of release
year = soup2.find_all("span",class_="lister-item-year text-muted unbold")
year_of_release = [] #empty list
for k in year:
    a=k.text.replace('(','')
    year_of_release.append(a.replace(')','')) 


      
# IMDB Rating
rating = soup2.find_all("div",class_="ipl-rating-star small")

# scrape text from rating web element
IMDB_rating = [] #empty list
for i in rating:
      IMDB_rating.append(float(i.text))
# Make data frame of top 100 movies on IMDB
IMDB_top_100=pd.DataFrame({})
IMDB_top_100['movies_name']=movies_name
IMDB_top_100['year_of_release']=year_of_release
IMDB_top_100['IMDB_rating']=IMDB_rating  
IMDB_top_100

Q3. write a python program to display IMDB's Top rated 100 indian movies data (i.e Name, IMDB rating, Year of release).
# In[5]:


from bs4 import BeautifulSoup
import requests


# In[6]:


url = 'https://www.imdb.com/india/top-rated-indian-movies/'
page3 = requests.get(url)

# check the page content
soup3 = BeautifulSoup(page3.content)

# top Movies name
name = soup3.find_all("h3", class_="lister-item-header")
# get text from movie name web elements
movies_name = [] #empty list
for i in name:
    for j in i.find_all("a"):
        movies_name.append(j.text)


# Year of release
year = soup3.find_all("span",class_="lister-item-year text-muted unbold")
year_of_release = [] #empty list

for k in year:
    a=k.text.replace('(','')
    year_of_release.append(a.replace(')','')) 
    

# IMDB Rating
rating = soup3.find_all("div",class_="ipl-rating-star small")

# scrape text from rating web element
IMDB_rating = [] #empty list
for i in rating:
      IMDB_rating.append(float(i.text))
# Make data frame of top 100 India imdb movies
indian_top_100=pd.DataFrame({})
indian_top_100['movies_name']=movies_name
indian_top_100['year_of_release']=year_of_release
indian_top_100['IMDB_rating']=IMDB_rating
indian_top_100

Q4. write a python program to scrap book name, author name, genre and book review of any five books from 'www.bookpahe.com'
# In[7]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[8]:


#sending get request to the webpage server to get the source code of the page


# In[9]:


page4 = requests.get('https://bookpage.com/reviews/')
soup4 = BeautifulSoup(page4.content, 'html.parser')
url_tags = soup4.find_all("h4",class_="italic") # Extract books URL
urls = []
for i in url_tags:
    for j in i.find_all("a", href=True):
        if j.text:
            urls.append(j['href'])
book_name = [] #empty list
author_name = [] #empty list
book_genre = [] #empty list
books_review = [] #empty list

for url in urls:
        book = requests.get('https://www.bookpage.com'+url)
        soup = BeautifulSoup(book.content, 'html.parser')
        book_name.append(soup.find('h1').text.replace('\n','').replace('★',''))  # scrape books name
        author_name.append(soup.find('h4').text.replace('\n',''))  # scrape books author name
        book_genre.append(soup.find('p', class_="genre-links").text.replace('\n',''))   # scrape books genre
        books_review.append(soup.find('div', class_= "article-body").text.replace('\n',''))  # scrape books review
        

# Make data frame 
books=pd.DataFrame({})
books["Book Name"]=book_name[:5]
books["Author"]=author_name[:5]
books["Genre"]=book_genre[:5]
books["Review"]=books_review[:5]
books

Q5. Write a python program to scrap cricket ranking from www.icc-cricket.com, you have to scrap
1. Top 10 ODI teams in men's cricket along with the records for matches, points and rating.
2. Top 10 ODI Batsmen in men along with the records of their team and rating.
3. Top 10 ODI bowlers along with the records of their teams and rating.

# In[10]:


# Top 10 ODI teams in men's cricket along with the records for matches, points and rating.


# In[11]:


url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
page5 = requests.get(url)
# see content in page5
soup5 = BeautifulSoup(page5.content)
#scrape team names
team = soup5.find_all("span",class_='u-hide-phablet')
team_name = []
for i in team:
    team_name.append(i.text)
matches = [] #empty list
points = [] #empty list
ratings = [] #empty list
new_list = [] #empty list

for i in soup5.find_all("td",class_='rankings-block__banner--matches'): # first place team number of matches
    matches.append(i.text)
for i in soup5.find_all("td",class_='rankings-block__banner--points'):# first place team points
    points.append(i.text)
for i in soup5.find_all("td",class_='rankings-block__banner--rating u-text-right'):# first place team ratings
    ratings.append(i.text.replace("\n",""))
for i in soup5.find_all("td",class_='table-body__cell u-center-text'):# other teams number of matches and points
    new_list.append(i.text)
for i in range(0,len(new_list)-1,2):
    matches.append(new_list[i]) # other teams matches
    points.append(new_list[i+1]) # other teams points
for i in soup5.find_all("td",class_='table-body__cell u-text-right rating'):# other teams ratings
    ratings.append(i.text)
    
# Make data frame of top 10 ICC teams
icc=pd.DataFrame({})
icc['Team_name']=team_name[:10]
icc['Matches']=matches[:10]
icc['Points']=points[:10]
icc['Ratings']=ratings[:10]
icc


# In[12]:


#Top 10 ODI Batsmen in men along with the records of their team and rating.


# In[13]:


url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
page6 = requests.get(url)
# see content in page6
soup6 = BeautifulSoup(page6.content)
players = [] #empty list
team_name = [] #empty list
rating = [] #empty list

for i in soup6.find_all("div",class_='rankings-block__banner--name-large'): # first place player name
    players.append(i.text)
for i in soup6.find_all("div",class_='rankings-block__banner--nationality'): # first place player team name
    team_name.append(i.text.replace("\n",""))
for i in soup6.find_all("div",class_='rankings-block__banner--rating'): # first place player rating
    rating.append(i.text)
for i in soup6.find_all("td",class_='table-body__cell rankings-table__name name'):# players name
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup6.find_all("span",class_='table-body__logo-text'): # players team name
    team_name.append(i.text)
for i in soup6.find_all("td",class_='table-body__cell rating'): # players rating
    rating.append(i.text)
# Make data frame of top 10 ICC Batsmen
Batsmen=pd.DataFrame({})
Batsmen['Player']=players[:10]
Batsmen['Team']=team_name[:10]
Batsmen['Rating']=rating[:10]
Batsmen


# In[14]:


# Top 10 ODI bowlers along with the records of their teams and rating.


# In[15]:


url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
page7 = requests.get(url)

# see content in page7
soup7 = BeautifulSoup(page7.content)

players = [] #empty list
team_name = [] #empty list  
rating = [] #empty list 

for i in soup7.find_all("div",class_='rankings-block__banner--name-large'): # first place player name
    players.append(i.text)
for i in soup7.find_all("div",class_='rankings-block__banner--nationality'): # first place player team name
    team_name.append(i.text.replace("\n",""))
for i in soup7.find_all("div",class_='rankings-block__banner--rating'): # first place player rating
    rating.append(i.text)
for i in soup7.find_all("td",class_='table-body__cell rankings-table__name name'):# players name
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup7.find_all("span",class_='table-body__logo-text'): # players team name
    team_name.append(i.text)
for i in soup7.find_all("td",class_='table-body__cell rating'): # players rating
    rating.append(i.text)
# Make data frame of top 10 ICC bowlers
bowlers=pd.DataFrame({})
bowlers['Player']=players[:10]
bowlers['Team']=team_name[:10]
bowlers['Rating']=rating[:10]
bowlers

Q6. Write a python program to scrap cricket ranking from WWW.icc-crocket.com 
1. Top 10 ODI teams in womens's cricket along with the records for matches, points and rating
2. Top 10 women's ODI player along with their records of their team nad rating.
3. Top 10 women's ODI all-rounder along with the records of their team and rating.
# In[16]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
print(page) # to show the response output
soup=BeautifulSoup(page.content)

# top 10 women odi team
women_odi_team=soup.find_all("span", class_="u-hide-phablet")
top_10_women_odi_teams=[]
for i in women_odi_team[:10]:
    top_10_women_odi_teams.append(i.text)

# top 10 women odi matches
women_odi_matches=soup.find_all("td", class_="rankings-block__banner--matches")
top_10_women_odi_matches=[]
for i in women_odi_matches:
    top_10_women_odi_matches.append(i.text)

# top 10 women odi scores
women_odi_matches1=soup.find_all("td", class_="table-body__cell u-center-text")
matches_and_scores=[]
for i in women_odi_matches1:
    matches_and_scores.append(i.text)
for i in range(0, len(matches_and_scores), 2):
    top_10_women_odi_matches.append(matches_and_scores[i])
women_odi_points=soup.find_all("td", class_="rankings-block__banner--points")
top_10_women_odi_points=[]
for i in women_odi_points:
    top_10_women_odi_points.append(i.text)
for i in range(1, len(matches_and_scores), 2):
    top_10_women_odi_points.append(matches_and_scores[i])

# top 10 women odi ratings
women_odi_ratings=soup.find_all("td", class_="rankings-block__banner--rating u-text-right")
top_10_women_odi_ratings=[]
for i in women_odi_ratings:
    top_10_women_odi_ratings.append(i.text.replace("\n","").strip())
women_odi_ratings1=soup.find_all("td", class_="table-body__cell u-text-right rating")
for i in women_odi_ratings1:
    top_10_women_odi_ratings.append(i.text.replace("\n","").strip())

# checking the length of the columns
print(f"Length of Women's ODI team, matches, points and ratings are:", len(top_10_women_odi_teams), 
      len(top_10_women_odi_matches), len(top_10_women_odi_points), len(top_10_women_odi_ratings))

# creating the dataframe
df_to_10_women_odi_teams=pd.DataFrame({})
df_to_10_women_odi_teams["Top 10 Women's ODI Team Names"]=top_10_women_odi_teams
df_to_10_women_odi_teams["Top 10 Women's ODI Team Matches"]=top_10_women_odi_matches
df_to_10_women_odi_teams["Top 10 Women's ODI Team Points"]=top_10_women_odi_points
df_to_10_women_odi_teams["Top 10 Women's ODI Team Ratings"]=top_10_women_odi_ratings
df_to_10_women_odi_teams

Top 10 women's ODI players along with the records of their teams and rating
# In[17]:


page2=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
print(page2) 
soup2=BeautifulSoup(page2.content)

women_odi_bat_name=soup2.find_all("div", class_="rankings-block__banner--name")
top_10_women_odi_bat_name=[]
for i in women_odi_bat_name[0:1]:
    top_10_women_odi_bat_name.append(i.text)
women_odi_bat_name1=soup2.find_all("td", class_="table-body__cell name")
for i in women_odi_bat_name1[0:9]:
    top_10_women_odi_bat_name.append(i.text.replace("\n",""))

women_odi_bat_team=soup2.find_all("div", class_="rankings-block__banner--nationality")
top_10_women_odi_bat_team=[]
for i in women_odi_bat_team[0:1]:
    top_10_women_odi_bat_team.append(i.text.replace("\n",""))
top_10_women_odi_bat_team = list(map(lambda x: x.split(' ')[0], top_10_women_odi_bat_team))
 
women_odi_bat_team1=soup2.find_all("span", class_="table-body__logo-text")
for i in women_odi_bat_team1[:9]:
    top_10_women_odi_bat_team.append(i.text.replace("\n",""))

women_odi_bat_rating=soup2.find_all("div", class_="rankings-block__banner--rating")
top_10_women_odi_bat_rating=[]
for i in women_odi_bat_rating[0:1]:
    top_10_women_odi_bat_rating.append(i.text)
women_odi_bat_rating1=soup2.find_all("td", class_="table-body__cell u-text-right rating")
for i in women_odi_bat_rating1[:9]:
    top_10_women_odi_bat_rating.append(i.text)

print(f"Length of Top 10 Women ODI Batting players, team and ratings are:", len(top_10_women_odi_bat_name), 
      len(top_10_women_odi_bat_team), len(top_10_women_odi_bat_rating))

df_batswomen=pd.DataFrame({})
df_batswomen["Top 10 Women's ODI Batswomen Names"]=top_10_women_odi_bat_name
df_batswomen["Top 10 Women's ODI Batswomen Teams"]=top_10_women_odi_bat_team
df_batswomen["Top 10 Women's ODI Batswomen Ratings"]=top_10_women_odi_bat_rating
df_batswomen

Top 10 women’s ODI all-rounder along with the records of their team and rating.
# In[18]:


women_odi_bowler_name=soup2.find_all("div", class_="rankings-block__banner--name")
top_10_women_odi_bowler_name=[]
for i in women_odi_bowler_name[1:2]:
    top_10_women_odi_bowler_name.append(i.text)
women_odi_bowler_name1=soup2.find_all("td", class_="table-body__cell name")
for i in women_odi_bowler_name1[9:18]:
    top_10_women_odi_bowler_name.append(i.text.replace("\n",""))
    
women_odi_bowler_team=soup2.find_all("div", class_="rankings-block__banner--nationality")
top_10_women_odi_bowler_teams=[]
for i in women_odi_bowler_team[1:2]:
    top_10_women_odi_bowler_teams.append(i.text.replace("\n",""))
top_10_women_odi_bowler_teams = list(map(lambda x: x.split(' ')[0], top_10_women_odi_bowler_teams))
 
women_odi_bowler_team1=soup2.find_all("span", class_="table-body__logo-text")
for i in women_odi_bowler_team1[9:18]:
    top_10_women_odi_bowler_teams.append(i.text.replace("\n",""))

women_odi_bowler_rating=soup2.find_all("div", class_="rankings-block__banner--rating")
top_10_women_odi_bowler_ratings=[]
for i in women_odi_bowler_rating[1:2]:
    top_10_women_odi_bowler_ratings.append(i.text)
women_odi_bowler_rating1=soup2.find_all("td", class_="table-body__cell u-text-right rating")
for i in women_odi_bowler_rating1[9:18]:
    top_10_women_odi_bowler_ratings.append(i.text)
    
print(f"Length of Top 10 Women ODI Bowling players, team and ratings are:", len(top_10_women_odi_bowler_name), 
      len(top_10_women_odi_bowler_teams), len(top_10_women_odi_bowler_ratings))

df_women_bowlers=pd.DataFrame({})
df_women_bowlers["Top 10 Women's ODI Bowler Names"]=top_10_women_odi_bowler_name
df_women_bowlers["Top 10 Women's ODI Bowler Teams"]=top_10_women_odi_bowler_teams
df_women_bowlers["Top 10 Women's ODI Bowler Ratings"]=top_10_women_odi_bowler_ratings
df_women_bowlers

Q7. Write a python program to scrape details of all the mobiles under RS 20000 listed on amazon in. the scraped data should include product name, price, image URL and average rating
# In[19]:



page=requests.get("https://www.amazon.in/s?k=mobiles+under+20000&rh=n%3A1389401031&ref=nb_sb_noss")
print(page)
soup=BeautifulSoup(page.content)

mob_name=soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
product_names=[]
for i in mob_name[:10]:
    product_names.append(i.text)

mob_price=soup.find_all("span", class_="a-price-whole")
product_price=[]
for i in mob_price[:10]:
    product_price.append(i.text)

images=soup.find_all("div", class_="a-section aok-relative s-image-fixed-height")
images_url=[]
for i in images[:10]:
    for j in i.find_all("img", class_="s-image"):
        images_url.append(j.get("src"))


avg_rating=soup.find_all("i", class_="a-icon a-icon-star-small a-star-small-4 aok-align-bottom")
ratings=[]
for i in avg_rating[:10]:
    ratings.append(i.text)


print(f"Length of product name, price, image url and ratings", len(product_names), 
      len(product_price), len(images_url), len(ratings))


df=pd.DataFrame({})
df["Product Names"]=product_names
df["Product Prices"]=product_price
df["Image Urls"]=images_url
df["Average Rating"]=ratings
df

Q8. Write a python program to extract information about the local weather from national weather services websites of USA https://www.weather.gov/ for the city, San Francisco. You need to extract data about 7 day extended forecast display for the city. The data should include period, short description, temperature and description
# In[20]:


page=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YR9KQnzitPY")
print(page)
soup=BeautifulSoup(page.content)

period=soup.find_all("p", class_="period-name")
period_names=[]
for i in period:
    period_names.append(i.text)
    
short_desc=soup.find_all("p", class_="short-desc")
short_detail=[]
for i in short_desc:
    short_detail.append(i.text)
    
temp1=soup.find_all("p", class_="temp temp-low")
temp2=soup.find_all("p", class_="temp temp-high")
temperature=[]
for i in temp1:
    temperature.append(i.text)
for i in temp2:
    temperature.append(i.text)
    
long_desc=soup.find_all("div", class_="col-sm-10 forecast-text")
description=[]
for i in long_desc[:9]:
    description.append(i.text)

print(f"Length of period, short description, temperature and long description are:", len(period_names), 
      len(short_detail), len(temperature), len(description))

df=pd.DataFrame({})
df['Period Names']=period_names
df['Short Detail']=short_detail
df['Temperature']=temperature
df['Description']=description
df

Q9. Write a python program to scrape fresher job listings from ‘https://internshala.com/’. It should include job title, company name, CTC, and apply date.
# In[22]:


page=requests.get("https://internshala.com/fresher-jobs")
print(page)
soup=BeautifulSoup(page.content)

job_title=soup.find_all("div", class_="heading_4_5 profile")
title=[]
for i in job_title:
    title.append(i.text.replace("\n","").strip())

company_names=soup.find_all("div", class_="heading_6 company_name")
company=[]
for i in company_names:
    company.append(i.text.replace("\n","").strip())

CTC_list=soup.find_all("div", class_="item_body")
CTC=[]
for i in CTC_list:
    for j in i.find_all("i"):
        CTC.append(i.text.replace("\n","").strip())

applying=soup.find_all("div", class_="item_body")
apply_date=[]
for i in applying:
    apply_date.append(i.text)
dates=[]
for i in range(2, len(apply_date), 3):
    dates.append(apply_date[i])

print(f"Lengths of Job title, Company name, CTC and Apply date are:", len(title), len(company), len(CTC), len(dates))

df=pd.DataFrame({})
df['Job Title']=title
df['Company Name']=company
df['CTC']=CTC
df['Apply Date']=dates
df

Q10. Write a python program to scrape house details from https://www.nobroker.in/ for any location. It should include house title, location, area, emi and price
# In[23]:


page=requests.get("https://www.nobroker.in/property/sale/pune/Pune?searchParam=W3sibGF0IjoxOC41NTc3NDQ2LCJsb24iOjczLjkxMjQ2NzQsInBsYWNlSWQiOiJDaElKaVNGeWVzWEF3anNScmN5RkZzUHlzTkUiLCJwbGFjZU5hbWUiOiJQdW5lIn1d&radius=2.0")
print(page) # to check the response output
soup=BeautifulSoup(page.content)

house_title=soup.find_all("h2", class_="heading-6 font-semi-bold nb__1AShY")
htitle=[]
for i in house_title:
    for j in i.find_all("span"):
        htitle.append(i.text)

loc=soup.find_all("div", class_="nb__2CMjv")
location=[]
for i in loc:
    location.append(i.text)

builtup=soup.find_all("div", class_="nb__3oNyC")
area=[]
for i in builtup:
    area.append(i.text)

estimated_emi=soup.find_all("div", class_="font-semi-bold heading-6")
EMI=[]
for i in estimated_emi:
    EMI.append(i.text)
emi_detail=[]
for i in range(1, len(EMI), 3):
    emi_detail.append(EMI[i])
emi_detail

price=[]
for i in range(2, len(EMI), 3):
    price.append(EMI[i])

print(f"Lengths of house title, location, area, emi and price:", len(htitle), len(location), len(area), 
      len(emi_detail), len(price))

df=pd.DataFrame({})
df["House Title"]=htitle
df["House Location"]=location
df["Area of the house"]=area
df["EMI Details"]=emi_detail
df["Price of the house"]=price
df


# In[ ]:




