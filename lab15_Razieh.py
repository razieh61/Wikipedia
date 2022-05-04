import datetime

from selenium import webdriver # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)

#--------Wikipedia web App DATA PARAMETERS ----------------
app = 'Wikipedia'
Wiki_navigate_url = 'https://en.wikipedia.org/'
Wiki_home_page_title = 'Wikipedia, the free encyclopedia'
Wiki_home_page_url = 'https://en.wikipedia.org/wiki/Main_Page'

#--------------------------------------------------------


def setUp():
    print(f'Launch {app} App')
    print(f'----------------***-----------------')
    # make browser full screen
    driver.maximize_window()

    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # navigate to Wiki App website
    driver.get(Wiki_navigate_url)

    # check that Wiki URL and the home page title are as expected
    if driver.current_url == Wiki_home_page_url and driver.title == Wiki_home_page_title:
        print(f'Yey! {app} App website launched successfully :)')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app} did not launch. check your code or application')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print(f'---------------***----------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()  # kill the instance


def search():
    if driver.current_url == Wiki_home_page_url: # check we are on the home page
        driver.find_element(By.ID, 'searchInput').send_keys('Python (programming language)')
        driver.find_element(By.XPATH, '//span[contains(., "Python (programming language)")]').click()
        print(driver.find_element(By.ID, 'firstHeading').is_displayed())
        assert driver.find_element(By.ID, 'firstHeading').is_displayed()
        driver.find_element(By.CLASS_NAME, 'mw-wiki-logo').click()
        if driver.current_url == Wiki_home_page_url and \
                driver.title == Wiki_home_page_title:
            print(f'{app} Home page is displayed successfully. - Page title: {driver.title}')
            sleep(0.25)
        else:
            print(f'{app} Home page is not displayed. check your code or website and try again')




# Launch app
setUp()
# search field
search()
# Close app
tearDown()
