from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Dejar esta lib cierra la venta
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
driver.implicitly_wait(0.5)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium")
search_button.click()

driver.set_window_size(500,500)

print("\n ====== Test Results ======")
print("✅ Tests successfully passed!")
print(driver.title) # => "title de la web"
print(driver.find_element(By.NAME, "q").get_attribute("value")) # => "Contenido del elemento en el estado actual"