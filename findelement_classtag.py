from selenium import webdriver


class FindByClass():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementclasstag = driver.find_element_by_class_name("displayed-class")
        elementclasstag.send_keys("Testing app")

        if elementclasstag is not None:
            print("we did it")

ss = FindByClass()

ss.test()