import getpass

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def load_eacrs(driver):
    driver.get('http://eacr.colostate.edu/')
    username = input("Enter your eID: ")
    password = getpass.getpass("Enter your password: ")
    while True:
        usernameField = driver.find_element_by_id("username")
        passwordField = driver.find_element_by_id("password")

        usernameField.send_keys(username)
        passwordField.send_keys(password)
        driver.find_element_by_name("_eventId_proceed").click()

        url = driver.current_url()
        print(url)
        if not driver.find_element_by_id("username"):
            return


def enter_CSV(CSV_path, driver):
    row_counter = 2
    line_counter = 0
    with open(CSV_path) as file:
        next(file)
        for split in file:
            delimited = split.split(',')
            serial = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_txtSerialNumber")
            make = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_txtMake")
            model = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_txtModel")
            description = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_txtDescription")
            quantity = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_txtQuantity")
            reason = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_ddlReasonCode")
            condition = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_ddlConditionCode")
            room = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_txtRoom")
            decal = driver.find_element_by_id(
                "ctl00_cphBody_gvEacrLotDetails_ctl" + format(row_counter, '02d') + "_txtDecal")
            serial.send_keys(delimited[0])
            make.send_keys(delimited[1])
            model.send_keys(delimited[2])
            description.send_keys(delimited[3])
            quantity.send_keys(delimited[4])
            reason.send_keys(delimited[5])
            condition.send_keys(delimited[6])
            room.send_keys(delimited[8])
            decal.send_keys(delimited[9])
            row_counter += 1
            line_counter += 1
            if line_counter == 15:
                driver.find_element_by_id("ctl00_cphBody_btnSaveEacrLotDetail").click()
                line_counter = 1
    driver.find_element_by_id("ctl00_cphBody_btnSaveEacrLotDetail").click()


csv_path = "surplus.csv"
user_input = input("Please enter the path to the CSV file (default: ./surplus.csv): ")

if len(user_input) < 1:
    print(user_input)


options = Options()
driver = webdriver.Firefox(options=options)
driver.get('http://eacr.colostate.edu/')
start = input("Open 'Line Items' window and type start when ready: ")

while not start == "start":
    start = input("Type start when ready: ")
enter_CSV(csv_path, driver)
