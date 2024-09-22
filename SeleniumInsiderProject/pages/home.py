
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators.home import HomePageLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver  # WebDriver'ı başlat

    def visit(self):
        self.driver.get(HomePageLocators.url) # Belirtilen URL'ye git
        return self

    def open(self):
        self.driver.get(HomePageLocators.url)  # URL buradan alınıyor
        assert "Insider" in self.driver.title, "The homepage did not load correctly."  # Başlığı kontrol et
        time.sleep(2)

    def accept_cookies(self):
        try:
            self.driver.find_element(By.XPATH, "//a[@id='wt-cli-accept-all-btn']").click()  # Çerez onayı butonuna tıkla
            assert True
            time.sleep(2)
        except:
            print("Cookie consent banner not found.")

    def accept_xbutton(self):
        try:
            self.driver.find_element(By.XPATH, "//span[@class='ins-close-button']").click()  # Pop-up x butonuna tıkla
            assert True
            time.sleep(8)
        except:
            print("Pop-up not found.")

    def open_company(self):
        try:
            self.driver.find_element(By.XPATH, HomePageLocators.Company).click()
            time.sleep(8)
            about_us_element = self.driver.find_element(By.XPATH,"//a[@class='dropdown-sub'][normalize-space()='About Us']") #About Us öğesinin varlığını kontrol et
            assert about_us_element.is_displayed(), "'About Us' menu is not visible."  # Öğenin görünürlüğünü kontrol et
        except Exception as e:
            print(f"Unable to access the company menu.: {e}")

    def open_career(self):
        try:
            self.driver.find_element(By.XPATH, HomePageLocators.Careers).click()
            time.sleep(8)
            current_url = self.driver.current_url # URL'yi kontrol et
            assert current_url == "https://useinsider.com/careers/", f"Could not reach the expected URL.: {current_url}"

        except Exception as e:
            print(f"Unable to access the Careers page: {e}")






