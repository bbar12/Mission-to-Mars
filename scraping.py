#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

def scrape_all():
   # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres":hemisphere_scrape(browser),
        "last_modified": dt.datetime.now()
    }
   #quit the automated browsing session
    browser.quit()
    return data
# Set the executable path and initialize the chrome browser in splinter
# executable_path = {'executable_path': 'chromedriver'}
# browser = Browser('chrome', **executable_path)

def mars_news(browser):
#assign the url and instruct the browser to visit it.
# Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
# Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


#set up the html parser and then quit the browser
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
     # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None
    
# Use the parent element to find the paragraph text 
    return news_title, news_p

# #Scraping images 
# ### Featured Images

def featured_image(browser):
#we determine the sequence of clicks we need Splinter to get through
# Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
# Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')[0]
    full_image_elem.click()
# Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()
# Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    try:
   # find the relative image url
       img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    except AttributeError:
        return None
# Use the base URL to create an absolute URL
#use the img url and plug it into a link
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    return img_url
    
#Mars facts 
def mars_facts():
    
    try:
      # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None

    df.columns=['Description', 'Value']
    df.set_index('Description', inplace=True)

#turn this table back into html code: notice it starts with table tag so we are OK
    return df.to_html(classes="table table-striped") 

def hemisphere_scrape(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    hemisphere_data=[];
    hemisphere_urls=[];

# Find and click the first hemisphere image
    browser.is_element_present_by_text('Cerberus Hemisphere Enhanced', wait_time=1)
    hem1_elem = browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced')
    hem1_elem.click()

#parse and collect title and image for hem1
    html = browser.html
    hem1_page = BeautifulSoup(html, 'html.parser')
    hem1_title = hem1_page.find("h2", class_='title').get_text()

    hem1_image = hem1_page.select_one('div.downloads a').get("href")
    hemisphere_urls.append(hem1_image)
    hem1_data={"title":hem1_title, "image_url": hem1_image}
    hemisphere_data.append(hem1_data)

#Second hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
# Find second hemisphere image and click it 
    browser.is_element_present_by_text('Schiaparelli Hemisphere Enhanced', wait_time=1)
    hem2_elem = browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced')
    hem2_elem.click()


#Collect title and image for hem2
    html = browser.html
    hem2_page = BeautifulSoup(html, 'html.parser')
    hem2_title = hem2_page.find("h2", class_='title').get_text()
    hem2_image = hem2_page.select_one('div.downloads a').get("href")
    hemisphere_urls.append(hem2_image)
    hem2_data={"title":hem2_title, "image_url": hem2_image}
    hemisphere_data.append(hem2_data)

#repeat for third and fourth hemispheres
#Third hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
# Find second hemisphere image and click it 
    browser.is_element_present_by_text('Syrtis Major Hemisphere Enhanced', wait_time=1)
    hem3_elem = browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced')
    hem3_elem.click()

#Collect title and image for hem3
    html = browser.html
    hem3_page = BeautifulSoup(html, 'html.parser')
    hem3_title = hem3_page.find("h2", class_='title').get_text()

    hem3_image = hem3_page.select_one('div.downloads a').get("href")
    hemisphere_urls.append(hem3_image)
    hem3_data={"title":hem3_title, "image_url": hem3_image}
    hemisphere_data.append(hem3_data)

#Fourth hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
# Find fourth hemisphere image and click it 
    browser.is_element_present_by_text('Valles Marineris Hemisphere Enhanced', wait_time=1)
    hem4_elem = browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced')
    hem4_elem.click()

#Collect title and image for hem4
    html = browser.html
    hem4_page = BeautifulSoup(html, 'html.parser')
    hem4_title = hem4_page.find("h2", class_='title').get_text()

    
    hem4_image = hem4_page.select_one('div.downloads a').get("href")
    hemisphere_urls.append(hem4_image)
    hem4_data={"title":hem4_title, "image_url": hem4_image}
    hemisphere_data.append(hem4_data)
    
    browser.quit()
    return hemisphere_data

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())




