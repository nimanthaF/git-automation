from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.google.lk/webhp?tab=rw')

searchBox=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys('tech with tharindu')

searchButton=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchButton.click()

