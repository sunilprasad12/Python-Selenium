from selenium import webdriver


class FindByID():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("we found on element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("we found on element by name")

        driver.get("https://www.google.com")

        driver.find_element_by_id("gsr")






ss = FindByID()
ss.test()
