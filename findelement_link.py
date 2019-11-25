from selenium import webdriver


class FindByLink():

    def test(self):
        baseUrl = "https://www.walmart.com/m/deals/christmas-gifts"
        drive = webdriver.Firefox()
        drive.get(baseUrl)

        elementPartiallink = drive.find_element_by_partial_link_text("Walma")

        if elementPartiallink is not None:
            print("we did it")

            
ss = FindByLink()
ss.test()