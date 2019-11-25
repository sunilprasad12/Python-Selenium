from selenium import webdriver


class FindByID():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
           print("we found on element by link Test")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print("we found on element by test")



ss = FindByID()
ss.test()