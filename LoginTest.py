from Scheduler import Scheduler
from DateTimeInput import DateTimeInput
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
from time import sleep

def login(driver: webdriver):
    username = driver.find_element_by_xpath("//*[@id=\"id_username\"]")
    username.send_keys("2022nkamath")
    sleep(.5)
    password = driver.find_element_by_xpath("//*[@id=\"id_password\"]")
    password.send_keys("")
    sleep(2)
    button = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/form/input[4]")
    button.click()



def main() -> None:
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://ion.tjhsst.edu")
    time.sleep(5)

    inputter = DateTimeInput()
    goal_time = inputter.input_time()
    goal_date = inputter.input_date()

    precision = 0.5
    ts = Scheduler(precision=precision)
    ts.schedule(login, goal_time, goal_date, driver)
    print('scheduled to run at ', goal_time, 'on', goal_date)

    while True:
        sleep(1)
        try:
            driver.title
        except WebDriverException:
            break




if __name__ == "__main__":
    main()
