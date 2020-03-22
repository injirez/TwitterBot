from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

class TwitterBot:
    def __init__(self, username, password):
        self.username = username        
        self.password = password
        #chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #self.bot = webdriver.Chrome('/Users/rodionibragimov/Downloads/chromedriver', options=chrome_options)

        #self.bot = webdriver.Firefox()

        #chromedriver = '/Users/rodionibragimov/Downloads/chromedriver' #ur way to chromedriver
        #self.bot = webdriver.Chrome(chromedriver)  #For Chrome users

    def login(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.bot = webdriver.Chrome('/Users/rodionibragimov/Downloads/chromedriver', options=chrome_options)
        bot = self.bot

        bot.get('https://twitter.com')
        #isGetable = False
        time.sleep(5)
        
        #while (True):
            #try:
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        #email.clear()
        #password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
                #isGetable = True
            
            #except BaseException:
                #print('you gay')
                #break
            
            #finally:
                #if (isGetable == True): break
            
        
                

        

    def like_tweet(self, hashtag, TagFriend):
        time.sleep(3)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.bot = webdriver.Chrome('/Users/rodionibragimov/Downloads/chromedriver', options=chrome_options)
        bot = self.bot
        self.TagFriend = TagFriend
        self.hashtag = hashtag
        search = bot.find_element_by_xpath("//input[@data-testid = 'SearchBox_Search_Input']")
        search.clear()
        search.send_keys(self.hashtag)
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        
        bot.find_element_by_xpath("//input[@name = 'People' and not(@checked)]").click()
        #bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query&pf=on')
        time.sleep(5)
        
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_elements_by_xpath("//a[@class = 'css-4rbku5 css-18t94o4 css-901oao r-111h2gw r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']")
            links = [elem.get_attribute('href') for elem in tweets]
            for link in links:
                bot.get(link)
                time.sleep(5)
                try:
                    #LIKE
                    like = bot.find_element_by_xpath("//div[@data-testid='like']")
                    like.click()
                    time.sleep(2)

                    #RETWEET
                    retweet = bot.find_element_by_xpath("//div[@data-testid='retweet']")
                    retweet.click()
                    time.sleep(2)
                    bot.find_element_by_xpath("//div[@data-testid='retweetConfirm']").click()
                    time.sleep(5)

                    #REPLY
                    reply = bot.find_element_by_xpath("//div[@data-testid='reply']")
                    reply.click()
                    time.sleep(2)
                    tag = bot.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']")
                    tag.clear()
                    tag.send_keys(self.TagFriend)
                    time.sleep(10)
                    tweetButton = bot.find_element_by_xpath("//div[@data-testid='tweetButton']")
                    tweetButton.click()
                    time.sleep(5)

                except Exception as ex:
                    time.sleep(10)


rod = TwitterBot("ur login", "ur password")
rod.login()
rod.like_tweet('giveaway', "      @og_seekg ")
