from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from locators.jobs import Jobs


class See_All_QA_Jobs:
    def __init__(self, driver):
        self.driver = driver  # Driver'ı burada tanımlıyoruz

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

    def open_see_all_qa_jobs_button(self):
        try:
            self.driver.find_element(By.XPATH, Jobs.see_all_qa_jobs).click()
            time.sleep(5)
        except Exception as e:
            print(f"Could not access the See All QA Jobs page.: {e}")

    def location_filter(self):
        try:
            location_filter = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Jobs.location_filter_element))
            )
            location_filter.click()
            time.sleep(2)

            location = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Jobs.location_element))
            )
            location.click()
            time.sleep(2)

            print("Location filter applied.")
        except Exception as e:
            print(f"Location filter could not be applied.: {e}")

        return self

    def department_filter(self):
        try:
            department_filter = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Jobs.department_filter_element))
            )
            department_filter.click()
            time.sleep(2)

            department = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Jobs.department_element))
            )
            department.click()
            time.sleep(2)

            print("Departman filter applied.")
        except Exception as e:
            print(f"Departman filter could not be applied.: {e}")

        return self

    def scroll_to_element(self, element):
        #Belirtilen elemana kaydır.
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def check_job_list(self):
        #'Browse Open Positions' başlığının mevcut ve görünür olup olmadığını kontrol eder.
        try:
            job_list_xpath = Jobs.job_list
            job_list_title = self.wait_for_element(By.XPATH, job_list_xpath)
            assert job_list_title.is_displayed()
            print("The 'Browse Open Positions' title is present and displayed.")
            self.scroll_to_element(job_list_title)
            time.sleep(2)  #
        except Exception as e:
            print(f"Error: {e} - 'Browse Open Positions' not found.")

    def check_jobs_list(self):
        #Tüm iş ilanlarının detaylarını kontrol eder.
        job_items = self.wait_for_elements(By.XPATH, "//div[@id='jobs-list']")
        time.sleep(2)  # İş ilanlarını kontrol etmeden önce bekle

        for job in job_items:
            position = job.find_element(By.XPATH, Jobs.position).text
            department = job.find_element(By.XPATH, Jobs.department).text
            location = job.find_element(By.XPATH, Jobs.location).text

            assert "Quality Assurance" in position, f"Error: Position '{position}' does not contain the expected 'Quality Assurance.'"
            assert "Quality Assurance" in department, f"Error: Department '{department}' does not contain the expected 'Quality Assurance.'"
            assert "Istanbul, Turkey" in location, f"Error: Location '{location}' does not contain the expected 'Istanbul, Turkey.'"

        print("All job listings comply with the filtering criteria.")

    def lever_application_form_page(self):
        """Check if the 'View Role' button is present on hover and click it."""
        try:
            check_view_role = self.wait_for_element(By.XPATH, Jobs.check_view_role)
            ActionChains(self.driver).move_to_element(check_view_role).perform()  # Hover over the element
            time.sleep(1)  # Wait after hover

            view_role = self.wait_for_element(By.XPATH, Jobs.view_role)

            if view_role.is_displayed():
                view_role.click()
                print("Clicked the 'View Role' button.")
                time.sleep(3)  # Wait after click
            else:
                print("Warning: 'View Role' button is not visible after hover.")

            current_url = self.driver.current_url  # Check the URL
            print(f"Current URL after clicking 'View Role': {current_url}")  # Debugging output
            time.sleep(2)  # Wait before checking the URL
            assert current_url == "https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc", f"The expected URL could not be reached: {current_url}"

        except NoSuchElementException:
            print("Error: 'Lever' element or 'View Role' button is not present.")
        except Exception as e:
            print(f"Error: An error occurred. Details: {e}")
