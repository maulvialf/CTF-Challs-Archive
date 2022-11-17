from selenium import webdriver
from flask import current_app
import time

def visit_report():
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-setuid-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-background-networking')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-sync')
    chrome_options.add_argument('--disable-translate')
    chrome_options.add_argument('--metrics-recording-only')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument('--no-first-run')
    chrome_options.add_argument('--safebrowsing-disable-auto-update')
    chrome_options.add_argument('--js-flags=--noexpose_wasm,--jitless')

    client = webdriver.Chrome(chrome_options=chrome_options)
    client.set_page_load_timeout(5)
    client.set_script_timeout(5)

    client.get('http://localhost:1337/')

    username = client.find_element_by_id('username')
    password = client.find_element_by_id('password')
    login = client.find_element_by_id('login-btn')

    username.send_keys(current_app.config['ADMIN_USERNAME'])
    password.send_keys(current_app.config['ADMIN_PASSWORD'])
    login.click()
    time.sleep(3)

    client.get('http://localhost:1337/review')

    time.sleep(3)
    client.quit()