from selenium import webdriver
from selenium.webdriver.common.by import By


class OrangeHrm:
    driver = webdriver.Chrome(executable_path=r"D:\Data\Official\Softwares\Drivers\chromedriver.exe")
    def __init__(self, driver):
        driver.implicitly_wait(10)
        driver.maximize_window()

    def loadurl(self, driver):
        driver.get(r"https://opensource-demo.orangehrmlive.com/index.php/auth/login")

    def action(self, driver):
        driver.find_element(By.ID, "txtUsername").send_keys("Admin ")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.ID, "btnLogin").click()
        try:
            driver.find_element(By.XPATH, "//a[text()='Welcome Paul']").click()
            driver.find_element(By.XPATH, "//a[text()='Logout']").click()
            driver.minimize_window()
            driver.quit()
        except Exception:
            driver.minimize_window()
            driver.quit()

o = OrangeHrm(OrangeHrm.driver)
o.loadurl(OrangeHrm.driver)
o.action(OrangeHrm.driver)
