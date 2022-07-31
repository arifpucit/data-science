from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import time
from bs4 import BeautifulSoup

chromeOptions = Options()
chromeOptions.add_argument("--start-maximized")

#driver = webdriver.Chrome(executable_path="/Users/arif/Documents/chromedriver", options=chromeOptions)
#Starts the driver and goes to twitter login page
s = Service('/Users/arif/Documents/chromedriver') #path where driver is located on your local disk
driver = webdriver.Chrome(service=s, options = chromeOptions) #create headless instance of chrome web driver
tweeter_url = "https://twitter.com/login"
driver.get(tweeter_url)
wait = WebDriverWait(driver, 10)

time.sleep(5)
# Enter user name
username_input = wait.until(ec.visibility_of_element_located((By.NAME, "text")))
username_input.send_keys('your-account-name')

#Press the next button
#Presses the enter button to search
# to press the enter key after entrying some search text in the text box
time.sleep(3)
username_input.send_keys(Keys.ENTER)


# Enter Password
time.sleep(3)
passwd_input = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
passwd_input.send_keys('your-password')
# to press the enter key after entrying some search text in the text box
time.sleep(3)
passwd_input.send_keys(Keys.ENTER)
time.sleep(3)


search_input = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')))


search_input.clear()
search_input.send_keys('Imran Khan')
# to press the enter key after entrying some search text in the text box
time.sleep(6)
search_input.send_keys(Keys.ENTER)



#Clicks on the people tab which has all the accounts associated with who we searched up
people = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div')
time.sleep(3)
people.click()
time.sleep(5)


#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a
#clicks on our celebrities profile
profile = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a')
time.sleep(6)
profile.click()


time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')
#time.sleep(5)
postings = soup.find_all('div', class_ = 'css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
#time.sleep(5)
tweets = []
for i in range(100):
    for post in postings:
        tweets.append(post.text)
print(tweets)
