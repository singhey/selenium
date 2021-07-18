from selenium import webdriver
import time
import requests
import Helper
import CONSTS

def login(username, password, browser):
    try:
        browser.get(CONSTS.LOGIN_URL)
        browser.find_element_by_id("loginEmail").send_keys(username)
        browser.find_element_by_id("getClients").click()
        Helper.sleep_for(5)
        browser.find_element_by_id("loginPassword").send_keys(password)
        browser.find_element_by_id("loginSubmit").click()
        Helper.sleep_for(10)
        return True
    except:
        return False

def print_result(message, result):
    print(message, end="")
    print("Passed" if result else "Failed")

def go_into_oms(browser):
    browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/a").click()
    Helper.sleep_for(30)
    return True

def select_orders_tab(browser):
    browser.find_element_by_xpath("//a[contains(text(), 'Orders')]").click()
    browser.find_element_by_xpath("//span[contains(text(), 'Sale Order')]/..").click()
    Helper.sleep_for(30)
    return True

def add_order(browser):
    browser.find_element_by_id("SOAddNew").click()
    Helper.sleep_for(10)
    

if __name__ == "__main__":
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    print_result("User Logged in: ", login("prakash", "abcd@1234", browser))
    print_result("Select OMS:", go_into_oms(browser))
    select_orders_tab(browser)
    add_order(browser)
    
