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
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]').click()
time.sleep(5)

#tambah diklat
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div/a/button').click()
time.sleep(5)

#Form tab diklat
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/input').send_keys("Kebencanaan Dummy 1")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[3]/div[2]/div/div[2]/div/input').send_keys("Lokasi online")
time.sleep(2)

#pilih pengajar
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[4]/div[2]/div/button').click()
time.sleep(2)
pyautogui.typewrite("wasprod")
time.sleep(2)
pyautogui.press("Enter")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[4]/div[2]/div/button').click()
time.sleep(2)

#pilih waktu pelaksanaan
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[5]/div[2]/div[2]/div/div[1]/div/div/input').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[5]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[5]/div[1]/div').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[5]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[6]/div[3]/div').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[5]/div[2]/div[2]/div/div[1]/div/div/input').click()
time.sleep(2)

#Kuota diklat
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/input').send_keys('2')
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div').send_keys('ini adalah deskripsi kuis')
time.sleep(3)

#upload thumbnail
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[8]/div[2]/div[2]/div/div').click()
time.sleep(2)
pyautogui.write(r"logo stat.png")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)

#scroll keatas untuk mencari tombol "Selanjutnya"
pyautogui.scroll(1000)
time.sleep(3)

#klik selanjutnya 
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/button').click()
time.sleep(2)

#tab pertemuan
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[5]/div[1]/div[2]/div/div[2]/div/input').send_keys('Pertemuan 1 materi satu')
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[5]/div[4]/div[2]/div[2]/div[2]/div').send_keys('Deskripsi pertemuan 1')
time.sleep(2)

#tambah bahan ajar
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[6]/div[1]/button').click()
time.sleep(5) 
#klik checkbox bahan ajar
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div/div[3]/div/div[4]/div/div[1]/div/div/input').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/button').click()
time.sleep(2)

#tambah kuis
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[7]/div[1]/button').click()
time.sleep(5)
#klik checkbox kuis
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div[1]/div/div/input').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/button').click()
time.sleep(2)

#set pengaturan kuis
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[7]/div[2]/div/div/div[4]/button').click()
time.sleep(2) 
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div/div/input').click()
time.sleep(2) #set waktu masuk
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[5]/div[5]').click()
time.sleep(2) 
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[5]/div[1]/div[2]/div/div[1]/div/div/input').click()
time.sleep(2) #set waktu berakhir
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[5]/div[1]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[6]/div[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[7]/div[1]/div/div[2]/div/input').clear()
time.sleep(2) 
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[7]/div[1]/div/div[2]/div/input').send_keys('0')
time.sleep(2) 
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[7]/div[3]/div/div[2]/div/input').clear()
time.sleep(2) 
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[7]/div[3]/div/div[2]/div/input').send_keys('5')
time.sleep(2) 
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[10]/button[2]').click()
time.sleep(2) 

#scroll keatas untuk mencari tombol "Selanjutnya"
pyautogui.scroll(1000)
time.sleep(2)

#klik selanjutnya 
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/button').click()
time.sleep(2)

#tab peserta
#klik tambah peserta
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[3]/div[1]/button').click()
time.sleep(2)

#pop up tambah peserta
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/input').click()
time.sleep(2) 
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[1]/div/div/div/input').click()
time.sleep(2) 
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/button').click()
time.sleep(2) 

#klik selanjutnya 
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/button').click()
time.sleep(2)

#Tab penilaian
#Standar kelulusan
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/input').send_keys('70')
time.sleep(2) 

#Bobot penilaian
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/table/tbody/tr/td[3]/div/div/div/div[2]/div/input').clear()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/table/tbody/tr/td[3]/div/div/div/div[2]/div/input').send_keys('100')
time.sleep(2)

#Pilh pejabat
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[3]/div[2]/div[2]/div/button').click()
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

#scroll keatas untuk mencari tombol "Simpan"
pyautogui.scroll(1000)
time.sleep(2)

#KLIK SIMPAN DIKLAT
#driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/button').click()
time.sleep(2)