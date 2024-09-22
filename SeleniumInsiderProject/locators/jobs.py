class Jobs:
    see_all_qa_jobs = "/html[1]/body[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]"
    location_filter_element = '//*[@id="select2-filter-by-location-container"]'
    location_element = "//li[text()='Istanbul, Turkey']"
    department_filter_element = '//*[@id="select2-filter-by-department-container"]'
    department_element = "//li[text()='Quality Assurance']"
    job_list = "/html[1]/body[1]/section[3]/div[1]/div[1]/div[1]/h3[1]"
    view_role = "/html[1]/body[1]/section[3]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]"
    position = ".//p[contains(@class, 'position-title font-weight-bold')]"
    department = ".//span[contains(@class, 'position-department text-large font-weight-600 text-primary')]"
    location = ".//div[contains(@class, 'position-location text-large')]"
    check_view_role = "//div[contains(@class, 'position-list-item-wrapper bg-light')]"
    view_role = "//a[contains(@href, 'https://jobs.lever.co/') and contains(text(), 'View Role')]"


