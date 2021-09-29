from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("http://www.uitestingplayground.com/")
driver.find_element_by_xpath("//a[contains(text(),'Sample App')]").click()
elmts=driver.find_elements_by_xpath("//input") #or driver.find_element_by_tag_name("input")
nbr=len(elmts)
print(nbr,"elements")
if(nbr!=0):
    for elmt in elmts:
        placeh=elmt.get_attribute("placeholder")
        print(placeh)
driver.save_screenshot("C:\captures\cap.png")
driver.quit()