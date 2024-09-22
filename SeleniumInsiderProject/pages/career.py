from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.careers import CareersObjects
import time


class CareersPage:
    def __init__(self, driver):
        self.driver = driver  # Driver'ı burada tanımlıyoruz

    def scroll_to_element(self, element):
        #Belirtilen elemana kaydır.
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def wait_for_element(self, by, value, timeout=20):
        #Tek bir eleman için tıklanabilir olana kadar bekle.
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))  # Görünürlük bekleme
        )

    def wait_for_elements(self, by, value, timeout=10):
        #Birden fazla elemanın varlığını kontrol et.
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )
        return self.driver.find_elements(by, value)

    def check_find_your_calling(self):
        #'Find your calling' başlığının mevcut ve görünür olup olmadığını kontrol et.
        try:
            find_your_calling_xpath = CareersObjects.find_your_calling
            find_your_calling_title = self.wait_for_element(By.XPATH, find_your_calling_xpath)
            assert find_your_calling_title.is_displayed()
            print("The 'Find your calling' title is present and displayed.")
            self.scroll_to_element(find_your_calling_title)
        except Exception as e:
            print(f"Error: {e} - 'Find your calling' could not be found.")

    def check_location(self):
        #'Location' başlığının mevcut ve görünür olup olmadığını kontrol et.
        try:
            location_xpath = CareersObjects.our_location
            location_title = self.wait_for_element(By.XPATH, location_xpath)
            assert location_title.is_displayed()
            print("The 'Our Location' title is present and displayed.")
            self.scroll_to_element(location_title)
        except Exception as e:
            print(f"Error: {e} - 'Our Location'could not be found.")

    def check_life_at_insider(self):
        #'Life At Insider' başlığının mevcut ve görünür olup olmadığını kontrol et.
        try:
            life_at_insider_xpath = CareersObjects.life_at_insider
            life_at_insider_title = self.wait_for_element(By.XPATH, life_at_insider_xpath)
            assert life_at_insider_title.is_displayed()
            print("The 'Life At Insider' title is present and displayed.")
            self.scroll_to_element(life_at_insider_title)
        except Exception as e:
            print(f"Error: {e} - 'Life At Insider' could not be found.")

    def scroll_smoothly_to_element(self, element):
        #Belirtilen elemana yavaşça kaydır.
        target_position = element.location['y']  # Hedef elemanın Y konumu
        current_position = self.driver.execute_script("return window.scrollY;")

        print(f"Current position: {current_position}, Target position: {target_position}")

        # Yavaşça hedef elemana kaydır
        while abs(current_position - target_position) > 5:  # Hedefe yaklaşma toleransı
            if current_position < target_position:
                self.driver.execute_script("window.scrollBy(0, 30);")  # 30 piksel aşağı kaydır
            else:
                self.driver.execute_script("window.scrollBy(0, -30);")  # 30 piksel yukarı kaydır

            time.sleep(0.1)
            current_position = self.driver.execute_script("return window.scrollY;")
            print("Current position:", current_position)

        # Hedef konumuna tam ulaşma
        self.driver.execute_script("window.scrollTo(0, arguments[0]);", target_position)
        print("Target position reached.:", target_position)

    def open_all_teams(self):
        try:
            self.driver.find_element(By.XPATH, CareersObjects.all_teams_button).click() # 'All Teams' butonuna tıkla
            time.sleep(8)

        except Exception as e:
            print(f"Could not access the All Teams page.: {e}")


    def check_qa(self):
        #'QA' başlığının mevcut ve görünür olup olmadığını kontrol et.
        try:
            qa_xpath = CareersObjects.qa # Xpath'i alır
            qa_title = self.wait_for_element(By.XPATH, qa_xpath) # Elemanı bekle
            assert qa_title.is_displayed() # Elemanın görünür olduğunu kontrol et
            print("The 'QA' title is present and displayed.")
            self.scroll_to_element(qa_title)
        except Exception as e:
            print(f"Error: {e} - 'Quality Assurance' not found.")

    def open_qa_button(self):
        try:
            self.driver.find_element(By.XPATH, CareersObjects.qa_button).click() # 'QA' butonuna tıkla
            time.sleep(8)
            current_url = self.driver.current_url # URL'yi kontrol et
            assert current_url == "https://useinsider.com/careers/quality-assurance/", f"Could not reach the expected URL.: {current_url}"

        except Exception as e:
            print(f"Could not access the Quality Assurance page.: {e}")

