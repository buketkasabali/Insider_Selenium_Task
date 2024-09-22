import unittest
from selenium import webdriver
from pages.home import HomePage
from pages.career import CareersPage


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Chrome WebDriver'ı başlat
        self.home_page = HomePage(self.driver)  # HomePage nesnesini oluştur
        self.careers_page = CareersPage(self.driver)  # CareersPage nesnesini oluştur
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_home(self):
        # Ana sayfayı aç
        self.home_page.open()  # Ana sayfayı aç
        self.home_page.accept_cookies()  # Çerezleri kabul et
        self.home_page.accept_xbutton()  # Pop-up x butonu
        self.home_page.open_company()  # Company menüsünü aç
        self.home_page.open_career()  # Career menüsünü aç
        self.careers_page.check_find_your_calling()    # 'Find your calling' kontrolü ve kaydırma
        self.careers_page.check_location()   # 'Location' kontrolü ve kaydırma
        self.careers_page.check_life_at_insider() # 'Life At Insider' kontrolü ve kaydırma














