import basic_funcs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

def web_driver_setup():
   global chrome_driver
   chrome_driver = webdriver.Chrome(ChromeDriverManager().install())

def google_search():
    chrome_driver.get("http://www.google.com")
    print("What can i search for you!")
    basic_funcs.speak("What can i search for you!")
    searched_query = basic_funcs.takeCommand()
    chrome_driver.find_element_by_name("q").send_keys(searched_query)
    chrome_driver.find_element_by_name("btnK").submit()
    chrome_driver.back()
    chrome_driver.refresh()
    chrome_driver.forward()

def youtube_search():
    chrome_driver.get("http://www.youtube.com")
    print("What can i search for you!")
    basic_funcs.speak("What can i search for you!")
    searched_query = basic_funcs.takeCommand()
    chrome_driver.find_element_by_name("search_query").send_keys(searched_query)
    chrome_driver.find_element_by_id("search-icon-legacy").click()

def stackoverflow_search():
    chrome_driver.get("http://www.stackoverflow.com")
    print("What can i search for you!")
    basic_funcs.speak("What can i search for you!")
    searched_query = basic_funcs.takeCommand()
    chrome_driver.find_element_by_name("q").send_keys(searched_query)
    chrome_driver.find_element_by_name("q").send_keys(Keys.ENTER)

