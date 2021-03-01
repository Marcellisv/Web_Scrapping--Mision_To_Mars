#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import Pandas , Beautiful soup, Mongodb ad Splinter

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


executable_path = {'executable_path': '/Users/marcellisv/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# ## Mars News Articles Headlines

# In[4]:



article_url = 'https://mars.nasa.gov/news/'
browser.visit(article_url)


# In[5]:


#create Buetiful soup 
article_html = browser.html
article_soup = bs(article_html, 'html' )
print(article_soup)


# In[6]:


# Retrieve the most recent article's title and paragraph.
article_list=article_soup.find("ul", class_="item_list")
article_item=article_list.find("li", class_="slide")
article_headline = article_item.find("div", class_="content_title").text
article_body = article_item.find("div", class_="article_teaser_body").text
print(article_headline)
print(article_body)


# ## JPL Mars Space Images - Featured Image
# 

# In[7]:


jpl_url = "https://www.jpl.nasa.gov/images?search=&category=Mars"
browser.visit(jpl_url)


# In[8]:


#create Buetiful soup 
img_html = browser.html
img_soup = bs(img_html, 'html')


# In[9]:



mars_img = img_soup.find_all('img')[3]["src"]
featured_image_url = 'https://www.jpl.nasa.gov' + mars_img
print(featured_image_url)


# ## Mars Facts

# In[10]:


facts_url = 'https://space-facts.com/mars/'
browser.visit = (facts_url)


# In[11]:


#Convert Table to HTML using pandas 
facts_table = pd.read_html(facts_url)
facts_table


# In[12]:


mars_facts_df = facts_table[0]

mars_facts_df.columns = ["Description", "Value"]

mars_facts_df


# In[13]:


html_table = mars_facts_df.to_html()
mars_facts_df.to_html("mars_facts_data.html")


# ## Mars Hemispheres

# In[25]:


executable_path = {'executable_path': '/Users/marcellisv/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[26]:


usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(usgs_url)


# In[27]:


#create Buetiful soup 
usgs_html = browser.html
hemi_soup = bs(usgs_html, 'html')


# In[28]:


hemi_items = hemi_soup.find_all('div', class_='item')

hemi_list = []

hemi_main_url = 'https://astrogeology.usgs.gov'

for item in hemi_items:
    #retrieve hemisphere names 
    hemi_title = item.find('h3').text
    #retireve thumbnail url
    hemi_thumb = item.find('a')['href']
    hemi_link = hemi_main_url + hemi_thumb
    browser.visit(hemi_link)
    img_html = browser.html
    img_soup = bs(img_html, 'html.parser')
    hemi_download = img_soup.find("div", class_="downloads")
    hemi_img = hemi_download.find("a")["href"]
    hemi_list.append({"Hemisphere Name" : hemi_title,
                      "img_url" : hemi_img})
    
hemi_list


# ## First Combine all data into one dictionary
# 

# In[58]:


combined_mars_dict= {}


# In[66]:


combined_mars_dict["article_headline"] = article_headline
combined_mars_dict["article_body"] = article_body
combined_mars_dict["featured_image_url"] = featured_image_url
combined_mars_dict["mars_facts_df"] = mars_facts_df
combined_mars_dict["hemi_list"]= hemi_list


# In[67]:


combined_mars_dict

