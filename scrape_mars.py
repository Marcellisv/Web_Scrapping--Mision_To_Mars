#!/usr/bin/env python
# coding: utf-8

# In[162]:


#import Pandas , Beautiful soup, Mongodb ad Splinter

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager


# In[163]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[164]:


executable_path = {'executable_path': '/Users/marcellisv/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# ## Mars News Articles Headlines

# In[165]:



article_url = 'https://mars.nasa.gov/news/'
browser.visit(article_url)


# In[166]:


#create Buetiful soup 
article_html = browser.html
article_soup = bs(article_html, 'html' )
print(article_soup)


# In[167]:


# Retrieve the most recent article's title and paragraph.
article_list=article_soup.find("ul", class_="item_list")
article_item=article_list.find("li", class_="slide")
article_headline = article_item.find("div", class_="content_title").text
article_body = article_item.find("div", class_="article_teaser_body").text
print(article_headline)
print(article_body)


# ## JPL Mars Space Images - Featured Image
# 

# In[168]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
time.sleep(5)


# In[169]:


img_html = browser.html
img_soup = bs(img_html, 'html.parser')
print(img_soup.prettify())


# In[170]:


featured_image_url = "https://www.jpl.nasa.gov/images/supercams-mars-meteorite-aboard-the-iss"
featured_image_url 


# ## Mars Facts

# In[194]:


executable_path = {'executable_path': '/Users/marcellisv/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[195]:


facts_url = 'https://space-facts.com/mars/'
browser.visit = (facts_url)


# In[196]:


#Convert Table to HTML using pandas 
facts_table = pd.read_html(facts_url)
facts_table


# In[197]:


mars_facts_df = facts_table[0]

mars_facts_df.columns = ["Description", "Value"]

mars_facts_df


# In[198]:


#Set the index to the `Description` column
mars_facts_df.set_index('Description', inplace=True)
mars_facts_df


# In[199]:


html_table = mars_facts_df.to_html()
mars_facts_df.to_html("mars_facts_data.html")


# In[200]:


mars_facts_dict = mars_facts_df.to_dict
mars_facts_dict


# ## Mars Hemispheres

# In[202]:


executable_path = {'executable_path': '/Users/marcellisv/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[203]:


usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(usgs_url)


# In[204]:


#create Buetiful soup 
usgs_html = browser.html
hemi_soup = bs(usgs_html, 'html.parser')
hemi_soup


# In[205]:


#create list for hisphere data 
hemi_url = []

#find each hemisphere
links = browser.find_by_css("a.product-item h3")

for i in range(len(links)):
    hemi = {}
    #Get name of hemisphere for title
    browser.find_by_css("a.product-item h3")[i].click()
    hemi['title'] = browser.find_by_css("h2.title").text
    ##find image url for each hemisphere 
    sample_elem = browser.links.find_by_text('Sample').first
    hemi['img_url'] = sample_elem['href']
    
    #Append to empty hemipere list 
    hemi_url.append(hemi)
    
    
    browser.back()
    
hemi_url


# ## First Combine all data into one dictionary
# 

# In[206]:


combined_mars_dict= {}


# In[207]:


combined_mars_dict["article_headline"] = article_headline
combined_mars_dict["article_body"] = article_body
combined_mars_dict["featured_image_url"] = featured_image_url
combined_mars_dict["mars_facts_dict"] = mars_facts_df
combined_mars_dict["hemi_url"]= hemi_url


# In[161]:


combined_mars_dict


# In[ ]:




