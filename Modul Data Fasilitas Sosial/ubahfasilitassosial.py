import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()

# driver.get("http://192.168.1.11:2030/login/")

# Setup Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "printing.print_preview_sticky_settings.appState": '{"recentDestinations":[{"id":"Save as PDF","origin":"local","account":"","capabilities":{}}],"selectedDestinationId":"Save as PDF","version":2}',
    "savefile.default_directory": "Downloads"
})
chrome_options.add_argument("--kiosk-printing")

try:
    # Buka halaman login
    driver.get("https://dsr-lms.dev-app.online/portal/auth/login")

    # Tunggu hingga elemen input username tersedia
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#__nuxt > div:nth-child(2) > div > div > div.intro-x.col-span-12.lg\:col-span-6.flex.items-center.h-screen.justify-center.drop-shadow-xl > div"))
    )

    # Masukkan username
    username = driver.find_element(By.CSS_SELECTOR, "input[type='text'][placeholder='Masukkan Username / NRP']")
    username.send_keys("admin")

    # Masukkan password
    password = driver.find_element(By.CSS_SELECTOR, "input[type='password'][placeholder='Masukkan Password']")
    password.send_keys("Admin")

    # Gunakan CSS Selector untuk menemukan tombol login
    login_button_selector = "#__nuxt > div:nth-child(2) > div > div > div.intro-x.col-span-12.lg\:col-span-6.flex.items-center.h-screen.justify-center.drop-shadow-xl > div > div > div.self-stretch.h-\[233px\].flex-col.justify-start.items-start.gap-\[62px\].flex > button"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, login_button_selector))
    )

    login_button.click()

    # # Scroll ke elemen tombol login
    # driver.execute_script("arguments[0].scrollIntoView();", login_button)

    # # Klik elemen menggunakan JavaScript
    # driver.execute_script("arguments[0].click();", login_button)

    # Tunggu hingga halaman utama setelah login tampil
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "__nuxt"))
    )

    print("Login berhasil! Browser tetap terbuka di halaman utama.")

    time.sleep(5)

    #Module Dashboard
    
     # Ganti dengan selector yang sesuai untuk menu atau modul yang diinginkan
    menu_modul_selector = "#__nuxt > div:nth-child(2) > div > div > div:nth-child(2) > div.z-10.py-16 > div > div:nth-child(11)"  # Ganti dengan selector yang sesuai
    menu_modul = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, menu_modul_selector))
    )
    
    menu_modul.click()

    time.sleep(2)

    data_master_fassos_selector = "#headlessui-dialog-panel-nHAJMhYDoe7_8 > div > div > div:nth-child(3)"
    data_master_fassos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, data_master_fassos_selector))
    )

    data_master_fassos_button.click()

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR, "input[type='text'][placeholder='Cari']")
    search.send_keys("Kantor Kecamatan Palmerah")

    search_button = driver.find_element(By.CSS_SELECTOR, "#__nuxt > div:nth-child(2) > div > div > div > div:nth-child(2) > div:nth-child(2) > div.w-\[492px\] > div > div:nth-child(2) > div > span > button.focus\:outline-none.focus-visible\:outline-0.disabled\:cursor-not-allowed.disabled\:opacity-75.flex-shrink-0.font-medium.rounded-md.text-sm.gap-x-1\.5.p-1\.5.text-gray-500.dark\:text-gray-400.hover\:text-gray-700.dark\:hover\:text-gray-200.underline-offset-4.hover\:underline.focus-visible\:ring-inset.focus-visible\:ring-2.focus-visible\:ring-primary-500.dark\:focus-visible\:ring-primary-400.inline-flex.items-center.ml-2")

    search_button.click()

    time.sleep(2)

    ubah_button_selector = "#__nuxt > div:nth-child(2) > div > div > div > div.overflow-x-auto.overflow-y-hidden.my-5 > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > div > div:nth-child(1) > button"
    ubah_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ubah_button_selector))
    )

    ubah_button.click()
    

    
    # Tunggu selama 10 detik sebelum menutup browser
    time.sleep(10)
    print("Berhasil melakukan tes dengan baik!")

finally:
    # Tutup browser
    driver.quit()