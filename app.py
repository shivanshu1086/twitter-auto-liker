from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

class Twitter:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.maximize_window()
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
    
    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+str(hashtag)+'&src=typed_query')
        time.sleep(5)
        while True:
            pyautogui.click(pyautogui.locateCenterOnScreen('heart.PNG'))
            time.sleep(5)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)

#email and password section
username = 'your-email'
password = 'your-password'
# data-testid 
#function calling
call = Twitter(username, password)
call.login()
call.like_tweet('searching_hashtag')