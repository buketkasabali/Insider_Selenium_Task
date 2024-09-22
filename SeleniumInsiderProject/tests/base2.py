import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.home import HomePage
from pages.career import CareersPage
from locators.careers import CareersObjects
from pages.jobs import See_All_QA_Jobs

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Chrome WebDriver'ı başlat
        self.home_page = HomePage(self.driver)  # HomePage nesnesini oluştur
        self.careers_page = CareersPage(self.driver)  # CareersPage nesnesini oluştur
        self.jobs_page = See_All_QA_Jobs(self.driver)  # QA nesnesini oluştur
        self.driver.implicitly_wait(10) #Bekleme süresi
        self.driver.maximize_window() # Tarayıcıyı tam ekran yap

    def test_home(self):
        # Ana sayfayı aç
        self.home_page.open()  # Ana sayfayı aç
        self.home_page.accept_cookies()  # Çerezleri kabul et
        self.home_page.accept_xbutton()  # Pop-up x butonu
        self.home_page.open_company()  # Company menüsünü aç
        self.home_page.open_career()  # Career menüsünü aç

        # Career page

        self.careers_page.check_find_your_calling() # 'Find your calling' kontrolü ve kaydırma
        self.careers_page.check_location() # 'Location' kontrolü ve kaydırma
        self.careers_page.check_life_at_insider() # 'Life At Insider' kontrolü ve kaydırma

        # 'All Teams' butonuna kadar yavaşça kaydır
        all_teams_xpath = CareersObjects.all_teams  # "All teams" için Xpath'i tanımla
        all_teams_title = self.careers_page.wait_for_element(By.XPATH, all_teams_xpath)  # Elemanı bekle
        self.careers_page.scroll_smoothly_to_element(all_teams_title)  # Elemanı argüman olarak ver
        self.careers_page.open_all_teams() # 'All Teams' butonuna tıkla
        self.careers_page.check_qa() # 'QA' kontrolü ve kaydırma
        self.careers_page.open_qa_button() # 'QA' butonuna tıkla


        self.jobs_page.open_see_all_qa_jobs_button()  # "See All QA Jobs" butonunu aç
        self.jobs_page.location_filter()  # Location seçimi
        self.jobs_page.department_filter()  # Department seçimi
        self.jobs_page.check_job_list() #Job List kontrolü
        self.jobs_page.check_jobs_list() #Job List detayları kontrolü
        self.jobs_page.lever_application_form_page() # lever application form page erişim





