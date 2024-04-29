from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 創建一個 chrome視窗
# let chrome browser not close automatically
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

# 訪問 url
driver.get("https://www.thsrc.com.tw/")

# 在 element class="swal2-confirm" 進行 click
confirm_button = driver.find_element(By.CLASS_NAME, 'swal2-confirm')
confirm_button.click()

# 在 element id="select_location01" 選擇：台北
select1 = Select(driver.find_element(By.ID, 'select_location01'))
select1.select_by_visible_text('台北')

# 在 element id="select_location02" 選擇：桃園
select2 = Select(driver.find_element(By.ID, 'select_location02'))
select2.select_by_visible_text('桃園')

# 找到 element id="start-search" 進行 click
search_button = driver.find_element(By.ID, 'start-search')
search_button.click()

# time wait 5 秒
time.sleep(5)

# 找到所有 class name 為 'font-16r' 的元素
elements = driver.find_elements(By.CLASS_NAME, 'font-16r')
for element in elements:
    print(element.text)

# chrome 視窗不要自動關閉
# 注意：這將使程式保持運行，直到您手動關閉它