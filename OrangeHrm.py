from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"D:\Data\Official\Softwares\Drivers\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(r"https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.find_element(By.ID, "txtUsername").send_keys("Admin ")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
driver.find_element(By.XPATH, "//a[text()='Welcome Paul']").click()
driver.find_element(By.XPATH, "//a[text()='Logout']").click()
driver.minimize_window()
driver.quit()