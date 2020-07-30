import os, sys
import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Test Account
usernameStr = 'blkmik@hotmail.com'
passwordStr = 'Pa33word'

# Vinh Account
##usernameStr = 'vnle74@hotmail.com'
##passwordStr = 'Pa33word'

# Thinh Account
##usernameStr = 'thinhle@cfenet.ubc.ca'
##passwordStr = 'tape418'

# Get today's date
currentDate = (datetime.datetime.strptime(datetime.datetime.now().strftime("%m/%d/%Y"), "%m/%d/%Y"))


# If it is Wednesday, Saturday, or Sunday, book a tee time at NBGC
#if (currentDate.weekday() == 2 or currentDate.weekday() == 5 or currentDate.weekday() == 6):
# if (currentDate.weekday() == 2 or currentDate.weekday() == 5 or currentDate.weekday() == 6):
#     # If the day is Wednesday or Saturday, book under Mr. Ty's account, else book under Vinh's account
#     if (currentDate.weekday() == 2):
#         # Thinh Account
#         #usernameStr = 'thinhle@cfenet.ubc.ca'
#         #passwordStr = 'tape418'
#         usernameStr = 'vnle74@hotmail.com'
#         passwordStr = 'Pa33word'
#         timeSlot = 0
#     else:
#         # Vinh Account
#         usernameStr = 'vnle74@hotmail.com'
#         passwordStr = 'Pa33word'
#         timeSlot = 0


# This will open a Chrome Browser and load North Bellingham's tee time system.
browser = webdriver.Chrome("C:/data/dev/tool/chromedriver_win32/chromedriver.exe")
browser.get(('https://secure.west.prophetservices.com/NorthBellinghamv3/Home'))

# fill in username and hit the next button
# file in login information
signButton = browser.find_element_by_xpath('/html/body/div[6]/div/ul[1]/li[3]/a')
signButton.click()

username = browser.find_element_by_id('Email')
username.send_keys(usernameStr)

password = browser.find_element_by_id('Password')
password.send_keys(passwordStr + Keys.RETURN)

# Fill in the search criteria that is 14 days after current date.
delta = datetime.timedelta(days=14)
futureDate = datetime.datetime.now() + datetime.timedelta(days=14)
futureDateStr = futureDate.strftime('%Y-%m-%d')

# Navigate to desired date 2 weeks ahead.
browser.get(('https://secure.west.prophetservices.com/NorthBellinghamv3/Home/nIndex?CourseId=1&Date=%s&Time=AnyTime&Player=4&Hole=18#')%(futureDateStr))

# Find all the HREF on the tee time sheet for that date.
#elems = browser.find_elements_by_xpath("//a[@href]")
elems = browser.find_elements_by_xpath("/html/body/div[7]/div[4]/div[3]/div[1]/div/a")

# Get first available tee time HREF which is the fifth item in the list of HREFs.
firstTeeTimeUrl = elems[0].get_attribute("href")

# Navigate to the form to enter players.
browser.get((firstTeeTimeUrl))

# This gets the data value for a given field in the first browser and stores it using "find_element_by_id" and "get_attribute('value')" to get actual data.
# Compound statement.
value1Browser1 = browser.find_element_by_id('NameOfPlayers2').get_attribute('value')
# You can separate if you need logic build in like "if" statements. If statement use indents are blocks
# field1Browser1 = browser.find_element_by_id('NameOfPlayers2')
# value1Browser1 = field1Browser1..get_attribute('value')

# This is to print out the data you are trying to get
print(value1Browser1)

# This will open a second Chrome Browser and load data from first browser to second.
browser2 = webdriver.Chrome("C:/data/dev/tool/chromedriver_win32/chromedriver.exe")
browser2.get(('https://www.google.com/'))

# This uses "find_element_by name"
input1Browser2 = browser2.find_element_by_name('q').send_keys(value1Browser1)





time.sleep(30)
browser.close()
browser.quit()
browser2.close()
browser2.quit()