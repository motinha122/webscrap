from selenium.webdriver.chrome.service import Service
from selenium import webdriver

url = 'https://starwars-visualguide.com/#/characters/1'

service = Service(executable_path='/home/tiago/Documents/webscrap/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get(url)

stats = driver.find_element(By.CLASS_NAME, "fs-headline display-block ng-binding")

driver.quit()