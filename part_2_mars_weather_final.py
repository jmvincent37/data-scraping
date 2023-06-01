#!/usr/bin/env python
# coding: utf-8

# # Module 12 Challenge
# ## Deliverable 2: Scrape and Analyze Mars Weather Data

# In[1]:


# Import relevant libraries
from splinter import Browser
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
pd.set_option('max_colwidth', 400)


# In[2]:


# Establishing executable path using chrome drive
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Step 1: Visit the Website
# 
# Use automated browsing to visit the [Mars Temperature Data Site](https://static.bc-edx.com/data/web/mars_facts/temperature.html). Inspect the page to identify which elements to scrape.
# 
#    > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools to discover whether the table contains usable classes.
# 

# In[3]:


# Visit the website
# https://static.bc-edx.com/data/web/mars_facts/temperature.html
url = "https://static.bc-edx.com/data/web/mars_facts/temperature.html"
browser.visit(url)


# ### Step 2: Scrape the Table
# 
# Create a Beautiful Soup object and use it to scrape the data in the HTML table.
# 
# Note that this can also be achieved by using the Pandas `read_html` function. However, use Beautiful Soup here to continue sharpening your web scraping skills.

# In[4]:


# Create a Beautiful Soup Object
html = browser.html
html_soup = soup(html, 'html.parser')
print(html_soup.prettify())


# In[5]:


# Extract all rows of data
table = html_soup.find_all("tr", class_="data-row")
table


# ### Step 3: Store the Data
# 
# Assemble the scraped data into a Pandas DataFrame. The columns should have the same headings as the table on the website. Here’s an explanation of the column headings:
# 
# * `id`: the identification number of a single transmission from the Curiosity rover
# * `terrestrial_date`: the date on Earth
# * `sol`: the number of elapsed sols (Martian days) since Curiosity landed on Mars
# * `ls`: the solar longitude
# * `month`: the Martian month
# * `min_temp`: the minimum temperature, in Celsius, of a single Martian day (sol)
# * `pressure`: The atmospheric pressure at Curiosity's location

# In[6]:


# Created a test dictionary of the first instance to prepare the for loop
rows = table
rows


# In[7]:


# Create an empty list
row_data = []
# Loop through the scraped data to create a list of rows

for row in rows:
    td = row.find_all('td')
    row = [col.text for col in td]
    row_data.append(row)
row_data    


# In[8]:


# Create a Pandas DataFrame by using the list of rows and a list of the column names
row_data = pd.DataFrame(row_data, columns=['id', 'terrestrial_date', 'sol', 'ls', 'month', 'min_temp', 'pressure'])
    


# In[9]:


# Confirm DataFrame was created successfully
row_data.head(5) 


# ### Step 4: Prepare Data for Analysis
# 
# Examine the data types that are currently associated with each column. If necessary, cast (or convert) the data to the appropriate `datetime`, `int`, or `float` data types.
# 
#   > **Hint** You can use the Pandas `astype` and `to_datetime` methods to accomplish this task.
# 

# In[10]:


# Examine data type of each column
df_type = row_data.convert_dtypes(infer_objects=True)
print(df_type.dtypes)


# In[11]:


# Change data types for data analysis
df_type["id"] = df_type["id"].astype(object)
df_type["sol"] = df_type["sol"].astype(int)
df_type["ls"] = df_type["ls"].astype(int)
df_type["month"] = df_type["month"].astype(int)
df_type["min_temp"] = df_type["min_temp"].astype(float)
df_type["pressure"] = df_type["pressure"].astype(float)


from datetime import datetime as dt
df_type["terrestrial_date"] = pd.to_datetime(df_type["terrestrial_date"], unit='ns')



# In[12]:


# Confirm type changes were successful by examining data types again
print(df_type.dtypes)


# ### Step 5: Analyze the Data
# 
# Analyze your dataset by using Pandas functions to answer the following questions:
# 
# 1. How many months exist on Mars?
# 2. How many Martian (and not Earth) days worth of data exist in the scraped dataset?
# 3. What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
#     * Find the average the minimum daily temperature for all of the months.
#     * Plot the results as a bar chart.
# 4. Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
#     * Find the average the daily atmospheric pressure of all the months.
#     * Plot the results as a bar chart.
# 5. About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
#     * Consider how many days elapse on Earth in the time that Mars circles the Sun once.
#     * Visually estimate the result by plotting the daily minimum temperature.
# 

# In[42]:


row_data_copy = df_type
row_data_copy


# In[43]:


# 1. How many months are there on Mars?
month_data =row_data_copy.groupby('month').count()["id"]
#month_data = month_data.drop("sol", axis=1)
#month_data = month_data.drop("ls", axis=1)
# month_data = month_data.drop("min_temp", axis=1)
# month_data = month_data.drop("pressure", axis=1)
# month_data = month_data.drop("terrestrial_date", axis=1)
month_data = month_data.sort_index()
month_data


# In[44]:


# 2. How many Martian days' worth of data are there?
row_data_copy["sol"].count()


# In[46]:


# 3. What is the average low temperature by month?
low_temp = df_type.groupby(by = ["month"]).mean()["min_temp"]
low_temp


# In[56]:


# Plot the average temperature by month
low_temp.plot.bar(xlabel="Month", ylabel="Temperature in Celcius",
                                   legend=False, rot=0)
plt.show()


# In[54]:


# 4. Average pressure by Martian month
avg_pressure_month = df_type.groupby("month").agg({"pressure": "mean"})
avg_pressure_month


# In[72]:


# Plot the average pressure by month
av_sorted = avg_pressure_month.sort_values(by="pressure", ascending=True)
av_sorted.plot.bar(xlabel="Month", ylabel="Atmospheric Pressure",
                                    legend=False, rot=0)
plt.show()


# In[80]:


# 5. How many terrestrial (earth) days are there in a Martian year?
plt.plot(df_type["sol"], df_type["min_temp"], color="blue")
plt.xlabel("Number of terrestrial days")
plt.ylabel("Minimum temperature")
plt.xlim(0, 2000)
plt.show()


# On average, the third month has the coldest minimum temperature on Mars, and the eighth month is the warmest. But it is always very cold there in human terms!
# 
# 

# Atmospheric pressure is, on average, lowest in the sixth month and highest in the ninth.

# The distance from peak to peak is roughly 1425-750, or 675 days. A year on Mars appears to be about 675 days from the plot. Internet search confirms that a Mars year is equivalent to 687 earth days.

# ### Step 6: Save the Data
# 
# Export the DataFrame to a CSV file.

# In[83]:


# Write the data to a CSV
df_type.to_csv("Mars_Export.csv", encoding='utf8', index=False)


# In[24]:


browser.quit()


# In[ ]:




