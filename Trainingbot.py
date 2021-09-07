from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import schedule

# timeWanted has to be on the form "11.00", gymWanted has to be a valid gym


def bookTraining1():

    training = trainingTime1.split(":")
    timeWanted = ".".join(training)

    # Changes gymWanted right format
    global gymWanted
    if gymWanted.upper() == "DMMH":
        gymWanted = gymWanted.upper()
    else:
        gymWanted = gymWanted.lower()
        gymWanted = gymWanted[0].upper() + gymWanted[1:]

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Access SiT's webpage
    driver.get("https://www.sit.no/")

    # Accessing correct pages by finding buttons
    login = driver.find_element_by_link_text("Logg inn")
    login.click()

    login = driver.find_element_by_link_text("Logg inn med Feide")
    login.click()

    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "org-chooser-selectized"))
    )

    login.click()
    login.send_keys("ntnu")
    login.send_keys(Keys.ENTER)
    login.submit()

    login = driver.find_element_by_id("username")
    login.click()

    # Username
    login.send_keys("username")

    login = driver.find_element_by_id("password")
    login.click()

    # Password
    login.send_keys("password")
    login.submit()

    # Accessing bookingpage
    notLoaded = True
    while notLoaded:
        try:
            driver.get("https://www.sit.no/trening/treneselv")

            time.sleep(2)

            driver.switch_to.frame("ibooking-iframe")

            # Removes the gyms you don't want
            gyms = ["Gløshaugen", "Moholt", "DMMH", "Portalen", "Dragvoll"]
            gyms.remove(gymWanted)

            gymKnapper = driver.find_elements_by_xpath(
                "//button[@class='active']")

            for i in range(5):
                if gymKnapper[i].text in gyms:
                    gymKnapper[i].click()

            notLoaded = False
        except:
            pass

    times = driver.find_elements_by_xpath("//p[@class='time']")

    rightStartTime = []

    # Number of checks depends on how many available options there are 48 time
    checks = 0
    if gymWanted == "Gløshaugen":
        checks = 70
    elif gymWanted == "Moholt":
        checks = 35
    elif gymWanted == "Dragvoll":
        checks = 55
    elif gymWanted == "Portalen":
        checks = 65
    elif gymWanted == "DMMH":
        checks = 45

    # Adds the spot with the correct starting time
    for i in range(checks):
        if times[i].text.startswith(timeWanted):
            rightStartTime.append(times[i])

    # Chooses the spot
    rightStartTime[-1].click()

    # Clicks on "Book time" pop-up
    try:
        book = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@class=' btn-primary btn' and @data-nomodal='true']"))
        )
        book.click()

    # Registers for waiting list if the bot is too slow
    except:
        book = driver.find_element_by_xpath(
            "//button[@class=' waitlistButton btn-primary btn' and @data-nomodal='true']")
        book.click()

    time.sleep(10)
    driver.quit()


def bookTraining2():

    if trainingTime2 == "00:00":
        return

    training = trainingTime2.split(":")
    timeWanted = ".".join(training)

    global gymWanted
    if gymWanted.upper() == "DMMH":
        gymWanted = gymWanted.upper()
    else:
        gymWanted = gymWanted.lower()
        gymWanted = gymWanted[0].upper() + gymWanted[1:]

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.sit.no/")

    login = driver.find_element_by_link_text("Logg inn")
    login.click()

    login = driver.find_element_by_link_text("Logg inn med Feide")
    login.click()

    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "org-chooser-selectized"))
    )

    login.click()
    login.send_keys("ntnu")
    login.send_keys(Keys.ENTER)
    login.submit()

    login = driver.find_element_by_id("username")
    login.click()

    login.send_keys("brukernavn")

    login = driver.find_element_by_id("password")
    login.click()

    login.send_keys("passord")
    login.submit()

    notLoaded = True
    while notLoaded:
        try:
            driver.get("https://www.sit.no/trening/treneselv")

            time.sleep(2)

            driver.switch_to.frame("ibooking-iframe")

            gyms = ["Gløshaugen", "Moholt", "DMMH", "Portalen", "Dragvoll"]
            gyms.remove(gymWanted)

            gymKnapper = driver.find_elements_by_xpath(
                "//button[@class='active']")

            for i in range(5):
                if gymKnapper[i].text in gyms:
                    gymKnapper[i].click()

            notLoaded = False
        except:
            pass

    times = driver.find_elements_by_xpath("//p[@class='time']")

    rightStartTime = []

    checks = 0
    if gymWanted == "Gløshaugen":
        checks = 70
    elif gymWanted == "Moholt":
        checks = 35
    elif gymWanted == "Dragvoll":
        checks = 55
    elif gymWanted == "Portalen":
        checks = 65
    elif gymWanted == "DMMH":
        checks = 45

    for i in range(checks):
        if times[i].text.startswith(timeWanted):
            rightStartTime.append(times[i])

    rightStartTime[-1].click()

    try:
        book = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@class=' btn-primary btn' and @data-nomodal='true']"))
        )
        book.click()

    except:
        book = driver.find_element_by_xpath(
            "//button[@class=' waitlistButton btn-primary btn' and @data-nomodal='true']")
        book.click()

    time.sleep(10)
    driver.quit()


# Makes the bot run at the desired time
def bookTrening(timeBooking1, timeBooking2):
    schedule.every().day.at(timeBooking1).do(bookTraining1)
    schedule.every().day.at(timeBooking2).do(bookTraining2)

    while True:
        schedule.run_pending()
        time.sleep(1)


# trainingTime has to be a string with the format "11:30", "00:00" you don't want to book
# gymWanted has to be a valid gym
trainingTime1 = "19:00"
trainingTime2 = "20:00"
gymWanted = "gløshaugen"

# Runs the bot
bookTrening(trainingTime1, trainingTime2)
