from selenium import webdriver
import sys
import os
import subprocess
import random


driver=webdriver.Chrome()
driver.get('https://github.com/')

signInButton=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
signInButton.click()

username=driver.find_element_by_xpath('//*[@id="login_field"]')
username.send_keys('xxxxxxxx.com')

password=driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('xxxxxxxx')

signInConfirm=driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
signInConfirm.click()

plusButton=driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary')
plusButton.click()

newRepo=driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]')
newRepo.click()

name=sys.argv[1]

repoName=driver.find_element_by_xpath('//*[@id="repository_name"]')
repoName.send_keys(name)

description=driver.find_element_by_xpath('//*[@id="repository_description"]')
description.send_keys('git hub repositary for project '+name)

readme=driver.find_element_by_xpath('//*[@id="repository_auto_init"]')
readme.click()

readme=driver.find_element_by_xpath('//*[@id="new_repository"]/div[5]/button')
readme.click()

