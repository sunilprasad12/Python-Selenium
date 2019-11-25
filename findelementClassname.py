from selenium import webdriver


class FindByClass():

    def test(self):
        baseUrl = "https://www.ebay.com"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementclass = driver.find_element_by_class_name("gh-tb")
        elementclass.send_keys("shoe")

        if elementclass is not None:
            print("we did it")

        elementtagname = driver.find_element_by_tag_name("a")

        if elementtagname is not None:
            print("we did id")



ss = FindByClass()
ss.test()