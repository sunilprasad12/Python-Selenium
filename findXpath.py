from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("we found it")

        elementByName = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        
        if elementByName is not None:
            print("we found XPATH")


ss = ByDemo()
ss.test()