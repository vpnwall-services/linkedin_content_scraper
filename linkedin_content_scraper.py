#!/usr/bin/python3
import time
import os
import re
import subprocess
import unittest
import json

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


customerlist = 'customerlist.txt'
linkedin_user = ''
linkedin_password = ''

# Prepare working folder
if not os.path.exists('company-linkedin-feed'):
    os.makedirs('company-linkedin-feed')

options = webdriver.FirefoxOptions()
#options.add_argument('--headless')
browser = webdriver.Firefox(options=options)
browser.get('https://www.linkedin.com/login')
username = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')

username.send_keys(linkedin_user)
password.send_keys(linkedin_password)

submitButton = browser.find_element_by_css_selector('html.artdeco body.system-fonts div#app__container main.app__content div form.login__form div.login__form_action_container button.btn__primary--large.from__button--floating')
submitButton.click()


# Execute retrieve_content function
        # Lets go for this customer feed
with open(customerlist) as f:
    lines = [line.rstrip() for line in f]
    for i in range(len(lines)):
        customer = lines[i]
        if not os.path.exists("company-linkedin-feed/"+customer):
            os.makedirs("company-linkedin-feed/"+customer)
        print('Go to company page')
        browser.get('https://www.linkedin.com/company/'+customer+'')
        print('Retrieve all posts')
        print('Click on all view more buttons')
        posts = browser.find_elements_by_class_name('feed-shared-update-v2')
        browser.execute_script("window.scrollTo(0, 1080)")
        search = browser.find_elements_by_xpath("//button[contains(.,'voir plus')]")
        for x in range(len(search)):
            (search[x]).click()
        browser.execute_script("window.scrollTo(0, 2080)")
        search = browser.find_elements_by_xpath("//button[contains(.,'voir plus')]")
        for x in range(len(search)):
            (search[x]).click()
        # POST 1
        # Company logo
        company_logo = posts[0].find_element_by_class_name('ivm-view-attr__img--centered').get_attribute('src')
        # Post image
        post1_images = posts[0].find_elements_by_class_name('ivm-view-attr__img--centered')
        post1_image = post1_images[1].get_attribute('src')
        # Post content
        post1_content = posts[0].find_element_by_class_name('feed-shared-inline-show-more-text')
        post1_text = post1_content.find_element_by_class_name('feed-shared-text').text
        # Post date
        post1_date = posts[0].find_element_by_class_name('visually-hidden').text
        
        # POST 2
        # Company logo
        company_logo = posts[1].find_element_by_class_name('ivm-view-attr__img--centered').get_attribute('src')
        # Post image
        post2_images = posts[1].find_elements_by_class_name('ivm-view-attr__img--centered')
        post2_image = post2_images[1].get_attribute('src')
        # Post content
        post2_content = posts[1].find_element_by_class_name('feed-shared-inline-show-more-text')
        post2_text = post2_content.find_element_by_class_name('feed-shared-text').text
        # Post date
        post2_date = posts[1].find_element_by_class_name('visually-hidden').text
        
        # POST 3
        # Company logo
        company_logo = posts[2].find_element_by_class_name('ivm-view-attr__img--centered').get_attribute('src')
        # Post image
        post3_images = posts[2].find_elements_by_class_name('ivm-view-attr__img--centered')
        post3_image = post3_images[1].get_attribute('src')
        # Post content
        post3_content = posts[2].find_element_by_class_name('feed-shared-inline-show-more-text')
        post3_text = post3_content.find_element_by_class_name('feed-shared-text').text
        # Post date
        post3_date = posts[2].find_element_by_class_name('visually-hidden').text
        last_three_posts = [
            {
                'linkedin_company_logo': ''+company_logo+'',
                'linkedin_post_image': ''+post1_image+'',
                'linkedin_post_content': ''+post1_text+'',
                'linkedin_post_date': ''+post1_date+'',
            },
            {
                'linkedin_company_logo': ''+company_logo+'',
                'linkedin_post_image': ''+post2_image+'',
                'linkedin_post_content': ''+post2_text+'',
                'linkedin_post_date': ''+post2_date+'',
            },
            {
                'linkedin_company_logo': ''+company_logo+'',
                'linkedin_post_image': ''+post3_image+'',
                'linkedin_post_content': ''+post3_text+'',
                'linkedin_post_date': ''+post3_date+'',
            }
        ]
        print('Write to json file')
        with open('company-linkedin-feed/'+customer+'/'+customer+'.json', 'w') as f:
            json.dump(last_three_posts, f)
browser.close()
