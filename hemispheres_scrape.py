#!/usr/bin/env python
# coding: utf-8

from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt


executable_path ={'executable_path':'chromedriver'}
browser = Browser('chrome',**executable_path)

def hemisphere_scrape():
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

# Find and click the first hemisphere image
    browser.is_element_present_by_text('Cerberus Hemisphere Enhanced', wait_time=1)
    hem1_elem = browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced')
    hem1_elem.click()

#parse and collect title and image for hem1
    html = browser.html
    hem1_page = BeautifulSoup(html, 'html.parser')
    hem1_title = hem1_page.find("h2", class_='title').get_text()

    hem1_image = hem1_page.select_one('div.downloads a').get("href")


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

#add all of the hemisphere into a list of dictionaries for all hemispheres
    all_hemispheres=[{'title':hem1_title, 'img_url':hem1_image},
                    {'title':hem2_title, 'img_url':hem2_image}, 
                    {'title':hem3_title, 'img_url':hem3_image},
                    {'title':hem4_title, 'img_url':hem4_image}]
    return all_hemispheres

browser.quit()


