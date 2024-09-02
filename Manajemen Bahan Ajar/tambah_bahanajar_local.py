from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pyautogui

options = Options()
options.add_experimental_option("detach", True) #agar web browser tidak close otomatis setelah skrip selenium selesai
driver = webdriver.Chrome(options=options) #connect Chrome

driver.implicitly_wait(10) #menunggu halaman muncul sampai 10 detik, implicit = semua element ditunggu
driver.maximize_window()

driver.get("https://dsr-lms.dev-app.online/portal/auth/login") #get URL
time.sleep(2)

#isi form login
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/input').send_keys("admin")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div/div[2]/div/input').send_keys("Admin")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/button').click()
time.sleep(5)

#navigasi modul
#klik manajemen diklat
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div/div[4]').click()
time.sleep(5)

#pilih klasifikasi bahan ajar
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[4]/div/div/div[1]/div/div[2]').click()
time.sleep(5)

#tambah bahan ajar
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/button').click()
time.sleep(5)

#input judul bahan ajar
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/input').send_keys("Test bahan ajar 1")
time.sleep(2)

#tambah gadik
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[2]/button').click()
time.sleep(2)
#pilih gadik
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[3]/div').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[1]/div[2]/button[2]').click()
time.sleep(2)

#tambah materi pokok
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div/div/button[1]').click()
time.sleep(2)
pyautogui.write(r"Banjir Rendam 6 Kecamatan di Kota Gorontalo Aktivitas Warga Nyaris Lumpuh Total_360p.mp4")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)

#input deskripsi
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[5]/div[2]/div/div[2]/div[2]/div').send_keys("ini adalah deskripsi dummy bahan ajar")
time.sleep(2)

#scroll keatas untuk mencari tombol "simpan"
pyautogui.scroll(1000)
time.sleep(2)

#klik simpan 
#driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/button').click()
time.sleep(2)