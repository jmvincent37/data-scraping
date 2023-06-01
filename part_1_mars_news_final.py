#!/usr/bin/env python
# coding: utf-8

# # Module 11 Challenge
# ## Deliverable 1: Scrape Titles and Preview Text from Mars News

# In[1]:


# Import Splinter, BeautifulSoup, and ChromeDriveManager
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Establishing executable path using chrome drive
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Step 1: Visit the Website
# 
# 1. Use automated browsing to visit the [Mars news site](https://static.bc-edx.com/data/web/mars_news/index.html). Inspect the page to identify which elements to scrape.
# 
#       > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools.

# In[3]:


# Visit the Mars news site
url = 'https://static.bc-edx.com/data/web/mars_news/index.html'
browser.visit(url)


# ### Step 2: Scrape the Website
# 
# Create a Beautiful Soup object and use it to extract text elements from the website.

# In[15]:


# Create a Beautiful Soup object
html = browser.html
html_soup = soup(html, 'html.parser')
print(html_soup.prettify())


# In[17]:


# Extract all the text elements
text = html_soup.find_all("div", class_="list_text")
text


# ### Step 3: Store the Results
# 
# Extract the titles and preview text of the news articles that you scraped. Store the scraping results in Python data structures as follows:
# 
# * Store each title-and-preview pair in a Python dictionary. And, give each dictionary two keys: `title` and `preview`. An example is the following:
# 
#   ```python
#   {'title': "NASA's MAVEN Observes Martian Light Show Caused by Major Solar Storm", 
#    'preview': "For the first time in its eight years orbiting Mars, NASA’s MAVEN mission witnessed two different types of ultraviolet aurorae simultaneously, the result of solar storms that began on Aug. 27."
#   }
#   ```
# 
# * Store all the dictionaries in a Python list.
# 
# * Print the list in your notebook.

# In[23]:


# Created a test dictionary of the first instance to prepare the for loop
test = text[0]
test

test_dict = {}
title_val = test.find("div", class_="content_title").text
test

preview_val = test.find("div", class_="article_teaser_body").text
preview_val

test_dict["title"] = title_val
test_dict["preview"] = preview_val

test_dict


# In[24]:


# Create an empty list to store the dictionaries
article_list = []


# In[27]:


# Loop through the text elements
# Extract the title and preview text from the elements
# Store each title and preview pair in a dictionary
# Add the dictionary to the list
for article in text:
    article_dict = {}
    title_val = article.find("div", class_="content_title").text

    preview_val = article.find("div", class_="article_teaser_body").text
   
    article_dict["title"] = title_val
    article_dict["preview"] = preview_val
   
    article_list.append(article_dict)


# In[26]:


# Print the list to confirm success
article_list


# In[ ]:


browser.quit()


# In[ ]:




