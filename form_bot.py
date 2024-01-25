from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def fill_form(addresses, prices, links):
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeRp2hJNUSopnPhfCVHX5tOKByg74WaOvAXNcMNIFGr1UROAg/viewform"

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options)
    driver.get(form_url)
    time.sleep(1)

    for address, price, link in zip(addresses, prices, links):
        address_fill = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_fill.send_keys(address)
        # time.sleep(1)

        price_fill = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_fill.send_keys(price)
        # time.sleep(1)

        link_fill = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_fill.send_keys(link)

        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_button.click()
        time.sleep(1)

        next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        next_button.click()
        time.sleep(1)