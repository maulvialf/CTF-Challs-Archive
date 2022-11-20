from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(chrome_options=chrome_options)

def wait_until(ec, by, value):
    return WebDriverWait(driver, 60).until(ec((by, value)))

url = "http://jointspay-nginx/"
driver.get(url + 's3cr3t_c0d3.php?p=8682a65aa7f080e0d8511018a9f64d77')

while True:
    time.sleep(10)
    driver.get(url)
