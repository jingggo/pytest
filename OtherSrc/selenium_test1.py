from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://10.125.2.173')

print(driver.title)

driver.quit()