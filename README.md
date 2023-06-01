### Module 11 Challenge - Data Scraping Challange

#### Introduction:
In this project, you will be working on web scraping and data analysis related to Mars. The assignment consists of two parts: scraping titles and preview text from Mars news articles, and scraping and analyzing Mars weather data. By completing this project, you will further strengthen your skills in data collection, organization, storage, analysis, and visual communication.


#### Part 1: Scrape Titles and Preview Text from Mars News

Use automated browsing to visit the Mars News website and inspect the page to identify the elements to scrape.\
Create a Beautiful Soup object to extract the text elements from the website.\
Extract the titles and preview text of the news articles that you scraped.\
Store the scraping results in Python data structures as follows:
* Store each title-and-preview pair in a Python dictionary and, give each dictionary two keys: title and preview. 
* Store all the dictionaries in a Python list.
* Print the list in your notebook.

Optionally, you can store the scraped data in a JSON file.


#### Part 2: Scrape and Analyze Mars Weather Data

Use automated browsing to visit the Mars Temperature Data Site and inspect the page to identify the elements to scrape.\
Create a Beautiful Soup object and scrape the data in the HTML table.\
Assemble the scraped data into a Pandas DataFrame with the appropriate column headings.\
Examine the data types associated with each column. If necessary, cast (or convert) the data to the appropriate data types.\
Analyze the dataset using Pandas functions to answer the following questions:

* How many months exist on Mars?
* How many Martian (and not Earth) days worth of data exist in the scraped dataset?
* What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
  * Find the average minimum daily temperature for all of the months.
  * Plot the results as a bar chart.
* Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
  * Find the average daily atmospheric pressure of all the months.
  * Plot the results as a bar chart.
* About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
  * Consider how many days elapse on Earth in the time that Mars circles the Sun once.
  * Visually estimate the result by plotting the daily minimum temperature.
* Export the DataFrame to a CSV file.

### Requirements and Point Values:
Part 1: Scrape Titles and Preview Text from Mars News (40 points)
* Automated browsing (with Splinter) was used to visit the Mars news site, and the HTML code was extracted (with Beautiful Soup). (10 points)
* The titles and preview text of the news articles were scraped and extracted. (20 points)
* The scraped information was stored in the specified Python data structure—specifically, a list of dictionaries. (10 points)

Part 2: Scrape and Analyze Mars Weather Data (60 points)
* The HTML table was extracted into a Pandas DataFrame. Either Pandas or Splinter and Beautiful Soup were used to scrape the data. 
* The columns have the correct headings and data types. (15 points)
* The data was analyzed to answer the following questions: 
  * How many months exist on Mars? (5 points)
  * How many Martian days' worth of data are there? (5 points)
* The data was analyzed to answer the following questions, and a data visualization was created to support each answer: (30 points)
* Which month, on average, has the lowest temperature? The highest? (10 points)
* Which month, on average, has the lowest atmospheric pressure? The highest? (10 points)
* How many terrestrial days exist in a Martian year? A visual estimate within 25% was made. (10 points)
* The DataFrame was exported into a CSV file. (5 points)

### Additional Support and Resources Used:
Tutor Sessions (2)\
https://stackoverflow.com \
https://www.askpython.com \
https://pandas.pydata.org
