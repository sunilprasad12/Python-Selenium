from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo():

    def test(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementListByClass = driver.find_elements_by_class_name("gh-tb")
        lenght = len(elementListByClass)

        if elementListByClass is not None:
            print("we found it : " +  str(lenght))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "div")
        lenght1 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("size of the list is : " + str(lenght1))



ss = ByDemo()
ss.test()