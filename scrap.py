from selenium import webdriver

url = 'https://starwars-visualguide.com/#/characters/1'

driver = webdriver.Chrome()
driver.get(url)
stats = driver.find_element(By.CLASS_NAME, "fs-headline display-block ng-binding")
print(stats)
driver.quit()