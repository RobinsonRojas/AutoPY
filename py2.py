from selenium import webdriver

# Dejar esta lib cierra la venta
#from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("start-maximized")


driver = webdriver.Chrome('C:\d\chromedriver.exe',options=options)
#driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)


driver.get("https://www.google.com")
#driver.close()
#driver.quit()