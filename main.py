from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

# login credentials
username = "demo"
password = "demo"
# webpage title
dashboardTitle = "Dashboard"
orderTitle = "Orders"

# initialize the Chrome driver
driver = webdriver.Chrome("/Users/reshma/Documents/Projects/RhombusPower/chromedriver")

# head to opencart login page
def login():
    driver.get("https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token=g")
    # clear username field and enter correct username
    driver.find_element_by_id("input-username").clear()
    driver.find_element_by_id("input-username").send_keys(username)

    # clear passsword field and enter correct pasword
    driver.find_element_by_id("input-password").clear()
    driver.find_element_by_id("input-password").send_keys(password)

    # click on login button
    ele = driver.find_element_by_xpath("//div[contains(@class,'text-right')]/button")
    click_element(ele)
    # wait for the webpage to load completely
    time.sleep(5)

    # check if the user is navigated to dashboard page
    if check_title(dashboardTitle):
        ele = driver.find_element_by_xpath("//div[contains(@class,'tile-footer')]/a")
        click_element(ele)
        if check_title(orderTitle):
            print("The user is on Orders page right now")
            
    # wait for the webpage to load completely
    time.sleep(5)


def click_element(element):
    # javascript code to exceute click buttton
    driver.execute_script("arguments[0].click();", element)


def check_title(titlename):
    if titlename == driver.title:
        return True


# main entry
if __name__ == '__main__':
    login()

    # close the driver
    driver.close()
