from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import schedule 

#timeWanted må være på form "11.00", gymWanted må være en av treningssenterne med stor forbokstav
def bookTraining1():

    training = trainingTime1.split(":")
    timeWanted = ".".join(training)

    # timeWanted = "20.00"
    # gymWanted = "Gløshaugen"

    # Endrer gymWanted til riktig format
    global gymWanted
    if gymWanted.upper() == "DMMH":
        gymWanted = gymWanted.upper()
    else:
        gymWanted = gymWanted.lower()
        gymWanted = gymWanted[0].upper() + gymWanted[1:]

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    #For å komme inn på siden
    driver.get("https://www.sit.no/")

    #Trykker på riktige knapper med tekst
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
    login.send_keys("skcheng")

    login = driver.find_element_by_id("password")
    login.click()
    login.send_keys("Sebastian1908")
    login.submit()

    #Kommer seg inn på siden man booker tid
    notLoaded = True
    while notLoaded:
        try:
            driver.get("https://www.sit.no/trening/treneselv")

            time.sleep(2)
            
            driver.switch_to.frame("ibooking-iframe")

            #Trykker vekk sentere man ikke vil ha
            gyms = ["Gløshaugen", "Moholt", "DMMH", "Portalen", "Dragvoll"]
            gyms.remove(gymWanted)

            gymKnapper = driver.find_elements_by_xpath("//button[@class='active']")

            for i in range(5):
                if gymKnapper[i].text in gyms:
                    gymKnapper[i].click()
            
            notLoaded = False
        except:
            pass

    
    times = driver.find_elements_by_xpath("//p[@class='time']")

    rightStartTime = []

    #Antall sjekk kommer an på antall timer tilgjengelig hver 48 time
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

    #Legger til timer som starter med samme starttidspunkt man har valgt
    for i in range(checks):
        if times[i].text.startswith(timeWanted):
            rightStartTime.append(times[i])

    #Velger den riktige timen
    rightStartTime[-1].click()

    #Trykker på "Book time pop-up"
    try:
        book = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class=' btn-primary btn' and @data-nomodal='true']"))
        )
        book.click()
    #Trykker på venteliste hvis man kommer for sent
    except:
        book = driver.find_element_by_xpath("//button[@class=' waitlistButton btn-primary btn' and @data-nomodal='true']")
        book.click()


    time.sleep(10)
    driver.quit()



def bookTraining2():

    if trainingTime2 == "00:00":
        return

    training = trainingTime2.split(":")
    timeWanted = ".".join(training)

    #Endrer gymWanted til riktig format
    global gymWanted
    if gymWanted.upper() == "DMMH":
        gymWanted = gymWanted.upper()
    else:
        gymWanted = gymWanted.lower()
        gymWanted = gymWanted[0].upper() + gymWanted[1:]

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    #For å komme inn på siden
    driver.get("https://www.sit.no/")

    #Trykker på riktige knapper med tekst
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

    #Brukernavn
    login.send_keys("brukernavn")

    login = driver.find_element_by_id("password")
    login.click()

    #Passord til bruker
    login.send_keys("passord")
    login.submit()

    #Kommer seg inn på siden man booker tid
    notLoaded = True
    while notLoaded:
        try:
            driver.get("https://www.sit.no/trening/treneselv")

            time.sleep(2)
            
            driver.switch_to.frame("ibooking-iframe")

            #Trykker vekk sentere man ikke vil ha
            gyms = ["Gløshaugen", "Moholt", "DMMH", "Portalen", "Dragvoll"]
            gyms.remove(gymWanted)

            gymKnapper = driver.find_elements_by_xpath("//button[@class='active']")

            for i in range(5):
                if gymKnapper[i].text in gyms:
                    gymKnapper[i].click()

            notLoaded = False
        except:
            pass


    times = driver.find_elements_by_xpath("//p[@class='time']")

    rightStartTime = []

    #Antall sjekk kommer an på antall timer tilgjengelig hver 48 time
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

    #Legger til timer som starter med samme starttidspunkt man har valgt
    for i in range(checks):
        if times[i].text.startswith(timeWanted):
            rightStartTime.append(times[i])

    #Velger den riktige timen
    rightStartTime[-1].click()

    #Trykker på "Book time pop-up"
    try:
        book = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class=' btn-primary btn' and @data-nomodal='true']"))
        )
        book.click()
    #Trykker på venteliste hvis man kommer for sent
    except:
        book = driver.find_element_by_xpath("//button[@class=' waitlistButton btn-primary btn' and @data-nomodal='true']")
        book.click()
        
    time.sleep(10)
    driver.quit()

#Denne gjør at scriptet blir kjørt på riktig tid
def bookTrening(timeBooking1, timeBooking2):
    schedule.every().day.at(timeBooking1).do(bookTraining1)
    schedule.every().day.at(timeBooking2).do(bookTraining2)

    while True:
        schedule.run_pending()
        time.sleep(1)


#trainingTime må være en streng på formatet "11:30", "00:00" hvis ikke ønsket
#gymWanted må være et gyldig treningssenter
trainingTime1 = "19:00"
trainingTime2 = "20:00"
gymWanted = "gløshaugen"



bookTrening(trainingTime1, trainingTime2)



