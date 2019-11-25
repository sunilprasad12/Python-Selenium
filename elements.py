from selenium import webdriver


class ElementsClass():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        lenght1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("size of the list is:"+ str(lenght1))





ss = ElementsClass()

ss.test()

