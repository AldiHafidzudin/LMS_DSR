from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import string

def generate_random_text(length=5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

random_text = generate_random_text()

options = Options()
options.add_experimental_option("detach", True) #agar web browser tidak close otomatis setelah skrip selenium selesai
driver = webdriver.Chrome(options=options) #connect Chrome

driver.implicitly_wait(10) #menunggu halaman muncul sampai 10 detik, implicit = semua element ditunggu
driver.maximize_window()

driver.get("https://dsr-lms.dev-app.online/portal/auth/login") #get URL
time.sleep(2)

#isi form login
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/input').send_keys("admin " + random_text)
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div/div[2]/div/input').send_keys("Admin")
time.sleep(2)