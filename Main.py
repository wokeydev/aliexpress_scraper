import getopt
import random
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

xpath_objs = { 'loginPart': '//div[@data-role="user-account-top"]', 'signLink': '//a[@data-role="sign-link"]',
               'username': '//input[@name="loginId"]', 'password': '//input[@name="password"]',
               'switcher': '//a[@id="switcher-info"]', 'switcher-country': '//div[@data-role="switch-country"]',
               'uk': '//span[contains(@class, "css_uk")]', 'currency-switcher': '//div[@class="switcher-currency-c"]',
               'gbp': '//a[@data-currency="GBP"]', 'save-btn': '//button[@data-role="save"]',
               'search-field': '//input[@name="SearchText"]', 'first-category': '//div[@class="item"]',
               'detail-category': '//a[@data-role="sign-link"]'}

def login(browser):
    loginPart = browser.find_element_by_xpath(xpath_objs['loginPart']) # Go over to the Login div to select the login page link 
    hover = ActionChains(browser).move_to_element(loginPart) 
    hover.perform()
    time.sleep(3)

    signBtn = browser.find_element_by_xpath(xpath_objs['signLink']) # Find the login page link and click
    ActionChains(browser).move_to_element(signBtn).click().perform()
    time.sleep(3)    

    time.sleep(10) # Wait until the login page's loading is done
    browser.switch_to_frame(0)

    userEle = browser.find_element_by_xpath(xpath_objs['username']) # Find the username input element
    ActionChains(browser).move_to_element(userEle).click().perform() # Click the input element
    ActionChains(browser).send_keys('whitedeveloper0313@gmail.com').perform() # Input email address
    time.sleep(2)

    passwordEle = browser.find_element_by_xpath(xpath_objs['password']) # Find the password input element
    ActionChains(browser).move_to_element(passwordEle).click().perform() # Click the input element
    ActionChains(browser).send_keys('passwordpassword').perform() # Input password   
    time.sleep(2)    
    ActionChains(browser).send_keys(Keys.RETURN).perform() # Press enter key to login to the main page
    time.sleep(5)
    ActionChains(browser).send_keys(Keys.ESCAPE).perform() # Esc ads
    time.sleep(3)


def shipTo(browser):
    switcherEle = browser.find_element_by_xpath(xpath_objs['switcher']) # Find the Shipping Regional Setting Selector
    ActionChains(browser).move_to_element(switcherEle).click().perform()
    time.sleep(3)

    switchCountry = browser.find_element_by_xpath(xpath_objs['switcher-country']) # Find the Ship to country element
    ActionChains(browser).move_to_element(switchCountry).click().perform()
    time.sleep(3)

    KingdomEle = browser.find_element_by_xpath(xpath_objs['uk']) # Select the United Kingdom 
    ActionChains(browser).move_to_element(KingdomEle).click().perform()
    time.sleep(3)    

    CurrencyEle = browser.find_element_by_xpath(xpath_objs['currency-switcher']) # Find the Currency element
    ActionChains(browser).move_to_element(CurrencyEle).click().perform()
    time.sleep(3)    

    PoundEle = browser.find_element_by_xpath(xpath_objs['gbp']) # Select the GBP 
    ActionChains(browser).move_to_element(PoundEle).click().perform()
    time.sleep(3)

    SaveEle = browser.find_element_by_xpath(xpath_objs['save-btn']) # Press save button
    ActionChains(browser).move_to_element(SaveEle).click().perform()
    time.sleep(5)

    ActionChains(browser).send_keys(Keys.ESCAPE).perform() # Esc ads
    time.sleep(1)

def searchBicycle(browser):
    searchEle = browser.find_element_by_xpath(xpath_objs['search-field']) # Find the Category search field 
    ActionChains(browser).move_to_element(searchEle).click().perform() # Click the search field
    ActionChains(browser).send_keys('Boys Bicycle').perform() # Type the Boys Bicycle in the search field
    ActionChains(browser).send_keys(Keys.ENTER).perform() # Press enter to search
    time.sleep(3)

    firstItem = browser.find_element_by_xpath(xpath_objs['first-category']) # Find the first result
    ActionChains(browser).move_to_element(firstItem).click().perform() 
    signLink = browser.find_element_by_xpath(xpath_objs['detail-category']) # Click the first result
    signLink.click()
    time.sleep(5)


def main(argv):

    browser = webdriver.Chrome("chromedriver") # Launch ChromeDriver, Chromedriver is in the same directory right now, but you can set the path.
    browser.get("https://www.Aliexpress.com") # Go to the www.Aliexpress.com page
    browser.maximize_window() # Maximize Chromebrowser
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.ESCAPE).perform() # Esc the ads
    time.sleep(3)

    login(browser) # Login in with my crendentail
    shipTo(browser) # Ship To country to United Kingdom and currency to GBP
    searchBicycle(browser) # Search Boys Bicycle and click the first search result
    
    browser.close()


if __name__ == "__main__":
    main(sys.argv[1:])
